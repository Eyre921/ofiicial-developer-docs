---
title: "List viewed issues for a session (Beta)"
source: https://docs.langchain.com/langsmith/smith-api/issues/list-viewed-issues-for-a-session-beta
path: langsmith/smith-api/issues/list-viewed-issues-for-a-session-beta
---

/langsmith/langsmith-platform-openapi.json get /v1/platform/sessions/{session_id}/issues/views
**Beta:** Returns the issues in this session that the current
user has opened, with timestamps. Used by the UI to derive
the per-row "unread" indicator and the Engine tab badge.
