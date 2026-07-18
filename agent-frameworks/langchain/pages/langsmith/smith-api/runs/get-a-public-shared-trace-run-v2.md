---
title: "Get a public shared trace run (v2)"
source: https://docs.langchain.com/langsmith/smith-api/runs/get-a-public-shared-trace-run-v2
path: langsmith/smith-api/runs/get-a-public-shared-trace-run-v2
---

/langsmith/langsmith-platform-openapi.json get /v2/public/{share_token}/run/{run_id}
**Alpha:** The request and response contract may change;
Returns one run within the trace identified by the share token. The request supplies only the run ID and that run's exact start_time coordinate.
