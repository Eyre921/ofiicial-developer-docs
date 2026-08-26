---
title: "JSON.ARRLEN"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/arrlen
path: docs/redis/sdks/ts/commands/json/arrlen
---

> Report the length of the JSON array at `path` in `key`.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path of the array. `$` is the root.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The length of the array.
</ResponseField>

<RequestExample>
```ts Example
const length = await redis.json.arrlen("key", "$.path.to.array");
```
</RequestExample>
