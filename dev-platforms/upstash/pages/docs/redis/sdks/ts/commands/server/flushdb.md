---
title: "FLUSHDB"
source: https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb
path: docs/redis/sdks/ts/commands/server/flushdb
---

<Warning>
Deletes all keys permanently. Use with caution!
</Warning>
## Arguments

<ParamField body="async" type="boolean">
  Whether to perform the operation asynchronously.
  Defaults to synchronous.
</ParamField>

<RequestExample>
```ts Sync
await redis.flushdb();
```
```ts Async
await redis.flushdb({async: true})
```
</RequestExample>
