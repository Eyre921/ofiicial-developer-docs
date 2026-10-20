---
title: "Create dashboard"
source: https://trigger.dev/docs/management/query/create-dashboard
path: docs/management/query/create-dashboard
---

v3-openapi POST /api/v1/query/dashboards
Create a custom dashboard, optionally with its widgets. Every widget query is checked against the queryable tables before it is saved. Creating more dashboards than your plan allows returns a 403.
