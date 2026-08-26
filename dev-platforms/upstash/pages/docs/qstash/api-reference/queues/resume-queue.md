---
title: "Resume Queue"
source: https://upstash.com/docs/qstash/api-reference/queues/resume-queue
path: docs/qstash/api-reference/queues/resume-queue
---

> Resumes a queue to starts the delivery of enqueued messages

`POST /v2/queues/{queueName}/resume`

Resuming a queue starts the delivery of enqueued messages, beginning with the earliest undelivered message. 

If the queue is already active, this action has no effect.

<Warning>
  Resuming or creating a queue may take up to a minute. Therefore, it is not recommended to pause or delete a queue during critical operations.
</Warning>
