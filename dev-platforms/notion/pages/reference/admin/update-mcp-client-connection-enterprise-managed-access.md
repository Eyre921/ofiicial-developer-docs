---
title: "Deny or restore enterprise-managed MCP client access"
source: https://developers.notion.com/reference/admin/update-mcp-client-connection-enterprise-managed-access
path: reference/admin/update-mcp-client-connection-enterprise-managed-access
---

openapi-adminApi.json PUT /v1/mcp_client_connections/enterprise_managed_access
Deny or restore a member's access through enterprise-managed MCP connections.

The organization bot token must have the following scopes:

* `mcp-client-connection:write-high-impact`

Use this endpoint only for enterprise-managed connections. It controls one member's enterprise-managed MCP access in one workspace. It does not apply to MCP client connections that members authorize themselves.

Set `access` to `denied` to block future connections and revoke the member's current tokens. Set it to `allowed` to remove the block.

You can repeat the same request safely. Repeating a deny keeps access blocked and revokes any new tokens. Repeating a restore keeps access allowed. You can restore access only when enterprise-managed connections are available for the workspace.

The workspace and member must belong to the organization that owns the token. The endpoint returns the same not-found response for invalid targets and targets outside the organization.
