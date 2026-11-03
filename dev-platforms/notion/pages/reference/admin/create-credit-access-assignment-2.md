---
title: "Create credit access assignment"
source: https://developers.notion.com/reference/admin/create-credit-access-assignment
path: reference/admin/create-credit-access-assignment
---

openapi-adminApi.json POST /v1/spaces/{space_id}/policies/credit_access/{policy_id}/assignments
Create credit access assignment.

The organization bot token must have the following scopes:

* `credit-limit-policy:write`

Assigns a credit access policy to a `selector`. Each selector has at most one assignment in a workspace. If the selector is already assigned to another policy, this request moves it to the policy in the path.

A member can match more than one assignment. Notion applies them in this order:

1. A `user` assignment for the member wins over every other assignment.
2. Otherwise, the highest limit among the member's `space_permission_group` and `scim_attribute` assignments applies. `unlimited` is highest and `no_access` is lowest.
3. Otherwise, the `all_space_members` assignment applies.

The `user_id` must belong to a workspace member, and the `group_id` must belong to a permission group in the workspace. Otherwise the request returns a 404 error.
