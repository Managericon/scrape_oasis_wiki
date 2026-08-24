#!/usr/bin/env python3
"""Search the Oasis Wiki Vector Store and print source-bearing excerpts."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--vector-store-id", default=os.getenv("OASIS_VECTOR_STORE_ID"))
    parser.add_argument("--state", type=Path, default=Path("knowledge/vector_store.json"))
    parser.add_argument("--max-results", type=int, default=8)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vector_store_id = args.vector_store_id
    if not vector_store_id and args.state.exists():
        state = json.loads(args.state.read_text(encoding="utf-8"))
        vector_store_id = state.get("vector_store_id")
    if not vector_store_id:
        raise RuntimeError("Set OASIS_VECTOR_STORE_ID or provide a Vector Store state file")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set")

    results = OpenAI().vector_stores.search(
        vector_store_id,
        query=args.query,
        max_num_results=max(1, min(50, args.max_results)),
        rewrite_query=True,
    )
    for index, result in enumerate(results.data, start=1):
        attributes = result.attributes or {}
        title = attributes.get("title") or result.filename
        print(f"## {index}. {title} (score: {result.score:.3f})")
        if attributes.get("source"):
            print(f"Source: {attributes['source']}")
        print()
        print("\n\n".join(item.text for item in result.content if item.type == "text"))
        print()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

