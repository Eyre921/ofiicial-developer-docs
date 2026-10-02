---
title: "Retrieve agent insights"
source: https://developers.notion.com/reference/notion-agent-apis/retrieve-agent-insights
path: reference/notion-agent-apis/retrieve-agent-insights
---

get /v1/agents/{agent_id}/insights
Retrieve configuration and usage insights for a Custom Agent or the authenticated user's personal agent.

### Personal agent insights

Pass `notion_ai` as the `agent_id` to read insights for the personal agent (Notion AI) instead of a Custom Agent. The response keeps the same `agent_insights` shape, with a few differences:

* `id` and `agent_type` are both `notion_ai`.
* `created_by` is the user the token acts as.
* `status` is always `active` and `pause_reason` is always `null`, because the personal agent has no per-agent status controls.
* `credit_limit` reports the workspace's default per-member credit limit, or `null` when the workspace has not set one.

<Info>
  **Access**

  Only a [personal access token](/guides/get-started/personal-access-tokens) can read personal agent insights, and the totals always cover the user that token acts as — never another member's usage. Any other token receives a `404` `object_not_found`.
</Info>
