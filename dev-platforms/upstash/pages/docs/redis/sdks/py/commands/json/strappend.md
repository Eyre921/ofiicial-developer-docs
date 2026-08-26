---
title: "JSON.STRAPPEND"
source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend
path: docs/redis/sdks/py/commands/json/strappend
---

> Append the json-string values to the string at path.

## Arguments

<ParamField body="key" type="str" required>
    The key of the json entry.
</ParamField>
<ParamField body="path" type="str" required>
    The path of the string.
</ParamField>

<ParamField body="value" type="str" required>
    The value to append to the existing string.
</ParamField>

## Response

<ResponseField type="List[int]" required>
  The length of the string after the appending.
</ResponseField>

<RequestExample>
```py Example
redis.json.strappend("key", "$.path.to.str", "abc")
```
</RequestExample>
