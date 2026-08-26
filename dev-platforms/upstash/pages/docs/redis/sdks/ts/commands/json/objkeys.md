---
title: "JSON.OBJKEYS"
source: https://upstash.com/docs/redis/sdks/ts/commands/json/objkeys
path: docs/redis/sdks/ts/commands/json/objkeys
---

> Return the keys in the object that`s referenced by path.

## Arguments

<ParamField body="key" type="string" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="string" required>
    The path of the array. `$` is the root.
</ParamField>

## Response

<ResponseField type="string[][]" required>
  The keys of the object at the path.
</ResponseField>

<RequestExample>
```ts Example
const keys = await redis.json.objkeys("key", "$.path");
```
</RequestExample>
