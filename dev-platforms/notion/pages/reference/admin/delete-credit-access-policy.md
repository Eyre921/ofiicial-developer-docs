---
title: "Delete credit access policy"
source: https://developers.notion.com/reference/admin/delete-credit-access-policy
path: reference/admin/delete-credit-access-policy
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/policies/credit_access/{policy_id}
Delete credit access policy.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Deletes a credit access policy. Its assignments stop applying, and covered members fall back to any other policy that matches them.

Pass the policy's current `version` as the `expected_version` query parameter. If the policy changed after you read it, the request returns a 409 error.

You can't delete the policy assigned to `all_space_members`, which is the workspace default. First [move that assignment](/reference/admin/update-credit-access-assignment) to another policy, then delete this one. Otherwise the request returns a 409 error.
