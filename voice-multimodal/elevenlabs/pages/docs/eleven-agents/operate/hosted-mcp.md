---
title: "Hosted MCP server"
source: https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp.md
path: docs/eleven-agents/operate/hosted-mcp
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Hosted MCP server

## Overview

The ElevenLabs hosted MCP server is a remote [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes agent management tools to AI assistants. Once connected, an assistant such as Claude can create, configure, and manage the agents in your workspace through natural language, with nothing to install or run locally.

The server is available at:

```
https://api.elevenlabs.io/v1/mcp
```

Authentication uses OAuth. When you connect, you sign in with your ElevenLabs account and grant the assistant scoped access to your workspace. No API keys are copied into the client.

Looking to give your ElevenLabs agent access to external MCP servers instead? See the [MCP
integration guide](/docs/eleven-agents/customization/tools/mcp).

## Connect from Claude Desktop

The hosted MCP server is published in the Claude Desktop directory.

#### Open the directory

In Claude Desktop, go to **Settings** > **Connectors** and browse the directory.

#### Add the ElevenLabs connector

Search for **ElevenLabs** and select **Connect**.

#### Sign in

Complete the OAuth flow with your ElevenLabs account. Claude can then list, create, and update
agents in your workspace on your behalf.

## Connect from other MCP clients

Add the server to any MCP client that supports remote servers with OAuth authentication:

* **Server URL**: `https://api.elevenlabs.io/v1/mcp`
* **OAuth client ID**: `dee9ba45-a592-4730-a321-a7b90a00c436`
* **Transport**: Streamable HTTP

When prompted, sign in with your ElevenLabs account to complete the OAuth flow.

## What you can do

Once connected, your assistant can:

* Create new agents by describing what you want
* Update any agent setting, including the system prompt, voice, language, and first message
* List your agents and inspect or compare their configurations
* Duplicate and delete agents
* Estimate an agent's expected LLM usage and cost before making changes
* Retrieve an agent's widget configuration and shareable link
* Check the size of an agent's knowledge base
* Generate speech audio from text, returned as a short-lived download link

## Example prompts

Once connected, try prompts like:

* "Create a support agent for my documentation site. It should be friendly, concise, and escalate billing questions."
* "What would my checkout agent cost per conversation with Gemini 2.5 Flash instead of GPT-4o?"
* "Duplicate my production agent, then change the voice and set the first message to Spanish."
* "List my agents and tell me which ones still use the default first message."
* "Generate a sample of my agent's voice saying our new greeting."

## Security

* Access is scoped by OAuth permissions covering ElevenAgents read and write operations and Text to Speech.
* Deleting an agent is destructive. Review tool calls in your MCP client before approving them, and restrict write access to workspace members who need it.
* You can revoke the connection at any time from your MCP client or from your ElevenLabs account settings.

## Related resources

#### [ElevenLabs CLI](/docs/eleven-agents/operate/cli)

Manage agents as code with version control and CI/CD.

#### [Agents skill](https://github.com/elevenlabs/skills/tree/main/agents)

Give coding agents deeper ElevenLabs workflows via the skills repository.

#### [API reference](/docs/api-reference/introduction)

Full REST API for programmatic control of the platform.
