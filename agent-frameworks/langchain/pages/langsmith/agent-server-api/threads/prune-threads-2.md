---
title: "Prune Threads"
source: https://docs.langchain.com/langsmith/agent-server-api/threads/prune-threads
path: langsmith/agent-server-api/threads/prune-threads
---

/langsmith/agent-server-openapi.json post /threads/prune
Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.
