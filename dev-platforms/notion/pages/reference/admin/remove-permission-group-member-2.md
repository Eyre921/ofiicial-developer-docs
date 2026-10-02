---
title: "Remove a group member"
source: https://developers.notion.com/reference/admin/remove-permission-group-member
path: reference/admin/remove-permission-group-member
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/groups/{group_id}/members/users/{user_id}
Remove a direct user member from an admin-managed permission group.

The organization bot token must have the following scopes:

* `permission-group:write`

SCIM-managed memberships must be changed through the configured identity provider. Trying to remove one returns a `409 conflict_error`.
