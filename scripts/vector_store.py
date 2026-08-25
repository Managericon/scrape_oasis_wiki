#!/usr/bin/env python3
"""Synchronize Markdown files with, or search, an OpenAI Vector Store."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=Path("knowledge/vector_store.json"))
    parser.add_argument("--vector-store-id")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync = subparsers.add_parser("sync", help="Upload changed Markdown documents")
    sync.add_argument("--directory", type=Path, action="append")
    sync.add_argument("--name", default="Tencent Oasis Wiki")
    sync.add_argument("--prune", action="store_true")

    search = subparsers.add_parser("search", help="Run semantic search")
    search.add_argument("query")
    search.add_argument("--max-results", type=int, default=8)
    search.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"files": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")[:8_192]
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, raw = line.partition(":")
        if not separator:
            continue
        raw = raw.strip()
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = raw
        result[key.strip()] = str(value)[:512]
    return result


def client_from_env(variable: str) -> OpenAI:
    api_key = os.environ.get(variable)
    if not api_key:
        raise RuntimeError(f"Environment variable {variable} is not set")
    return OpenAI(api_key=api_key)


def resolve_store(client: OpenAI, args: argparse.Namespace, state: dict[str, Any]):
    vector_store_id = args.vector_store_id or state.get("vector_store_id")
    if vector_store_id:
        return client.vector_stores.retrieve(vector_store_id)
    store = client.vector_stores.create(
        name=args.name,
        description="Tencent Oasis Wiki and API reference converted to Markdown",
        metadata={"source": "developer.gp.qq.com", "catalog": "20418+api"},
    )
    print(f"Created Vector Store {store.id}")
    return store


def remove_remote_file(client: OpenAI, vector_store_id: str, file_id: str) -> None:
    try:
        client.vector_stores.files.delete(file_id, vector_store_id=vector_store_id)
    except Exception as exc:
        print(f"Warning: detach {file_id} failed: {exc}", file=sys.stderr)
    try:
        client.files.delete(file_id)
    except Exception as exc:
        print(f"Warning: delete {file_id} failed: {exc}", file=sys.stderr)


def sync_store(client: OpenAI, args: argparse.Namespace, state: dict[str, Any]) -> int:
    directories = args.directory or [Path("knowledge/articles")]
    directories = [directory.expanduser().resolve() for directory in directories]
    paths = sorted(
        (directory, path)
        for directory in directories
        for path in directory.rglob("*.md")
        if path.is_file()
    )
    if not paths:
        raise RuntimeError("No Markdown files found in: " + ", ".join(map(str, directories)))

    store = resolve_store(client, args, state)
    old_files = state.get("files", {})
    new_files: dict[str, Any] = {}
    uploaded = 0
    skipped = 0
    failed = 0

    for index, (directory, path) in enumerate(paths, start=1):
        local_relative = path.relative_to(directory).as_posix()
        relative = local_relative if directory.name == "articles" else f"{directory.name}/{local_relative}"
        fingerprint = sha256(path)
        old = old_files.get(relative, {})
        if old.get("sha256") == fingerprint and old.get("file_id"):
            new_files[relative] = old
            skipped += 1
            continue
        if old.get("file_id"):
            remove_remote_file(client, store.id, old["file_id"])

        print(f"[{index}/{len(paths)}] Uploading {relative}")
        metadata = frontmatter(path)
        attributes = {
            key: metadata[key]
            for key in ("id", "title", "source", "category")
            if metadata.get(key)
        }
        try:
            with path.open("rb") as document:
                remote = client.vector_stores.files.upload_and_poll(
                    vector_store_id=store.id,
                    file=document,
                    attributes=attributes,
                )
            if remote.status != "completed":
                raise RuntimeError(f"indexing status is {remote.status}")
            new_files[relative] = {
                "sha256": fingerprint,
                "file_id": remote.id,
                "attributes": attributes,
            }
            uploaded += 1
        except Exception as exc:
            print(f"  Failed: {exc}", file=sys.stderr)
            failed += 1

    stale = set(old_files) - set(new_files)
    if args.prune:
        for relative in sorted(stale):
            file_id = old_files[relative].get("file_id")
            if file_id:
                print(f"Pruning {relative}")
                remove_remote_file(client, store.id, file_id)
    else:
        for relative in stale:
            new_files[relative] = old_files[relative]

    state = {
        "vector_store_id": store.id,
        "name": store.name,
        "files": new_files,
        "summary": {"uploaded": uploaded, "skipped": skipped, "failed": failed},
    }
    save_state(args.state.expanduser().resolve(), state)
    print(json.dumps(state["summary"], ensure_ascii=False))
    print(f"VECTOR_STORE_ID={store.id}")
    return 0 if failed == 0 else 2


def result_to_dict(result: Any) -> dict[str, Any]:
    return {
        "file_id": result.file_id,
        "filename": result.filename,
        "score": result.score,
        "attributes": result.attributes,
        "content": [item.text for item in result.content if item.type == "text"],
    }


def search_store(client: OpenAI, args: argparse.Namespace, state: dict[str, Any]) -> int:
    vector_store_id = args.vector_store_id or state.get("vector_store_id")
    if not vector_store_id:
        raise RuntimeError("No Vector Store ID; run sync first or pass --vector-store-id")
    page = client.vector_stores.search(
        vector_store_id,
        query=args.query,
        max_num_results=max(1, min(50, args.max_results)),
        rewrite_query=True,
    )
    results = [result_to_dict(result) for result in page.data]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    for index, result in enumerate(results, start=1):
        title = (result["attributes"] or {}).get("title") or result["filename"]
        print(f"## {index}. {title} (score: {result['score']:.3f})")
        source = (result["attributes"] or {}).get("source")
        if source:
            print(f"Source: {source}")
        print()
        print("\n\n".join(result["content"]))
        print()
    return 0


def main() -> int:
    args = parse_args()
    state = load_state(args.state.expanduser().resolve())
    client = client_from_env(args.api_key_env)
    if args.command == "sync":
        return sync_store(client, args, state)
    return search_store(client, args, state)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

