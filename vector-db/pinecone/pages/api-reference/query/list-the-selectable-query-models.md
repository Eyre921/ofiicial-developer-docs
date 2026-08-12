---
title: "List the selectable query models"
source: https://docs.pinecone.io/api-reference/query/list-the-selectable-query-models
path: api-reference/query/list-the-selectable-query-models
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml get /models
The model catalog the `model` field on `POST /query` draws from. Returns the default model, every catalog entry, the tier → model-id map, per-phase defaults, and the curate-capable model ids. Only entries with `available: true` are selectable (others are coming soon and rejected with `400`).
