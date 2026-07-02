---
title: "Upsert text"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/upsert_records
path: reference/api/2026-04/data-plane/upsert_records
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /records/namespaces/{namespace}/upsert
Upsert text into a namespace. Pinecone converts the text to vectors automatically using the hosted embedding model associated with the index.

Upserting text is supported only for [indexes with integrated embedding](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Upsert records into a namespace
  # `chunk_text` fields are converted to dense vectors
  # `category` fields are stored as metadata
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
    -H "Content-Type: application/x-ndjson" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{"_id": "rec1", "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.", "category": "digestive system"}
        {"_id": "rec2", "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.", "category": "cultivation"}
        {"_id": "rec3", "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.", "category": "immune system"}
        {"_id": "rec4", "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.", "category": "endocrine system"}'
  ```
</RequestExample>

<ResponseExample />
