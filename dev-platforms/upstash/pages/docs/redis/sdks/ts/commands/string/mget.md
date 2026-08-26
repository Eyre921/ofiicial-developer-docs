---
title: "MGET"
source: https://upstash.com/docs/redis/sdks/ts/commands/string/mget
path: docs/redis/sdks/ts/commands/string/mget
---

> Load multiple keys from Redis in one go.

For billing purposes, this counts as a single command.

## Arguments 

<ParamField body="keys" type="...string" required>
  Multiple keys to load from Redis.
</ParamField>

## Response

<ResponseField type="T[]" required>
An array of values corresponding to the keys passed in. If a key doesn't exist, the value will be `null`.
</ResponseField>

<RequestExample>
```ts Example
type MyType = {
    a: number;
    b: string;
}
const values = await redis.mget<MyType>("key1", "key2", "key3");
// values.length -> 3
```
</RequestExample>
