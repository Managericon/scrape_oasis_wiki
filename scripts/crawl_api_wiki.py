#!/usr/bin/env python3
"""Crawl the official Tencent Oasis API JSON corpus into Markdown."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

import html2text


DEFAULT_URL = "https://developer.gp.qq.com/api/"
INDEXES = {
    "class": "class/list/sorted_list.json",
    "cppenum": "cppenum/list/sorted_list.json",
    "cppstruct": "cppstruct/list/sorted_list.json",
    "globalfunc": "globalfunc/list/sorted_list.json",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output-dir", type=Path, default=Path("knowledge/api"))
    parser.add_argument("--kind", action="append", choices=sorted(INDEXES))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--discover-only", action="store_true")
    parser.add_argument("--prune-output", action="store_true")
    parser.add_argument("--chunk-chars", type=int, default=500_000)
    return parser.parse_args()


def configure_console() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def fetch_json(url: str, timeout: int, attempts: int = 3) -> Any:
    request = Request(url, headers={"User-Agent": "oasis-wiki-knowledge/1.0"})
    error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8-sig"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            error = exc
            if attempt < attempts:
                time.sleep(attempt * 0.5)
    raise RuntimeError(f"Failed to fetch {url}: {error}")


def flatten_paths(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from flatten_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from flatten_paths(child)


def safe_segment(value: str, fallback: str = "unnamed") -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value.strip())
    return value.strip(" .")[:140] or fallback


def source_url(base_url: str, relative: str) -> str:
    return urljoin(base_url, quote(relative, safe="/"))


def discover(base_url: str, kinds: list[str], timeout: int) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for kind in kinds:
        index_url = urljoin(base_url, INDEXES[kind])
        index = fetch_json(index_url, timeout)
        for relative in flatten_paths(index):
            name = Path(relative).stem
            key = (kind, relative)
            if key in seen:
                continue
            seen.add(key)
            parts = relative.replace("\\", "/").split("/")
            categories = parts[2:-1] if kind == "class" and len(parts) > 3 else []
            entries.append(
                {
                    "id": f"api:{kind}:{name}",
                    "name": name,
                    "title": name,
                    "kind": kind,
                    "categories": categories,
                    "json_path": relative,
                    "url": source_url(base_url, relative),
                    "api_root": base_url,
                }
            )
    return sorted(entries, key=lambda item: (item["kind"], item["name"].casefold()))


def description(value: Any) -> str:
    if value is None:
        return ""
    text = html.unescape(str(value)).replace("\r\n", "\n").strip()
    if re.search(r"</?[a-z][^>]*>", text, flags=re.IGNORECASE):
        converter = html2text.HTML2Text()
        converter.body_width = 0
        converter.ignore_images = False
        converter.ignore_links = False
        converter.unicode_snob = True
        text = converter.handle(text).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def table_cell(value: Any) -> str:
    return description(value).replace("|", "\\|").replace("\n", "<br>") or "-"


def type_name(item: dict[str, Any]) -> str:
    return str(item.get("Type") or item.get("Value") or "").strip()


def signature(function: dict[str, Any]) -> str:
    params = []
    for param in function.get("Params") or []:
        name = str(param.get("Name") or "arg").strip()
        kind = type_name(param)
        params.append(f"{name}: {kind}" if kind else name)
    returns = [type_name(item) for item in function.get("Return") or [] if type_name(item)]
    result = f"{function.get('Name', 'function')}({', '.join(params)})"
    return result + (f" -> {', '.join(returns)}" if returns else "")


def render_fields(title: str, fields: list[dict[str, Any]]) -> list[str]:
    if not fields:
        return []
    lines = [f"## {title}", "", "| Name | Type/Value | Description |", "|---|---|---|"]
    for field in fields:
        lines.append(
            f"| `{table_cell(field.get('Name'))}` | `{table_cell(type_name(field))}` | "
            f"{table_cell(field.get('Description'))} |"
        )
    lines.append("")
    return lines


def render_functions(functions: list[dict[str, Any]], title: str = "Functions") -> list[str]:
    if not functions:
        return []
    lines = [f"## {title}", ""]
    for function in functions:
        name = str(function.get("Name") or "Function")
        lines.extend([f"### `{name}`", "", "```text", signature(function), "```", ""])
        details = description(function.get("Description"))
        if details:
            lines.extend([details, ""])
        params = function.get("Params") or []
        if params:
            lines.extend(["**Parameters**", "", "| Name | Type | Description |", "|---|---|---|"])
            for param in params:
                lines.append(
                    f"| `{table_cell(param.get('Name'))}` | `{table_cell(type_name(param))}` | "
                    f"{table_cell(param.get('Description'))} |"
                )
            lines.append("")
        returns = function.get("Return") or []
        if returns:
            lines.extend(["**Returns**", "", "| Type | Description |", "|---|---|"])
            for item in returns:
                lines.append(
                    f"| `{table_cell(type_name(item))}` | {table_cell(item.get('Description'))} |"
                )
            lines.append("")
    return lines


def markdown_document(entry: dict[str, Any], data: dict[str, Any]) -> str:
    title = str(data.get("Name") or entry["name"])
    category_parts = ["API Wiki", entry["kind"], *entry["categories"]]
    metadata = {
        "id": entry["id"],
        "title": title,
        "source": entry["url"],
        "category": "/".join(category_parts),
        "kind": entry["kind"],
        "api_root": entry["api_root"],
    }
    lines = ["---"]
    lines.extend(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items())
    lines.extend(["---", "", f"# {title}", ""])
    details = description(data.get("Description"))
    if details:
        lines.extend([details, ""])
    parents = data.get("Parents") or []
    if parents:
        lines.extend(["## Inheritance", "", " -> ".join(f"`{parent}`" for parent in parents), ""])
    lines.extend(render_fields("Variables", data.get("Variables") or []))
    lines.extend(render_functions(data.get("Functions") or []))
    lines.extend(render_functions(data.get("Event") or [], "Events"))
    lines.extend(render_functions(data.get("Delegate") or [], "Delegates"))
    if entry["kind"] == "globalfunc" and not data.get("Functions"):
        lines.extend(render_functions([data]))
    language = description(data.get("Language"))
    if language:
        lines.extend(["## Language", "", f"`{language}`", ""])
    known = {
        "Name", "Description", "Variables", "Functions", "Event", "Delegate",
        "Parents", "Language", "Params", "Return"
    }
    extras = {key: value for key, value in data.items() if key not in known and value not in (None, "", [], {})}
    if extras:
        lines.extend(["## Additional Data", "", "```json", json.dumps(extras, ensure_ascii=False, indent=2), "```", ""])
    return "\n".join(lines).rstrip() + "\n"


def document_path(output_dir: Path, entry: dict[str, Any]) -> Path:
    path = output_dir / "documents" / entry["kind"]
    for category in entry["categories"]:
        path /= safe_segment(category)
    return path / f"{safe_segment(entry['name'])}.md"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def crawl_one(entry: dict[str, Any], output_dir: Path, timeout: int, force: bool) -> dict[str, Any]:
    path = document_path(output_dir, entry)
    relative = path.relative_to(output_dir).as_posix()
    if path.is_file() and not force:
        document = path.read_text(encoding="utf-8")
        return {**entry, "status": "cached", "file": relative, "sha256": sha256_text(document)}
    data = fetch_json(entry["url"], timeout)
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected an object from {entry['url']}")
    document = markdown_document(entry, data)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")
    return {**entry, "status": "ok", "file": relative, "sha256": sha256_text(document)}


def strip_frontmatter(document: str) -> str:
    if document.startswith("---\n"):
        end = document.find("\n---\n", 4)
        if end >= 0:
            return document[end + 5 :].lstrip()
    return document


def build_chunks(output_dir: Path, manifest: list[dict[str, Any]], max_chars: int) -> int:
    chunks_dir = output_dir / "chunks"
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in manifest:
        if item.get("status") in {"ok", "cached"}:
            grouped.setdefault(item["kind"], []).append(item)
    count = 0
    expected: set[Path] = set()
    for kind, items in sorted(grouped.items()):
        parts: list[str] = []
        size = 0
        number = 1
        for item in sorted(items, key=lambda value: value["name"].casefold()):
            body = strip_frontmatter((output_dir / item["file"]).read_text(encoding="utf-8"))
            section = f"<!-- Source: {item['url']} -->\n\n{body}\n"
            if parts and size + len(section) > max(50_000, max_chars):
                target = chunks_dir / kind / f"{kind}_{number:03d}.md"
                write_chunk(target, kind, number, parts)
                expected.add(target.resolve())
                count += 1
                number += 1
                parts, size = [], 0
            parts.append(section)
            size += len(section)
        if parts:
            target = chunks_dir / kind / f"{kind}_{number:03d}.md"
            write_chunk(target, kind, number, parts)
            expected.add(target.resolve())
            count += 1
    if chunks_dir.exists():
        for path in chunks_dir.rglob("*.md"):
            if path.resolve() not in expected:
                path.unlink()
    return count


def write_chunk(path: Path, kind: str, number: int, parts: list[str]) -> None:
    header = (
        "---\n"
        f"id: {json.dumps(f'api-chunk:{kind}:{number}', ensure_ascii=False)}\n"
        f"title: {json.dumps(f'Oasis API {kind} chunk {number}', ensure_ascii=False)}\n"
        f"source: {json.dumps(DEFAULT_URL)}\n"
        f"category: {json.dumps(f'API Wiki/{kind}', ensure_ascii=False)}\n"
        "kind: \"api_chunk\"\n"
        "---\n\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + "\n---\n\n".join(parts), encoding="utf-8")


def prune_documents(output_dir: Path, entries: list[dict[str, Any]]) -> int:
    root = (output_dir / "documents").resolve()
    if not root.exists():
        return 0
    expected = {document_path(output_dir, entry).resolve() for entry in entries}
    removed = 0
    for path in root.rglob("*.md"):
        resolved = path.resolve()
        if root not in resolved.parents:
            raise RuntimeError(f"Refusing to prune outside {root}: {resolved}")
        if resolved not in expected:
            path.unlink()
            removed += 1
    return removed


def main() -> int:
    configure_console()
    args = parse_args()
    base_url = args.url.rstrip("/") + "/"
    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    kinds = args.kind or list(INDEXES)
    entries = discover(base_url, kinds, max(1, args.timeout))
    if args.limit > 0:
        entries = entries[: args.limit]
    for entry in entries:
        entry["file"] = document_path(output_dir, entry).relative_to(output_dir).as_posix()
    write_json(output_dir / "catalog.json", entries)
    print(f"Discovered {len(entries)} API documents")
    if args.discover_only:
        return 0
    if args.prune_output:
        print(f"Pruned {prune_documents(output_dir, entries)} stale documents")

    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, min(32, args.workers))) as executor:
        futures = {
            executor.submit(crawl_one, entry, output_dir, max(1, args.timeout), args.force): entry
            for entry in entries
        }
        for index, future in enumerate(as_completed(futures), start=1):
            entry = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {**entry, "status": "failed", "error": str(exc)}
                print(f"  failed: {entry['kind']}/{entry['name']}: {exc}", file=sys.stderr)
            results.append(result)
            if index % 100 == 0 or index == len(entries):
                print(f"[{index}/{len(entries)}] completed")
                write_json(output_dir / "manifest.json", sorted(results, key=lambda x: x["id"]))

    results.sort(key=lambda item: item["id"])
    write_json(output_dir / "manifest.json", results)
    chunk_count = build_chunks(output_dir, results, args.chunk_chars)
    succeeded = sum(item["status"] in {"ok", "cached"} for item in results)
    failed = len(results) - succeeded
    summary = {
        "api_root": base_url,
        "total": len(results),
        "succeeded": succeeded,
        "failed": failed,
        "chunks": chunk_count,
        "by_kind": {
            kind: sum(item["kind"] == kind and item["status"] in {"ok", "cached"} for item in results)
            for kind in kinds
        },
    }
    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

