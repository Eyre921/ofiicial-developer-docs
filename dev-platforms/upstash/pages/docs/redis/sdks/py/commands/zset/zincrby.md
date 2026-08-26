---
title: "ZINCRBY"
source: https://upstash.com/docs/redis/sdks/py/commands/zset/zincrby
path: docs/redis/sdks/py/commands/zset/zincrby
---

> Increment the score of a member.

## Arguments 

<ParamField body="key" type="str" required>
  The key of the sorted set.
</ParamField>

<ParamField body="increment" type="int" required>
    The increment to add to the score.
</ParamField>

<ParamField body="member" type="str" required>
  The member to increment.
</ParamField>

## Response

<ResponseField type="float" required>
    The new score of `member` after the increment operation.
</ResponseField>

<RequestExample>
```py Example
redis.zadd("myset", {"one": 1, "two": 2, "three": 3})

assert redis.zincrby("myset", 2, "one") == 3
```
</RequestExample>
