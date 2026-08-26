---
title: "ZREVRANK"
source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zrevrank
path: docs/redis/sdks/ts/commands/zset/zrevrank
---

> Returns the rank of a member in a sorted set, with scores ordered from high to low.

## Arguments 

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

<ParamField body="member" type="TMember" required>
  The member to get the reverse rank of.
</ParamField>

## Response

<ResponseField type="integer" required>
    The reverse rank of the member.
</ResponseField>

<RequestExample>
```ts Example
const rank = await redis.rank("key", "member");
```
</RequestExample>
