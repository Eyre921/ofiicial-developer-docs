---
title: "Disable or re-enable an agent in a space"
source: https://developers.notion.com/reference/admin/update-agent-status
path: reference/admin/update-agent-status
---

openapi-adminApi.json PATCH /v1/spaces/{space_id}/agents/{agent_id}/status
Disable or re-enable an agent in a space.

The organization bot token must have the following scopes:

* `workflows:write`

Lets an organization administrator turn an individual agent off, or turn a previously disabled agent back on. Disabling an agent stops its triggers from firing; re-enabling restores normal operation.

<Note>
  Disabling an agent sets its status to `disabled_from_workspace_settings`.

  Re-enabling an agent that an administrator disabled restores it to `active`.
</Note>

### What to expect

#### Disable a running agent

The agent is paused.

<CodeGroup>
  ```json 200 OK theme={null}
  {
    "admin_status": "disabled",
    "run_status": "paused",
    "paused_reason": "disabled_from_workspace_settings"
  }
  ```
</CodeGroup>

#### Disable an already admin-disabled agent

The request makes no change and is idempotent.

<CodeGroup>
  ```json 200 OK theme={null}
  {
    "admin_status": "disabled",
    "run_status": "paused",
    "paused_reason": "disabled_from_workspace_settings"
  }
  ```
</CodeGroup>

#### Change an agent blocked by another condition

When the agent has a credit-related pause reason such as `credit_limit` or `workspace_credit_limit`, or an operational pause reason such as `run_limit`, `failure_limit`, or `tool_unavailable`, either request is rejected with a `validation_error` and leaves the agent unchanged.

<CodeGroup>
  ```json 400 validation_error theme={null}
  {
    "type": "error",
    "status": 400,
    "code": "validation_error",
    "message": "…"
  }
  ```
</CodeGroup>

#### Enable an admin-disabled agent with no other condition

The admin disable is cleared.

<CodeGroup>
  ```json 200 OK theme={null}
  {
    "admin_status": "active",
    "run_status": "active"
  }
  ```
</CodeGroup>

#### Enable an admin-disabled agent when the workspace is over its credit limit

The admin disable is cleared, but the agent remains paused for the workspace credit limit.

<CodeGroup>
  ```json 200 OK theme={null}
  {
    "admin_status": "active",
    "run_status": "paused",
    "paused_reason": "workspace_credit_limit"
  }
  ```
</CodeGroup>

#### Enable an already active agent

The request makes no change and is idempotent.

<CodeGroup>
  ```json 200 OK theme={null}
  {
    "admin_status": "active",
    "run_status": "active"
  }
  ```
</CodeGroup>

### Important behaviors

**Usage limits are always reflected in the response.** A credit-limit or workspace-credit-limit pause is reported as paused rather than appearing runnable, so the response always reflects whether the agent can actually run. If an agent is currently active but blocked by one of these limits, both disable and enable requests are rejected with a `validation_error` naming the condition, and the agent is left unchanged. If you enable an admin-disabled agent whose workspace is over its credit limit, the admin disable is cleared, but the response reports `run_status: paused` with `paused_reason: workspace_credit_limit` rather than a misleading `active`. Agents whose usage is billed outside Notion credits are exempt from the workspace credit limit and stay active even when the workspace is out of credits.

**Disabling won't replace another pause reason.** If an agent is already paused for a platform or usage reason (for example, a credit limit), an admin disable will not overwrite that reason. Resolve the underlying condition first.

**Workspace policy takes precedence.** If your workspace policy currently disallows Custom Agents, you cannot re-enable and run an agent — even one that was only admin-disabled.
