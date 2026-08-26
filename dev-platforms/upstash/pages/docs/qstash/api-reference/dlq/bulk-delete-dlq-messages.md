---
title: "Bulk Delete DLQ messages"
source: https://upstash.com/docs/qstash/api-reference/dlq/bulk-delete-dlq-messages
path: docs/qstash/api-reference/dlq/bulk-delete-dlq-messages
---

> Delete multiple messages from the DLQ

`DELETE /v2/dlq`

<Info>
  For multi-value filters, a message matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 
  
  Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
