---
title: "[Beta] Create the issues agent for a session"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-create-the-issues-agent-for-a-session
path: langsmith/smith-api/issues-agent/beta--create-the-issues-agent-for-a-session
---

/langsmith/langsmith-platform-openapi.json post /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Configures the issues agent for the given tracer session and enqueues
the initial scan. Fails if an agent already exists for the session.
