---
title: "Get the curation ledger"
source: https://docs.pinecone.io/reference/api/nexus/get_curation_ledger
path: reference/api/nexus/get_curation_ledger
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /contexts/{slug}/curate
The full ledger: per-source hashes, edges, corpus groups, chunk-id lineage, version pin, reclaim intents, pointers, and glossary. This pays an O(corpus) chunk-id-lineage read — use `GET /contexts/{slug}/curate/version/pin` on the per-turn path.
