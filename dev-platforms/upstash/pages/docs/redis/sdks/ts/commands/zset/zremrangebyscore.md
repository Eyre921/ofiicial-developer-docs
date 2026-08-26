---
title: "ZREMRANGEBYSCORE"
source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyscore
path: docs/redis/sdks/ts/commands/zset/zremrangebyscore
---

> Remove all members in a sorted set between the given scores.

## Arguments 

<ParamField body="key" type="string" required>
  The key of the sorted set
</ParamField>

<ParamField body="min" type="number" required>
    The minimum score to remove.
</ParamField>
<ParamField body="max" type="number" required>
    The maximum score to remove.
</ParamField>

## Response

<ResponseField type="integer"  required>
    The number of elements removed from the sorted set.
</ResponseField>

<RequestExample>
```ts Example
await redis.zremrangebyscore("key", 2, 5)
```
</RequestExample>
