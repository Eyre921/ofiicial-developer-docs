---
title: "Trigger an on-demand self-tuning optimize"
source: https://docs.pinecone.io/api-reference/contexts/trigger-an-on-demand-self-tuning-optimize
path: api-reference/contexts/trigger-an-on-demand-self-tuning-optimize
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml post /contexts/{slug}/optimize
Tunes the manifest from real query traffic and chains a forced re-curate. A body is required but every field in it is optional, so `{}` is valid — and a no-op when no `candidate_queries` are supplied. The context must have been curated, and only one optimize runs at a time.
