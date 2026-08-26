---
title: "SCRIPT FLUSH"
source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_flush
path: docs/redis/sdks/ts/commands/scripts/script_flush
---

> Removes all scripts from the script cache.

## Arguments

<ParamField body="options" type="Object">
  <ParamField body="async" type="boolean">
    Performs the flush asynchronously.
  </ParamField>
  <ParamField body="sync" type="boolean">
    Performs the flush synchronously.
  </ParamField>
</ParamField>

<RequestExample>
```ts Example
await redis.scriptFlush();
```

```ts With options
await redis.scriptFlush({
  async: true,
});
```
</RequestExample>
