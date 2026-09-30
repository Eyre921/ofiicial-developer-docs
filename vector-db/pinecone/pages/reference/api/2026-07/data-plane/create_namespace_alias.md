---
title: "Create a namespace alias"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/create_namespace_alias
path: reference/api/2026-07/data-plane/create_namespace_alias
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespace-aliases
Create an alias that resolves to an existing namespace in the index. Reads
through the alias are served from its target namespace; writes to an alias
name are rejected. Many aliases can resolve to the same namespace.

The call returns once the alias resolves on every reader, which takes about
a second; size client timeouts accordingly. A 409 whose
`details.metadata.target_namespace` matches the requested target carries
the same guarantee: your earlier call committed and the alias is live.

For guidance and examples, see [Manage namespace aliases](https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases).

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/namespace-aliases" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
          "name": "dataset",
          "target_namespace": "dataset_v1"
      }'
  ```
</RequestExample>
