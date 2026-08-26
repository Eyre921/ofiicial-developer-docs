---
title: "PERSIST"
source: https://upstash.com/docs/redis/sdks/py/commands/generic/persist
path: docs/redis/sdks/py/commands/generic/persist
---

> Remove any timeout set on the key.

## Arguments

<ParamField body="key" type="str" required>
  The key to persist
</ParamField>

## Response

<ResponseField type="bool">
  `True` if the timeout was set
</ResponseField>

<RequestExample>
```py Example
redis.set("key1", "Hello")
redis.expire("key1", 10)

assert redis.ttl("key1") == 10

redis.persist("key1")

assert redis.ttl("key1") == -1
```
</RequestExample>
