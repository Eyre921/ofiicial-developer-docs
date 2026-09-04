---
title: "Build or rebuild the context's index from its sources"
source: https://docs.pinecone.io/api-reference/curation/build-or-rebuild-the-contexts-index-from-its-sources
path: api-reference/curation/build-or-rebuild-the-contexts-index-from-its-sources
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml post /contexts/{slug}/curate
Curate the staged sources under the active manifest. **Required before querying** — there is no auto-curate. Body is optional; `force: true` rebuilds fully, which is what a manifest edit needs. Search contexts only: a work context builds via `work`/`groom`.
