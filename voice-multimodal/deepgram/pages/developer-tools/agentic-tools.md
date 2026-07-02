---
title: "Agentic developer tools"
source: https://developers.deepgram.com/developer-tools/agentic-tools.md
path: developer-tools/agentic-tools
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Agentic developer tools

Deepgram provides multiple ways to embed Deepgram knowledge directly into AI-powered developer tools: a **CLI with a built-in MCP server**, a **docs MCP server** for querying documentation, and a **skills marketplace** with structured reference material your tools can load on demand.

## Deepgram CLI

The [`dg` CLI](https://cli.deepgram.com) gives you full access to Deepgram APIs from your terminal — speech-to-text, text-to-speech, voice agents, and more — with 28 commands and a built-in MCP server.

### Install

**macOS / Linux:**

```shell
curl -fsSL https://deepgram.com/install.sh | sh
```

**Windows (PowerShell):**

```powershell
iwr https://deepgram.com/install.ps1 -useb | iex
```

**Package managers:**

```shell
pip install deepctl          # pip
uv tool install deepctl      # uv
pipx install deepctl         # pipx
```

### Built-in MCP server

The CLI includes a built-in MCP server that gives your AI coding tools direct access to Deepgram APIs:

```shell
dg mcp                                    # Start MCP server (stdio)
dg mcp --transport sse --port 8000        # SSE transport
```

Add to your editor's MCP configuration:

```json
{
  "mcpServers": {
    "deepgram": {
      "type": "stdio",
      "command": "dg",
      "args": ["mcp"]
    }
  }
}
```

For full CLI documentation, visit the [CLI documentation](/developer-tools/cli/getting-started) on developers.deepgram.com, or explore [cli.deepgram.com](https://cli.deepgram.com) for the quick reference.

## Docs MCP server

The Deepgram docs MCP server lets AI coding tools query the full Deepgram documentation. It is available over HTTP at two endpoints:

|                     |                                        |
| ------------------- | -------------------------------------- |
| **Transport**       | HTTP                                   |
| **URL**             | `https://api.dx.deepgram.com/kapa/mcp` |
| **Alternative URL** | `https://deepgram.mcp.kapa.ai`         |

### Claude Code

Add the server with a single command:

```shell
claude mcp add deepgram-docs --scope project --transport http https://api.dx.deepgram.com/kapa/mcp
```

### Cursor, Windsurf, and other MCP clients

Add the following to your MCP configuration file (for example, `.cursor/mcp.json` or `.windsurf/mcp.json`):

```json
{
  "mcpServers": {
    "deepgram-docs": {
      "type": "http",
      "url": "https://api.dx.deepgram.com/kapa/mcp"
    }
  }
}
```

Once connected, your AI tool can answer questions about any Deepgram API, SDK, or feature using the official documentation as its source.

## Skills marketplace

The [Deepgram skills repository](https://github.com/deepgram/skills) contains agent-agnostic skill files that AI coding tools load to understand specific parts of the Deepgram platform. Each skill is a folder of plain Markdown that any tool can consume.

### Available skills

| Skill       | Description                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| `api`       | Full API reference for all Deepgram REST and WebSocket APIs, generated from OpenAPI and AsyncAPI specs |
| `docs`      | Documentation navigator with topic-by-topic pointers and MCP server setup instructions                 |
| `starters`  | Ready-to-run demo apps across 13 frameworks and 7 features                                             |
| `setup-mcp` | Set up the Deepgram MCP server for your AI coding tool                                                 |

### Quick setup (Claude Code)

Register the repository as a plugin marketplace:

```shell
/plugin marketplace add deepgram/skills
```

Install the Deepgram plugin:

```shell
/plugin install deepgram@deepgram-agent-skills
```

This gives you the following slash commands: `/deepgram:api`, `/deepgram:docs`, `/deepgram:starters`, and `/deepgram:setup-mcp`.

## SDKs

Deepgram provides official SDKs so you can integrate speech-to-text, text-to-speech, voice agents, and audio intelligence into your application in the language of your choice.

* [Python SDK](https://github.com/deepgram/deepgram-python-sdk)
* [JavaScript / TypeScript SDK](https://github.com/deepgram/deepgram-js-sdk)
* [Go SDK](https://github.com/deepgram/deepgram-go-sdk)
* [.NET SDK](https://github.com/deepgram/deepgram-dotnet-sdk)
* [Java SDK](https://github.com/deepgram/deepgram-java-sdk)
* [Rust SDK](https://github.com/deepgram/deepgram-rust-sdk)

For a full breakdown of which SDK supports which API feature, see the [SDK feature matrix](/sdks/sdk-features).
