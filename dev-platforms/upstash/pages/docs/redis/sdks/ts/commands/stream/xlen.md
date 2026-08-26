---
title: "XLEN"
source: https://upstash.com/docs/redis/sdks/ts/commands/stream/xlen
path: docs/redis/sdks/ts/commands/stream/xlen
---

> Returns the number of entries inside a stream.

## Arguments

<ParamField body="key" type="string" required>
  The key of the stream.
</ParamField>

## Response

<ResponseField type="number">
  The number of entries in the stream. Returns 0 if the stream does not exist.
</ResponseField>

<RequestExample>
```ts Get stream length
const result = await redis.xlen("mystream");
```
</RequestExample>
