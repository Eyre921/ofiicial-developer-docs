---
title: "Create the issues agent for a session (Beta)"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/create-the-issues-agent-for-a-session-beta
path: langsmith/smith-api/issues-agent/create-the-issues-agent-for-a-session-beta
---

/langsmith/langsmith-platform-openapi.json post /api/v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Configures the issues agent for the given tracer session and enqueues
the initial scan. Fails if an agent already exists for the session.
