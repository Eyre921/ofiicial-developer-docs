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

## What you can do

Once connected, your assistant can:

* Create new agents by describing what you want
* Update any agent setting, including the system prompt, voice, language, and first message
* List your agents and inspect or compare their configurations
* Review an agent's recent conversations and read full transcripts
* Explore the topics your agents' conversations cover
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

## Permissions

Two layers control what a connected assistant can do: the permissions you grant to ElevenLabs when you connect, and the tool controls in your MCP client.

### ElevenLabs permissions

When you connect, the OAuth consent screen lists the permissions the assistant is requesting, such as reading and writing agents. The assistant can only perform actions covered by the permissions you approve, and access is limited to the workspace you sign in with. You can revoke the connection at any time from your MCP client or from your ElevenLabs account settings.

### Tool controls in your MCP client

MCP clients such as Claude let you choose which of the connector's tools the assistant can use and which require your approval before each call. In Claude, open the ElevenLabs connector's settings to enable or disable individual tools and to set whether a tool runs automatically or asks for confirmation first.

These controls work at two levels. Workspace administrators can configure the connector and its tools for everyone in their organization, and individual users can apply stricter settings for themselves. A tool disabled by an administrator cannot be re-enabled by an individual user.

## Security

* Access is scoped by OAuth permissions covering ElevenAgents read and write operations and Text to Speech.
* Deleting an agent is destructive. Review tool calls in your MCP client before approving them, and restrict write access to workspace members who need it.

## Related resources

#### [ElevenLabs CLI](/docs/eleven-agents/operate/cli)

Manage agents as code with version control and CI/CD.

#### [Agents skill](https://github.com/elevenlabs/skills/tree/main/agents)

Give coding agents deeper ElevenLabs workflows via the skills repository.

#### [API reference](/docs/api-reference/introduction)

Full REST API for programmatic control of the platform.
