---
title: "Update credit access policy"
source: https://developers.notion.com/reference/admin/update-credit-access-policy
path: reference/admin/update-credit-access-policy
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/policies/credit_access/{policy_id}
Update credit access policy.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Renames a credit access policy or changes its limit. Send `name`, `limit`, or both. A new limit applies right away to every member the policy covers.

Pass the policy's current `version` as `expected_version`. If the policy changed after you read it, the request returns a 409 error. Get the policy again and retry with the new `version`.
