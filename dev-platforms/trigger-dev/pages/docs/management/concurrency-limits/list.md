---
title: "List Concurrency Limits"
source: https://trigger.dev/docs/management/concurrency-limits/list
path: docs/management/concurrency-limits/list
---

v3-openapi GET /api/v1/concurrency-limits
List the environment's declared concurrency limits (anonymous inline limits
appear under their derived `task/<task-id>` names), with each limit's bounds
and its live running and queued counts. Results are ordered by the underlying
row name, so named limits sort before `task/`-derived inline limits.
