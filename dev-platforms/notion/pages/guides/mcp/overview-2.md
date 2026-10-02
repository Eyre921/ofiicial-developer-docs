---
title: "Notion MCP"
source: https://developers.notion.com/guides/mcp/overview
path: guides/mcp/overview
---

Learn how MCP clients connect to your Notion workspace.

Notion MCP lets an [MCP client](/guides/mcp/common-mcp-clients), such as Claude Code, Cursor, or Codex, connect to your Notion workspace through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction).

## How Notion MCP works

Notion MCP is a remote MCP server hosted by Notion. After you authorize a connection with OAuth, the MCP client can use Notion MCP tools to read and update content that you can access.

<Frame>
  <img alt="Diagram showing an MCP client connecting to Notion's remote MCP server, which uses the Notion API." />
</Frame>

## What you can do

MCP clients can combine Notion MCP tools to:

* Search content in Notion and connected sources.
* Read, create, and update Notion content.
* Create pages and databases.

See [Supported tools](/guides/mcp/mcp-supported-tools) for the current tool list, or [connect an MCP client](/guides/mcp/get-started-with-mcp).

## Admin controls

Workspace owners can manage MCP client access in **Settings** → **Connections**. Organization owners can also use the Admin API to [list](/reference/admin/list-mcp-client-connections) and [revoke](/reference/admin/revoke-mcp-client-connection) members' connections.

See [Admin controls for MCP](https://www.notion.com/help/notion-mcp#admin-controls-for-mcp) in the Notion Help Center for workspace settings and allowlists.
