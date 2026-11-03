---
title: "Delete credit access assignment"
source: https://developers.notion.com/reference/admin/delete-credit-access-assignment
path: reference/admin/delete-credit-access-assignment
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/policies/credit_access/assignments/{assignment_id}
Delete credit access assignment.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Deletes a credit access assignment. Members it covered fall back to any other assignment that matches them.

Pass the assignment's current `version` as the `expected_version` query parameter. If the assignment changed after you read it, the request returns a 409 error.
