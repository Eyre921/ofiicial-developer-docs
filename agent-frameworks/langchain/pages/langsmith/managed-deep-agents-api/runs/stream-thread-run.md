---
title: "Stream a thread run"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/stream-thread-run
path: langsmith/managed-deep-agents-api/runs/stream-thread-run
---

/langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/runs/stream
Start a run on a thread and stream output as server-sent events. The request must use `agent_id`; `assistant_id` is reserved for server-side forwarding and is rejected.
