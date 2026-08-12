---
title: "Agent Skills"
source: https://docs.pinecone.io/integrations/agent-skills
path: integrations/agent-skills
---

Install the Pinecone Agent Skills library in any agentic IDE to manage indexes, run semantic search, and build RAG assistants with natural language.

Pinecone's official [Agent Skills](https://github.com/pinecone-io/skills) library brings Pinecone capabilities to any agentic IDE that supports the Agent Skills standard. Use skills to manage indexes, run semantic search, create document Q\&A assistants, and more — all through natural language in your IDE.

Compatible with [GitHub Copilot](https://github.com/features/copilot), [Codex](https://chatgpt.com/codex), and other agentic IDEs.

<PrimarySecondaryCTA />

<Tip>
  If you use **Claude Code**, install the dedicated [Pinecone plugin for Claude Code](/integrations/claude-code) instead. If you use **Gemini CLI**, install the dedicated [Pinecone extension for Gemini CLI](/integrations/gemini-cli) instead. If you use **Cursor**, install the dedicated [Pinecone plugin for Cursor](/integrations/cursor) instead. Each includes additional features specific to that tool.
</Tip>

## Features

* **Built-in skills** for index management, semantic search, full-text search, assistant creation, and more
* **Universal compatibility** with any IDE that supports Agent Skills
* **Works with the Pinecone MCP server** for direct index operations

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Node.js](https://nodejs.org/) installed (for `npx`)
* [Pinecone MCP server](/guides/operations/mcp-server) configured in your IDE (optional, enables the `query` skill)
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (optional, runs bundled Python scripts)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, enables the `cli` skill)

## Installation

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

| Skill                | Description                                                                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **quickstart**       | Step-by-step onboarding — create an index, upload data, and run your first search.                                                                              |
| **query**            | Search integrated indexes using natural language text via the Pinecone MCP.                                                                                     |
| **assistant**        | Create, manage, and chat with Pinecone Assistants for document Q\&A with citations.                                                                             |
| **cli**              | Use the Pinecone CLI for terminal-based index and vector management across all index types.                                                                     |
| **full-text-search** | Create, ingest into, and query a Pinecone full-text-search (FTS) index using the preview API.                                                                   |
| **n8n**              | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| **mcp**              | Reference for all available Pinecone MCP server tools and their parameters.                                                                                     |
| **pinecone-docs**    | Curated links to official Pinecone documentation, organized by topic.                                                                                           |
| **help**             | Overview of all skills and what you need to get started.                                                                                                        |

## MCP tools

Agent Skills work alongside the [Pinecone MCP server](/guides/operations/mcp-server), which provides tools for listing indexes, creating indexes, upserting records, searching, reranking, and more. Configure the MCP server in your IDE to enable the `query` skill and direct index operations.

For the full list of MCP tools, see [Use the Pinecone MCP server](/guides/operations/mcp-server).

## Resources

* [GitHub repository](https://github.com/pinecone-io/skills)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
