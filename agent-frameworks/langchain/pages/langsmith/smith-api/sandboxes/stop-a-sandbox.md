---
title: "Stop a sandbox"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/stop-a-sandbox
path: langsmith/smith-api/sandboxes/stop-a-sandbox
---

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/{name}/stop
Stop a ready sandbox. This endpoint is not idempotent; the filesystem is preserved for later restart.
