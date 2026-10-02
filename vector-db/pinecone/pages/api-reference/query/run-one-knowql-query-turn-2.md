---
title: "Run one KnowQL query turn"
source: https://docs.pinecone.io/api-reference/query/run-one-knowql-query-turn
path: api-reference/query/run-one-knowql-query-turn
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /query
Send `ask` and, on a new session, a `scope` of 1–10 contexts; continue an existing one with
`session_id` or `previous_query_id`. Scoped search contexts must be curated, and a scope may
not mix work and search contexts. Read the answer from `output[].content[].text`.

`stream` and `background` are mutually exclusive. `background: true` returns `202` with an
`in_progress` query to poll. `stream: true` emits an SSE stream whose `event:` names are the
event `type` (see `QueryEvent`), closed by a final `query` frame carrying the whole turn:

```
id: 1
event: response.created
data: {"type":"response.created","query_id":"qry_8b3d5f1a","session_id":"ses_4f9c1e2a"}

id: 2
event: response.output_text.delta
data: {"type":"response.output_text.delta","query_id":"qry_8b3d5f1a","delta":"Revenue grew 12%..."}

id: 3
event: response.completed
data: {"type":"response.completed","query_id":"qry_8b3d5f1a"}

event: query
data: {"id":"qry_8b3d5f1a","object":"query","status":"completed","output":[...]}
```
