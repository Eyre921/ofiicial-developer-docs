---
title: "DECR"
source: https://upstash.com/docs/redis/sdks/ts/commands/string/decr
path: docs/redis/sdks/ts/commands/string/decr
---

> Decrement the integer value of a key by one

If a key does not exist, it is initialized as 0 before performing the operation. An error is returned if the key contains a value of the wrong type or contains a string that can not be represented as integer.

## Arguments

<ParamField body="key" type="string" required>
The key to decrement.
</ParamField>

## Response

<ResponseField  type="integer" required>
The value at the key after the decrementing.
</ResponseField>

<RequestExample>
```ts Example
await redis.set("key", 6);
await redis.decr("key");
// returns 5
```
</RequestExample>
