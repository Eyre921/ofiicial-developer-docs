---
title: "Restart Workflow from DLQ"
source: https://upstash.com/docs/workflow/api-reference/dlq/restart-workflow-from-dlq
path: docs/workflow/api-reference/dlq/restart-workflow-from-dlq
---

> Restart a failed workflow run from the DLQ. The workflow will start from the beginning.

Unlike resume, which continues from where the workflow failed, restart executes the entire workflow
from the first step. A new workflow run ID is generated and all steps will be executed again.


`POST /v2/workflows/dlq/restart/{dlqId}`
