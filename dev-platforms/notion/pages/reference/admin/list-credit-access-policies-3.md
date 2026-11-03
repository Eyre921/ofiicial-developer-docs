---
title: "List credit access policies"
source: https://developers.notion.com/reference/admin/list-credit-access-policies
path: reference/admin/list-credit-access-policies
---

openapi-adminApi.json GET /v1/spaces/{space_id}/policies/credit_access
List credit access policies.

The organization bot token must have the following scopes:

* `credit-limit-policy:read`

A credit access policy sets how many Notion credits members can use. Each policy has a `limit`: `no_access`, `limited` with a number of `credits`, or `unlimited`. To decide who a policy covers, [create a credit access assignment](/reference/admin/create-credit-access-assignment).

This endpoint lists every policy in the workspace. Use `has_more` and `next_cursor` to page through policies.
