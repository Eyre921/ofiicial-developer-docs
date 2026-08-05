---
title: "Security best practices"
source: https://developers.notion.com/guides/mcp/mcp-security-best-practices
path: guides/mcp/mcp-security-best-practices
---

Learn how to keep your workspace secure when using Notion MCP.

Use Notion's official MCP endpoints:

1. [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp) for Streamable HTTP (recommended).
2. [https://mcp.notion.com/sse](https://mcp.notion.com/sse) for Server-Sent Events (SSE).

Review the [documentation for common MCP clients](/guides/mcp/common-mcp-clients), and only connect clients you trust. A connected client can use Notion MCP to access content that you can access. Before installing a client from a third-party marketplace, verify the marketplace and the MCP server URL.

## Protect against prompt injection

[Prompt injection](https://devblogs.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp) occurs when untrusted content contains instructions that try to change a client's behavior.

<Note>
  **Protect your data**

  An attacker could put a malicious instruction in content that your MCP client reads. If the client follows the instruction, it could disclose data or change content without your intent.

  Treat content returned by tools as untrusted. Review proposed actions and data sharing before approving them.
</Note>

Review the permissions of every MCP client and tool. Notion MCP operates within your workspace, but a connected client may send content returned by Notion MCP to systems outside Notion.

Enable confirmation before actions that change content. This lets you review an action before the MCP client runs it.

## Admin controls

Workspace owners can manage MCP client access in **Settings** → **Connections**. Organization owners can also use the Admin API to [list](/reference/admin/list-mcp-client-connections) and [revoke](/reference/admin/revoke-mcp-client-connection) members' connections. See [Admin controls for MCP](https://www.notion.com/help/notion-mcp#admin-controls-for-mcp) for details.
