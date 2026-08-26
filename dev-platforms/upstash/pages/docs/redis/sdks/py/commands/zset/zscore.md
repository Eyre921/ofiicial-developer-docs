---
title: "ZSCORE"
source: https://upstash.com/docs/redis/sdks/py/commands/zset/zscore
path: docs/redis/sdks/py/commands/zset/zscore
---

> Returns the scores of a member.

## Arguments 

<ParamField body="key" type="str" required>
  The key to get.
</ParamField>

## Response

<ResponseField body="member" type="TMember" required>
    A member of the sortedset.
</ResponseField>

<RequestExample>
```py Example
redis.zadd("myset", {"a": 1, "b": 2, "c": 3})

assert redis.zscore("myset", "a") == 1
```
</RequestExample>
