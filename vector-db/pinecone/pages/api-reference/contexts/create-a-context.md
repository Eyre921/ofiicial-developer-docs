---
title: "Create a context"
source: https://docs.pinecone.io/api-reference/contexts/create-a-context
path: api-reference/contexts/create-a-context
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml post /contexts
The context is created empty and is not queryable until you import sources and curate them (curate is explicit — there is no auto-curate). Optionally seed a `manifest`. A `work` context is the exception: it is queryable from day zero and is built from traces of work rather than source documents.
