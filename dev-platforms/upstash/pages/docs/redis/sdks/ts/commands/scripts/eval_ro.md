---
title: "EVAL_RO"
source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/eval_ro
path: docs/redis/sdks/ts/commands/scripts/eval_ro
---

> Evaluate a read-only Lua script server side.

## Arguments

<ParamField body="script" type="string" required>
  The read-only lua script to run.
</ParamField>

<ParamField body="keys" type="string[]" required>
  All of the keys accessed in the script
</ParamField>

<ParamField body="args" type="unknown[]" required>
  All of the arguments you passed to the script
</ParamField>

## Response

<ResponseField type="any" required>
  The result of the script.
</ResponseField>

<RequestExample>
```ts Example
const script = `
    return ARGV[1]
`
const result = await redis.evalRo(script, [], ["hello"]);
console.log(result) // "hello"

```
</RequestExample>
