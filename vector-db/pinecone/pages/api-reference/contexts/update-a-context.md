---
title: "Update a context"
source: https://docs.pinecone.io/api-reference/contexts/update-a-context
path: api-reference/contexts/update-a-context
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml put /contexts/{slug}
All fields optional; absent leaves untouched. Empty string clears description/guide; `{}` clears the manifest back to defaults. A supplied manifest is validated against the manifest schema.
