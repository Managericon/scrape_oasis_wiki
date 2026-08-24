---
name: oasis-wiki-knowledge
description: Search and refresh the Tencent Oasis/绿洲启元 Wiki knowledge base. Use for questions that need current official Wiki evidence, semantic retrieval from the crawled Markdown corpus, or maintenance of the developer.gp.qq.com catalog 20418 crawl and Vector Store.
---

# Oasis Wiki Knowledge

Use the crawled official Wiki as the primary evidence source for Oasis editor, UGC Lua,
gameplay systems, templates, debugging, and release-note questions.

## Search

1. If `knowledge/articles` exists in the current repository, search those Markdown files
   with `rg` first and open only the most relevant documents.
2. Otherwise run `scripts/search_vector_store.py "<query>"`. It reads the Vector Store ID
   from `OASIS_VECTOR_STORE_ID` or a `knowledge/vector_store.json` state file.
3. Base the answer on retrieved text and include the original `Source` URL when present.
4. If retrieval returns weak or conflicting evidence, say so and search with a narrower
   API, class, editor feature, or error-message keyword.

## Refresh

Only mutate the remote Vector Store or crawl the public site when the user asks to refresh,
sync, or rebuild the knowledge base. From this repository, run:

```powershell
python scripts/crawl_wiki.py --output-dir knowledge --force
python scripts/vector_store.py --state knowledge/vector_store.json sync --directory knowledge/articles --prune
```

The crawler must use JavaScript rendering, recursively expand `.el-tree`, derive article
routes from leaf-node `data-key` values, and extract `.github-markdown-body` before any
fallback selector. Preserve fenced code blocks, Markdown images, source URLs, article IDs,
and category paths. Never index navigation, `.articleTop`, search UI, or sidebar text.

Vector Store writes require `OPENAI_API_KEY`. Do not print, store, or commit the key.

