---
title: "Connect MCP tools to Managed Deep Agents"
source: https://docs.langchain.com/langsmith/managed-deep-agents-mcp
path: langsmith/managed-deep-agents-mcp
---

Declare remote MCP servers with Managed Deep Agents connectors.

Managed Deep Agents use connectors to load tools from remote MCP servers. Declare the MCP servers in `connectors/mcp.ts` or `connectors/mcp.py`, export a named `mcp` declaration, and MDA loads those tools into the agent at runtime.

<Note>
  Managed Deep Agents is in **private [beta](/langsmith/release-stages)**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

The current `mda` CLI does not include workspace MCP server management commands. Do not use older `deepagents mcp-servers ...` examples for Managed Deep Agents projects. For MCP tools, use the `connectors/` project convention documented here.

## Add a connector

Add `connectors/mcp.py` or `connectors/mcp.ts` next to your agent entry file. For the full project layout, see the [CLI project file reference](/langsmith/managed-deep-agents-cli#project-file-reference).

The connector module must export a named `mcp` declaration.

<CodeGroup>
  ```python connectors/mcp.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents.connectors import define_mcp_servers

  mcp = define_mcp_servers(
      mcp_servers={
          "langchainDocs": {
              "transport": "http",
              "url": "https://docs.langchain.com/mcp",
          },
      },
  )
  ```

  ```ts connectors/mcp.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineMcpServers } from "managed-deepagents";

  export const mcp = defineMcpServers({
    mcpServers: {
      langchainDocs: {
        transport: "http",
        url: "https://docs.langchain.com/mcp",
      },
    },
  });
  ```
</CodeGroup>

You do not import `MultiServerMCPClient` or call `getTools()` / `get_tools()` yourself. `mda` discovers the connector module, injects the MCP adapter dependency into the compiled build, creates the client in the managed runtime, loads the tools, and appends them to the authored tools from `agent.ts` or `agent.py`.

## Supported servers

Connectors support remote MCP servers only:

| Transport | Use                          |
| --------- | ---------------------------- |
| `http`    | Streamable HTTP MCP servers. |
| `sse`     | Legacy SSE MCP servers.      |

Stdio MCP servers are not supported in connectors. If a server needs local process management, expose it over HTTP/SSE or wrap the behavior as a normal authored tool.

## Configure server options

Each server key is the logical server name MDA uses for validation, tracing metadata, and tool-name prefixing. Server configs can include static headers.

Connectors do not run an OAuth authorization flow. If an MCP server requires OAuth, provide a pre-provisioned access token or another static credential through headers. Store the token in `.env` so `mda dev` can load it locally and `mda deploy` can forward it as a hosted deployment secret.

The connector module is normal project code, so read secrets as environment variables with `os.environ` in Python or `process.env` in TypeScript. You do not import the `.env` file directly.

<CodeGroup>
  ```python connectors/mcp.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os

  from managed_deepagents.connectors import define_mcp_servers

  mcp = define_mcp_servers(
      mcp_servers={
          "github": {
              "transport": "http",
              "url": "https://example.com/mcp",
              "headers": {
                  "Authorization": f"Bearer {os.environ['GITHUB_MCP_TOKEN']}",
              },
          },
      },
  )
  ```

  ```ts connectors/mcp.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineMcpServers } from "managed-deepagents";

  export const mcp = defineMcpServers({
    mcpServers: {
      github: {
        transport: "http",
        url: "https://example.com/mcp",
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_MCP_TOKEN}`,
        },
      },
    },
  });
  ```
</CodeGroup>

<Warning>
  Do not commit MCP tokens, API keys, OAuth access tokens, or passwords. Put local values in `.env`; `mda dev` loads them for local development, and `mda deploy` forwards non-reserved `.env` values as hosted deployment secrets.
</Warning>

## Connector defaults

MDA applies managed defaults when it loads connector tools:

| Option                                                               | Default   | Description                                                                                                                  |
| -------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `prefixToolNameWithServerName` / `prefix_tool_name_with_server_name` | `true`    | Prefix MCP tool names with the server name, for example `github__search`, to avoid collisions.                               |
| `throwOnLoadError` / `throw_on_load_error`                           | `true`    | Fail when tools cannot be loaded instead of starting with a partial tool surface.                                            |
| `useStandardContentBlocks` / `use_standard_content_blocks`           | `true`    | Convert MCP tool outputs to standard LangChain content blocks. Python connectors currently require the default `true` value. |
| `onConnectionError` / `on_connection_error`                          | `"throw"` | Fail when a server cannot be reached. `"throw"` is the only supported value.                                                 |

Disable tool-name prefixing only when you know the MCP tool names do not collide. MDA validates duplicate MCP tool names when prefixing is disabled.

## Combine connectors with authored tools

Connector tools are appended to the tools you define in the agent file. Use [custom tools](/langsmith/managed-deep-agents-tools) for project-owned code and [custom middleware](/langsmith/managed-deep-agents-middleware) for cross-cutting behavior around model calls, tool calls, lifecycle hooks, retries, limits, and data handling.

## Test and deploy

Test the project locally with [`mda dev`](/langsmith/managed-deep-agents-cli#develop-locally), then deploy it with [`mda deploy`](/langsmith/managed-deep-agents-deploy). Open deployment traces in LangSmith to inspect model calls, tool calls, errors, and latency.

Connector misconfiguration surfaces during local startup or first tool load, depending on when the runtime reaches the MCP server.

## Next steps

<CardGroup>
  <Card title="Deploy an agent" icon="upload" href="/langsmith/managed-deep-agents-deploy">
    Run and deploy the connector-enabled agent.
  </Card>

  <Card title="CLI reference" icon="terminal" href="/langsmith/managed-deep-agents-cli">
    Look up `mda dev` and `mda deploy` flags.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-mcp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
