---
title: "Trigger an on-demand self-tuning optimize"
source: https://docs.pinecone.io/api-reference/contexts/trigger-an-on-demand-self-tuning-optimize
path: api-reference/contexts/trigger-an-on-demand-self-tuning-optimize
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /contexts/{slug}/optimize
Tunes the manifest from real query traffic, then chains a forced re-curate. Every field of the required body is optional, so `{}` is valid — and a no-op without `candidate_queries`. The context must be curated, and only one optimize runs at a time.
