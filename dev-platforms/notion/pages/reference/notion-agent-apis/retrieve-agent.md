---
title: "Retrieve an agent"
source: https://developers.notion.com/reference/notion-agent-apis/retrieve-agent
path: reference/notion-agent-apis/retrieve-agent
---

get /v1/agents/{agent_id}
Retrieve metadata for one accessible Custom Agent.

<Info>
  **Favorites**

  `is_favorited` is `true` or `false` for a personal access token and `null` for a connection token, which has no personal favorites scope. For `notion_ai`, it is `false` for a personal access token.
</Info>
