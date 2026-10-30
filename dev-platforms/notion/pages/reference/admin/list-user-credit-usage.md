---
title: "Get credit usage for users in a space"
source: https://developers.notion.com/reference/admin/list-user-credit-usage
path: reference/admin/list-user-credit-usage
---

openapi-adminApi.json GET /v1/spaces/{space_id}/users/credit_usage
Get credit usage for users in a space.

The organization bot token must have the following scopes:

* `user:read`

Lists every current member of the workspace, including members with no usage, ordered by user ID. Use `has_more` and `next_cursor` to page through members.

Each result reports Notion credits, the unit your workspace is billed in. `credits_used` is the person's usage in the current billing period, which `metrics_period_start_ms` and `metrics_period_end_ms` describe. `total_credits_used` is their usage across every billing period. Both include agents the person owns that run on their credits (`credit_source: "owner"`). That usage also appears in the agent's own credit usage. Credits are whole credits, rounded down.

`credit_limit` is the member credit limit that applies to the person right now, or `null` when no limit applies. It's `0` when the person has no limit and can't use Notion credits until one is set. It limits Notion credits only. The response doesn't say which setting the limit came from.

To see a person's usage in past billing periods, use [list credit usage per billing period for a user](/reference/admin/list-user-credit-usage-periods).

The request returns a 404 `object_not_found` error when the workspace has no billing period.
