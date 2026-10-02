---
title: "Delete a namespace alias"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/delete_namespace_alias
path: reference/api/2026-07/data-plane/delete_namespace_alias
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml delete /namespace-aliases/{alias_name}
Remove an alias. The target namespace and its data are unchanged. Reads
that still use the alias name are treated as reads of a nonexistent
namespace (empty results, not an error), so migrate readers off the alias
first.

The call returns once no reader still resolves the alias, which takes about
a second; size client timeouts accordingly. A retried delete that returns
404 means the alias is already gone and carries the same guarantee.

For guidance and examples, see [Manage namespace aliases](https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases).

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  ALIAS_NAME="dataset"

  curl -X DELETE "https://$INDEX_HOST/namespace-aliases/$ALIAS_NAME" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
