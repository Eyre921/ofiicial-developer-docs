---
title: "Describe a namespace alias"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/describe_namespace_alias
path: reference/api/2026-07/data-plane/describe_namespace_alias
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /namespace-aliases/{alias_name}
Get an alias and the namespace it resolves to.

For guidance and examples, see [Manage namespace aliases](https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases).

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  ALIAS_NAME="dataset"

  curl "https://$INDEX_HOST/namespace-aliases/$ALIAS_NAME" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
