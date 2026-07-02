---
title: "Cancel In-Progress Failure Callback"
source: https://upstash.com/docs/workflow/api-reference/dlq/cancel-in-progress-failure-callback
path: docs/workflow/api-reference/dlq/cancel-in-progress-failure-callback
---

/workflow/openapi.yaml delete /v2/workflows/dlq/callback/{dlqId}
Cancel an in-progress failure callback for a failed workflow.

When you retry a failed failure callback using the POST endpoint, it enters an in-progress state.
This endpoint allows you to cancel that in-progress callback before it completes.

The callback must be in an in-progress state. If there's no in-progress callback,
the request will fail with a 400 error.
