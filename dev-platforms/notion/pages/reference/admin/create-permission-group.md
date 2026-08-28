---
title: "Create a group"
source: https://developers.notion.com/reference/admin/create-permission-group
path: reference/admin/create-permission-group
---

openapi-adminApi.json POST /v1/spaces/{space_id}/groups
Create an admin-managed permission group in a workspace.

The organization bot token must have the following scopes:

* `permission-group:write`

Creates an admin-managed permission group. Creating a group returns `409 conflict_error` if another active group has the same exact, case-sensitive name. Legacy duplicates may still appear in list responses.

After creating the group, use [Add a group member](/reference/admin/add-permission-group-member) to add direct user memberships.
