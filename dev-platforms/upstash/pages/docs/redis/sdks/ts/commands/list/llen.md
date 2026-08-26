---
title: "LLEN"
source: https://upstash.com/docs/redis/sdks/ts/commands/list/llen
path: docs/redis/sdks/ts/commands/list/llen
---

> Returns the length of the list stored at key.

## Arguments

<ParamField body="key" type="string" required>
    The key of the list.
</ParamField>

## Response

<ResponseField type="number" required>
    The length of the list at key.
</ResponseField>

<RequestExample>
```ts Example
await redis.rpush("key", "a", "b", "c");
const length = await redis.llen("key");
console.log(length); // 3
```
</RequestExample>
