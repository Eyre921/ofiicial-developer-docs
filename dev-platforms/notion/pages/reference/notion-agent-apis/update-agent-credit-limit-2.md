---
title: "Update an agent credit limit"
source: https://developers.notion.com/reference/notion-agent-apis/update-agent-credit-limit
path: reference/notion-agent-apis/update-agent-credit-limit
---

patch /v1/agents/{agent_id}/credit_limit
Set or clear the credit limit for a Custom Agent.

Only a personal access token can change a credit limit, and its user needs full access to the Custom Agent. A connection token gets a `403` `restricted_resource`, even with the Edit selected agents capability. Workspace admins can also use the [Admin API](/reference/admin/update-agent-credit-limit).

The personal agent (`notion_ai`) has no per-agent credit limit. Passing it returns a `400` `validation_error`.
