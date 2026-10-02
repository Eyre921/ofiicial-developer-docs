---
title: "List groups"
source: https://developers.notion.com/reference/admin/list-permission-groups
path: reference/admin/list-permission-groups
---

openapi-adminApi.json GET /v1/spaces/{space_id}/groups
List permission groups in a workspace.

The organization bot token must have the following scopes:

* `permission-group:read`

Returns both admin-managed and SCIM-managed permission groups. Use a group's `id` to retrieve the group or manage its direct user memberships.
