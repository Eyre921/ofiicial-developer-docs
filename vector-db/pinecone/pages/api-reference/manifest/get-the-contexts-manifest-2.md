---
title: "Get the context's manifest"
source: https://docs.pinecone.io/api-reference/manifest/get-the-contexts-manifest
path: api-reference/manifest/get-the-contexts-manifest
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml get /contexts/{slug}/manifest
The context's pinned manifest document. A context that pins nothing returns `null` — the runtime fills defaults. Writes go through the `manifest` field on `PUT /contexts/{slug}`.
