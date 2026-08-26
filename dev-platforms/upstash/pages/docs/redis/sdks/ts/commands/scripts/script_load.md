---
title: "SCRIPT LOAD"
source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load
path: docs/redis/sdks/ts/commands/scripts/script_load
---

> Load the specified Lua script into the script cache.

## Arguments

<ParamField body="script" type="string" required>
  The script to load.
</ParamField>

## Response

<ResponseField type="string" required>
  The sha1 of the script.
</ResponseField>

<RequestExample>
```ts Example
const script = `
  local value = redis.call('GET', KEYS[1])
  return value
`;
const sha1 = await redis.scriptLoad(script);

```
</RequestExample>
