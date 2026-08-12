---
title: "Fork a context (copy manifest into a fresh target)"
source: https://docs.pinecone.io/api-reference/contexts/fork-a-context-copy-manifest-into-a-fresh-target
path: api-reference/contexts/fork-a-context-copy-manifest-into-a-fresh-target
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml post /contexts/{slug}/fork
Copies the source context's manifest and lifecycle metadata onto an **already-created** target context in the same project, so the target's query and curate gates pass. It does not create the target — create it first with `POST /contexts`. The target's index stays empty until curated. The source must have been optimized (`last_optimized_at` set) and must not be optimizing.
