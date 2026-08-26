---
title: "JSON.DEL"
source: https://upstash.com/docs/redis/sdks/py/commands/json/del
path: docs/redis/sdks/py/commands/json/del
---

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="str" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="str" required>
    The path to delete. `$` is the root.
</ParamField>

## Response

<ResponseField type="int" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
```py Example
redis.json.del("key", "$.path.to.value")
```
</RequestExample>
