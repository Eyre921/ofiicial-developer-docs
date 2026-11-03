---
title: "Retrieve an agent"
source: https://developers.notion.com/reference/notion-agent-apis/retrieve-agent
path: reference/notion-agent-apis/retrieve-agent
---

get /v1/agents/{agent_id}
Retrieve metadata for one accessible Custom Agent or the personal agent.

Pass `notion_ai` as the `agent_id` to retrieve the personal agent (Notion AI) of the user a [personal access token](/guides/connections-and-tokens/personal-access-tokens) acts as. Its `id` and `agent_type` are both `notion_ai`. Any other token receives a `404` `object_not_found`.

> [!NOTE]
>
> **Favorites**
>
> `is_favorited` is `true` or `false` for a personal access token and `null` for a connection token, which has no personal favorites scope. For `notion_ai`, it is `false` for a personal access token.
