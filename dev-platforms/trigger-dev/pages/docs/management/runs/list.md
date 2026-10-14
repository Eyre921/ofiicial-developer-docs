---
title: "List runs"
source: https://trigger.dev/docs/management/runs/list
path: docs/management/runs/list
---

v3-openapi GET /api/v1/runs
List runs in a specific environment. You can filter the runs by status, created at, task identifier, version, and more. Without a `filter[createdAt]` value, only runs created in the last 7 days are returned. This endpoint is for browsing, reporting, and bulk operations, not for coordinating runs, so don't call it before every trigger or poll it in a loop. See [runs.list() best practices](/runs/list-best-practices).
