---
title: "Upsert documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/upsert_documents
path: reference/api/2026-07/data-plane/upsert_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/upsert
Upsert documents into a namespace.

Each document must include an `_id` field and at least one field defined in the index schema; metadata fields may be
provided alongside them.
Any metadata field you provide that is not declared in the schema is stored on the document, returned via include_fields, and
automatically indexed for filtering.

If a document with the same `_id` already exists, it is completely replaced. Documents become searchable within approximately one minute. The `namespace` is auto-created on first upsert; use `"__default__"` if you don't need partitioning.

<Note>
  Upsert replaces the whole document. For partial changes to specific fields, use [`POST /namespaces/{namespace}/documents/update`](/reference/api/2026-07/data-plane/update_documents), which patches fields per ID or in bulk by metadata filter.
</Note>

<Note>
  Each document in the `documents` array is validated against your index schema. If any document fails validation, **the entire request fails** and nothing is upserted. Field names starting with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators) are rejected.
</Note>

<Note>
  To ingest many documents, use the Python SDK's `index.documents.batch_upsert(documents=..., batch_size=..., max_workers=..., show_progress=...)`, a client-side convenience that splits a large list into batches and issues concurrent `POST /namespaces/{namespace}/documents/upsert` requests in the background. It's a wrapper around this endpoint, not a separate API.
</Note>

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  docs = [
      {"_id": "doc1", "title": "Machine learning in 2024", "body": "Machine learning models are revolutionizing natural language processing", "category": "technology", "year": 2024},
      {"_id": "doc2", "title": "Vector databases", "body": "Vector databases enable fast similarity search across embeddings", "category": "technology", "year": 2023},
      {"_id": "doc3", "title": "Quantum computing", "body": "Quantum computers leverage superposition for faster computation", "category": "science", "year": 2024},
  ]

  index.documents.upsert(
      namespace=NAMESPACE,
      documents=docs,
  )
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"
  curl "https://$INDEX_HOST/namespaces/__default__/documents/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "documents": [
        {
          "_id": "doc1",
          "title": "Machine learning in 2024",
          "body": "Machine learning models are revolutionizing natural language processing",
          "category": "technology",
          "year": 2024
        },
        {
          "_id": "doc2",
          "title": "Vector databases",
          "body": "Vector databases enable fast similarity search across embeddings",
          "category": "technology",
          "year": 2023
        },
        {
          "_id": "doc3",
          "title": "Quantum computing",
          "body": "Quantum computers leverage superposition for faster computation",
          "category": "science",
          "year": 2024
        }
      ]
    }'
  ```
</RequestExample>
