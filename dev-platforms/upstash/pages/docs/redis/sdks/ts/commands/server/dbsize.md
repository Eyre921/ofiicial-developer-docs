---
title: "DBSIZE"
source: https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize
path: docs/redis/sdks/ts/commands/server/dbsize
---

> Count the number of keys in the database.

## Arguments

This command has no arguments

## Response

<ResponseField type="integer" required>
 The number of keys in the database
</ResponseField>

<RequestExample>
```ts Example
const keys = await redis.dbsize();
console.log(keys) // 20
```
</RequestExample>
