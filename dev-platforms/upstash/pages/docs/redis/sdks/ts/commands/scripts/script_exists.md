---
title: "SCRIPT EXISTS"
source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_exists
path: docs/redis/sdks/ts/commands/scripts/script_exists
---

> Check if scripts exist in the script cache.

## Arguments

<ParamField body="hashes" type="string[]" required>
  The sha1 of the scripts to check.
</ParamField>

## Response

<ResponseField type="number[]" required>
  An array of numbers. `1` if the script exists, otherwise `0`.
</ResponseField>

<RequestExample>
```ts Example
await redis.scriptExists("<sha1>", "<sha2>")

// Returns 1 
// [1, 0]
```
</RequestExample>
