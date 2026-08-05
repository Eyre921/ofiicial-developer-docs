---
title: "List MCP client connections in an organization"
source: https://developers.notion.com/reference/admin/list-mcp-client-connections
path: reference/admin/list-mcp-client-connections
---

openapi-adminApi.json GET /v1/mcp_client_connections
List members' connections to Notion through MCP clients.

The organization bot token must have the following scopes:

* `mcp-client-connection:read`

This endpoint lists OAuth connections that members use to connect MCP clients, such as Claude Code or Codex, to Notion MCP. It does not include MCP requests authenticated with [personal access tokens](/guides/get-started/personal-access-tokens) or workspace-owned internal connections.

For workspace settings that control which MCP clients members can connect, see [Admin controls for Notion MCP](https://www.notion.com/help/notion-mcp#admin-controls-for-mcp).

## Results

Each result identifies a member, an MCP client, and the workspaces where they are connected. Within a result, `created_at` is the earliest connection time and `last_active_at` is the most recent activity time.

Connections for the same member and client can appear in one result across several workspaces. If your organization uses enterprise-managed connections, the API returns separate results when `is_enterprise_managed` or `idp_issuer` differs. `idp_issuer` is present only for enterprise-managed connections.

## Filter results

Use bracket encoding to filter by one or more members or workspaces:

```text theme={null}
?user_ids[]=aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa&workspace_ids[]=bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb
```

Filters only match workspaces in the organization that owns the token. Unknown IDs and IDs outside the organization return no results. A `workspace_ids` filter also limits the `workspaces` array in each result.

## Identify an MCP client

For recognized MCP clients, Notion provides `client.name` and `client.type`. A custom or unregistered client can provide its own name, and its type is `other`. Use `client.key`, not the name, to identify the client in later API requests.
