---
title: "ZREVRANK"
source: https://upstash.com/docs/redis/sdks/py/commands/zset/zrevrank
path: docs/redis/sdks/py/commands/zset/zrevrank
---

> Returns the rank of a member in a sorted set, with scores ordered from high to low.

## Arguments 

<ParamField body="key" type="str" required>
  The key to get.
</ParamField>

<ParamField body="member" type="str" required>
  The member to get the reverse rank of.
</ParamField>

## Response

<ResponseField type="int" required>
    The reverse rank of the member.
</ResponseField>

<RequestExample>
```py Example
redis.zadd("myset", {"a": 1, "b": 2, "c": 3})

assert redis.zrevrank("myset", "a") == 2
```
</RequestExample>
