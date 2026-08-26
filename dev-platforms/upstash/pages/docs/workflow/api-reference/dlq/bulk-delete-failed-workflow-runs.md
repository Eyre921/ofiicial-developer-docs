---
title: "Bulk Delete Failed Workflow Runs"
source: https://upstash.com/docs/workflow/api-reference/dlq/bulk-delete-failed-workflow-runs
path: docs/workflow/api-reference/dlq/bulk-delete-failed-workflow-runs
---

> Delete multiple failed workflow runs from the DLQ.

When a workflow run fails, it is moved to the DLQ. You can manually remove a failed workflow run from the DLQ using this endpoint. This is useful for cleaning up failed runs that you no longer wish to retry or analyze.

You can either specify specific DLQ IDs to delete, or use filters to delete matching workflows.
When using filters without DLQ IDs, the operation supports pagination via cursor.


`DELETE /v2/workflows/dlq`

<Info>
  For multi-value filters, a workflow run matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 
  
  Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
