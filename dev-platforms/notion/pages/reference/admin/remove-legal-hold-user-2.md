---
title: "Remove a user from a legal hold"
source: https://developers.notion.com/reference/admin/remove-legal-hold-user
path: reference/admin/remove-legal-hold-user
---

openapi-adminApi.json DELETE /v1/legal_holds/{legal_hold_id}/users/{user_id}
Remove a user from a legal hold.

The organization bot token must have the following scopes:

* `legal-hold:write`
