---
title: "Replace dashboard widgets"
source: https://trigger.dev/docs/management/query/replace-dashboard
path: docs/management/query/replace-dashboard
---

v3-openapi PUT /api/v1/query/dashboards/{dashboardId}
Replace every widget on a custom dashboard, and optionally its title and description. A widget that already exists keeps its position unless you pass a new one; new widgets without a position are stacked full width below the others, in order.
