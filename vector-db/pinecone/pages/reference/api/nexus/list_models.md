---
title: "List the selectable query models"
source: https://docs.pinecone.io/reference/api/nexus/list_models
path: reference/api/nexus/list_models
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /models
The model catalog the `model` field on `POST /query` draws from. Returns the default model, every catalog entry, the tier → model-id map, per-phase defaults, and the curate-capable model ids. Only entries with `available: true` are selectable (others are coming soon and rejected with `400`).
