---
title: "ZSCORE"
source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zscore
path: docs/redis/sdks/ts/commands/zset/zscore
---

> Returns the scores of a member.

## Arguments 

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

## Response

<ResponseField body="member" type="TMember" required>
    A member of the sortedset.
</ResponseField>

<RequestExample>
```ts Example

await redis.zadd("key", 
    { score: 1, member: "m1" },
    { score: 2, member: "m2" },
    { score: 3, member: "m3" },
    { score: 4, member: "m4" },
)

const score = await redis.zscore("key", "m2")
console.log(score) // 2
```
</RequestExample>
