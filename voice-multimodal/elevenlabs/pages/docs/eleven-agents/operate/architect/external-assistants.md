---
title: "Claude, Cursor, and other AI assistants"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/external-assistants.md
path: docs/eleven-agents/operate/architect/external-assistants
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Claude, Cursor, and other AI assistants

## Overview

You can work on your agents from outside the ElevenLabs dashboard, in assistants such as Claude, Claude Code, ChatGPT, and Cursor. Every one of these connects through the same thing: the ElevenLabs [hosted MCP server](/docs/eleven-agents/operate/hosted-mcp), a remote [Model Context Protocol](https://modelcontextprotocol.io/) server at `https://api.elevenlabs.io/v1/mcp`. The server exposes agent management tools and signs you in with OAuth, so no API keys are copied into the client.

Coding assistants can also install the **ElevenLabs plugin**, which bundles the MCP server with ElevenAgents Architect's own skills: the workflows Architect uses in the dashboard to explore an agent, edit its configuration, workflow, and tools, write tests, and work the triage queue.

## Set up your assistant

#### Claude

The ElevenLabs connector is listed in the Claude connector directory. In Claude, go to **Settings** > **Connectors**, search for **ElevenLabs**, select **Connect**, and complete the OAuth sign-in.

For data residency environments, add a custom connector with your region's URL instead. See [Hosted MCP server](/docs/eleven-agents/operate/hosted-mcp#data-residency-regions).

#### Claude Code

Install the ElevenLabs plugin, which includes the MCP server and Architect's skills:

```bash
/plugin marketplace add elevenlabs/plugin
/plugin install elevenlabs@elevenlabs
```

To add only the MCP server, without the skills:

```bash
claude mcp add --transport http elevenlabs https://api.elevenlabs.io/v1/mcp
```

Then run `/mcp` in Claude Code and complete the OAuth sign-in.

#### Cursor

Install the ElevenLabs plugin from the [Cursor marketplace](https://cursor.com/marketplace). It includes the MCP server and Architect's skills.

To add only the MCP server, add it to your `mcp.json`:

```json
{
  "mcpServers": {
    "elevenlabs": {
      "url": "https://api.elevenlabs.io/v1/mcp"
    }
  }
}
```

Cursor prompts you to sign in with OAuth the first time it connects.

#### ChatGPT

Add ElevenLabs as a custom connector in ChatGPT, using the server URL `https://api.elevenlabs.io/v1/mcp`, and complete the OAuth sign-in. Custom connectors may need to be enabled by your ChatGPT workspace administrator.

#### Other clients

Any MCP client that supports remote servers with OAuth can connect. Point the client at `https://api.elevenlabs.io/v1/mcp`, or your region's URL, and complete the sign-in. Clients that support hosted client metadata (CIMD) don't need a separate client registration.

The plugin's source, including the Architect skills, is at [github.com/elevenlabs/plugin](https://github.com/elevenlabs/plugin/tree/main/architect).

## In the dashboard compared with an external assistant

In-app Architect and the MCP server call the same ElevenAgents APIs under your account, so both are limited by your permissions, and their results appear in the same places. They differ in how changes are staged and approved.

|                       | Architect in the dashboard                                                                                           | External assistant through MCP                                                                                                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity              | You, through your browser session                                                                                    | You, through the OAuth grant you approved                                                                                                                                                                        |
| Configuration changes | Staged in a draft. You always publish.                                                                               | Applied directly. Updating an agent publishes a new version on the target branch, or on `main` if no branch is given. Ask the assistant to work on a branch, or to create a draft, for changes that need review. |
| Approvals             | Architect's [approval modes](/docs/eleven-agents/operate/architect/authentication#approval-modes)                    | Your client's tool settings. The server marks each tool as read-only or destructive, and clients such as Claude let you choose which tools run automatically and which ask first.                                |
| Merge proposals       | Can open proposals and request reviewers. Can't review or merge them.                                                | Can open, review, comment on, and merge proposals, within your permissions. You still can't approve your own proposal.                                                                                           |
| Context               | The page you're on, the agent summary, agent context, your preferences, and what the entry point passed in           | Only what you tell the assistant, plus what it reads with tools. Agent context and your preferences aren't sent automatically.                                                                                   |
| Extras                | Plan mode, dashboards in the chat, code execution, Spotlight and triage hand-offs, guiding you through the dashboard | Your own codebase and other tools in the client. Some management actions not in Architect, such as managing MCP servers and deleting knowledge base documents.                                                   |

Branches, versions, merge proposals, tests, and triage tickets created from an external assistant appear in the dashboard in the same places as ones made in ElevenAgents. For example, a merge proposal appears under **Version Control** > **Proposals**, with you as the author.

> **Warning**
>
> Because MCP updates publish directly, changing `main` from an external assistant can affect live
> callers immediately. Set agent update and merge tools to require confirmation in your client, and
> protect `main` if every change must be reviewed.

## Choosing where to work

* **Use Architect in the dashboard** to improve a live agent. It starts from Spotlight findings, failed tests, and triage tickets, stages every change in a draft, and leaves publishing to you.
* **Use a chat assistant such as Claude or ChatGPT** for quick questions and changes across agents when you're already working there, for example "Which of my agents still use the default first message?"
* **Use a coding assistant with the plugin** when your agents are managed as code alongside your application. The assistant can change an agent and the code that calls it in the same session. See also the [ElevenLabs CLI](/docs/eleven-agents/operate/cli).
