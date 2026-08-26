---
title: "JSON.FORGET"
source: https://upstash.com/docs/redis/sdks/py/commands/json/forget
path: docs/redis/sdks/py/commands/json/forget
---

> Delete a key from a JSON document.

## Arguments

<ParamField body="key" type="str" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="str" required>
    The path to forget. `$` is the root.
</ParamField>

## Response

<ResponseField type="int" required>
  How many paths were deleted.
</ResponseField>

<RequestExample>
```py Example
redis.json.forget("key", "$.path.to.value")
```
</RequestExample>
