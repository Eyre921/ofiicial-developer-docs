---
title: "HGETALL"
source: https://upstash.com/docs/redis/sdks/py/commands/hash/hgetall
path: docs/redis/sdks/py/commands/hash/hgetall
---

> Retrieves all fields from a hash.

## Arguments

<ParamField body="key" type="str" required>
  The key to get.
</ParamField>

## Response

<ResponseField type="Optional[str]" required>
  An object with all fields in the hash.
</ResponseField>

<RequestExample>
```py Example
redis.hset("myhash", values={
"field1": "Hello",
"field2": "World"
})

assert redis.hgetall("myhash") == {"field1": "Hello", "field2": "World"}
```
</RequestExample>
