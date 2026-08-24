# Search Routing

Use one primary retrieval mode. Do not load this reference plus every topic reference by default.

## Mode Selection

| Request | First choice | Fallback |
|---|---|---|
| Exact API, class, event, error text, or catalog ID | Local lexical search | Catalog lookup, then exact official URL |
| Natural-language feature or architecture question | Local lexical search with topic aliases | Vector Store semantic search |
| Latest/current/change/version question | Release-note titles and newest matching article | Narrow semantic search |
| Known article title or category | Bundled catalog | Local lexical search |
| Crawl, refresh, indexing, or Vector Store operation | `maintenance.md` | Repository workflow logs |

## Context Budget

1. Run one query with `--max-results 5 --context-chars 700 --max-total-chars 5000`.
2. Inspect titles, categories, scores, and source URLs before opening bodies.
3. Open at most the top 3 articles and only the matching heading or nearby lines.
4. If results are weak, add one narrower API/class/editor term and search once more.
5. Stop after authoritative documentation directly answers the question.

## Query Construction

- Keep exact identifiers intact: `UGCGameSystem`, `UGC_CastSkill`, `Skill.Slot.Main`.
- Add one domain term when a name is ambiguous: `怪物 行为树`, `技能 Task`, `UI 控件`.
- For errors, search the exact stable substring first; omit timestamps, IDs, and paths.
- For legacy/current ambiguity, include `1.0`, `2.0`, `旧版`, `新版`, or the release number.

## Evidence Rules

- Prefer current official Wiki articles over legacy tutorials and forum summaries.
- A forum tutorial can supply practical steps, but identify it as an example rather than an API guarantee.
- Never infer that a Blueprint property or Lua API exists solely from a similar name.
- When old and current workflows differ, recommend one coherent workflow and mention the alternative separately.

