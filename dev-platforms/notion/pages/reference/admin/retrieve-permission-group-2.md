---
title: "Retrieve a group"
source: https://developers.notion.com/reference/admin/retrieve-permission-group
path: reference/admin/retrieve-permission-group
---

openapi-adminApi.json GET /v1/spaces/{space_id}/groups/{group_id}
Retrieve a permission group in a workspace.

The organization bot token must have the following scopes:

* `permission-group:read`

Returns an admin-managed or SCIM-managed permission group by ID. SCIM-managed groups are readable, but must be changed through the configured identity provider.
