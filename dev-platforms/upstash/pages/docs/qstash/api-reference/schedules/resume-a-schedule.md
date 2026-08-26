---
title: "Resume a Schedule"
source: https://upstash.com/docs/qstash/api-reference/schedules/resume-a-schedule
path: docs/qstash/api-reference/schedules/resume-a-schedule
---

> Resume a paused Schedule

`POST /v2/schedules/{scheduleId}/resume`

Resuming a schedule marks the schedule as active. This means the upcoming messages will be delivered and will not be ignored. 

If the schedule is already active, this action has no effect.
