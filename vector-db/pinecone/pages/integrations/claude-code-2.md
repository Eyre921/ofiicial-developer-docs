---
title: "Claude Code Plugin"
source: https://docs.pinecone.io/integrations/claude-code
path: integrations/claude-code
---

Install the official Pinecone plugin for Claude Code to manage indexes, run vector search, and build RAG assistants from the terminal with slash commands.

The official Pinecone plugin for [Claude Code](https://claude.ai/code) provides AI-powered skills, MCP server integration, and slash commands directly in your terminal. Use natural language to manage indexes, query data, build RAG applications, and create document Q\&A assistants — all with up-to-date Pinecone API knowledge.

<PrimarySecondaryCTA />

## Features

* **Built-in skills** for index management, semantic search, full-text search, assistant creation, and more
* **MCP server integration** for direct Pinecone operations from Claude Code
* **Slash commands** like `/pinecone:quickstart` and `/pinecone:query` for quick access
* **Natural language recognition** — assistant commands work without explicit slash commands

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Node.js](https://nodejs.org/) installed (`npx` must be on your `PATH`)
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (required for assistant commands)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, for advanced operations)

## Installation

<Steps>
  <Step title="Set your API key">
    ```shell theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```

    Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys).
  </Step>

  <Step title="Install the plugin">
    From your terminal:

    ```shell theme={null}
    claude plugin install pinecone
    ```

    Or from within Claude Code:

    ```text theme={null}
    /plugin install pinecone
    ```
  </Step>

  <Step title="Restart Claude Code">
    Restart Claude Code to activate the plugin. Then run `/pinecone:help` to verify the installation.
  </Step>
</Steps>

## Available skills

| Skill                | Command                      | Description                                                                                                                                                     |
| -------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Help**             | `/pinecone:help`             | Overview of all skills and setup requirements.                                                                                                                  |
| **Quickstart**       | `/pinecone:quickstart`       | Interactive onboarding — create an index, upsert data, and query.                                                                                               |
| **Query**            | `/pinecone:query`            | Search integrated indexes using natural language.                                                                                                               |
| **Assistant**        | `/pinecone:assistant`        | Create, upload, sync, and chat with Pinecone Assistants.                                                                                                        |
| **CLI**              | `/pinecone:cli`              | Guide for using the Pinecone CLI from the terminal.                                                                                                             |
| **Full-text search** | `/pinecone:full-text-search` | Create, ingest into, and query a Pinecone full-text-search (FTS) index.                                                                                         |
| **n8n**              | `/pinecone:n8n`              | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| **MCP**              | `/pinecone:mcp`              | Reference for all Pinecone MCP server tools.                                                                                                                    |
| **Docs**             | `/pinecone:docs`             | Curated links to official Pinecone documentation.                                                                                                               |

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

* [GitHub repository](https://github.com/pinecone-io/pinecone-claude-code-plugin)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
* [Claude Code documentation](https://docs.claude.com/en/docs/claude-code/quickstart)
