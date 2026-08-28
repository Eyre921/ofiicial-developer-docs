---
title: "List users"
source: https://developers.notion.com/reference/admin/list-users
path: reference/admin/list-users
---

openapi-adminApi.json GET /v1/spaces/{space_id}/users
List active workspace members and guest bots.

The organization bot token must have the following scopes:

* `user:read`

Returns a cursor-paginated directory of active workspace members—including restricted members—and guest bots. Each result uses the standard Notion user object shape. Person entries include an email at `person.email` when available; bot entries include a `bot` object. This endpoint currently returns `avatar_url` as `null`.

Page guests and expired temporary memberships are not included. Search and single-user lookup parameters are not supported.
