---
title: "Delete a group"
source: https://developers.notion.com/reference/admin/delete-permission-group
path: reference/admin/delete-permission-group
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/groups/{group_id}
Delete an admin-managed permission group.

The organization bot token must have the following scopes:

* `permission-group:write`

If deleting the group would orphan access, pass an active workspace owner as `transfer_to_owner_id`. Omitting a required transfer target returns a `409 conflict_error` and leaves the group unchanged.

SCIM-managed groups must be deleted through the configured identity provider.
