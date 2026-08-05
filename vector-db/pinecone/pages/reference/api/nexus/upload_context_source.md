---
title: "Upload a source file or archive"
source: https://docs.pinecone.io/reference/api/nexus/upload_context_source
path: reference/api/nexus/upload_context_source
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml POST /contexts/{slug}/import/upload
One file per request, max 2 GiB. Archives (`.zip`, `.tar`, `.tar.gz`, `.tgz`) are expanded by the import runtime. Stages the source only — it does not index anything. Curate explicitly with `POST /contexts/{slug}/curate` before querying.
