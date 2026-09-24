---
title: "Claude, Cursor, and other AI assistants"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/external-assistants.md
path: docs/eleven-agents/operate/architect/external-assistants
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Claude, Cursor, and other AI assistants

## Overview

Architect lives inside the ElevenLabs dashboard, but the agent APIs behind it are also reachable from external AI assistants, such as Claude and Cursor, through two separate integrations: the hosted MCP server and the ElevenLabs plugin.

> **Note**
>
> These are separate integrations from the in-app Architect experience described elsewhere in this
> section. They call the same underlying platform, but through the external client's own tool or
> skill interface rather than the Architect chat UI, so the available actions and approval flow
> differ from what's described in [Authentication, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication).

## Hosted MCP server

The [hosted MCP server](/docs/eleven-agents/operate/hosted-mcp) is a remote [Model Context Protocol](https://modelcontextprotocol.io/) server at `https://api.elevenlabs.io/v1/mcp` that exposes agent management tools to any MCP-compatible client. Once connected, an assistant can create, configure, and manage the agents in your workspace through natural language, with nothing to install.

It is published in the Claude Desktop connector directory, and works with any other MCP client that supports OAuth-authenticated remote servers, including Cursor.

## Architect Plugin

Architect's own skills — the same workflows it uses in-app to explore an agent, edit its configuration, workflow, and tools, write tests, and work the triage queue — come packaged in the [ElevenLabs plugin](https://github.com/elevenlabs/plugin/tree/main/architect), alongside the hosted MCP server and ElevenLabs's general product skills. Installing the plugin gives a coding assistant already working in your codebase the same skills Architect uses, so it can manage agents as code.

In Cursor, install the plugin from the [Cursor marketplace](https://cursor.com/marketplace). In Claude Code, install it with:

```bash
/plugin marketplace add elevenlabs/plugin
/plugin install elevenlabs@elevenlabs
```

## Choosing between them

Use the hosted MCP server when you want conversational agent management from a chat client with no local setup, for example Claude Desktop. Use the ElevenLabs plugin when a coding assistant is already working in your repository and should manage agents as code, with Architect's own skills guiding how it edits tools, workflows, and tests.

## Approvals in these clients

Each client controls its own approval behavior for tool calls. Claude and Cursor, for example, let you choose which tools run automatically and which require your confirmation before every call, independently of the approval modes described for the in-app Architect chat.
