---
title: "List MCP client connections in an organization"
source: https://developers.notion.com/reference/admin/list-mcp-client-connections
path: reference/admin/list-mcp-client-connections
---

openapi-adminApi.json GET /v1/mcp_client_connections
List inbound MCP client connections across an organization.

The organization bot token must have the following scopes:

* `mcp-client-connection:read`

Returns one result for each member, client, and governance state. Connections are grouped into one row only when `is_enterprise_managed` and `idp_issuer` match, so every workspace in a row can be governed the same way. Within a row, `created_at` is the earliest connection time and `last_active_at` is the most recent activity time.

Use bracket encoding to filter by one or more members or workspaces:

```text theme={null}
?user_ids[]=aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa&workspace_ids[]=bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb
```

Filters only match workspaces in the organization that owns the token. Unknown or out-of-organization IDs return no matching results. A `workspace_ids` filter limits both the returned rows and their connection metadata to the selected workspaces; state from an excluded workspace is not folded into a matching row.

The response contains the standard user reference only. For clients in Notion's trusted registry, `client.name` and `client.type` come from that registry. A custom or unregistered client's name can come from metadata reported by the client and its type is `other`; use `client.key` as the stable identifier. `idp_issuer` is present only for enterprise-managed connections.

This endpoint inventories member-bound OAuth client connections. It does not include direct MCP usage through personal access tokens or workspace-owned internal integrations. Govern personal access tokens with the [personal access token endpoints](/reference/admin/revoke-personal-access-token); manage internal integrations in the workspace's integration settings.
