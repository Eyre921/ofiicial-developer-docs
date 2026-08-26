---
title: "PING"
source: https://upstash.com/docs/redis/sdks/py/commands/auth/ping
path: docs/redis/sdks/py/commands/auth/ping
---

> Send a ping to the server and get a response if the server is alive.

## Arguments

No arguments

## Response

<ResponseField type="str" required>
  `PONG`
</ResponseField>

<RequestExample>
```py Example
assert redis.ping() == "PONG"
```
</RequestExample>
