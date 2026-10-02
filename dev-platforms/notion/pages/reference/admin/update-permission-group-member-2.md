---
title: "Update a group member"
source: https://developers.notion.com/reference/admin/update-permission-group-member
path: reference/admin/update-permission-group-member
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/groups/{group_id}/members/users/{user_id}
Change a direct member's role in an admin-managed permission group.

The organization bot token must have the following scopes:

* `permission-group:write`

Set `role` to `owner` or `member`. Restricted members cannot be group owners.

SCIM-managed memberships must be changed through the configured identity provider. Trying to update one returns a `409 conflict_error`.
