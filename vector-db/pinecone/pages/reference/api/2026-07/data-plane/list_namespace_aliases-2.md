---
title: "List namespace aliases"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/list_namespace_aliases
path: reference/api/2026-07/data-plane/list_namespace_aliases
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /namespace-aliases
List the namespace aliases in a serverless index, ordered by name. Filter by name prefix or by target namespace.

Up to 100 aliases are returned per page; set `limit` to return fewer. When more remain, the response includes `pagination.next`; pass it as `paginationToken` to get the next page.

For guidance and examples, see [Manage namespace aliases](https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases).

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespace-aliases" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
