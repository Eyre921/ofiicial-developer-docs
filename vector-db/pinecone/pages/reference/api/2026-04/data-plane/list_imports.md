---
title: "List imports"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/list_imports
path: reference/api/2026-04/data-plane/list_imports
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml get /bulk/imports
List all recent and ongoing import operations.

By default, `list_imports` returns up to 100 imports per page. If the `limit` parameter is set, `list` returns up to that number of imports instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of imports. When the response does not include a `pagination_token`, there are no more imports to return.

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

  curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken==Tm90aGluZyB0byBzZWUgaGVyZQo" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-Api-Version: 2026-04'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "1",
        "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
        "status": "Pending",
        "started_at": "2024-08-19T20:49:00.754Z",
        "finished_at": "2024-08-19T20:49:00.754Z",
        "percent_complete": 42.2,
        "records_imported": 1000000
      }
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>
