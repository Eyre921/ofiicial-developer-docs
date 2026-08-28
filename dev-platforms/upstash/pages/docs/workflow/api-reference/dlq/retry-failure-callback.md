---
title: "Retry Failure Callback"
source: https://upstash.com/docs/workflow/api-reference/dlq/retry-failure-callback
path: docs/workflow/api-reference/dlq/retry-failure-callback
---

/workflow/openapi.yaml post /v2/workflows/dlq/callback/{dlqId}
If the failure callback for a workflow run has failed, you can use this endpoint to manually trigger the failure callback again. 
This is useful for ensuring that your system is notified of workflow failures even if the original callback attempt did not succeed.

The state of the failure callback for each workflow run is included in the DLQ message response as failureCallbackInfo.state. 
You can filter for all workflow runs with a failed failure callback by using the failureCallbackState filter when listing workflow runs in the DLQ with the `/v2/workflows/dlq` endpoint.
