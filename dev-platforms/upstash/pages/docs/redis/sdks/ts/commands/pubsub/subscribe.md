---
title: "SUBSCRIBE"
source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/subscribe
path: docs/redis/sdks/ts/commands/pubsub/subscribe
---

> Subscribe to a channel

## Arguments

<ParamField body="channels" type="string | string[]" required>
The channel to publish to.
</ParamField>

## Response

<ResponseField type="Subscriber" required>
  A subscriber instance which can subscribe to channels.
</ResponseField>

<RequestExample>
```ts Example
const subscription = redis.subscribe(["my-channel"]);

const messages = [];
subscription.on("message", (data) => {
  messages.push(data.message);
});
```
</RequestExample>
