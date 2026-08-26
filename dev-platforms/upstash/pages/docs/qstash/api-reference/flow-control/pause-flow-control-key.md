---
title: "Pause Flow Control Key"
source: https://upstash.com/docs/qstash/api-reference/flow-control/pause-flow-control-key
path: docs/qstash/api-reference/flow-control/pause-flow-control-key
---

> Pauses the delivery of messages associated with a specific flow-control key.

`POST /v2/flowControl/{flowControlKey}/pause`

When a flow-control key is paused, messages associated with that key will not be delivered until the key is resumed.

Messages that are already in the waitlist will remain there. New incoming messages will be added directly to the waitlist.

While the key is paused, the current rate period continues to elapse and the existing rate count is preserved for that period.
