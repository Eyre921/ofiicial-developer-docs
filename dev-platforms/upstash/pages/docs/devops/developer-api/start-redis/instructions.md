---
title: "Get Instructions"
source: https://upstash.com/docs/devops/developer-api/start-redis/instructions
path: docs/devops/developer-api/start-redis/instructions
---

This endpoint does not require authentication. It returns a markdown
document that explains how to create a free, temporary Redis database with
[`POST /start-redis`](/docs/devops/developer-api/start-redis/create), including how
the `Idempotency-Key` header works and how the database can be claimed later.

It is meant to be read by AI agents: point an agent at
`https://upstash.com/start-redis` and it has everything it needs.

## Request

This endpoint doesn't require any parameters.

## Response

The response body is `text/markdown`.

<RequestExample>

```sh curl
curl https://upstash.com/start-redis \
  -H "User-Agent: <your-agent-name>"
```

</RequestExample>

<ResponseExample>

```md 200 OK
# Upstash Redis for Agents

A zero-config Redis database for AI agents — no signup, no UI.

To create a database, generate a fresh UUIDv4 and POST it as the
`Idempotency-Key` header:

  curl -X POST -H "Idempotency-Key: <uuidv4>" \
    -H "User-Agent: <your-agent-name>" https://upstash.com/start-redis

...
```

</ResponseExample>
