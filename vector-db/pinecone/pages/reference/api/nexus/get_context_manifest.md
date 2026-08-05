---
title: "Get the context's manifest"
source: https://docs.pinecone.io/reference/api/nexus/get_context_manifest
path: reference/api/nexus/get_context_manifest
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /contexts/{slug}/manifest
The context's pinned manifest document. A context with no pinned manifest returns `{}` — the runtime fills defaults. Writes go through the `manifest` field on `PUT /contexts/{slug}`.
