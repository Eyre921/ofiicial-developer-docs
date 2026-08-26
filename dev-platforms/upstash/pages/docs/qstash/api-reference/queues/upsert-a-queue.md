---
title: "Upsert a Queue"
source: https://upstash.com/docs/qstash/api-reference/queues/upsert-a-queue
path: docs/qstash/api-reference/queues/upsert-a-queue
---

> Updates or creates a queue

`POST /v2/queues`

<Warning>
  For rate-limiting use cases, we've introduced a more performant and less restrictive Flow Control feature for the Publish API. 
  
  We are planning to deprecate setting parallelism greater than 1 for the Queue API in future. If you're currently using Queue API with parallelism greater than 1 for rate limiting, consider using Flow Control. 
  
  Queues with parallelism set to 1 provide FIFO guarantees, which remains a valid use case for the Queue API.
</Warning>
