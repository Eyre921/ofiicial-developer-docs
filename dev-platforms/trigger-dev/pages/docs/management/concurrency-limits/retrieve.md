---
title: "Retrieve Concurrency Limit"
source: https://trigger.dev/docs/management/concurrency-limits/retrieve
path: docs/management/concurrency-limits/retrieve
---

v3-openapi GET /api/v1/concurrency-limits/{name}
Retrieve a concurrency limit by name, with its bounds and live running and queued counts. With the concurrencyKey query parameter, retrieve the limit's view for that one key instead (its per-key bound, any per-key override and when it expires, and the runs executing for the key).
