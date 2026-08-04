---
title: "Revoke an MCP client connection"
source: https://developers.notion.com/reference/admin/revoke-mcp-client-connection
path: reference/admin/revoke-mcp-client-connection
---

openapi-adminApi.json POST /v1/mcp_client_connections/revoke
Revoke a member's current MCP client connection tokens.

The organization bot token must have the following scopes:

* `mcp-client-connection:write-high-impact`

Revokes active tokens for one member and client in a workspace. Use the [list MCP client connections](/reference/admin/list-mcp-client-connections) endpoint to obtain the `client_key`.

The operation returns the number of tokens revoked. If the member, workspace, or connection is not available to the organization token, the endpoint returns the same not-found response.

<Warning>
  For an enterprise-managed connection, token revocation is temporary because the client can authenticate again. To block future connections, use [deny or restore enterprise-managed access](/reference/admin/update-mcp-client-connection-enterprise-managed-access) with `access` set to `denied`. The deny applies to that member's enterprise-managed access for the workspace, not only to the connection identified by `client_key`.
</Warning>
