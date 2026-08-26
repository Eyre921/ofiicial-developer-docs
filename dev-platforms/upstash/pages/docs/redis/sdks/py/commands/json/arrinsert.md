---
title: "JSON.ARRINSERT"
source: https://upstash.com/docs/redis/sdks/py/commands/json/arrinsert
path: docs/redis/sdks/py/commands/json/arrinsert
---

> Insert the json values into the array at path before the index (shifts to the right).

## Arguments

<ParamField body="key" type="str" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="str" required>
    The path of the array.
</ParamField>

<ParamField body="index" type="int" required>
   The index where to insert the values.
</ParamField>

<ParamField body="values" type="...TValue[]" required>
    One or more values to append to the array.
</ParamField>

## Response

<ResponseField type="List[int]" required>
  The length of the array after the insertion.
</ResponseField>

<RequestExample>
```py Example
length = redis.json.arrinsert("key", "$.path.to.array", 2, "a", "b")
```
</RequestExample>
