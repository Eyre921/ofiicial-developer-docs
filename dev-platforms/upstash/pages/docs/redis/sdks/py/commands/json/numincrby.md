---
title: "JSON.NUMINCRBY"
source: https://upstash.com/docs/redis/sdks/py/commands/json/numincrby
path: docs/redis/sdks/py/commands/json/numincrby
---

> Increment the number value stored at `path` by number.

## Arguments

<ParamField body="key" type="str" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="str" required>
    The path of the number.
</ParamField>

<ParamField body="increment" type="number" required>
    The number to increment by.
</ParamField>

## Response

<ResponseField type="List[int]" required>
  The new value after incrementing
</ResponseField>

<RequestExample>
```py Example
newValue = redis.json.numincrby("key", "$.path.to.value", 2)
```
</RequestExample>
