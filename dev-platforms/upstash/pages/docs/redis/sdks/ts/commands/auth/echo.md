---
title: "ECHO"
source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo
path: docs/redis/sdks/ts/commands/auth/echo
---

Returns a message back to you. Useful for debugging the connection.

## Arguments

<ParamField body="message" type="string" required>
  A message to send to the server.
</ParamField>

## Response

<ResponseField type="string" required>
  The same message you sent.
</ResponseField>

<RequestExample>
```ts Example
const response = await redis.echo("hello world");
console.log(response); // "hello world"
```
</RequestExample>
