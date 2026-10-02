---
title: "Override Concurrency Limit"
source: https://trigger.dev/docs/management/concurrency-limits/override
path: docs/management/concurrency-limits/override
---

v3-openapi POST /api/v1/concurrency-limits/{name}/override
Override a concurrency limit's bounds. Only the given fields change; the declared
values are kept and restored by reset. To stop runs holding a limit, prefer the
pause endpoint (it keeps the configured bounds); overriding `total` to `0` also
blocks every run holding the limit.
