---
title: "Import source documents from a project connector"
source: https://docs.pinecone.io/api-reference/source-files/import-source-documents-from-a-project-connector
path: api-reference/source-files/import-source-documents-from-a-project-connector
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /contexts/{slug}/import
Pull source documents from a linked project connector (Box, ...) into the context. Supply either `folder` or `files`. Stages the source only — curate explicitly before querying.
