---
title: "Delete runs"
source: https://docs.langchain.com/langsmith/smith-api/run/delete-runs
path: langsmith/smith-api/run/delete-runs
---

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/delete
DELETE with body payload — removes the runs identified by the request payload.

Delete specific runs by supplying `session_id` and `trace_ids`.
