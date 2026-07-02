---
title: "Retrieve batch results"
source: https://trigger.dev/docs/management/batches/retrieve-results
path: docs/management/batches/retrieve-results
---

v3-openapi GET /api/v1/batches/{batchId}/results
Returns the execution results of all completed runs in a batch. Only finished runs (successful or failed) are included in the items array — runs that are still executing are omitted. Returns 404 if the batch doesn't exist.
