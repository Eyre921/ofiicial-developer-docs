---
title: "Abort bulk action"
source: https://trigger.dev/docs/management/bulk-actions/abort
path: docs/management/bulk-actions/abort
---

v3-openapi POST /api/v1/bulk-actions/{bulkActionId}/abort
Abort a pending bulk action so it stops processing additional runs. Runs already processed by the action are not undone.
