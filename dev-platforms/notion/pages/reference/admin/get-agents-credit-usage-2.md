---
title: "Get credit usage for agents in a space"
source: https://developers.notion.com/reference/admin/get-agents-credit-usage
path: reference/admin/get-agents-credit-usage
---

openapi-adminApi.json GET /v1/spaces/{space_id}/agents/credit_usage
Get credit usage for agents in a space.

The organization bot token must have the following scopes:

* `workflows:read`

`credits_used_by_type` breaks usage down into Notion, Select, and Standard credits. [Learn what each credit type covers](https://www.notion.com/help/standard-select-and-notion-credits-eligible-features). `credits_used` counts only Notion credits, so the credits in `credits_used_by_type` don't add up to `credits_used`.
