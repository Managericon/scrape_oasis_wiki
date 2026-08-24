# Knowledge Base Maintenance

Read only when the user explicitly asks to refresh, crawl, sync, rebuild, or troubleshoot indexing.

## Assets

- Repository: `https://github.com/Managericon/scrape_oasis_wiki`
- Workflow: `.github/workflows/crawl-and-index.yml`
- Corpus: `knowledge/articles`
- Catalog: `knowledge/catalog.json`
- Crawl state: `knowledge/manifest.json`
- Vector Store state: `knowledge/vector_store.json`
- Entry catalog: `https://developer.gp.qq.com/wikieditor/#/catalog/20418`

## Refresh Sequence

1. Run the JavaScript crawler and require all catalog leaves to complete.
2. Verify article count, failed count, image references, code fences, and extraction selector.
3. Sync changed Markdown files to the existing Vector Store using the committed state file.
4. Commit refreshed Markdown, manifest, catalog, and Vector Store state.
5. Upload the knowledge artifact even when a later step fails.

Repository commands:

```powershell
python -u scripts/crawl_wiki.py --output-dir knowledge --force --prune-output
python scripts/vector_store.py --state knowledge/vector_store.json sync --directory knowledge/articles --prune
```

## Invariants

- Use JavaScript rendering and recursively expand `.el-tree`.
- Derive article routes from leaf `data-key` values.
- Prefer `.github-markdown-body`; keep only documented fallback selectors.
- Preserve code fences, image URLs, source URLs, article IDs, and category paths.
- Exclude navigation, `.articleTop`, search UI, and sidebar text.
- Reuse the committed `vector_store_id`; do not create a new store when state recovery is possible.
- `OPENAI_API_KEY` is a secret. Never print, paste into chat, write to files, or commit it.

## Success Criteria

- Crawl reports all expected articles saved.
- Vector sync reports zero failures.
- `knowledge/vector_store.json` contains the store ID and one entry per indexed article.
- A second unchanged run skips every indexed file.

