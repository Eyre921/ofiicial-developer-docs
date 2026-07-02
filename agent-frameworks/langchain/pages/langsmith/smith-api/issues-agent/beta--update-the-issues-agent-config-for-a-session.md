---
title: "[Beta] Update the issues agent config for a session"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-update-the-issues-agent-config-for-a-session
path: langsmith/smith-api/issues-agent/beta--update-the-issues-agent-config-for-a-session
---

/langsmith/langsmith-platform-openapi.json patch /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Patches the agent config. All side effects (clearing fix fields when
the GitHub repo changes, setting agent_overview_repo_id) happen in a
single CRUD transaction. Omitted fields are left unchanged.
