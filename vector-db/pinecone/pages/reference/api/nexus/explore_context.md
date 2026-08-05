---
title: "Run the Design-flow explore agent (propose a manifest)"
source: https://docs.pinecone.io/reference/api/nexus/explore_context
path: reference/api/nexus/explore_context
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml POST /contexts/{slug}/explore
Inspects the uploaded source and proposes manifest-template matches, returned in the task's `output` (see `ExploreOutput`). Persists nothing on the index — review the proposal, then apply it via the manifest update + a forced curate. Body is optional.
