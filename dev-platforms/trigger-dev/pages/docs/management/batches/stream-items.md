---
title: "Stream batch items"
source: https://trigger.dev/docs/management/batches/stream-items
path: docs/management/batches/stream-items
---

openapi POST /api/v3/batches/{batchId}/items
Phase 2 of 2-phase batch API. Accepts an NDJSON stream of batch items and enqueues them.
Each line in the body should be a valid BatchItemNDJSON object.
The stream is processed with backpressure - items are enqueued as they arrive.
The batch is sealed when the stream completes successfully.
