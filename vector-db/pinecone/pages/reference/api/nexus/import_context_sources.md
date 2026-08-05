---
title: "Import source documents from a project connector"
source: https://docs.pinecone.io/reference/api/nexus/import_context_sources
path: reference/api/nexus/import_context_sources
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml POST /contexts/{slug}/import
Pull source documents from a linked project connector (Box, ...) into the context. Supply either `folder` or `files`. Stages the source only — curate explicitly before querying.
