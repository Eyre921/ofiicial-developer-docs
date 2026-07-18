---
title: "Unshare a run (v2)"
source: https://docs.langchain.com/langsmith/smith-api/runs/unshare-a-run-v2
path: langsmith/smith-api/runs/unshare-a-run-v2
---

/langsmith/langsmith-platform-openapi.json delete /v2/runs/{trace_id}/share
Deletes the share token for the trace identified by trace_id and session_id. Idempotent: returns 204 whether or not a share token existed.
