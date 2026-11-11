---
title: "List workspaces in the organization"
source: https://developers.notion.com/reference/admin/list-spaces
path: reference/admin/list-spaces
---

openapi-adminApi.json GET /v1/spaces
List the workspaces your organization owns.

The organization bot token must have the following scopes:

* `workspace:read`

Returns the live workspaces owned by your organization, ordered by ID. Each result includes the workspace `id` and `name`. Use the `id` as the `space_id` path parameter in workspace-scoped endpoints, such as [List users](/reference/admin/list-users).

Deleted workspaces and workspaces outside your organization aren't included. Use `page_size` and `start_cursor` to page through results.
