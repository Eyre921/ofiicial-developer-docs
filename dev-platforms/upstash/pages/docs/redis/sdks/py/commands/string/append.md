---
title: "APPEND"
source: https://upstash.com/docs/redis/sdks/py/commands/string/append
path: docs/redis/sdks/py/commands/string/append
---

> Append a value to a string stored at key.

## Arguments

<ParamField body="key"type="str" required>
  The key to get.
</ParamField>

<ParamField body="value" required>
  The value to append.
</ParamField>

## Response

<ResponseField  type="int" required>
How many characters were added to the string.
</ResponseField>

<RequestExample>
```py Example
redis.set("key", "Hello")

assert redis.append("key", " World") == 11

assert redis.get("key") == "Hello World"
```
</RequestExample>
