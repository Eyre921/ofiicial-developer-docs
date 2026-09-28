---
title: "Get Thread Storage"
source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-storage
path: langsmith/agent-server-api/threads/get-thread-storage
---

/langsmith/agent-server-openapi.json get /threads/{thread_id}/storage
Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.
