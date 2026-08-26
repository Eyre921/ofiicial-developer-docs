---
title: "RANDOMKEY"
source: https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey
path: docs/redis/sdks/ts/commands/generic/randomkey
---

> Returns a random key from database

## Arguments

No arguments

## Response

<ResponseField type="string" required>
A random key from database, or `null` when database is empty.
</ResponseField>

<RequestExample>
```ts Example
const key = await redis.randomkey();
```
</RequestExample>
