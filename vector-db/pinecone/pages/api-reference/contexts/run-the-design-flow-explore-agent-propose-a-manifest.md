---
title: "Run the Design-flow explore agent (propose a manifest)"
source: https://docs.pinecone.io/api-reference/contexts/run-the-design-flow-explore-agent-propose-a-manifest
path: api-reference/contexts/run-the-design-flow-explore-agent-propose-a-manifest
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /contexts/{slug}/explore
Inspects the uploaded source and proposes manifest-template matches in the task's `output` (see `ExploreOutput`). Persists nothing — review the proposal, then apply it with a manifest update and a forced curate. Body is optional.
