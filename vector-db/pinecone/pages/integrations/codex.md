---
title: "Codex plugin"
source: https://docs.pinecone.io/integrations/codex
path: integrations/codex
---

Install the official Pinecone plugin for Codex to manage indexes, run vector search, and build RAG assistants from Codex using skills and MCP tools.

The official Pinecone plugin for [Codex](https://developers.openai.com/codex) adds Pinecone skills and the Pinecone MCP server to your Codex sessions. Use natural language to manage indexes, query data, build RAG applications, and create document Q\&A assistants, with up-to-date Pinecone API knowledge.

<PrimarySecondaryCTA />

## Features

* Built-in skills cover index management, semantic search, full-text search, assistant creation, and more.
* The bundled MCP server runs Pinecone operations directly from Codex, with no extra setup.
* Codex invokes the right skill based on your conversation.

## Prerequisites

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* The [ChatGPT desktop app](https://developers.openai.com/codex/app) (which includes Codex) or the [Codex CLI](https://developers.openai.com/codex/cli)
* A local Codex session, since the plugin runs on your machine and doesn't work in Codex cloud tasks
* [Node.js](https://nodejs.org/) installed and on your `PATH` (required for the bundled MCP server)
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (required to run the bundled Python scripts, including the quickstart skill)
* [Pinecone CLI](/reference/cli/quickstart) installed (optional, enables the `pinecone:cli` skill)

## Installation

Install the plugin from the plugin directory or the command line, then set your API key and launch Codex.

<Steps>
  <Step title="Add the plugin to Codex">
    <Tabs>
      <Tab title="Plugin directory">
        Open the [Pinecone plugin](https://chatgpt.com/codex/open-app?target=plugin\&plugin_id=plugins_6ab1957381a88191b41034b7a47dc51f) in the ChatGPT desktop app, then click **Install plugin**.

        To find it yourself instead:

        1. In the ChatGPT desktop app, click your profile in the bottom left, then click **Settings**.

        2. In the left navigation, click **Plugins**.

           You'll see a list of the plugins you already have.

        3. Click **Browse directory**.

        4. Search for Pinecone, then select **Pinecone**.

        5. Click **Install plugin**.

        For more about installing plugins, see [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) in the OpenAI Help Center.
      </Tab>

      <Tab title="Command line">
        1. Add the Pinecone marketplace:

           ```shell theme={null}
           codex plugin marketplace add pinecone-io/pinecone-codex-plugin
           ```

        2. Install the plugin:

           ```shell theme={null}
           codex plugin add pinecone --marketplace pinecone-codex-plugins
           ```

        3. Confirm the plugin is installed:

           ```shell theme={null}
           codex plugin list | grep pinecone
           ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Set your API key and launch Codex">
    Installing the plugin doesn't set your API key. Codex reads it from the environment it launches in.

    <Tabs>
      <Tab title="CLI (macOS, Linux)">
        1. Set the key in the same shell where you run Codex:

           ```shell theme={null}
           export PINECONE_API_KEY="YOUR_API_KEY"
           ```

           Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys). To keep it across terminal sessions, add the line to your shell profile, such as `~/.zshrc`.

        2. Start Codex:

           ```shell theme={null}
           codex
           ```
      </Tab>

      <Tab title="CLI (Windows)">
        If you run Codex in WSL, use the **CLI (macOS, Linux)** tab instead.

        1. Set the key in the same PowerShell session where you run Codex:

           ```powershell theme={null}
           $env:PINECONE_API_KEY="YOUR_API_KEY"
           ```

           Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys). This lasts for the current session only. To keep it across sessions, run `setx PINECONE_API_KEY "YOUR_API_KEY"` and open a new terminal.

        2. Start Codex:

           ```powershell theme={null}
           codex
           ```
      </Tab>

      <Tab title="Desktop app (macOS)">
        1. Set the key for all macOS apps:

           ```shell theme={null}
           launchctl setenv PINECONE_API_KEY "YOUR_API_KEY"
           ```

           Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys). This setting doesn't persist after you restart your Mac, so run it again after each restart.

        2. Quit the ChatGPT desktop app completely, then reopen it.
      </Tab>

      <Tab title="Desktop app (Windows)">
        1. Set the key for your Windows user account:

           ```powershell theme={null}
           setx PINECONE_API_KEY "YOUR_API_KEY"
           ```

           Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys). `setx` persists across restarts.

        2. Quit the ChatGPT desktop app completely, then reopen it.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Run the quickstart">
    In a new Codex session, ask:

    ```text theme={null}
    Use Pinecone's quickstart to create an index, add sample data, and run my first search.
    ```

    Codex invokes the `pinecone:quickstart` skill, checks the connection to the Pinecone MCP server, creates an integrated index, upserts sample records, and runs a search.
  </Step>
</Steps>

## Available skills

Codex picks the right skill based on what you ask. To call a skill directly, type `$` followed by its name, such as `$pinecone:quickstart`. To bring in the whole plugin, mention `@pinecone`.

| Skill | Description |
| - | - |
| `pinecone:help` | Overview of all skills and setup requirements. Start here. |
| `pinecone:quickstart` | Walks you through creating an index, upserting data, and running a query. |
| `pinecone:query` | Search integrated indexes using natural language via the Pinecone MCP server. |
| `pinecone:assistant` | Create, upload, sync, and chat with Pinecone Assistants for document Q\&A with citations. |
| `pinecone:cli` | Guide for using the Pinecone CLI (`pc`) from the terminal. |
| `pinecone:full-text-search` | Create, ingest into, and query a Pinecone full-text-search (FTS) index. Requires Python SDK v10.0.0 or later. |
| `pinecone:n8n` | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| `pinecone:mcp` | Reference for all Pinecone MCP server tools. |
| `pinecone:docs` | Curated links to official Pinecone documentation. |

## MCP tools

The plugin includes the Pinecone MCP server, which provides the following tools:

* `search-docs`: Search the official Pinecone documentation.
* `list-indexes`: List all available Pinecone indexes.
* `describe-index`: Get index configuration and namespaces.
* `describe-index-stats`: Get record counts and namespace statistics.
* `create-index-for-model`: Create a new index with integrated embeddings.
* `upsert-records`: Insert or update records in an index.
* `search-records`: Search records with optional metadata filtering and reranking.
* `cascading-search`: Search across multiple indexes with deduplication and reranking.
* `rerank-documents`: Rerank documents using a specified reranking model.

For full MCP server documentation, see [Use the Pinecone MCP server](/guides/operations/mcp-server).

## Troubleshooting

<AccordionGroup>
  <Accordion title="API key not found or 401 errors">
    Check whether your API key is set in the environment Codex runs in:

    * For the CLI on macOS or Linux, in the same shell where you run `codex`, run `[ -n "$PINECONE_API_KEY" ] && echo "set" || echo "not set"`. If it prints `not set`, set the key again.
    * For the CLI on Windows, in the same PowerShell session where you run `codex`, run `if ($env:PINECONE_API_KEY) { "set" } else { "not set" }`. If it prints `not set`, set the key again.
    * For the desktop app on macOS, run `launchctl getenv PINECONE_API_KEY`. If it returns nothing, set the key again, then quit and reopen the app.
    * For the desktop app on Windows, run `[Environment]::GetEnvironmentVariable("PINECONE_API_KEY", "User")` in PowerShell. If it returns nothing, set the key again, then quit and reopen the app.
  </Accordion>

  <Accordion title="MCP server not responding">
    Make sure Node.js is on your `PATH` and your API key is valid, then restart Codex.
  </Accordion>

  <Accordion title="The query skill returns no results">
    The `pinecone:query` skill works only with integrated indexes, which use a Pinecone-hosted embedding model. For indexes that use external embeddings, use the `pinecone:cli` skill or the MCP tools directly.
  </Accordion>

  <Accordion title="Skill script errors">
    Run `uv --version` to confirm `uv` is installed. If it's missing, install it and restart your terminal.
  </Accordion>
</AccordionGroup>

## Resources

* [GitHub repository](https://github.com/pinecone-io/pinecone-codex-plugin)
* [Codex documentation](https://developers.openai.com/codex)
* [Plugins in ChatGPT (OpenAI Help Center)](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
* [Pinecone MCP server guide](/guides/operations/mcp-server)
