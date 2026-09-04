---
title: "Add a group member"
source: https://developers.notion.com/reference/admin/add-permission-group-member
path: reference/admin/add-permission-group-member
---

openapi-adminApi.json POST /v1/spaces/{space_id}/groups/{group_id}/members
Add a direct user member to an admin-managed permission group.

The organization bot token must have the following scopes:

* `permission-group:write`

The target must be a workspace member; guests aren't supported. Restricted members must be allowed by the workspace's plan and security settings and cannot be group owners.

SCIM-managed memberships must be changed through the configured identity provider. Trying to add a member to one returns a `409 conflict_error`.
