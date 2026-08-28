---
title: "Bulk Delete Failed Workflow Runs"
source: https://upstash.com/docs/workflow/api-reference/dlq/bulk-delete-failed-workflow-runs
path: docs/workflow/api-reference/dlq/bulk-delete-failed-workflow-runs
---

/workflow/openapi.yaml delete /v2/workflows/dlq
Delete multiple failed workflow runs from the DLQ.

When a workflow run fails, it is moved to the DLQ. You can manually remove a failed workflow run from the DLQ using this endpoint. This is useful for cleaning up failed runs that you no longer wish to retry or analyze.

You can either specify specific DLQ IDs to delete, or use filters to delete matching workflows.
When using filters without DLQ IDs, the operation supports pagination via cursor.
