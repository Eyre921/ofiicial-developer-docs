---
title: "Bulk Restart Workflows from DLQ"
source: https://upstash.com/docs/workflow/api-reference/dlq/bulk-restart-workflows-from-dlq
path: docs/workflow/api-reference/dlq/bulk-restart-workflows-from-dlq
---

/workflow/openapi.yaml post /v2/workflows/dlq/restart
Restart multiple failed workflow runs from the DLQ. Each workflow will start from the beginning.

Unlike resume, which continues from where workflows failed, restart executes the entire workflows
from the first step. New workflow run IDs are generated and all steps will be executed again.

A maximum of 50 workflow runs can be restarted per request. If more runs are available, a cursor is returned, which can be used in subsequent requests to continue the operation. When no cursor is returned, all entries have been processed.
Each restarted workflow run is assigned a new random Run ID.
