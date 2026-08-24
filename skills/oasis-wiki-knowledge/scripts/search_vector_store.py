#!/usr/bin/env python3
"""Search the Oasis Wiki Vector Store with a bounded context budget."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INFO = SKILL_ROOT / "references" / "knowledge-base.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--vector-store-id", default=os.getenv("OASIS_VECTOR_STORE_ID"))
    parser.add_argument("--state", type=Path)
    parser.add_argument("--max-results", type=int, default=5)
    parser.add_argument("--context-chars", type=int, default=900)
    parser.add_argument("--max-total-chars", type=int, default=6000)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def discover_state(explicit: Path | None) -> Path | None:
    if explicit:
        return explicit.expanduser().resolve()
    for parent in (Path.cwd(), *Path.cwd().parents):
        candidate = parent / "knowledge" / "vector_store.json"
        if candidate.is_file():
            return candidate
    return None


def default_store_id() -> str | None:
    if not DEFAULT_INFO.is_file():
        return None
    return json.loads(DEFAULT_INFO.read_text(encoding="utf-8")).get("vector_store_id")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args()
    vector_store_id = args.vector_store_id
    state_path = discover_state(args.state)
    if not vector_store_id and state_path and state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        vector_store_id = state.get("vector_store_id")
    vector_store_id = vector_store_id or default_store_id()
    if not vector_store_id:
        raise RuntimeError("Set OASIS_VECTOR_STORE_ID or provide a Vector Store state file")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install the OpenAI SDK with: pip install openai") from exc

    results = OpenAI().vector_stores.search(
        vector_store_id,
        query=args.query,
        max_num_results=max(1, min(50, args.max_results)),
        rewrite_query=True,
    )
    rendered_results = []
    used = 0
    for result in results.data:
        attributes = result.attributes or {}
        title = attributes.get("title") or result.filename
        excerpt = "\n\n".join(item.text for item in result.content if item.type == "text")
        excerpt = excerpt[: max(200, args.context_chars)]
        item = {
            "title": title,
            "score": result.score,
            "source": attributes.get("source", ""),
            "category": attributes.get("category", ""),
            "excerpt": excerpt,
        }
        size = len(json.dumps(item, ensure_ascii=False))
        if used + size > max(1000, args.max_total_chars):
            break
        rendered_results.append(item)
        used += size
    if args.json:
        print(json.dumps(rendered_results, ensure_ascii=False, indent=2))
        return 0
    for index, item in enumerate(rendered_results, start=1):
        print(f"## {index}. {item['title']} (score: {item['score']:.3f})")
        if item["category"]:
            print(f"Category: {item['category']}")
        if item["source"]:
            print(f"Source: {item['source']}")
        print()
        print(item["excerpt"])
        print()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

