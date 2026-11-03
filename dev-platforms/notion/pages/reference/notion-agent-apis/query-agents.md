---
title: "Query agents"
source: https://developers.notion.com/reference/notion-agent-apis/query-agents
path: reference/notion-agent-apis/query-agents
---

post /v1/agents/query
Find the Custom Agents and personal agent that an integration can access.

Use filters, sorting, and cursor pagination to find accessible agents. For a personal access token, results also include the personal agent, with `id` and `agent_type` set to `notion_ai`. Filter on `agent_type` to include or leave it out.

> [!NOTE]
>
> **Access**
>
> A personal access token returns the agents its user can read, plus that user's personal agent. A connection returns only Custom Agents explicitly shared with it. No matching agents returns an empty `results` array.
