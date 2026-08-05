---
title: "Stream a query turn's events (SSE)"
source: https://docs.pinecone.io/reference/api/nexus/stream_query_events
path: reference/api/nexus/stream_query_events
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /queries/{id}/events
Server-sent event stream of the turn's events as they land — the same `type`-named events POST /query emits with `stream: true`, but as a standalone, resumable subscription. Reconnect with `Last-Event-ID` to replay from where the stream dropped.
