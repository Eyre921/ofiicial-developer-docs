---
title: "Delete Failed Workflow Run"
source: https://upstash.com/docs/workflow/api-reference/dlq/delete-failed-workflow-run
path: docs/workflow/api-reference/dlq/delete-failed-workflow-run
---

/workflow/openapi.yaml delete /v2/workflows/dlq/{dlqId}
Delete a specific failed workflow run from the DLQ.

Use this endpoint to remove a workflow from the DLQ after you have addressed the issue
or determined that the workflow should not be retried.
