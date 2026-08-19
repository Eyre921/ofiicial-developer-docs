---
title: "REST endpoint"
source: https://langfuse.com/docs/docs-mcp.md
path: docs/docs-mcp
---

---
title: Docs MCP Server
---

# Langfuse Docs MCP Server

The Langfuse Docs MCP server exposes the Langfuse docs to AI agents.

Core use case: Use Cursor (or other AI Coding Agent) to automatically integrate Langfuse Tracing into your codebase, see [get started](/docs/get-started) for detailed instructions and an example prompt.

This is the public MCP server for the Langfuse documentation. There is also an authenticated MCP server to integrate with the rest of the Langfuse data platform ([docs](/docs/api-and-data-platform/features/mcp-server)).

## Install

<Tabs items={["Claude Code", "Codex", "Cursor", "Windsurf", "Copilot (in VSCode)", "Other MCP Clients"]}>

<Tab>

Add Langfuse Docs MCP to Claude Code via the CLI:

```bash
claude mcp add \
  --transport http \
  langfuse-docs \
  https://langfuse.com/api/mcp \
  --scope user
```

<details>
<summary>Manual configuration</summary>

Alternatively, add the following to your settings file:

- **User scope**: `~/.claude/settings.json`
- **Project scope**: `your-repo/.claude/settings.json`
- **Local scope**: `your-repo/.claude/settings.local.json`

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "transportType": "http",
      "url": "https://langfuse.com/api/mcp",
      "verifySsl": true
    }
  }
}
```

**One-liner JSON import**

```bash
claude mcp add-json langfuse-docs \
  '{"type":"http","url":"https://langfuse.com/api/mcp"}'
```

Once added, start a Claude Code session (`claude`) and type `/mcp` to confirm the connection.

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Codex via the CLI:

```bash
codex mcp add langfuse-docs --url https://langfuse.com/api/mcp
```

<details>
<summary>Manual configuration</summary>

Alternatively, add the following to `~/.codex/config.toml`:

```toml
[mcp_servers.langfuse-docs]
url = "https://langfuse.com/api/mcp"
```

Start a new Codex session, then run `codex mcp list` to confirm the server is registered.

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Cursor via the one-click install:

<div className="flex gap-2 mt-3 mb-6">
  <Button asChild>
    <Link
      href="https://cursor.com/en/install-mcp?name=langfuse-docs&config=eyJ1cmwiOiJodHRwczovL2xhbmdmdXNlLmNvbS9hcGkvbWNwIn0%3D"
      target="_blank"
      rel="noopener noreferrer"
    >
      Install MCP Server in Cursor
    </Link>
  </Button>
</div>

<details>
<summary>Manual configuration</summary>

Add the following to your `mcp.json`:

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "url": "https://langfuse.com/api/mcp"
    }
  }
}
```

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Windsurf via the following steps:

1. Open Command Palette (⌘+Shift+P)
2. Open "MCP Configuration Panel"
3. Select `Add custom server`
4. Add the following configuration:

   ```json
   {
     "mcpServers": {
       "langfuse-docs": {
         "command": "npx",
         "args": ["mcp-remote", "https://langfuse.com/api/mcp"]
       }
     }
   }
   ```

</Tab>

<Tab>

Add Langfuse Docs MCP to Copilot in VSCode via the one-click install:

<div className="flex gap-2 mt-3 mb-6">
  <Button asChild>
    <Link
      href="vscode:mcp/install?%7B%22name%22%3A%22langfuse-docs%22%2C%22url%22%3A%22https%3A%2F%2Flangfuse.com%2Fapi%2Fmcp%22%7D"
      target="_blank"
      rel="noopener noreferrer"
    >
      Install MCP Server in VS Code
    </Link>
  </Button>
</div>

<details>
<summary>Manual configuration</summary>

Add Langfuse Docs MCP to Copilot in VSCode via the following steps:

1. Open Command Palette (⌘+Shift+P)
2. Open "MCP: Add Server..."
3. Select `HTTP`
4. Paste `https://langfuse.com/api/mcp`
5. Select name (e.g. `langfuse-docs`) and whether to save in user or workspace settings
6. You're all set! The MCP server is now available in Agent mode

</details>

</Tab>

<Tab>

Langfuse uses the `streamableHttp` protocol to communicate with the MCP server. This is supported by most clients.

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "url": "https://langfuse.com/api/mcp"
    }
  }
}
```

If you use a client that does not support `streamableHttp` (e.g. Windsurf), you can use the `mcp-remote` command as a local proxy.

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "command": "npx",
      "args": ["mcp-remote", "https://langfuse.com/api/mcp"]
    }
  }
}
```

</Tab>

</Tabs>

## About

- Endpoint: `https://langfuse.com/api/mcp`
- Transport: `streamableHttp`
- Authentication: None

The [MCP Reference](https://mcp.reference.langfuse.com) is the canonical source for current Docs MCP tools, input schemas, and generated request examples.

## References

- Implementation of the MCP server: [route.ts](https://github.com/langfuse/langfuse-docs/blob/main/app/api/mcp/route.ts)
- [MCP Reference](https://mcp.reference.langfuse.com): reference for MCP servers, setup snippets, tools, schemas, and requests
- [Agentic Onboarding](/docs/get-started) powered by the MCP server
- [Ask AI](/docs/ask-ai): RAG chat with the Langfuse docs to get answers to your questions
- [langfuse.com/llms.txt](https://langfuse.com/llms.txt): concise overview with page titles and links to detailed sub-files ([llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt))

## REST Endpoint [#rest-endpoint]

The underlying docs search (`searchLangfuseDocs` tool) is also available independently as a REST API at `https://langfuse.com/api/search-docs`.

```bash
curl "https://langfuse.com/api/search-docs?query=Langfuse+Docs+MCP+Server"
```

Use this endpoint directly when you need lightweight semantic search outside of MCP.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/docs-mcp.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx langfuse-cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

