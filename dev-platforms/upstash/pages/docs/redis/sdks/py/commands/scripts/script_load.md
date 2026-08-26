---
title: "SCRIPT LOAD"
source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load
path: docs/redis/sdks/py/commands/scripts/script_load
---

> Load the specified Lua script into the script cache.

## Arguments

<ParamField body="script" type="str" required>
  The script to load.
</ParamField>

## Response

<ResponseField type="str" required>
  The sha1 of the script.
</ResponseField>

<RequestExample>
```py Example
sha1 = redis.script_load("return 1")

assert redis.evalsha(sha1) == 1
```
</RequestExample>
