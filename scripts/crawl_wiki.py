#!/usr/bin/env python3
"""Deep-crawl the JavaScript-rendered Tencent Oasis Wiki into Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

import html2text
from playwright.sync_api import BrowserContext, Locator, Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


DEFAULT_URL = "https://developer.gp.qq.com/wikieditor/#/catalog/20418"
CONTENT_SELECTORS = (
    ".github-markdown-body",
    ".article-content",
    "#wiki-content",
    ".v-md-editor-preview",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output-dir", type=Path, default=Path("knowledge"))
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--delay", type=float, default=0.25)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--article-id", action="append", default=[])
    parser.add_argument("--discover-only", action="store_true")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--force", action="store_true", help="Refresh existing files")
    parser.add_argument(
        "--prune-output", action="store_true", help="Remove Markdown no longer in the catalog"
    )
    parser.add_argument("--download-images", action="store_true")
    parser.add_argument("--browser-executable")
    return parser.parse_args()


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def safe_segment(value: str, fallback: str = "uncategorized") -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", clean_text(value))
    return value.strip(" .")[:100] or fallback


def find_visible_content(page: Page, timeout_ms: int) -> tuple[Locator, str]:
    deadline = time.monotonic() + timeout_ms / 1000
    while time.monotonic() < deadline:
        for selector in CONTENT_SELECTORS:
            candidates = page.locator(selector)
            for index in range(candidates.count()):
                candidate = candidates.nth(index)
                try:
                    if candidate.is_visible() and candidate.inner_text().strip():
                        return candidate, selector
                except Exception:
                    continue
        page.wait_for_timeout(250)
    raise RuntimeError("Article content not found: " + ", ".join(CONTENT_SELECTORS))


def expand_entire_tree(page: Page, timeout_ms: int) -> None:
    page.locator(".el-tree").wait_for(state="visible", timeout=timeout_ms)
    page.locator(".el-tree-node__expand-icon.is-leaf").first.wait_for(
        state="attached", timeout=timeout_ms
    )
    stable_rounds = 0
    previous_count = -1
    for _ in range(2_000):
        icons = page.locator(
            ".el-tree-node__expand-icon:not(.is-leaf):not(.expanded)"
        )
        clicked = False
        for index in range(icons.count()):
            icon = icons.nth(index)
            try:
                if icon.is_visible():
                    icon.scroll_into_view_if_needed(timeout=2_000)
                    icon.click(timeout=2_000)
                    page.wait_for_timeout(100)
                    clicked = True
                    stable_rounds = 0
                    break
            except Exception:
                continue
        if not clicked:
            page.wait_for_timeout(500)
            current_count = page.locator(".el-tree-node[data-key]").count()
            stable_rounds = stable_rounds + 1 if current_count == previous_count else 0
            previous_count = current_count
            if stable_rounds >= 3:
                return
    raise RuntimeError("Directory expansion exceeded the 2000-node safety limit")


def discover_articles(page: Page, url: str, timeout_ms: int) -> list[dict[str, Any]]:
    page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
    expand_entire_tree(page, timeout_ms)
    articles = page.locator(".el-tree").evaluate(
        """(tree) => {
            const directLabel = (node) => (node.querySelector(
                ':scope > .el-tree-node__content .catalog-lebel-text, ' +
                ':scope > .el-tree-node__content .el-tree-node__label'
            )?.textContent || '').trim();
            return [...tree.querySelectorAll('.el-tree-node[data-key]')]
                .filter(node => node.querySelector(
                    ':scope > .el-tree-node__content > .el-tree-node__expand-icon.is-leaf'
                ))
                .map(node => {
                    const categories = [];
                    let parent = node.parentElement?.closest('.el-tree-node[data-key]');
                    while (parent) {
                        const label = directLabel(parent);
                        if (label) categories.unshift(label);
                        parent = parent.parentElement?.closest('.el-tree-node[data-key]');
                    }
                    return {
                        id: node.getAttribute('data-key'),
                        title: directLabel(node),
                        categories
                    };
                })
                .filter(article => article.id && article.title);
        }"""
    )
    base = url.split("#", 1)[0]
    for article in articles:
        article["url"] = f"{base}#/catalog/{article['id']}"
    unique = {article["id"]: article for article in articles}
    return list(unique.values())


def wait_for_article(page: Page, article_id: str, previous_html: str, timeout_ms: int) -> None:
    page.wait_for_function(
        """id => document.querySelector(
            `.el-tree-node[data-key="${CSS.escape(id)}"].is-current`
        ) !== null""",
        arg=article_id,
        timeout=timeout_ms,
    )
    if previous_html:
        try:
            page.wait_for_function(
                """([selector, oldHtml]) => {
                    const node = document.querySelector(selector);
                    return node && node.innerHTML !== oldHtml && node.innerText.trim();
                }""",
                arg=[CONTENT_SELECTORS[0], previous_html],
                timeout=min(timeout_ms, 10_000),
            )
        except PlaywrightTimeoutError:
            pass
    page.wait_for_timeout(250)


def extract_content(page: Page, timeout_ms: int) -> dict[str, Any]:
    content, selector = find_visible_content(page, timeout_ms)
    extracted = content.evaluate(
        """(root) => {
            const clone = root.cloneNode(true);
            clone.querySelectorAll('script, style, noscript').forEach(el => el.remove());

            const codeBlocks = [];
            clone.querySelectorAll('pre').forEach((pre, index) => {
                const code = pre.querySelector('code');
                const classes = `${code?.className || ''} ${pre.className || ''}`;
                const language = classes.match(/(?:language-|lang-)([\\w+-]+)/i)?.[1] || '';
                const token = `CODEBLOCKTOKEN${String(index).padStart(6, '0')}END`;
                codeBlocks.push({
                    token,
                    language,
                    code: (code || pre).textContent.replace(/\\n$/, '')
                });
                const marker = document.createElement('p');
                marker.textContent = token;
                pre.replaceWith(marker);
            });

            const images = [];
            clone.querySelectorAll('img').forEach((image) => {
                const source = image.getAttribute('src') || image.getAttribute('data-src') ||
                    image.getAttribute('data-original');
                if (!source) {
                    image.remove();
                    return;
                }
                let absolute;
                try {
                    absolute = new URL(source, location.href).href;
                } catch {
                    image.remove();
                    return;
                }
                image.setAttribute('src', absolute);
                image.removeAttribute('srcset');
                images.push({url: absolute, alt: image.getAttribute('alt') || ''});
            });
            clone.querySelectorAll('a[href]').forEach((link) => {
                try {
                    link.setAttribute(
                        'href', new URL(link.getAttribute('href'), location.href).href
                    );
                } catch {
                    link.removeAttribute('href');
                }
            });
            return {html: clone.innerHTML, codeBlocks, images};
        }"""
    )
    extracted["selector"] = selector
    return extracted


def fenced_code(code: str, language: str) -> str:
    longest = max((len(run) for run in re.findall(r"`+", code)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}{language}\n{code.rstrip()}\n{fence}"


def html_to_markdown(extracted: dict[str, Any]) -> str:
    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_images = False
    converter.ignore_links = False
    converter.inline_links = True
    converter.protect_links = True
    converter.unicode_snob = True
    converter.wrap_links = False
    markdown = converter.handle(extracted["html"])
    for block in extracted["codeBlocks"]:
        markdown = markdown.replace(
            block["token"], fenced_code(block["code"], block["language"])
        )
    markdown = "\n".join(line.rstrip() for line in markdown.splitlines())
    return re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"


def image_extension(url: str, content_type: str | None) -> str:
    suffix = Path(unquote(urlparse(url).path)).suffix.lower()
    if re.fullmatch(r"\.[a-z0-9]{1,5}", suffix):
        return suffix
    mime = (content_type or "").split(";", 1)[0].strip()
    return mimetypes.guess_extension(mime) or ".bin"


def localize_images(
    context: BrowserContext,
    markdown: str,
    images: list[dict[str, str]],
    article_id: str,
    output_dir: Path,
    article_file: Path,
) -> str:
    image_dir = output_dir / "assets" / safe_segment(article_id)
    seen: set[str] = set()
    number = 0
    for image in images:
        url = image["url"]
        if url in seen or url.startswith("data:"):
            continue
        seen.add(url)
        try:
            response = context.request.get(url, timeout=30_000)
            if not response.ok:
                continue
            number += 1
            filename = f"image_{number:03d}{image_extension(url, response.headers.get('content-type'))}"
            image_dir.mkdir(parents=True, exist_ok=True)
            target = image_dir / filename
            target.write_bytes(response.body())
            relative = os.path.relpath(target, article_file.parent).replace("\\", "/")
            markdown = markdown.replace(url, relative)
        except Exception as exc:
            print(f"  image failed: {url} ({exc})", file=sys.stderr)
    return markdown


def article_path(output_dir: Path, article: dict[str, Any]) -> Path:
    directory = output_dir / "articles"
    for category in article["categories"]:
        directory /= safe_segment(category)
    return directory / f"{safe_segment(article['id'])}_{safe_segment(article['title'])}.md"


def build_document(article: dict[str, Any], body: str) -> str:
    categories = "/".join(article["categories"])
    metadata = (
        "---\n"
        f"id: {json.dumps(str(article['id']), ensure_ascii=False)}\n"
        f"title: {json.dumps(article['title'], ensure_ascii=False)}\n"
        f"source: {json.dumps(article['url'], ensure_ascii=False)}\n"
        f"category: {json.dumps(categories, ensure_ascii=False)}\n"
        "---\n\n"
    )
    body = body.strip()
    first = body.splitlines()[0] if body else ""
    if re.sub(r"^#+\s*", "", first).strip() != article["title"]:
        body = f"# {article['title']}\n\n{body}"
    return metadata + body + "\n"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def prune_stale_articles(output_dir: Path, articles: list[dict[str, Any]]) -> int:
    article_dir = (output_dir / "articles").resolve()
    if not article_dir.exists():
        return 0
    expected = {article_path(output_dir, article).resolve() for article in articles}
    removed = 0
    for path in article_dir.rglob("*.md"):
        resolved = path.resolve()
        if article_dir not in resolved.parents:
            raise RuntimeError(f"Refusing to prune path outside article directory: {resolved}")
        if resolved not in expected:
            path.unlink()
            removed += 1
    return removed


def crawl_articles(
    page: Page,
    context: BrowserContext,
    articles: list[dict[str, Any]],
    output_dir: Path,
    timeout_ms: int,
    delay: float,
    force: bool,
    download_images: bool,
) -> list[dict[str, Any]]:
    manifest: list[dict[str, Any]] = []
    combined: list[str] = []
    previous_html = ""

    for index, article in enumerate(articles, start=1):
        path = article_path(output_dir, article)
        relative_path = path.relative_to(output_dir).as_posix()
        print(f"[{index}/{len(articles)}] {article['title']}")
        if path.exists() and not force:
            document = path.read_text(encoding="utf-8")
            combined.append(document)
            manifest.append(
                {**article, "status": "cached", "file": relative_path, "sha256": sha256_text(document)}
            )
            continue

        error = None
        for attempt in range(1, 4):
            try:
                page.goto(article["url"], wait_until="domcontentloaded", timeout=timeout_ms)
                wait_for_article(page, str(article["id"]), previous_html, timeout_ms)
                extracted = extract_content(page, timeout_ms)
                previous_html = extracted["html"]
                body = html_to_markdown(extracted)
                path.parent.mkdir(parents=True, exist_ok=True)
                if download_images:
                    body = localize_images(
                        context, body, extracted["images"], str(article["id"]), output_dir, path
                    )
                document = build_document(article, body)
                path.write_text(document, encoding="utf-8")
                combined.append(document)
                manifest.append(
                    {
                        **article,
                        "status": "ok",
                        "file": relative_path,
                        "selector": extracted["selector"],
                        "images": len(extracted["images"]),
                        "code_blocks": len(extracted["codeBlocks"]),
                        "sha256": sha256_text(document),
                    }
                )
                error = None
                break
            except Exception as exc:
                error = str(exc)
                print(f"  attempt {attempt}/3 failed: {error}", file=sys.stderr)
                page.wait_for_timeout(attempt * 750)
        if error:
            manifest.append({**article, "status": "failed", "error": error})
        write_json(output_dir / "manifest.json", manifest)
        if delay > 0:
            page.wait_for_timeout(int(delay * 1_000))

    (output_dir / "all_articles.md").write_text(
        "\n\n---\n\n".join(combined), encoding="utf-8"
    )
    return manifest


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    timeout_ms = max(1, args.timeout) * 1_000
    launch_options: dict[str, Any] = {"headless": not args.headed}
    if args.browser_executable:
        launch_options["executable_path"] = args.browser_executable

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(**launch_options)
        context = browser.new_context(locale="zh-CN", viewport={"width": 1440, "height": 1000})
        page = context.new_page()
        try:
            articles = discover_articles(page, args.url, timeout_ms)
            if args.article_id:
                requested = set(args.article_id)
                articles = [article for article in articles if article["id"] in requested]
            if args.limit > 0:
                articles = articles[: args.limit]
            if not articles:
                raise RuntimeError("No leaf articles discovered in the sidebar")
            write_json(output_dir / "catalog.json", articles)
            if args.discover_only:
                print(f"Discovered {len(articles)} articles")
                return 0
            if args.prune_output:
                print(f"Pruned {prune_stale_articles(output_dir, articles)} stale articles")
            manifest = crawl_articles(
                page,
                context,
                articles,
                output_dir,
                timeout_ms,
                max(0, args.delay),
                args.force,
                args.download_images,
            )
        finally:
            context.close()
            browser.close()

    succeeded = sum(item["status"] in ("ok", "cached") for item in manifest)
    print(f"Saved {succeeded}/{len(manifest)} articles to {output_dir}")
    return 0 if succeeded == len(manifest) else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

