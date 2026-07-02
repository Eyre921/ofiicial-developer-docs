---
title: "Start import"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/start_import
path: reference/api/2026-04/data-plane/start_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /bulk/imports
Start an asynchronous import of vectors from object storage into an index.

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

  curl "https://$INDEX_HOST/bulk/imports" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-Api-Version: 2026-04' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
     "id": "101"
  }
  ```
</ResponseExample>
