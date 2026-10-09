---
title: "AI coding tools"
source: https://docs.pinecone.io/integrations/ai-coding-tools
path: integrations/ai-coding-tools
---

Use Pinecone with AI coding tools like Claude Code, Codex, and Cursor through the Pinecone MCP server, plugins, and agent skills.

Pinecone provides official plugins and agent skills for AI coding tools. Use the Pinecone [MCP server](/guides/operations/mcp-server) (Model Context Protocol) and built-in skills to manage indexes, run semantic search, and build RAG applications, all through natural language in your development environment. For direct, scriptable access from the same terminal, the [Pinecone CLI](/reference/cli/quickstart) (`pc`) lets you manage indexes, namespaces, and records without an agent in the loop.

## Choose your tool

<CardGroup>
  <Card title="Claude Code plugin" icon="plug" href="/integrations/claude-code">
    Official Pinecone plugin for Claude Code with skills, MCP tools, and slash commands.
  </Card>

  <Card title="Codex plugin" icon="plug" href="/integrations/codex">
    Official Pinecone plugin for Codex with skills and MCP tools.
  </Card>

  <Card title="Cursor plugin" icon="plug" href="/integrations/cursor">
    Official Pinecone plugin for Cursor with skills, MCP tools, and slash commands.
  </Card>

  <Card title="Agent Skills" icon="layer-group" href="/integrations/agent-skills">
    Universal skills library for GitHub Copilot and other agentic IDEs.
  </Card>

  <Card title="MCP server" icon="server" href="/guides/operations/mcp-server">
    Connect any MCP-compatible client to Pinecone for index management and search.
  </Card>

  <Card title="Pinecone CLI" icon="rectangle-terminal" href="/reference/cli/quickstart">
    Direct terminal access to Pinecone. Manage indexes, namespaces, and records with `pc` commands.
  </Card>
</CardGroup>

## Tool recommendations

| Your tool | What to install | Command |
| - | - | - |
| [Claude Code](https://claude.ai/code) | [Pinecone plugin for Claude Code](/integrations/claude-code) | `claude plugin install pinecone` |
| [Codex](https://developers.openai.com/codex) | [Pinecone plugin for Codex](/integrations/codex) | See [install steps](/integrations/codex#installation) |
| [Cursor](https://www.cursor.com/) | [Pinecone Cursor plugin](/integrations/cursor) | `/add-plugin pinecone` |
| [GitHub Copilot](https://github.com/features/copilot) or another agentic IDE | [Pinecone Agent Skills](/integrations/agent-skills) | `npx skills add pinecone-io/skills` |
| Claude Desktop, Antigravity, or another MCP client | [Pinecone MCP server](/guides/operations/mcp-server) | See [MCP server setup](/guides/operations/mcp-server) |
| Your terminal directly (no agent) | [Pinecone CLI](/reference/cli/quickstart) | `brew install pinecone-io/tap/pinecone` |

All tools require a [Pinecone API key](https://app.pinecone.io/organizations/-/keys). Sign up for a free account at [app.pinecone.io](https://app.pinecone.io).

## What's included

Each tool provides access to the following Pinecone skills. Invocation names vary by tool, for example `/pinecone:quickstart` in Claude Code and `pinecone-quickstart` in Agent Skills.

| Skill | Description |
| - | - |
| Quickstart | Step-by-step onboarding that walks you through creating an index, uploading data, and running your first search. |
| Query | Search integrated indexes using natural language text via the Pinecone MCP. |
| Assistant | Create, manage, and chat with Pinecone Assistants for document Q\&A with citations. |
| CLI | Use the Pinecone CLI for terminal-based index and vector management. |
| Full-text search | Create, ingest into, and query a Pinecone full-text-search (FTS) index. |
| n8n | Build [n8n](/integrations/n8n) workflows with the Pinecone Assistant node or Pinecone Vector Store, including best practices and full workflow JSON generation. |
| MCP | Reference for all available Pinecone MCP server tools and their parameters. |
| Docs | Curated links to official Pinecone documentation, organized by topic. |
| Help | Overview of all skills and what you need to get started. |

In addition, the [Pinecone MCP server](/guides/operations/mcp-server) provides tools for listing indexes, creating indexes, upserting records, searching, reranking, and more.
