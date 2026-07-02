---
title: "Describe an import"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/describe_import
path: reference/api/2026-04/data-plane/describe_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml get /bulk/imports/{id}
Return details of a specific import operation.

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

  curl -X GET "https://$INDEX_HOST/bulk/imports/101" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-Api-Version: 2026-04'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "101",
    "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
    "status": "Pending",
    "created_at": "2024-08-19T20:49:00.754Z",
    "finished_at": "2024-08-19T20:49:00.754Z",
    "percent_complete": 42.2,
    "records_imported": 1000000
  }
  ```
</ResponseExample>
