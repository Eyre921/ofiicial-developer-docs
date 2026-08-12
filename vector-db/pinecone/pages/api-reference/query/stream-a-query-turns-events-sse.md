---
title: "Stream a query turn's events (SSE)"
source: https://docs.pinecone.io/api-reference/query/stream-a-query-turns-events-sse
path: api-reference/query/stream-a-query-turns-events-sse
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml get /queries/{id}/events
Server-sent event stream of the turn's events as they land — the same `type`-named events POST /query emits with `stream: true`, but as a standalone, resumable subscription. Reconnect with `Last-Event-ID` to replay from where the stream dropped.
