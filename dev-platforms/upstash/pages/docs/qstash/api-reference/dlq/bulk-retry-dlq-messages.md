---
title: "Bulk Retry DLQ messages"
source: https://upstash.com/docs/qstash/api-reference/dlq/bulk-retry-dlq-messages
path: docs/qstash/api-reference/dlq/bulk-retry-dlq-messages
---

> Retry delivery of multiple messages from the DLQ

`POST /v2/dlq/retry`

When DLQ messages are retried, new messages with the same body and headers are created and scheduled for delivery.
The original DLQ messages are then removed from the DLQ.

<Note> 
  You can pass all configuration headers to override the configuration of the original messages.

  For example, if the retry count of the original messages is 5, you can set it to 0 for the retried messages by passing `Upstash-Retries: 0 ` header to this request.
  Check out publish documentation for complete list of configuration options you can pass.
</Note>

<Info>
  For multi-value filters, a message matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 
  
  Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
