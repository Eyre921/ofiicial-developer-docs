---
title: "Read a thread's share state"
source: https://docs.langchain.com/langsmith/smith-api/threads/read-a-threads-share-state
path: langsmith/smith-api/threads/read-a-threads-share-state
---

/langsmith/langsmith-platform-openapi.json get /api/v2/threads/{thread_id}/share
Returns the share token for a thread. The token is omitted when
the thread is not shared. Gated on runs:share so the control's
state matches the control's permission.
