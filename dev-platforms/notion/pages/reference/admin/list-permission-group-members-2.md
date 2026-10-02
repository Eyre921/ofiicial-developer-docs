---
title: "List group members"
source: https://developers.notion.com/reference/admin/list-permission-group-members
path: reference/admin/list-permission-group-members
---

openapi-adminApi.json GET /v1/spaces/{space_id}/groups/{group_id}/members
List a permission group's direct user memberships.

The organization bot token must have the following scopes:

* `permission-group:read`

Returns direct user memberships for admin-managed and SCIM-managed groups. Nested-group memberships are not included.

Each membership's `role` is either `owner` or `member`.
