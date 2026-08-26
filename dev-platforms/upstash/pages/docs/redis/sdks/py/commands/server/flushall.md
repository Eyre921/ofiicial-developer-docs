---
title: "FLUSHALL"
source: https://upstash.com/docs/redis/sdks/py/commands/server/flushall
path: docs/redis/sdks/py/commands/server/flushall
---

<Warning>
Deletes all keys permanently. Use with caution!
</Warning>
## Arguments

<ParamField body="flush_type" type='"ASYNC" | "SYNC"'>
  Whether to perform the operation asynchronously.
  Defaults to synchronous.
</ParamField>

<RequestExample>
```py Sync
redis.flushall()
```
```py Async
redis.flushall(flush_type="ASYNC")
```
</RequestExample>
