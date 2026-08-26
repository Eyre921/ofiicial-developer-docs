---
title: "JSON.NUMINCRBY"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/numincrby
path: docs/redis/sdks/ts/commands/json/numincrby
---

> Increment the number value stored at `path` by number.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path of the array. `$` is the root.
</ParamField>

<ParamField body="increment" type="number" required>
    The number to increment by.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The new value after incrementing
</ResponseField>

<RequestExample>
```ts Example
const newValue = await redis.json.numincrby("key", "$.path.to.value", 2);
```
</RequestExample>
