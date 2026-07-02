---
title: "Submit a queued job"
source: https://docs.together.ai/reference/queue-submit
path: reference/queue-submit
---

POST /queue/submit
Submit a new job to the queue for asynchronous processing. Jobs are
processed in strict priority order (higher priority first, FIFO within
the same priority). Returns a request ID that can be used to poll status
or cancel the job.
