---
title: "Pause Queue"
source: https://upstash.com/docs/qstash/api-reference/queues/pause-queue
path: docs/qstash/api-reference/queues/pause-queue
---

> Pause a queue to stop the delivery of enqueued messages

`POST /v2/queues/{queueName}/pause`

Pausing a queue stops the delivery of enqueued messages. The queue continues to accept new messages, but they will not be delivered until the queue is resumed.

If the queue is already paused, this action has no effect.

<Warning>
  Resuming or creating a queue may take up to a minute. Therefore, it is not recommended to pause or delete a queue during critical operations.
</Warning>
