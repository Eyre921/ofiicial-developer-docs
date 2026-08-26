---
title: "SCRIPT FLUSH"
source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_flush
path: docs/redis/sdks/py/commands/scripts/script_flush
---

> Removes all scripts from the script cache.

## Arguments

<ParamField body="flush_type" type='"ASYNC" | "SYNC"' required>
  Whether to perform the flush asynchronously or synchronously.
</ParamField>

<RequestExample>
```py Example
redis.script_flush(flush_type="ASYNC")
```
</RequestExample>
