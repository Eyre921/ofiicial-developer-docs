---
title: "Agent Skills"
source: https://docs.pinecone.io/integrations/agent-skills
path: integrations/agent-skills
---

Install the Pinecone Agent Skills library in any agentic IDE to manage indexes, run semantic search, and build RAG assistants with natural language.

Pinecone's official [Agent Skills](https://github.com/pinecone-io/skills) library brings Pinecone capabilities to any agentic IDE that supports the Agent Skills standard. Use skills to manage indexes, run semantic search, create document Q\&A assistants, and more, all through natural language in your IDE.

Agent Skills work with [GitHub Copilot](https://github.com/features/copilot) and other agentic IDEs.

<PrimarySecondaryCTA />

<Tip>
  These tools have a dedicated Pinecone plugin or extension with additional features. Install it instead of Agent Skills:

  * [Claude Code](/integrations/claude-code)
  * [Codex](/integrations/codex)
  * [Cursor](/integrations/cursor)
  * [Gemini CLI](/integrations/gemini-cli)
</Tip>

## Features

* Built-in skills cover index management, semantic search, full-text search, assistant creation, and more.
* The skills work in any IDE that supports Agent Skills.
* The skills work with the Pinecone MCP server for direct index operations.

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Node.js](https://nodejs.org/) installed (for `npx`)
* [Pinecone MCP server](/guides/operations/mcp-server) configured in your IDE (optional, enables the `query` skill)
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (required to run the bundled Python scripts, including the quickstart skill)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, enables the `cli` skill)

## Installation

Set your API key, add the skills to your project, and optionally connect the MCP server.

<Steps>
  <Step title="Set your API key">
    ```shell theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```

    Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys).
  </Step>

  <Step title="Install the skills">
    ```shell theme={null}
    npx skills add pinecone-io/skills
    ```

    This downloads Pinecone's skills into your project, making them available to your IDE's AI agent.
  </Step>

  <Step title="Configure the MCP server (optional)">
    For full functionality, configure the [Pinecone MCP server](/guides/operations/mcp-server) in your IDE. This enables the `query` skill and direct index operations.
  </Step>
</Steps>

## Available skills

| Skill | Description |
| - | - |
| `quickstart` | Step-by-step onboarding that walks you through creating an index, uploading data, and running your first search. |
| `query` | Search integrated indexes using natural language text via the Pinecone MCP. |
| `assistant` | Create, manage, and chat with Pinecone Assistants for document Q\&A with citations. |
| `cli` | Use the Pinecone CLI for terminal-based index and vector management across all index types. |
| `full-text-search` | Create, ingest into, and query a Pinecone full-text-search (FTS) index. |
| `n8n` | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| `mcp` | Reference for all available Pinecone MCP server tools and their parameters. |
| `pinecone-docs` | Curated links to official Pinecone documentation, organized by topic. |
| `help` | Overview of all skills and what you need to get started. |

## MCP tools

Agent Skills work alongside the [Pinecone MCP server](/guides/operations/mcp-server), which provides tools for listing indexes, creating indexes, upserting records, searching, reranking, and more. Configure the MCP server in your IDE to enable the `query` skill and direct index operations.

For the full list of MCP tools, see [Use the Pinecone MCP server](/guides/operations/mcp-server).

## Resources

* [GitHub repository](https://github.com/pinecone-io/skills)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
