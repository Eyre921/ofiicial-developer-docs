---
title: "Unshare a thread"
source: https://docs.langchain.com/langsmith/smith-api/threads/unshare-a-thread
path: langsmith/smith-api/threads/unshare-a-thread
---

/langsmith/langsmith-platform-openapi.json delete /api/v2/threads/{thread_id}/share
Deletes the share token for a thread. Idempotent: returns 204
whether or not a share token existed. Deliberately does not
verify the thread still exists.
