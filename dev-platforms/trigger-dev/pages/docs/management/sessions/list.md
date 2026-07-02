---
title: "List sessions"
source: https://trigger.dev/docs/management/sessions/list
path: docs/management/sessions/list
---

v3-openapi GET /api/v1/sessions
List sessions in the current environment, newest first. Filter by type, tags, task identifier, external id, status, and creation window. Use cursor-based pagination with `page[after]` and `page[before]` to navigate pages.

List rows omit `triggerConfig`; retrieve a single session to read it.
