---
title: "SCRIPT EXISTS"
source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_exists
path: docs/redis/sdks/py/commands/scripts/script_exists
---

> Check if scripts exist in the script cache.

## Arguments

<ParamField body="hashes" type="List[str]" required>
  The sha1 of the scripts to check.
</ParamField>

## Response

<ResponseField type="List[bool]" required>
  A list of booleans indicating if the script exists in the script cache.
</ResponseField>

<RequestExample>
```py Example
# Script 1 exists
# Script 0 does not
await redis.scriptExists("<sha1>", "<sha2>") == [1, 0]
```
</RequestExample>
