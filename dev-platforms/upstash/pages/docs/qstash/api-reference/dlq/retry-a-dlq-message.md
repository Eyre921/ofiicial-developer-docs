---
title: "Retry a DLQ message"
source: https://upstash.com/docs/qstash/api-reference/dlq/retry-a-dlq-message
path: docs/qstash/api-reference/dlq/retry-a-dlq-message
---

> Retry delivery of a message from the DLQ

`POST /v2/dlq/retry/{dlqId}`

When a DLQ message is retried, a new message with the same body and headers is created and scheduled for delivery.
The original DLQ message is then removed from the DLQ.

<Note> 
  You can pass all configuration headers to override the configuration of the original message.

  For example, if the retry count of the original message is 5, you can set it to 0 for the retried message by passing `Upstash-Retries: 0 ` header to this request. 
  Check out publish documentation for complete list of configuration options you can pass.
</Note>
