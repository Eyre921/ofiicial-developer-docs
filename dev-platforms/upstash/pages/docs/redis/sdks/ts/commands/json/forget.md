---
title: "JSON.FORGET"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/forget
path: docs/redis/sdks/ts/commands/json/forget
---

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path to forget. `$` is the root.
</ParamField>

## Response

<ResponseField type="integer" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
```ts Example
await redis.json.forget("key", "$.path.to.value");
```
</RequestExample>
