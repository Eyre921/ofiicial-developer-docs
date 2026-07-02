---
title: "Agentic IDEs and CLIs"
source: https://docs.pinecone.io/guides/get-started/ai-coding-tools
path: guides/get-started/ai-coding-tools
---

Use Pinecone with agentic IDEs and CLIs like Claude Code, Gemini CLI, Cursor, and more.

Pinecone provides official plugins, extensions, and agent skills for agentic IDEs and CLIs. Use the Pinecone [MCP server](/guides/operations/mcp-server) (Model Context Protocol) and built-in skills to manage vector database indexes, run semantic search, and build RAG applications — all through natural language in your development environment. For direct, scriptable access from the same terminal, the [Pinecone CLI](/reference/cli/quickstart) (`pc`) lets you manage indexes, namespaces, and records without an agent in the loop.

## Choose your tool

<CardGroup>
  <Card title="Claude Code Plugin" icon="plug" href="/integrations/claude-code">
    Official Pinecone plugin for Claude Code with skills, MCP tools, and slash commands.
  </Card>

  <Card title="Gemini CLI Extension" icon="terminal" href="/integrations/gemini-cli">
    Official Pinecone extension for Gemini CLI with skills and MCP tools.
  </Card>

  <Card title="Cursor Plugin" icon="plug" href="/integrations/cursor">
    Official Pinecone plugin for Cursor with skills, MCP tools, and slash commands.
  </Card>

  <Card title="Agent Skills" icon="layer-group" href="/integrations/agent-skills">
    Universal skills library for GitHub Copilot, Codex, and other agentic IDEs.
  </Card>

  <Card title="MCP Server" icon="server" href="/guides/operations/mcp-server">
    Connect any MCP-compatible client to Pinecone for index management and search.
  </Card>

  <Card title="Pinecone CLI" icon="rectangle-terminal" href="/reference/cli/quickstart">
    Direct terminal access to Pinecone — manage indexes, namespaces, and records with `pc` commands.
  </Card>
</CardGroup>

## Which tool should I use?

| If you use...                                                                                                     | Install...                                                   | Command                                                                         |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [Claude Code](https://claude.ai/code)                                                                             | [Pinecone plugin for Claude Code](/integrations/claude-code) | `claude plugin install pinecone`                                                |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)                                                         | [Pinecone Gemini CLI extension](/integrations/gemini-cli)    | `gemini extensions install https://github.com/pinecone-io/gemini-cli-extension` |
| [Cursor](https://www.cursor.com/)                                                                                 | [Pinecone Cursor plugin](/integrations/cursor)               | `/add-plugin pinecone`                                                          |
| [GitHub Copilot](https://github.com/features/copilot), [Codex](https://chatgpt.com/codex), or another agentic IDE | [Pinecone Agent Skills](/integrations/agent-skills)          | `npx skills add pinecone-io/skills`                                             |
| Claude Desktop, Antigravity, or another MCP client                                                                | [Pinecone MCP server](/guides/operations/mcp-server)         | See [MCP server setup](/guides/operations/mcp-server)                           |
| Your terminal directly (no agent)                                                                                 | [Pinecone CLI](/reference/cli/quickstart)                    | `brew install pinecone-io/tap/pinecone`                                         |

All tools require a [Pinecone API key](https://app.pinecone.io/organizations/-/keys). Sign up for a free account at [app.pinecone.io](https://app.pinecone.io).

## What's included

Each tool provides access to the following Pinecone skills:

| Skill                | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| **quickstart**       | Step-by-step onboarding — create an index, upload data, and run your first search.            |
| **query**            | Search integrated indexes using natural language text via the Pinecone MCP.                   |
| **assistant**        | Create, manage, and chat with Pinecone Assistants for document Q\&A with citations.           |
| **cli**              | Use the Pinecone CLI for terminal-based index and vector management.                          |
| **full-text-search** | Create, ingest into, and query a Pinecone full-text-search (FTS) index using the preview API. |
| **mcp**              | Reference for all available Pinecone MCP server tools and their parameters.                   |
| **pinecone-docs**    | Curated links to official Pinecone documentation, organized by topic.                         |
| **help**             | Overview of all skills and what you need to get started.                                      |

In addition, the [Pinecone MCP server](/guides/operations/mcp-server) provides tools for listing indexes, creating indexes, upserting records, searching, reranking, and more.
