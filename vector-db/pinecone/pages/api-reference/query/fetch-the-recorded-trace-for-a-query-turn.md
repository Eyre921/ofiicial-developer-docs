---
title: "Fetch the recorded trace for a query turn"
source: https://docs.pinecone.io/api-reference/query/fetch-the-recorded-trace-for-a-query-turn
path: api-reference/query/fetch-the-recorded-trace-for-a-query-turn
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml get /queries/{id}/trace
The per-turn debug trace (steps, tool calls, strategy, cost, rollup). Trace persistence is unconditional — every turn lands a trace blob — so this is available once the turn is terminal.
