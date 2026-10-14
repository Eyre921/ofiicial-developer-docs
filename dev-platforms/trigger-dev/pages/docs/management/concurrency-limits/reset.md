---
title: "Reset Concurrency Limit"
source: https://trigger.dev/docs/management/concurrency-limits/reset
path: docs/management/concurrency-limits/reset
---

v3-openapi POST /api/v1/concurrency-limits/{name}/reset
Reset a concurrency limit back to the values declared in your code, clearing any override. With a concurrencyKey in the body, clear that key's per-key override instead and leave the limit itself alone.
