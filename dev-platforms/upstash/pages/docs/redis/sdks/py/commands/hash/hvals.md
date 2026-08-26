---
title: "HVALS"
source: https://upstash.com/docs/redis/sdks/py/commands/hash/hvals
path: docs/redis/sdks/py/commands/hash/hvals
---

> Returns all values in the hash stored at key.

## Arguments

<ParamField body="key" type="str" required>
  The key of the hash.
</ParamField>

## Response

<ResponseField type="List[str]" required>
  All values in the hash, or an empty list when key does not exist.
</ResponseField>

<RequestExample>
```py Example
redis.hset("myhash", values={
  "field1": "Hello",
  "field2": "World"
})

assert redis.hvals("myhash") == ["Hello", "World"]
```
</RequestExample>
