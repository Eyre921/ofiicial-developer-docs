---
title: "Cursor Plugin"
source: https://docs.pinecone.io/integrations/cursor
path: integrations/cursor
---

Install the official Pinecone plugin for Cursor to manage indexes, run vector search, and build RAG apps from the editor using MCP and slash commands.

The official Pinecone plugin for [Cursor](https://www.cursor.com/) provides AI-powered skills, MCP server integration, and slash commands directly in your editor. Use natural language to manage indexes, query data, build RAG applications, and create document Q\&A assistants — all with up-to-date Pinecone API knowledge.

<PrimarySecondaryCTA />

## Features

* **Built-in skills** for index management, semantic search, full-text search, assistant creation, and more
* **Bundled MCP server** (`@pinecone-database/mcp`) for direct Pinecone operations from Cursor Agent
* **Slash commands** like `/pinecone-quickstart` and `/pinecone-query` for quick access
* **Natural language activation** — Cursor Agent invokes the right skill automatically based on your conversation

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Cursor](https://www.cursor.com/) installed
* [Node.js](https://nodejs.org/) v18+ (required for the bundled MCP server)
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (optional, runs bundled Python scripts)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, enables the `pinecone-cli` skill)

## Installation

<Steps>
  <Step title="Set your API key">
    Add your [Pinecone API key](https://app.pinecone.io/organizations/-/keys) to a `.env` file at your workspace root:

    ```text theme={null}
    PINECONE_API_KEY=your-key
    ```

    Cursor loads this file into the MCP server via its [`envFile`](https://cursor.com/docs/mcp) field, so you don't need to export the key in your shell.
  </Step>

  <Step title="Install the plugin">
    In Cursor chat, run:

    ```text theme={null}
    /add-plugin pinecone
    ```

    Or install directly from the [Cursor Marketplace](https://cursor.com/marketplace/pinecone).
  </Step>

  <Step title="Verify the installation">
    Open Cursor Agent chat and run `/pinecone-help` to confirm the skills are loaded. You can also check:

    * **Skills:** Cursor Settings > Rules — listed under "Agent Decides"
    * **MCP server:** Cursor Settings > Features > Model Context Protocol
  </Step>
</Steps>

## Available skills

| Skill                | Command                      | Description                                                                                                                                                     |
| -------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Help**             | `/pinecone-help`             | Overview of all skills and setup requirements.                                                                                                                  |
| **Quickstart**       | `/pinecone-quickstart`       | Interactive onboarding — create an index, upsert data, and query. Choose between a Database path or Assistant path.                                             |
| **Query**            | `/pinecone-query`            | Search integrated indexes using natural language via the Pinecone MCP server.                                                                                   |
| **Assistant**        | `/pinecone-assistant`        | Create, upload, sync, and chat with Pinecone Assistants for document Q\&A with citations.                                                                       |
| **CLI**              | `/pinecone-cli`              | Guide for using the Pinecone CLI (`pc`) from the terminal.                                                                                                      |
| **Full-text search** | `/pinecone-full-text-search` | Create, ingest into, and query a Pinecone full-text-search (FTS) index using the preview API.                                                                   |
| **n8n**              | `/pinecone-n8n`              | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| **MCP**              | `/pinecone-mcp`              | Reference for all Pinecone MCP server tools.                                                                                                                    |
| **Docs**             | `/pinecone-docs`             | Curated links to official Pinecone documentation.                                                                                                               |

## MCP tools

The plugin includes the Pinecone MCP server, which provides the following tools:

* `search-docs` — Search the official Pinecone documentation.
* `list-indexes` — List all available Pinecone indexes.
* `describe-index` — Get index configuration and namespaces.
* `describe-index-stats` — Get record counts and namespace statistics.
* `create-index-for-model` — Create a new index with integrated embeddings.
* `upsert-records` — Insert or update records in an index.
* `search-records` — Search records with optional metadata filtering and reranking.
* `cascading-search` — Search across multiple indexes with deduplication and reranking.
* `rerank-documents` — Rerank documents using a specified reranking model.

For full MCP server documentation, see [Use the Pinecone MCP server](/guides/operations/mcp-server).

## Resources

* [GitHub repository](https://github.com/pinecone-io/pinecone-cursor-plugin)
* [Cursor Marketplace listing](https://cursor.com/marketplace/pinecone)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
* [Cursor documentation](https://cursor.com/docs)
