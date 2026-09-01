---
title: "Development Setup with Fireworks Docs MCP"
source: https://docs.fireworks.ai/ecosystem/integrations/development-setup
path: ecosystem/integrations/development-setup
---

Configure the Fireworks AI Docs MCP server for Claude Code and Cursor

## Claude Code

Add the MCP server via the CLI:

```bash theme={null}
claude mcp add --transport http fireworks-docs https://docs.fireworks.ai/mcp
```

Or add it to your project's `mcp.json`:

```json theme={null}
{
  "mcpServers": {
    "fireworks-docs": {
      "url": "https://docs.fireworks.ai/mcp"
    }
  }
}
```

## Cursor

One-click install:

[Install Fireworks Docs MCP](https://cursor.com/en/install-mcp?name=fireworks-docs\&config=eyJ1cmwiOiJodHRwczovL2RvY3MuZmlyZXdvcmtzLmFpL21jcCJ9)

Or manually add to your workspace's `mcp.json`:

```json theme={null}
{
  "mcpServers": {
    "fireworks-docs": {
      "url": "https://docs.fireworks.ai/mcp"
    }
  }
}
```

## Using the MCP Server

Once configured, your AI coding agent can search the full Fireworks AI documentation. Example queries:

* "How do I configure autoscaling for deployments?"
* "What parameters does the chat completions endpoint accept?"
* "Show me examples of function calling with Fireworks models"
* "Find the API reference for batch inference"
