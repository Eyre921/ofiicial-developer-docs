---
title: "JSON.DEL"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/del
path: docs/redis/sdks/ts/commands/json/del
---

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path to delete. `$` is the root.
</ParamField>

## Response

<ResponseField type="integer" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
```ts Example
await redis.json.del("key", "$.path.to.value");
```
</RequestExample>
