---
title: "RENAME"
source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename
path: docs/redis/sdks/ts/commands/generic/rename
---

> Rename a key

## Arguments

<ParamField body="source" type="string" required>
  The original key.
</ParamField>

<ParamField body="destination" type="string" required>
  A new name for the key.
</ParamField>

## Response

<ResponseField type="string" required>
 `OK`
</ResponseField>

<RequestExample>
```ts Example
 await redis.rename("old", "new");
```
</RequestExample>
