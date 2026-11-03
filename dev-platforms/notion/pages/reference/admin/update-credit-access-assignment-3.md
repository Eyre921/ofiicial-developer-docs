---
title: "Update credit access assignment"
source: https://developers.notion.com/reference/admin/update-credit-access-assignment
path: reference/admin/update-credit-access-assignment
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/policies/credit_access/assignments/{assignment_id}
Update credit access assignment.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Moves a credit access assignment to another policy in the same workspace. The assignment keeps its `selector`. The new policy's limit applies right away.
