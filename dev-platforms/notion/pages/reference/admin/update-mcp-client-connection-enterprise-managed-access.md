---
title: "Deny or restore enterprise-managed MCP client access"
source: https://developers.notion.com/reference/admin/update-mcp-client-connection-enterprise-managed-access
path: reference/admin/update-mcp-client-connection-enterprise-managed-access
---

openapi-adminApi.json PUT /v1/mcp_client_connections/enterprise_managed_access
Deny or restore a member's enterprise-managed MCP client access.

The organization bot token must have the following scopes:

* `mcp-client-connection:write-high-impact`

Set `access` to `denied` to block future connections and revoke the member's current tokens. Set it to `allowed` to remove the block.

The operation is idempotent. Repeating a deny keeps access blocked and cleans up any current tokens; repeating a restore keeps access allowed. Restoring access requires enterprise-managed connections to be available for the workspace.

The workspace and member must belong to the organization that owns the token. Invalid and out-of-organization targets return the same not-found response.
