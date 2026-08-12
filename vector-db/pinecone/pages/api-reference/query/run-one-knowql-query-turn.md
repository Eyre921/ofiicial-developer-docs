---
title: "Run one KnowQL query turn"
source: https://docs.pinecone.io/api-reference/query/run-one-knowql-query-turn
path: api-reference/query/run-one-knowql-query-turn
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml post /query
Send `ask` (the natural-language question) and, when starting a new session, a `scope` of 1–10 contexts. Continue an existing session with `session_id` or `previous_query_id`. Scoped search contexts must be curated (work contexts are queryable immediately), and a scope may not mix work and search contexts.

`stream` and `background` are mutually exclusive. With `background: true` the API returns `202` with an `in_progress` query and the client polls `GET /queries/{id}`. With `stream: true` the API emits an SSE stream whose `event:` names are the event `type` (`response.created`, `response.step`, `response.output_text.delta`, `response.turn_rollup`, `response.synthesis`, `response.trace`, and a terminal `response.completed` / `response.failed` / `response.cancelled`), followed by a final `query` event carrying the full query object. Read the answer from `output[].content[].text`.
