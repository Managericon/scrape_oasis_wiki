---
name: oasis-wiki-knowledge
description: Retrieve current official Tencent Oasis/绿洲启元 tutorial Wiki and API reference evidence with low-context local, catalog, or Vector Store search, with an optional UGCAskQ MCP proxy for live editor state. Use for Wiki-backed API, class, function, enum, struct, editor, Lua, debugging, template, release-note, and knowledge-base maintenance questions; do not use for unrelated general programming.
---

# Oasis Wiki Knowledge

Retrieve the smallest sufficient set of official Wiki passages before answering. Prefer evidence over memory and include each article's original `Source` URL.

## Route

1. Read [references/search-routing.md](references/search-routing.md) only when the best retrieval mode is unclear.
2. For familiar domains, use [references/topic-map.md](references/topic-map.md) to expand the query without loading Wiki articles.
3. Search with the first available mode:
   - Local corpus: run `scripts/search_wiki.py "<query>"` from this skill directory. It discovers both `knowledge/articles` and `knowledge/api/documents`; repeat `--directory <path>` for external corpora.
   - Bundled catalogs: the same command falls back to `references/catalog.json` and `references/api-catalog.json`, returning candidate source URLs without loading bodies.
   - Semantic retrieval: when `OPENAI_API_KEY` is already available, run `scripts/search_vector_store.py "<query>"`. Never request or expose the key.
4. Start with at most 5 results. Open at most 3 articles and only the relevant heading or excerpt. Broaden once only when evidence is weak.
5. Distinguish current and legacy systems. Do not combine old and new editor workflows unless the user needs migration guidance.
6. For exact classes, functions, enums, structs, signatures, parameters, or execution scope, prefer API Wiki evidence over tutorial prose. Use tutorial Wiki for workflows and editor steps.
7. Use the `ugcaskq` MCP only when the request needs live editor state, project-specific inspection, or an explicitly authorized editor operation. Read [references/mcp-proxy.md](references/mcp-proxy.md) only for those requests; ordinary knowledge retrieval must not call MCP.

## Answer

- State the recommended path first, then concise implementation steps or code.
- Cite the original Wiki URL near the supported claim.
- Label inference, version uncertainty, or conflicting documentation explicitly.
- Preserve fenced code and Markdown image URLs only when they are necessary to answer.

## Maintenance

Read [references/maintenance.md](references/maintenance.md) only for explicit refresh, crawl, sync, Vector Store, GitHub Actions, or indexing requests. Remote writes require the user's request and must not print or commit credentials.

