---
title: "Cancel an import"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/cancel_import
path: reference/api/2026-07/data-plane/cancel_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml delete /bulk/imports/{id}
Cancel an import operation if it is not yet finished. It has no effect if the operation is already finished.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X DELETE "https://$INDEX_HOST/bulk/imports/101" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
