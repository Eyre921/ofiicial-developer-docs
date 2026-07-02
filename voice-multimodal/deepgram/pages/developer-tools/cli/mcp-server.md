---
title: "MCP Server"
source: https://developers.deepgram.com/developer-tools/cli/mcp-server.md
path: developer-tools/cli/mcp-server
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# MCP Server

The `dg` CLI includes a built-in MCP (Model Context Protocol) server that gives AI coding tools direct access to Deepgram APIs.

## Start the MCP Server

```shell
dg mcp
```

Starts a server using stdio transport (default).

## HTTP/SSE Transport

For HTTP-based MCP clients:

```shell
dg mcp --transport sse --port 8000
```

## Configuration

### Claude Code

Add to your project's `.claude/mcp.json`:

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

Or add globally:

```shell
claude mcp add deepgram --scope user --command dg --args mcp
```

### Cursor

Add to `.cursor/mcp.json`:

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

### Windsurf

Add to `.windsurf/mcp.json`:

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

## Available Tools

The MCP server exposes these capabilities:

* `transcribe_audio` — Transcribe audio from URL or file path
* `synthesize_speech` — Generate speech from text
* `analyze_text` — Sentiment, topics, summarization
* `list_models` — List available Deepgram models
* `get_usage` — Check API usage

## Authentication

The MCP server uses your stored credentials (`dg login`) automatically.

For CI environments:

```shell
DEEPGRAM_API_KEY=sk_xxx dg mcp
```
