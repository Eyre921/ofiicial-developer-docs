---
title: "Get Metrics"
source: https://upstash.com/docs/devops/developer-api/start-redis/metrics
path: docs/devops/developer-api/start-redis/metrics
---

> Returns usage metrics for a database created with start-redis.

`GET https://upstash.com/start-redis/metrics/{id}`

This endpoint does not require authentication. It returns usage metrics for
a free database created with
[`POST /start-redis`](/devops/developer-api/start-redis/create), so an agent
can check how the database is being used without a console login.

## Request

<ParamField path="id" type="string" required>
  The database ID: the UUID you sent as `Idempotency-Key` when creating the
  database, or the ID returned in the response if you omitted it.
</ParamField>

<ParamField header="User-Agent" type="string">
  The name of the agent making the request, for example `claude-code`.
</ParamField>

## Response

<ResponseField name="uptime_seconds" type="number">
  Seconds since the database was created.
</ResponseField>
<ResponseField name="expires_at" type="string">
  When the database will be deleted unless claimed, as an ISO 8601 timestamp.
</ResponseField>
<ResponseField name="console_url" type="string">
  The console page where a user can view usage and claim the database.
</ResponseField>
<ResponseField name="commands_total" type="number">
  Total number of commands executed.
</ResponseField>
<ResponseField name="commands_per_sec_1m" type="number">
  Command throughput over the last minute.
</ResponseField>
<ResponseField name="keys" type="number">
  Number of keys in the database.
</ResponseField>
<ResponseField name="memory_bytes" type="number">
  Memory used by the data, in bytes.
</ResponseField>
<ResponseField name="bytes_in" type="number">
  Total bytes received by the database.
</ResponseField>
<ResponseField name="bytes_out" type="number">
  Total bytes sent by the database.
</ResponseField>

Returns `404 Not Found` if no database exists with that ID.
