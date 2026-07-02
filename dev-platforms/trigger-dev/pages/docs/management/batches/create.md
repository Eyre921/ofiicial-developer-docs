---
title: "Create batch"
source: https://trigger.dev/docs/management/batches/create
path: docs/management/batches/create
---

openapi POST /api/v3/batches
Phase 1 of 2-phase batch API. Creates a batch record and optionally blocks the parent run for batchTriggerAndWait.
After creating a batch, stream items via POST /api/v3/batches/{batchId}/items.
