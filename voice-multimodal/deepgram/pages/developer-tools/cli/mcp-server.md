---
title: "MCP server"
source: https://developers.deepgram.com/developer-tools/cli/mcp-server.md
path: developer-tools/cli/mcp-server
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# MCP server

The `dg` CLI includes a built-in MCP (Model Context Protocol) server that gives AI coding tools direct access to Deepgram APIs.

## Start the MCP server

```shell
dg mcp
```

Starts a server using stdio transport (default).

## HTTP/SSE transport

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

## Available tools

`dg mcp` proxies the tools exposed by the Deepgram developer API to your editor. The remote service owns the available tool list, so inspect the connected MCP client for the current tools and their schemas.

## Authentication

The MCP server uses your stored credentials (`dg login`) automatically.

For CI environments:

```shell
DEEPGRAM_API_KEY=sk_xxx dg mcp
```
