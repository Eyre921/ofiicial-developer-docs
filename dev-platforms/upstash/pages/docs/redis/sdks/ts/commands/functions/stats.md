---
title: "FUNCTION STATS"
source: https://upstash.com/docs/redis/sdks/ts/commands/functions/stats
path: docs/redis/sdks/ts/commands/functions/stats
---

> Return information about the function running engine.

## Response

<ResponseField type="Object" required>
  Stats about the engines and functions.
  
  <Note> 
  Currently, `LUA` is the only supported engine.
  </Note>
  <Expandable>
    <ParamField body="engines" type="Object">
      <Expandable>
        <ParamField body="LUA" type="Object">
          <Expandable>
            <ParamField body="librariesCount" type="number">
              The number of libraries.
            </ParamField>
            <ParamField body="functionsCount" type="number">
              The number of functions.
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ResponseField>

<RequestExample>
```ts Example
const stats = await redis.functions.stats()

console.log(stats)
// {
//   engines: {
//     LUA: {
//       librariesCount: 3,
//       functionsCount: 15
//     }
//   }
// }
```
</RequestExample>
