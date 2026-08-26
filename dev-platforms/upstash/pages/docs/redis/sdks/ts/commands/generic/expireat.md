---
title: "EXPIREAT"
source: https://upstash.com/docs/redis/sdks/ts/commands/generic/expireat
path: docs/redis/sdks/ts/commands/generic/expireat
---

> Sets a timeout on key. The key will automatically be deleted.

## Arguments

<ParamField body="key" type="string" required>
  The key to set the timeout on.
</ParamField>

<ParamField body="unix" type="integer">
A unix timestamp in seconds at which point the key will expire.
</ParamField>

## Response

<ResponseField type="integer" required>
  `1` if the timeout was set, `0` otherwise
</ResponseField>

<RequestExample>
```ts Example
await redis.set("mykey", "Hello");
const tenSecondsFromNow = Math.floor(Date.now() / 1000) + 10;
await redis.expireat("mykey", tenSecondsFromNow);
```
</RequestExample>
