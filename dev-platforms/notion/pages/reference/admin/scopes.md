---
title: "Scopes"
source: https://developers.notion.com/reference/admin/scopes
path: reference/admin/scopes
---

Admin API scopes control an organization bot token's access.

When you create an organization bot token, you assign scopes that control which resources the token can access and which actions it can take.

Each scope combines a resource and a capability, such as `legal-hold:read`.

## Scope resources

| Scope resource          | Controls access to                                      |
| :---------------------- | :------------------------------------------------------ |
| `legal-hold`            | Legal hold data and members                             |
| `managed-user-session`  | Managed users' active sessions                          |
| `mcp-client-connection` | Members' MCP client connections                         |
| `personal-access-token` | Personal access tokens in the organization's workspaces |
| `workspace`             | Workspace data and settings                             |

<Warning>
  This table may not include every scope. Each endpoint's reference lists the exact scope it requires.
</Warning>

## Scope capabilities

| Scope capability    | Allows the token to                                            |
| :------------------ | :------------------------------------------------------------- |
| `read`              | View a resource                                                |
| `write`             | Modify a resource                                              |
| `write-high-impact` | Make sensitive changes, such as revoking credentials or access |
| `export`            | Export a resource                                              |
