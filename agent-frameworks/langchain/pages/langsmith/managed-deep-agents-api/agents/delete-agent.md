---
title: "Delete an agent"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/delete-agent
path: langsmith/managed-deep-agents-api/agents/delete-agent
---

/langsmith/managed-deep-agents-openapi.json delete /agents/{agent_id}
Delete the agent. The call is idempotent: deleting a non-existent agent returns `204`. Deletion does not cascade to the agent's threads — existing threads remain queryable but cannot start new runs (attempts return `502`). Delete threads explicitly when you want to clean them up.
