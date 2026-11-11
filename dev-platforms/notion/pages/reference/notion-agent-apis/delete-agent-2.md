---
title: "Delete an agent"
source: https://developers.notion.com/reference/notion-agent-apis/delete-agent
path: reference/notion-agent-apis/delete-agent
---

delete /v1/agents/{agent_id}
Soft-delete a Custom Agent with a personal access token.

Only a personal access token can delete a Custom Agent, and its user needs edit access to the agent. A connection token gets a `403` `restricted_resource`, even with the Edit selected agents capability. Workspace admins can also use the [Admin API](/reference/admin/delete-agent).

You can't delete the personal agent (`notion_ai`). Passing it returns a `400` `validation_error`.
