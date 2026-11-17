---
title: "MCP server"
source: https://developers.deepgram.com/developer-tools/cli/mcp-server.md
path: developer-tools/cli/mcp-server
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# MCP server

`dg mcp` runs a local stdio bridge to Deepgram's hosted docs MCP server at `https://api.dx.deepgram.com/kapa/mcp`, authenticated with your `dg` credentials. It exposes one tool, `search_deepgram_knowledge_sources`. Use `dg mcp` when your editor runs only stdio MCP servers; otherwise add the hosted server directly from [Agentic Developer Tools](/developer-tools/agentic-tools). Add one of the two.

`dg mcp` bridges an editor to Deepgram's docs-search MCP server over `stdio`, the only transport it supports, and exposes one tool, `search_deepgram_knowledge_sources`. To call the Deepgram APIs from an agent, use `dg listen`, `dg speak`, `dg read`, or the SDKs.

## Start the MCP server

```shell
dg mcp
```

Starts the bridge over stdio, the only transport `dg mcp` supports.

## Transport

`dg mcp` runs only over stdio. `--transport`, `--host`, and `-p`/`--port` still exist as flags, kept for compatibility with older MCP client configs, but they're ignored except for `--transport stdio`; passing `--transport sse` (or anything other than `stdio`) now fails outright:

```shell
$ dg mcp --transport sse
ERROR: dg mcp supports only the stdio transport, not sse. Nothing was started.
HINT: Use stdio: remove --transport from your MCP config and let your editor start dg mcp.
```

`--base-url` still sets the Deepgram developer API host (default `https://api.dx.deepgram.com`), and `--debug` still turns on debug logging.

## Configuration

### Claude Code

Add to your project's `.mcp.json`:

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
claude mcp add deepgram --scope user -- dg mcp
```

### OpenAI Codex

Add the server from the terminal:

```shell
codex mcp add deepgram -- dg mcp
```

Or add it to `~/.codex/config.toml`, which the Codex CLI, IDE extension, and desktop app share:

```toml
[mcp_servers.deepgram]
command = "dg"
args = ["mcp"]
```

### Gemini CLI

```shell
gemini mcp add deepgram dg mcp
```

### VS Code and GitHub Copilot

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "deepgram": {
      "type": "stdio",
      "command": "dg",
      "args": ["mcp"]
    }
  }
}
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

### Other MCP clients

Any client that runs stdio MCP servers reads the same entry. Add it to the client's MCP configuration file:

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

`dg mcp` exposes one tool, `search_deepgram_knowledge_sources`. The server answers questions from the Deepgram documentation.

## Authentication

The bridge uses the credentials stored by `dg login`. With no stored `dg login` credential and no `DEEPGRAM_API_KEY`, `dg mcp` still starts and completes the stdio handshake; the credential check only runs on the first `search_deepgram_knowledge_sources` call, which fails with `dg mcp can't start the documentation search: No API key is set. Run dg login or set DEEPGRAM_API_KEY, then restart the MCP server.` Your editor shows the server as connected even though every tool call will fail until a credential is set and the server is restarted.

For CI environments:

```shell
DEEPGRAM_API_KEY=YOUR_API_KEY dg mcp
```
