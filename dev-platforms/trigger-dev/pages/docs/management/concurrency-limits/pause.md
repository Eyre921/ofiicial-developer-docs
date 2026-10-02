---
title: "Pause or Resume Concurrency Limit"
source: https://trigger.dev/docs/management/concurrency-limits/pause
path: docs/management/concurrency-limits/pause
---

v3-openapi POST /api/v1/concurrency-limits/{name}/pause
Pause a concurrency limit to prevent runs holding it from starting, or resume a
paused limit. Runs that are currently executing will continue to completion, and
the limit's configured bounds are kept.
