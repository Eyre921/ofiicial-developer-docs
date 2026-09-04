---
title: "Use the Pinecone MCP server"
source: https://docs.pinecone.io/guides/operations/mcp-server
path: guides/operations/mcp-server
---

Connect AI agents to Pinecone through the MCP server to search docs, manage indexes, and query data from Claude, Cursor, Antigravity, or Claude Code.

The Pinecone MCP server enables AI agents to interact directly with Pinecone's functionality and documentation via the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Using the MCP server, agents can search Pinecone documentation, manage indexes, upsert data, and query indexes for relevant information.

This page shows you how to configure [Antigravity](https://antigravity.google/), [Claude Desktop](https://claude.ai/download), [Claude Code](https://claude.ai/code), and [Cursor](https://www.cursor.com/) to connect with the Pinecone MCP server.

<Note>
  Pinecone also provides a dedicated MCP server for each [Pinecone Assistant](/guides/assistant/overview), giving AI agents direct access to context from that assistant's uploaded files. The assistant MCP server is available as a managed remote endpoint or as a self-hosted Docker container that you can extend and run in your own infrastructure. See [Use an Assistant MCP server](/guides/assistant/mcp-server).
</Note>

<Tip>
  Pinecone also offers plugins and extensions with built-in skills for agentic IDEs and CLIs. See [Agentic IDEs and CLIs](/integrations/ai-coding-tools) for an overview, or jump directly to the [Claude Code plugin](/integrations/claude-code), [Gemini CLI extension](/integrations/gemini-cli), [Cursor plugin](/integrations/cursor), or [Agent Skills](/integrations/agent-skills) for GitHub Copilot and other IDEs.
</Tip>

## Tools

The Pinecone MCP server provides the following tools:

* `search-docs`: Search the official Pinecone documentation.
* `list-indexes`: Lists all Pinecone indexes.
* `describe-index`: Describes the configuration of an index.
* `describe-index-stats`: Provides statistics about the data in the index, including the  number of records and available namespaces.
* `create-index-for-model`: Creates a new index that uses an integrated inference model to embed text as vectors.
* `upsert-records`: Inserts or updates records in an index with integrated inference.
* `search-records`: Searches for records in an index based on a text query, using integrated inference for embedding. Has options for metadata filtering and reranking.
* `cascading-search`: Searches for records across multiple indexes, deduplicating and reranking the results.
* `rerank-documents`: Reranks a collection of records or text documents using a specialized reranking model.

<Note>
  The Pinecone MCP supports only [indexes with integrated embedding](/guides/index-data/indexing-overview#vector-embedding). Indexes for vectors you create with external embedding models are not supported.
</Note>

## Before you begin

Ensure you have the following:

* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys)
* [Node.js](https://nodejs.org/en) installed, with `node` and `npx` available on your `PATH`

## Configure Antigravity

Antigravity supports MCP via its built-in MCP Store. You can install the Pinecone server from the store or add it via the raw config.

<Steps>
  <Step title="Add the MCP server">
    **Install from the MCP Store**

    1. Open the **MCP Store** via the "..." dropdown at the top of the editor's agent panel.
    2. Find **Pinecone** in the list of supported servers and click **Install**.
    3. Follow the on-screen prompts to authenticate and set your Pinecone API key.

    **Add via raw config**

    1. Open the MCP Store via the "..." dropdown at the top of the editor's agent panel.
    2. Click **Manage MCP Servers**, then **View raw config**.
    3. Edit `mcp_config.json` and add the Pinecone server:

    ```json theme={null}
    {
      "mcpServers": {
        "pinecone": {
          "command": "npx",
          "args": [
            "-y", "@pinecone-database/mcp"
          ],
          "env": {
            "PINECONE_API_KEY": "{{YOUR_API_KEY}}"
          }
        }
      }
    }
    ```

    Replace `YOUR_API_KEY` with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys).
  </Step>

  <Step title="Check the status">
    After installing or saving the config, the Pinecone server and its tools should appear in the agent panel. Use the MCP tools list to confirm the server is connected.
  </Step>

  <Step title="Test the server">
    In the agent chat, try prompts that use Pinecone. For example, try generating code that creates an index, upserts records, or searches the index. The AI can use the connected MCP server for context and actions.
  </Step>
</Steps>

## Configure Claude Code

<Tip>
  For the easiest setup, install the [Pinecone Claude Code plugin](/integrations/claude-code) instead — it bundles the MCP server, 8 skills, and slash commands. The manual configuration below is for users who only want the MCP server.
</Tip>

<Steps>
  <Step title="Add the MCP server">
    Run the following command to add the Pinecone MCP server to your Claude Code instance:

    ```bash theme={null}
    claude mcp add-json pinecone-mcp \
      '{"type": "stdio",
        "command": "npx",
        "args": ["-y", "@pinecone-database/mcp"],
        "env": {"PINECONE_API_KEY": "YOUR_API_KEY"}}'
    ```
  </Step>

  <Step title="Check the status">
    Restart Claude Code. Then, run the `/mcp` command to check the status of the Pinecone MCP. You should see the following:

    ```bash theme={null}
      > /mcp 
        ⎿  MCP Server Status

          • pinecone-mcp: ✓ connected

    ```
  </Step>

  <Step title="Test the server">
    Test the Pinecone MCP server with prompts to Claude Code that require the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates an index for dense vectors with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create an index for dense vectors with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>

## Configure Claude Desktop

<Steps>
  <Step title="Add the MCP server">
    Go to **Settings > Developer > Edit Config** and add the following configuration:

    ```json theme={null}
    {
      "mcpServers": {
        "pinecone": {
          "command": "npx",
          "args": [
            "-y", "@pinecone-database/mcp"
          ],
          "env": {
            "PINECONE_API_KEY": "YOUR_API_KEY"
          }
        }
      }
    }
    ```

    Replace `YOUR_API_KEY` with your Pinecone API key.
  </Step>

  <Step title="Check the status">
    Restart Claude Desktop. On the new chat screen, you should see a hammer (MCP) icon appear with the new MCP tools available.
  </Step>

  <Step title="Test the server">
    Test the Pinecone MCP server with prompts that required the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates an index for dense vectors with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create an index for dense vectors with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>

## Configure Cursor

<Tip>
  For the easiest setup, install the [Pinecone Cursor plugin](/integrations/cursor) instead — it bundles the MCP server, 8 skills, and slash commands. The manual configuration below is for users who only want the MCP server.
</Tip>

<Steps>
  <Step title="Add the MCP server">
    In your project root, create a `.cursor/mcp.json` file, if it doesn't exist, and add the following configuration:

    ```json theme={null}
    {
      "mcpServers": {
        "pinecone": {
          "command": "npx",
          "args": [
            "-y", "@pinecone-database/mcp"
          ],
          "env": {
            "PINECONE_API_KEY": "{{YOUR_API_KEY}}"
          }
        }
      }
    }
    ```
  </Step>

  <Step title="Check the status">
    Go to **Cursor Settings > MCP**. You should see the server and its list of tools.
  </Step>

  <Step title="Add Pinecone rules">
    The Pinecone MCP server works well out of the box. However, you can add explicit rules to ensure the server behaves as you expect.

    In your project root, create a `.cursor/rules/pinecone.mdc` file and add the following:

    ```mdx [expandable] theme={null}
    ### Tool Usage for Code Generation

    - When generating code related to Pinecone, always use the `pinecone` MCP and the `search_docs` tool.

    - Perform at least two distinct searches per request using different, relevant questions to ensure comprehensive context is gathered before writing code.

    ### Error Handling

    - If an error occurs while executing Pinecone-related code, immediately invoke the `pinecone` MCP and the `search_docs` tool.

    - Search for guidance on the specific error encountered and incorporate any relevant findings into your resolution strategy.

    ### Syntax and Version Accuracy

    - Before writing any code, verify and use the correct syntax for the latest stable version of the Pinecone SDK.

    - Prefer official code snippets and examples from documentation over generated or assumed field values.

    - Do not fabricate field names, parameter values, or request formats.

    ### SDK Installation Best Practices

    - When providing installation instructions, always reference the current official package name.

    - For Pinecone, use `pip install pinecone` not deprecated packages like `pinecone-client`.
    ```
  </Step>

  <Step title="Test the server">
    Press `Command + i` to open the Agent chat. Test the Pinecone MCP server with prompts that required the server to generate Pinceone-compatible code and perform tasks in your Pinecone account.

    Generate code:

    > Write a Python script that creates an index for dense vectors with integrated embedding, upserts 20 sentences about dogs, waits 10 seconds, searches the index, and reranks the results.

    Perform tasks:

    > Create an index for dense vectors with integrated embedding, upsert 20 sentences about dogs, waits 10 seconds, search the index, and reranks the results.
  </Step>
</Steps>
