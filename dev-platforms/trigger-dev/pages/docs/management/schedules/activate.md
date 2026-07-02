---
title: "Activate Schedule"
source: https://trigger.dev/docs/management/schedules/activate
path: docs/management/schedules/activate
---

v3-openapi POST /api/v1/schedules/{schedule_id}/activate
Activate a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.
