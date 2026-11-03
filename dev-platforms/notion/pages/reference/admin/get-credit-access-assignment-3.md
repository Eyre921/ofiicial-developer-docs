---
title: "Get credit access assignment"
source: https://developers.notion.com/reference/admin/get-credit-access-assignment
path: reference/admin/get-credit-access-assignment
---

openapi-adminApi.json GET /v1/spaces/{space_id}/policies/credit_access/assignments/{assignment_id}
Get credit access assignment.

The organization bot token must have the following scopes:

* `credit-limit-policy:read`

Returns one credit access assignment, including its `selector`, its `policy_id`, and its current `version`.
