---
title: "Create a namespace"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/createnamespace
path: reference/api/2026-04/data-plane/createnamespace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /namespaces
Create a namespace in a serverless index.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "name": "example-namespace",
          "schema": {
  		  "fields": { 
              "document_id": {"filterable": true},
              "document_title": {"filterable": true},
              "chunk_number": {"filterable": true},
              "document_url": {"filterable": true},
              "created_at": {"filterable": true}
            }
          }
        }'
  ```
</RequestExample>
