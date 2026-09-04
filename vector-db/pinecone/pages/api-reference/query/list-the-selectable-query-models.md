---
title: "List the selectable query models"
source: https://docs.pinecone.io/api-reference/query/list-the-selectable-query-models
path: api-reference/query/list-the-selectable-query-models
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml get /models
What the `model` field on `POST /query` draws from: the default, every catalog entry, the tier → model-id map, per-phase defaults, and the curate-capable ids. Only entries with `available: true` are selectable; the rest are rejected with `400`.
