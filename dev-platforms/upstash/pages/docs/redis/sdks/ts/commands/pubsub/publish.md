---
title: "PUBLISH"
source: https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish
path: docs/redis/sdks/ts/commands/pubsub/publish
---

> Publish a message to a channel

## Arguments

<ParamField body="channel" type="string" required>
The channel to publish to.
</ParamField>

<ParamField body="message" type="TMessage">
The message to publish.
</ParamField>

## Response

<ResponseField type="integer" required>
  The number of clients who received the message.
</ResponseField>

<RequestExample>
```ts Example
const listeners = await redis.publish("my-channel", "my-message");
```
</RequestExample>
