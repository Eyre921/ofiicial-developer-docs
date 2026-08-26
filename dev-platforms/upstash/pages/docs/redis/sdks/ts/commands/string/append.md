---
title: "APPEND"
source: https://upstash.com/docs/redis/sdks/ts/commands/string/append
path: docs/redis/sdks/ts/commands/string/append
---

> Append a value to a string stored at key.

## Arguments

<ParamField body="key"type="string" required>
  The key to get.
</ParamField>

<ParamField body="value" required>
  The value to append.
</ParamField>

## Response

<ResponseField  type="integer" required>
How many characters were added to the string.
</ResponseField>

<RequestExample>
```ts Example
await redis.append(key, "Hello");
// returns 5
```
</RequestExample>
