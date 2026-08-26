---
title: "Stop Resumable Query"
source: https://upstash.com/docs/vector/api/endpoints/resumable-query/stop
path: docs/vector/api/endpoints/resumable-query/stop
---

> Ends a resumable query and releases associated resources.

`POST https://{endpoint}/resumable-query-end`

## Request

<ParamField body="uuid" type="string" required>
  The unique identifier of the resumable query to end.
</ParamField>

## Response

<ResponseField name="result" type="string">
  A success message indicating the query was ended.
</ResponseField>
