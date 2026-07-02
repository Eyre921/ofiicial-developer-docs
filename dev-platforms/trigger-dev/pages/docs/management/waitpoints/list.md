---
title: "List waitpoint tokens"
source: https://trigger.dev/docs/management/waitpoints/list
path: docs/management/waitpoints/list
---

v3-openapi GET /api/v1/waitpoints/tokens
Returns a paginated list of waitpoint tokens for the current environment. Results are ordered by creation date, newest first. Use cursor-based pagination with `page[after]` and `page[before]` to navigate pages.
