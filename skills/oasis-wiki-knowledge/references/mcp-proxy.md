# UGCAskQ MCP Proxy

Read only when a request requires live Oasis editor state, project-specific inspection, or editor automation.

## Connection

- Dependency name: `ugcaskq`
- Transport: `sse`
- Local endpoint: `http://127.0.0.1:12463/sse`
- Source configuration: the UGCProjects workspace `.mcp.json`

The endpoint is local and contains no credential. Do not copy unrelated workspace settings, logs, tokens, or project data into the skill or a public repository.

## Routing

- Use local Markdown, catalogs, or Vector Store for documentation, API signatures, tutorials, and general implementation guidance.
- Use MCP for selected actors/assets, editor schemas, current project state, live logs, or operations that cannot be answered from static documentation.
- Search official Wiki/API evidence before an MCP mutation when the operation depends on an API name, property, enum, or editor workflow.
- If MCP is unavailable, stop live-editor work and report that the local proxy at port `12463` must be running. Continue documentation-only work when possible.

## Safety

- Read-only discovery may run without a mutation plan.
- Any editor mutation requires the user's explicit request and the MCP server's Plan-Resolve-Verify workflow.
- Resolve exact APIs, schemas, asset paths, and enum values before mutation; do not guess Unreal properties or signatures.
- Never expose or commit project-private data returned by the editor unless the user explicitly requests that exact output.

