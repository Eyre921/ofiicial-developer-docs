---
title: "Query agents"
source: https://developers.notion.com/reference/notion-agent-apis/query-agents
path: reference/notion-agent-apis/query-agents
---

post /v1/agents/query
Find Custom Agents that an integration can access.

Use filters, sorting, and cursor pagination to find accessible Custom Agents.

<Info>
  **Access**

  A personal access token returns the agents its user can read. A connection returns only agents explicitly shared with it. No matching agents returns an empty `results` array.
</Info>
