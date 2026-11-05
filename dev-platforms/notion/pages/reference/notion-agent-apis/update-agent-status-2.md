---
title: "Update agent status"
source: https://developers.notion.com/reference/notion-agent-apis/update-agent-status
path: reference/notion-agent-apis/update-agent-status
---

patch /v1/agents/{agent_id}/status
Enable or disable a Custom Agent. Deprecated in favor of Update an agent.

> [!WARNING]
>
> This endpoint is deprecated. Use [Update an agent](/reference/notion-agent-apis/update-agent) and send `{"status": "active"}` or `{"status": "disabled"}` instead. The request rules are the same, but the response and one error code change. This endpoint returns `agent_id`, `status`, and `pause_reason`. Update an agent returns the full [agent object](/reference/notion-agent-apis/retrieve-agent), so read the ID from `id` instead of `agent_id`. A status change that isn't allowed returns `403` `status_change_not_allowed` here and `403` `restricted_resource` from Update an agent.

The personal agent (`notion_ai`) has no status control. Passing it returns a `400` `validation_error`.
