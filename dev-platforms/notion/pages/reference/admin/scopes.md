---
title: "Scopes"
source: https://developers.notion.com/reference/admin/scopes
path: reference/admin/scopes
---

Learn about customizing the capabilities for an organization bot token.

When organization bot tokens are created, they are assigned some collection of unique scopes. These scopes determine which resources in your organization the bot token can access and how it can access them.

Scopes are structured by combining a `resource` and a `capability` (for example, `legal-hold:read`).

### List of Admin API scope resources

| Scope resource          | Description                                                         |
| :---------------------- | :------------------------------------------------------------------ |
| `legal-hold`            | Ability to manage legal hold data and members                       |
| `managed-user-session`  | Ability to control managed users' active sessions                   |
| `mcp-client-connection` | Ability to view and govern members' MCP client connections          |
| `workspace`             | Ability to manage your organization's workspaces' data and settings |

<Warning>
  These scope resources may not be exhaustive. Please consult the API reference you wish to use to see the most accurate scope required to manage the resource you want.
</Warning>

### List of Admin API scope capabilities

| Scope capability    | Description                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------ |
| `read`              | Ability to view a resource                                                                  |
| `write`             | Ability to modify a resource                                                                |
| `write-high-impact` | Ability to make sensitive changes, including revoking credentials or changing member access |
| `export`            | Ability to export a resource                                                                |
