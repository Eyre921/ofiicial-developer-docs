---
title: "ZRANK"
source: https://upstash.com/docs/redis/sdks/ts/commands/zset/zrank
path: docs/redis/sdks/ts/commands/zset/zrank
---

> Returns the rank of a member

## Arguments 

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

<ParamField body="member" type="TMember" required>
  The member to get the rank of.
</ParamField>

## Response

<ResponseField type="integer" required>
    The rank of the member.
</ResponseField>

<RequestExample>
```ts Example
const rank = await redis.rank("key", "member");
```
</RequestExample>
