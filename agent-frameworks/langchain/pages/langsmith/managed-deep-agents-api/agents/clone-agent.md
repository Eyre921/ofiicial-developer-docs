---
title: "Clone an agent"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/clone-agent
path: langsmith/managed-deep-agents-api/agents/clone-agent
---

/langsmith/managed-deep-agents-openapi.json post /agents/{agent_id}/clone
Create a new agent that mirrors the source agent behavior but is owned by the caller. The clone copies runtime, backend, file tree, tools, subagents, and skills; caller metadata and sharing state start fresh.
