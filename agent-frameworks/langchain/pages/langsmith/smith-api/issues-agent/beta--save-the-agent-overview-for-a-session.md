---
title: "[Beta] Save the agent overview for a session"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-save-the-agent-overview-for-a-session
path: langsmith/smith-api/issues-agent/beta--save-the-agent-overview-for-a-session
---

/langsmith/langsmith-platform-openapi.json patch /v1/platform/sessions/{session_id}/issues-agent/overview
**Beta:** This endpoint is in active development and may change without notice.

Saves the issues agent overview content server-side, creating or updating
the backing private Prompt Hub repo and linking it to the issues agent config.
