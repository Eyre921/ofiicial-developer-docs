---
title: "Upload a source file or archive"
source: https://docs.pinecone.io/api-reference/source-files/upload-a-source-file-or-archive
path: api-reference/source-files/upload-a-source-file-or-archive
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /contexts/{slug}/import/upload
One file per request, max 2 GiB; archives (`.zip`, `.tar`, `.tar.gz`, `.tgz`) are expanded by the import runtime. Stages the source without indexing it — curate explicitly before querying.
