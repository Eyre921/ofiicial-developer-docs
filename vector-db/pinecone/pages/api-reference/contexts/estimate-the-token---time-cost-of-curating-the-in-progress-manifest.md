---
title: "Estimate the token + time cost of curating the in-progress manifest"
source: https://docs.pinecone.io/api-reference/contexts/estimate-the-token-+-time-cost-of-curating-the-in-progress-manifest
path: api-reference/contexts/estimate-the-token---time-cost-of-curating-the-in-progress-manifest
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml post /contexts/{slug}/profile
Spins up the `profile` runtime to estimate the token + time cost of curating the sources under the in-progress manifest (sent in the request body), returned as the task's `output` (see `ProfileEstimateOutput`). Persists nothing; the console polls it for the Design-page cost box. Body is optional.
