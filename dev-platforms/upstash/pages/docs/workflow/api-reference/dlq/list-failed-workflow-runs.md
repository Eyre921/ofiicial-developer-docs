---
title: "List Failed Workflow Runs"
source: https://upstash.com/docs/workflow/api-reference/dlq/list-failed-workflow-runs
path: docs/workflow/api-reference/dlq/list-failed-workflow-runs
---

> List and paginate through all failed workflow runs currently in the DLQ.

Failed workflows end up in the DLQ after exhausting all retry attempts. You can filter,
paginate, and inspect these failures to understand what went wrong and decide whether to
resume, restart, or delete them.


`GET /v2/workflows/dlq`

<Info>
  For multi-value filters, a workflow run matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 
  
  Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
