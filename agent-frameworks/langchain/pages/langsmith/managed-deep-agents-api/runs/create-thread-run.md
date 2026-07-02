---
title: "Create a thread run"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/create-thread-run
path: langsmith/managed-deep-agents-api/runs/create-thread-run
---

/langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/runs
Start a run on the thread. This endpoint is proxied to the upstream agent runtime and accepts its run payload. Include the assistant or agent identifier and run inputs in the request body.
