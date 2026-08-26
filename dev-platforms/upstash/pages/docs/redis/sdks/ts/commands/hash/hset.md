---
title: "HSET"
source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hset
path: docs/redis/sdks/ts/commands/hash/hset
---

> Write one or more fields to a hash.

## Arguments

<ParamField body="key" type="string" required>
  The key of the hash.
</ParamField>

<ParamField body="fields" type="{ [fieldName]: TValue }" required>
  An object of fields and their values.

</ParamField>

## Response

<ResponseField type="integer" required>
  The number of fields that were added.
</ResponseField>

<RequestExample>
```ts Example
await redis.hset("key", {
  id: 1,
  username: "chronark",
  name: "andreas"
  });
```
</RequestExample>
