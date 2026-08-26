---
title: "JSON.CLEAR"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/clear
path: docs/redis/sdks/ts/commands/json/clear
---

> Clear container values (arrays/objects) and set numeric values to 0.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path to clear. `$` is the root.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  How many values were cleared.
</ResponseField>

<RequestExample>
```ts Example
await redis.json.clear("key");
```
```ts With path
await redis.json.clear("key", "$.my.key");
```
</RequestExample>
