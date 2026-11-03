---
title: "Create credit access policy"
source: https://developers.notion.com/reference/admin/create-credit-access-policy
path: reference/admin/create-credit-access-policy
---

openapi-adminApi.json POST /v1/spaces/{space_id}/policies/credit_access
Create credit access policy.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Creates a named credit access policy. The policy covers no one until you [create a credit access assignment](/reference/admin/create-credit-access-assignment) for it.

Policy names must be unique within a workspace. A request with a name that's already in use returns a 400 error.
