---
title: "List runs in a trace"
source: https://docs.langchain.com/langsmith/smith-api/v2/list-runs-in-a-trace
path: langsmith/smith-api/v2/list-runs-in-a-trace
---

/langsmith/langsmith-platform-openapi.json get /v2/traces/{trace_id}/runs
**Alpha:** The request and response contract may change;
Returns runs for a trace ID within min/max start time. Optional `filter`; repeatable `selects` to select fields to return.
