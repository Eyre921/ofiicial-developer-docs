---
title: "Cancel an in-progress query turn"
source: https://docs.pinecone.io/reference/api/nexus/cancel_query
path: reference/api/nexus/cancel_query
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml POST /queries/{id}/cancel
Idempotent — an already-terminal query is returned unchanged. On success the turn's `status` becomes `cancelled`.
