---
title: "Get credit usage for an agent in a space"
source: https://developers.notion.com/reference/admin/get-agent-credit-usage
path: reference/admin/get-agent-credit-usage
---

openapi-adminApi.json GET /v1/spaces/{space_id}/agents/{agent_id}/credit_usage
Get credit usage for an agent in a space.

The organization bot token must have the following scopes:

* `workflows:read`

This endpoint also reports usage for lite database Autofill agents, including those with zero premium AI credit usage or those moved to Trash.

`credits_used_by_type` breaks usage down into Notion, Select, and Standard credits. [Learn what each credit type covers](https://www.notion.com/help/standard-select-and-notion-credits-eligible-features). `credits_used` counts only Notion credits, so the credits in `credits_used_by_type` don't add up to `credits_used`.
