---
title: "List credit access assignments"
source: https://developers.notion.com/reference/admin/list-credit-access-assignments
path: reference/admin/list-credit-access-assignments
---

openapi-adminApi.json GET /v1/spaces/{space_id}/policies/credit_access/{policy_id}/assignments
List credit access assignments.

The organization bot token must have the following scopes:

* `credit-limit-policy:read`

Lists the assignments for one credit access policy. An assignment connects a policy to a `selector`, which says who the policy covers:

| Selector `type` | Covers |
| :- | :- |
| `all_space_members` | Every workspace member. This is the workspace default. |
| `user` | One workspace member, by `user_id` |
| `space_permission_group` | Members of a permission group, by `group_id` |
| `scim_attribute` | Members whose SCIM `attribute` has the given `value` |

Use `has_more` and `next_cursor` to page through assignments.
