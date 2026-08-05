---
title: "(Re)build the context's index from its sources"
source: https://docs.pinecone.io/reference/api/nexus/curate_context
path: reference/api/nexus/curate_context
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml POST /contexts/{slug}/curate
Curate the staged sources under the active manifest. **Required before querying** — there is no auto-curate. Body is optional. Set `force: true` to do a full rebuild (use after editing the manifest); the default is an incremental curate. Search contexts only — a work context builds via `work`/`groom` instead.
