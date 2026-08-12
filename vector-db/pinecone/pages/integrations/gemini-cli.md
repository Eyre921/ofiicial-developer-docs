---
title: "Gemini CLI Extension"
source: https://docs.pinecone.io/integrations/gemini-cli
path: integrations/gemini-cli
---

Install the official Pinecone extension for Gemini CLI to manage indexes, run vector search, and build RAG assistants with natural-language commands.

The official Pinecone extension for [Gemini CLI](https://github.com/google-gemini/gemini-cli) provides AI-powered skills and MCP server integration directly in your terminal. Use natural language to manage indexes, query data, build RAG applications, and create document Q\&A assistants.

<PrimarySecondaryCTA />

## Features

* **7 built-in skills** for index management, semantic search, assistant creation, and more
* **MCP server integration** for direct Pinecone operations from Gemini CLI
* **Natural language activation** — just describe what you want and the right skill is invoked automatically

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (required for skill scripts)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, for advanced operations)

## Installation

<Steps>
  <Step title="Set your API key">
    ```shell theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```

    Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys).
  </Step>

  <Step title="Install the extension">
    ```shell theme={null}
    gemini extensions install https://github.com/pinecone-io/gemini-cli-extension
    ```
  </Step>

  <Step title="Restart Gemini CLI">
    Restart Gemini CLI to activate the extension. Then ask:

    ```text theme={null}
    Use the help skill to show me what Pinecone skills are available.
    ```
  </Step>
</Steps>

<Note>
  If you hit API key errors, exit Gemini CLI, run `export PINECONE_API_KEY="your-key"` in your terminal, and start Gemini CLI again. The CLI only reads environment variables at launch.
</Note>

## Available skills

| Skill             | Description                                                                         |
| ----------------- | ----------------------------------------------------------------------------------- |
| **quickstart**    | Step-by-step onboarding — create an index, upload data, and run your first search.  |
| **query**         | Search integrated indexes using natural language text via the Pinecone MCP.         |
| **assistant**     | Create, manage, and chat with Pinecone Assistants for document Q\&A with citations. |
| **cli**           | Guide for using the Pinecone CLI from the terminal.                                 |
| **mcp**           | Reference for all available Pinecone MCP server tools and their parameters.         |
| **pinecone-docs** | Curated links to official Pinecone documentation, organized by topic.               |
| **help**          | Overview of all skills and what you need to get started.                            |

Skills are activated automatically based on your conversation. If the agent doesn't pick up a specific skill, explicitly ask for it: *"Use the quickstart skill to help me get started."*

## MCP tools

The extension includes the Pinecone MCP server, which provides the following tools:

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

* [GitHub repository](https://github.com/pinecone-io/gemini-cli-extension)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
* [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli)
