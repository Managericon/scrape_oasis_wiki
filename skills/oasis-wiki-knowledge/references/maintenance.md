# Knowledge Base Maintenance

Read only when the user explicitly asks to refresh, crawl, sync, rebuild, or troubleshoot indexing.

## Assets

- Repository: `https://github.com/Managericon/scrape_oasis_wiki`
- Workflow: `.github/workflows/crawl-and-index.yml`
- Corpus: `knowledge/articles`
- API corpus: `knowledge/api/documents`
- API Vector Store chunks: `knowledge/api/chunks`
- Catalog: `knowledge/catalog.json`
- API catalog: `knowledge/api/catalog.json`
- Crawl state: `knowledge/manifest.json`
- Vector Store state: `knowledge/vector_store.json`
- Entry catalog: `https://developer.gp.qq.com/wikieditor/#/catalog/20418`
- API root: `https://developer.gp.qq.com/api/#/`

## Refresh Sequence

1. Run the JavaScript tutorial crawler and the static JSON API crawler.
2. Verify tutorial article count plus API class, enum, struct, global-function, failure, and chunk counts.
3. Sync tutorial articles and API chunks to the existing Vector Store using the committed state file.
4. Commit refreshed Markdown, manifest, catalog, and Vector Store state.
5. Upload the knowledge artifact even when a later step fails.

Repository commands:

```powershell
python -u scripts/crawl_wiki.py --output-dir knowledge --force --prune-output
python -u scripts/crawl_api_wiki.py --output-dir knowledge/api --force --prune-output
python scripts/vector_store.py --state knowledge/vector_store.json sync --directory knowledge/articles --directory knowledge/api/chunks --prune
```

## Invariants

- Use JavaScript rendering and recursively expand `.el-tree`.
- Derive article routes from leaf `data-key` values.
- Prefer `.github-markdown-body`; keep only documented fallback selectors.
- Preserve code fences, image URLs, source URLs, article IDs, and category paths.
- Exclude navigation, `.articleTop`, search UI, and sidebar text.
- Discover API detail paths from the official static sorted-list JSON files; do not guess API names or routes.
- Preserve one Markdown file per API item and use generated chunks only for Vector Store upload.
- Reuse the committed `vector_store_id`; do not create a new store when state recovery is possible.
- `OPENAI_API_KEY` is a secret. Never print, paste into chat, write to files, or commit it.

## Success Criteria

- Crawl reports all expected tutorial articles and API documents saved with zero failures.
- API summary counts match its catalog and generated Markdown files.
- Vector sync reports zero failures.
- `knowledge/vector_store.json` contains the store ID and one entry per indexed article.
- A second unchanged run skips every indexed file.

