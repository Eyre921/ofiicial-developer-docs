---
title: "Get credit access policy"
source: https://developers.notion.com/reference/admin/get-credit-access-policy
path: reference/admin/get-credit-access-policy
---

openapi-adminApi.json GET /v1/spaces/{space_id}/policies/credit_access/{policy_id}
Get credit access policy.

The organization bot token must have the following scopes:

* `credit-limit-policy:read`

Returns one credit access policy, including its current `version`. Pass the `version` as `expected_version` when you update or delete the policy.
