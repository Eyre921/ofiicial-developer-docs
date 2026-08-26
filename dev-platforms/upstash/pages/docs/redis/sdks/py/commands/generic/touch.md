---
title: "TOUCH"
source: https://upstash.com/docs/redis/sdks/py/commands/generic/touch
path: docs/redis/sdks/py/commands/generic/touch
---

> Alters the last access time of one or more keys

## Arguments

<ParamField body="keys" type="*List[str]" required>
  One or more keys.
</ParamField>

## Response

<ResponseField type="int">
  The number of keys that were touched.
</ResponseField>

<RequestExample>
```py Example
redis.touch("key1", "key2", "key3")
```
</RequestExample>
