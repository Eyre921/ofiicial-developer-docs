---
title: "Update a group"
source: https://developers.notion.com/reference/admin/update-permission-group
path: reference/admin/update-permission-group
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/groups/{group_id}
Rename an admin-managed permission group.

The organization bot token must have the following scopes:

* `permission-group:write`

Renaming a group returns `409 conflict_error` if another active group has the same exact, case-sensitive name. Legacy duplicates may still appear in list responses.

SCIM-managed groups must be changed through the configured identity provider. Trying to update one returns a `409 conflict_error`.
