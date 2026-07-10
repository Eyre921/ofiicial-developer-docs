---
title: "Query public shared trace runs"
source: https://docs.langchain.com/langsmith/smith-api/runs/query-public-shared-trace-runs
path: langsmith/smith-api/runs/query-public-shared-trace-runs
---

/langsmith/langsmith-platform-openapi.json post /v2/public/{share_token}/runs/v2/query
**Alpha:** The request and response contract may change;
Returns all runs within the trace identified by the share token. The share token supplies the tenant, project, and trace scope.
