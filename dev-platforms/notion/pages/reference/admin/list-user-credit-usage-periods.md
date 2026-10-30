---
title: "Get credit usage for a user in a space"
source: https://developers.notion.com/reference/admin/list-user-credit-usage-periods
path: reference/admin/list-user-credit-usage-periods
---

openapi-adminApi.json GET /v1/spaces/{space_id}/users/{user_id}/credit_usage
Get credit usage for a user in a space.

The organization bot token must have the following scopes:

* `user:read`

Returns one person's Notion credit usage per billing period, starting with the current billing period and going back in time. The first result is the current billing period. Returns up to 100 periods per page by default; use `has_more` and `next_cursor` to get older periods.

`credits_used` is the person's usage in the period, in whole Notion credits, rounded down. It includes agents the person owns that run on their credits (`credit_source: "owner"`). That usage also appears in the agent's own credit usage.

The request returns a 404 `object_not_found` error when the user isn't a current member of the workspace or the workspace has no billing period.
