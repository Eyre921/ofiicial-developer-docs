---
title: "Revoke an MCP client connection"
source: https://developers.notion.com/reference/admin/revoke-mcp-client-connection
path: reference/admin/revoke-mcp-client-connection
---

openapi-adminApi.json POST /v1/mcp_client_connections/revoke
Revoke a member's active connection to Notion from an MCP client.

The organization bot token must have the following scopes:

* `mcp-client-connection:write-high-impact`

This endpoint revokes the active OAuth tokens for one member and MCP client in a workspace. Use [List MCP client connections](/reference/admin/list-mcp-client-connections) to get the `client_key`.

The response gives the number of tokens revoked. The endpoint returns the same not-found response when the member, workspace, or connection does not exist or is outside the organization.

Revoking tokens disconnects the member, but does not prevent them from connecting the client again if workspace policy allows it. To control which MCP clients members can connect, see [Admin controls for Notion MCP](https://www.notion.com/help/notion-mcp#admin-controls-for-mcp).

## Enterprise-managed access

If your organization uses enterprise-managed connections, you can [deny a member's enterprise-managed access](/reference/admin/update-mcp-client-connection-enterprise-managed-access) to revoke their current tokens and prevent them from connecting again through enterprise-managed authentication. This setting applies to the member and workspace, not only to the client identified by `client_key`.
