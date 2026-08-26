---
title: "Reset Rate for Flow Control Key"
source: https://upstash.com/docs/qstash/api-reference/flow-control/reset-rate-for-flow-control-key
path: docs/qstash/api-reference/flow-control/reset-rate-for-flow-control-key
---

> Resets the rate configuration state for a specific flow-control key.

`POST /v2/flowControl/{flowControlKey}/resetRate`

Rate configuration limits the number of messages delivered within a given time period for messages sharing the same flow-control key.

When the rate limit is reached, subsequent messages with the same flow-control key are placed in the waitlist and are not delivered until the next time period begins.

In some situations, you may want to immediately resume message delivery without waiting for the current period to expire. Resetting the rate configuration clears the current rate count and immediately ends the current period.

After the reset, the current timestamp becomes the start of the new rate period.
