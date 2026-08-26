---
title: "DBSIZE"
source: https://upstash.com/docs/redis/sdks/py/commands/server/dbsize
path: docs/redis/sdks/py/commands/server/dbsize
---

> Count the number of keys in the database.

## Arguments

This command has no arguments

## Response

<ResponseField type="int" required>
 The number of keys in the database
</ResponseField>

<RequestExample>
```py Example
redis.dbsize()
```
</RequestExample>
