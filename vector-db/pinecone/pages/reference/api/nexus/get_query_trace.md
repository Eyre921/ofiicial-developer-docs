---
title: "Fetch the recorded trace for a query turn"
source: https://docs.pinecone.io/reference/api/nexus/get_query_trace
path: reference/api/nexus/get_query_trace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /queries/{id}/trace
The per-turn debug trace (steps, tool calls, strategy, cost, rollup). Trace persistence is unconditional — every turn lands a trace blob — so this is available once the turn is terminal.
