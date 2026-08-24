#!/usr/bin/env python3
"""Compact lexical search for a local Oasis Wiki corpus or bundled catalog."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = SKILL_ROOT / "references" / "catalog.json"
ALIASES = {
    "怪物": ("monster", "AI", "行为树", "黑板"),
    "技能": ("skill", "PESkill", "技能编辑器", "技能Task"),
    "抛体": ("projectile", "发射抛体"),
    "日志": ("log", "DSlog", "Clientlog", "PIE"),
    "断线": ("重连", "reconnect", "弱网"),
    "界面": ("UI", "Widget", "UMG", "控件"),
    "输入": ("InputAction", "输入映射", "GameplayTag"),
    "网络": ("replication", "RPC", "同步"),
}
KNOWN_TERMS = tuple(ALIASES)


@dataclass
class Hit:
    score: float
    title: str
    category: str
    source: str
    path: str
    excerpt: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--max-results", type=int, default=5)
    parser.add_argument("--context-chars", type=int, default=700)
    parser.add_argument("--max-total-chars", type=int, default=5000)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def discover_articles(explicit: Path | None) -> Path | None:
    candidates: list[Path] = []
    if explicit:
        candidates.append(explicit)
    if os.getenv("OASIS_WIKI_DIR"):
        candidates.append(Path(os.environ["OASIS_WIKI_DIR"]))
    for parent in (Path.cwd(), *Path.cwd().parents):
        candidates.append(parent / "knowledge" / "articles")
    for candidate in candidates:
        expanded = candidate.expanduser().resolve()
        if expanded.name == "knowledge" and (expanded / "articles").is_dir():
            expanded = expanded / "articles"
        if expanded.is_dir() and next(expanded.rglob("*.md"), None):
            return expanded
    return None


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if separator:
            raw = value.strip()
            try:
                raw = str(json.loads(raw))
            except json.JSONDecodeError:
                pass
            data[key.strip()] = raw
    return data, text[end + 5 :]


def configure_console() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def query_terms(query: str) -> tuple[list[str], list[str]]:
    normalized = query.strip().casefold()
    primary = [normalized]
    primary.extend(term.casefold() for term in KNOWN_TERMS if term in query)
    primary.extend(re.findall(r"[A-Za-z_][\w.]*|\d+", query.casefold()))
    aliases: list[str] = []
    for key, values in ALIASES.items():
        if key in query:
            aliases.extend(value.casefold() for value in values)
    return list(dict.fromkeys(filter(None, primary))), list(dict.fromkeys(filter(None, aliases)))


def count_score(text: str, terms: Iterable[str], weight: float, cap: int = 3) -> float:
    lowered = text.casefold()
    return sum(min(lowered.count(term), cap) * weight for term in terms)


def combination_bonus(fields: Iterable[str], primary: list[str]) -> float:
    meaningful = [term for term in primary if term in KNOWN_TERMS]
    if len(meaningful) < 2:
        return 0
    combined = "\n".join(fields).casefold()
    matches = sum(term in combined for term in meaningful)
    return 30.0 if matches >= 2 else 0


def compact_excerpt(body: str, terms: list[str], size: int) -> str:
    body = re.sub(r"^!\[[^\]]*\]\([^)]*\)\s*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    lowered = body.casefold()
    positions = [lowered.find(term) for term in terms if lowered.find(term) >= 0]
    center = min(positions) if positions else 0
    start = max(0, center - size // 3)
    end = min(len(body), start + size)
    if start:
        start = body.find("\n", start)
        start = start + 1 if start >= 0 else 0
    if end < len(body):
        boundary = body.rfind("\n", start, end)
        end = boundary if boundary > start else end
    excerpt = body[start:end].strip()
    return ("...\n" if start else "") + excerpt + ("\n..." if end < len(body) else "")


def local_hits(
    directory: Path, primary: list[str], aliases: list[str], context_chars: int
) -> list[Hit]:
    hits: list[Hit] = []
    for path in directory.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        meta, body = frontmatter(text)
        title = meta.get("title") or path.stem
        category = meta.get("category") or path.parent.relative_to(directory).as_posix()
        headings = "\n".join(re.findall(r"^#{1,4}\s+(.+)$", body, flags=re.MULTILINE))
        score = (
            count_score(title, primary, 20)
            + count_score(category, primary, 10)
            + count_score(headings, primary, 8)
            + count_score(body, primary, 1)
            + count_score(title, aliases, 4, cap=1)
            + count_score(category, aliases, 2, cap=1)
            + count_score(headings, aliases, 2, cap=1)
            + count_score(body, aliases, 0.15, cap=2)
            + combination_bonus((title, category, headings), primary)
        )
        if score <= 0:
            continue
        hits.append(
            Hit(
                score=score,
                title=title,
                category=category,
                source=meta.get("source", ""),
                path=str(path),
                excerpt=compact_excerpt(body, primary + aliases, context_chars),
            )
        )
    return sorted(hits, key=lambda hit: (-hit.score, hit.title))


def catalog_hits(catalog: Path, primary: list[str], aliases: list[str]) -> list[Hit]:
    entries = json.loads(catalog.read_text(encoding="utf-8"))
    hits: list[Hit] = []
    for entry in entries:
        title = str(entry.get("title", ""))
        category = "/".join(entry.get("categories") or [])
        score = (
            count_score(title, primary, 20)
            + count_score(category, primary, 10)
            + count_score(title, aliases, 4, cap=1)
            + count_score(category, aliases, 2, cap=1)
            + combination_bonus((title, category), primary)
        )
        if score <= 0:
            continue
        hits.append(
            Hit(
                score=score,
                title=title,
                category=category,
                source=str(entry.get("url", "")),
                path=str(entry.get("file", "")),
            )
        )
    return sorted(hits, key=lambda hit: (-hit.score, hit.title))


def render(hits: list[Hit], total_limit: int) -> str:
    chunks: list[str] = []
    used = 0
    for index, hit in enumerate(hits, start=1):
        chunk = [f"## {index}. {hit.title} (score: {hit.score:g})"]
        if hit.category:
            chunk.append(f"Category: {hit.category}")
        if hit.source:
            chunk.append(f"Source: {hit.source}")
        if hit.path:
            chunk.append(f"Path: {hit.path}")
        if hit.excerpt:
            chunk.extend(("", hit.excerpt))
        rendered = "\n".join(chunk) + "\n"
        if used + len(rendered) > total_limit:
            break
        chunks.append(rendered)
        used += len(rendered)
    return "\n".join(chunks)


def main() -> int:
    configure_console()
    args = parse_args()
    primary, aliases = query_terms(args.query)
    directory = discover_articles(args.directory)
    if directory:
        hits = local_hits(directory, primary, aliases, max(200, args.context_chars))
        mode = f"local:{directory}"
    elif args.catalog.is_file():
        hits = catalog_hits(args.catalog, primary, aliases)
        mode = f"catalog:{args.catalog}"
    else:
        raise RuntimeError("No local knowledge/articles directory or bundled catalog found")
    hits = hits[: max(1, min(12, args.max_results))]
    if args.json:
        print(json.dumps({"mode": mode, "results": [asdict(hit) for hit in hits]}, ensure_ascii=False, indent=2))
    else:
        print(f"Mode: {mode}")
        print(render(hits, max(1000, args.max_total_chars)))
    return 0 if hits else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

