---
title: "Cancel a queued job"
source: https://docs.together.ai/reference/queue-cancel
path: reference/queue-cancel
---

POST /queue/cancel
Cancel a pending job. Only jobs in pending status can be canceled.
Running jobs cannot be stopped. Returns the job status after the
attempt. If the job is not pending, returns 409 with the current status
unchanged.
