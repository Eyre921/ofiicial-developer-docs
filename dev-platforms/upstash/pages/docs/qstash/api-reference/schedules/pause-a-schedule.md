---
title: "Pause a Schedule"
source: https://upstash.com/docs/qstash/api-reference/schedules/pause-a-schedule
path: docs/qstash/api-reference/schedules/pause-a-schedule
---

> Pause a Schedule

`POST /v2/schedules/{scheduleId}/pause`

When a schedule is paused, the cron trigger will simply be ignored.

If the schedule is already paused, this action has no effect.
