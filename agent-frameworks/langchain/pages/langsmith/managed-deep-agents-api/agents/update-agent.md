---
title: "Update an agent"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/update-agent
path: langsmith/managed-deep-agents-api/agents/update-agent
---

/langsmith/managed-deep-agents-openapi.json patch /agents/{agent_id}
Update the specified agent. Top-level scalar fields merge field-by-field. Nested objects such as `runtime`, `permissions`, `tools`, `subagents`, `skills`, and `extras` are replaced in full when provided. Providing file-tree fields such as `instructions`, `tools`, `subagents`, `skills`, or `files` creates a new file tree commit.
