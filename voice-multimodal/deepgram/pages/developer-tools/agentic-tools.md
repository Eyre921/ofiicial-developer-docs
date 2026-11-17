---
title: "Agentic Developer Tools"
source: https://developers.deepgram.com/developer-tools/agentic-tools.md
path: developer-tools/agentic-tools
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Agentic Developer Tools

We provide multiple ways to embed Deepgram knowledge directly into AI-powered developer tools: a **CLI** that includes a local bridge to the docs MCP server, a **docs MCP server** for querying documentation, and a **skills marketplace** with structured reference material your tools can load on demand.

## Deepgram CLI

The [`dg` CLI](/developer-tools/cli/getting-started) runs Deepgram from your terminal. It transcribes files, URLs, and your microphone (`dg listen`), synthesizes speech (`dg speak`), analyzes text (`dg read`), manages projects, keys, members, and usage, scaffolds starter apps (`dg init`), and runs `dg mcp`, a local stdio bridge to the docs MCP server below.

The PyPI package is `deepctl` and needs Python 3.10 or later; see [Getting Started](/developer-tools/cli/getting-started).

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
# Homebrew
brew install deepgram/tap/deepgram
# pip
pip install deepctl
# uv
uv tool install deepctl
# pipx
pipx install deepctl
# npm
npm install -g @deepgram/cli
```

### Local MCP bridge (`dg mcp`)

`dg mcp` runs a local stdio bridge to Deepgram's hosted docs MCP server at `https://api.dx.deepgram.com/kapa/mcp`, authenticated with your `dg` credentials. It exposes one tool, `search_deepgram_knowledge_sources`. Use it or the hosted docs MCP server below; adding both registers the same tool twice.

```shell
# Start the bridge on stdio, the only transport dg mcp supports
dg mcp
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

Full CLI documentation: [Getting Started](/developer-tools/cli/getting-started). The source is in the [deepgram/cli GitHub repository](https://github.com/deepgram/cli), and [Skills](/developer-tools/cli/skills) covers `dg skills`.

## Docs MCP server

The Deepgram docs MCP server lets AI coding tools query the full Deepgram documentation. It's available over HTTP at two endpoints:

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

### Cursor and other MCP clients

Add the following to your MCP configuration file (for example, `.cursor/mcp.json`):

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

`dg skills install` installs the same skills into each detected coding tool; see [Skills](/developer-tools/cli/skills).

## SDKs

We provide official SDKs so you can integrate speech-to-text, text-to-speech, voice agents, and audio intelligence into your application in the language of your choice.

* [Python SDK](https://github.com/deepgram/deepgram-python-sdk)
* [JavaScript / TypeScript SDK](https://github.com/deepgram/deepgram-js-sdk)
* [Go SDK](https://github.com/deepgram/deepgram-go-sdk)
* [.NET SDK](https://github.com/deepgram/deepgram-dotnet-sdk)
* [Java SDK](https://github.com/deepgram/deepgram-java-sdk)
* [Rust SDK](https://github.com/deepgram/deepgram-rust-sdk)

For a full breakdown of which SDK supports which API feature, see the [SDK feature matrix](/sdks/sdk-features).
