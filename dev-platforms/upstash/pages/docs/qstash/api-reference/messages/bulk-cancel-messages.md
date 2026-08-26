---
title: "Bulk Cancel Messages"
source: https://upstash.com/docs/qstash/api-reference/messages/bulk-cancel-messages
path: docs/qstash/api-reference/messages/bulk-cancel-messages
---

> Delete all pending messages

`DELETE /v2/messages`

<Note>Cancelling a message will remove it from QStash and stop it from being delivered in the future. If a message is in flight to your API, it might be too late to cancel.</Note>
<Warning>
  If you provide a set of message IDs in the request, only those messages will be cancelled.

  If you include filter parameters in the request, only the messages that match the filters will be canceled.
  
  If no filter or messageIds are sent, QStash will cancel all of your messages. We highly recommend at least providing count parameter and cancel in batches. 
</Warning> 

This operation scans all your messages and attempts to cancel them. If an individual message cannot be cancelled, it will not continue and will return an error message. Therefore, some messages may not be cancelled at the end. In such cases, you can run the bulk cancel operation multiple times.

<Info>
For multi-value filters, a message matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 

Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
