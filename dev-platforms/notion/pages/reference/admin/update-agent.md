---
title: "Update an agent in a space"
source: https://developers.notion.com/reference/admin/update-agent
path: reference/admin/update-agent
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/agents/{agent_id}
Update an agent's owner, credit source, credit limits, or admin status in one request.

The organization bot token must have the following scopes:

* `workflows:write`

Provide at least one field to update. The API validates the requested changes together and saves them in one transaction. If validation fails, none of the requested changes are saved.

### Ownership and credit limits

Changing the owner doesn't clear the agent's editor credit limit. To set a new owner and a new limit together, provide both fields:

```json Request body theme={null}
{
  "owner_user_id": "d71b6edc-0580-4fa3-b7a8-1523e3916bd1",
  "credit_limit_by_editor": 200
}
```

The new owner must be an eligible workspace member and receives full access to the agent.

Omit a credit limit to keep it unchanged. Set it to `null` to remove it. Both limit fields accept non-negative integers.

When the agent spends workspace credits, the editor limit can't exceed the workspace admin's limit or the workspace credit limit. These checks use the values after your requested changes. For example, setting the admin limit to `100` and the editor limit to `200` in the same request returns `validation_error` and leaves the agent unchanged.

You can't set a workspace admin limit when the agent spends its owner's credits.

### Agent status

Use `admin_status` to disable an agent or turn an agent back on after an admin or editor disabled it. This field can't override a Notion-managed pause, such as a credit-limit pause.

Credit-limit changes can pause or resume an agent. The API evaluates `admin_status` after applying the other requested fields to the proposed state.

### Response

The response has the same agent metadata shape as [List agents in a space](/reference/admin/get-workflows-metadata-for-space). It doesn't include the credit limits. Read those with [Get agent credit usage](/reference/admin/get-agent-credit-usage).
