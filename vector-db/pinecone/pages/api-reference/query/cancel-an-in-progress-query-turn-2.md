---
title: "Cancel an in-progress query turn"
source: https://docs.pinecone.io/api-reference/query/cancel-an-in-progress-query-turn
path: api-reference/query/cancel-an-in-progress-query-turn
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /queries/{id}/cancel
Idempotent — an already-terminal query is returned unchanged. On success the turn's `status` becomes `cancelled`.
