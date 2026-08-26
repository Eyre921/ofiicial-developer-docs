---
title: "RANDOMKEY"
source: https://upstash.com/docs/redis/sdks/py/commands/generic/randomkey
path: docs/redis/sdks/py/commands/generic/randomkey
---

> Returns a random key from database

## Arguments

No arguments

## Response

<ResponseField type="str">
A random key from database, or `None` when database is empty.
</ResponseField>

<RequestExample>
```py Example
assert redis.randomkey() is None

redis.set("key1", "Hello")
redis.set("key2", "World")

assert redis.randomkey() is not None
```
</RequestExample>
