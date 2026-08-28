---
title: "List Failed Workflow Runs"
source: https://upstash.com/docs/workflow/api-reference/dlq/list-failed-workflow-runs
path: docs/workflow/api-reference/dlq/list-failed-workflow-runs
---

/workflow/openapi.yaml get /v2/workflows/dlq
List and paginate through all failed workflow runs currently in the DLQ.

Failed workflows end up in the DLQ after exhausting all retry attempts. You can filter,
paginate, and inspect these failures to understand what went wrong and decide whether to
resume, restart, or delete them.
