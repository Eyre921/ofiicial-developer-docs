---
title: "Repoint a namespace alias"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/repoint_namespace_alias
path: reference/api/2026-07/data-plane/repoint_namespace_alias
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml patch /namespace-aliases/{alias_name}
Update the namespace an alias resolves to. The change is atomic: the target
is validated in the same transaction that rewrites the alias, and on
failure the alias keeps its current target.

The call returns once the new target is live on every reader, which takes
about a second; size client timeouts accordingly. Reads through the alias
that start after the response are served from the new namespace, so no
polling is needed. Repointing is safe to retry; `updated_at` advances on
every attempt.

For guidance and examples, see [Manage namespace aliases](https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases).

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  ALIAS_NAME="dataset"

  curl -X PATCH "https://$INDEX_HOST/namespace-aliases/$ALIAS_NAME" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
          "target_namespace": "dataset_v2"
      }'
  ```
</RequestExample>
