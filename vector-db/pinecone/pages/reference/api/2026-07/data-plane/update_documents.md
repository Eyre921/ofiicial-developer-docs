---
title: "Update documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/update_documents
path: reference/api/2026-07/data-plane/update_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/update
Apply partial updates to documents in a namespace. Documents are selected either per ID with `documents`, or in bulk with `filter`.

- `documents`: Each update is identified by its `_id`. Any other fields set new values for those fields, and fields listed in `_remove_fields` are removed from the document. Fields that are not mentioned are left unchanged. Updates to a document that does not exist are accepted but have no effect.
- `filter`: The same patch is applied to every document matching a metadata filter expression. The patch is given by `set_fields` and/or `remove_fields`, at least one of which must be specified. Text-match operators (`$match_phrase`, `$match_all`, `$match_any`) are not supported in a filtered update; they are only supported in search. The response reports `matched_records`, the number of documents the filter matched.

`documents` and the by-filter fields (`filter`, `set_fields`, `remove_fields`) are mutually exclusive.

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  # Patch specific documents by ID
  index.documents.update(
      namespace=NAMESPACE,
      documents=[
          {"_id": "doc1", "title": "Updated title"},
          {"_id": "doc2", "_remove_fields": ["content"]},
      ],
  )

  # Apply the same patch to every document matching a metadata filter
  index.documents.update(
      namespace=NAMESPACE,
      filter={"category": {"$eq": "news"}},
      set_fields={"category": "archive"},
      remove_fields=["content"],
  )
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"

  # EXAMPLE REQUEST 1: Patch specific documents by ID
  curl "https://$INDEX_HOST/namespaces/__default__/documents/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "documents": [
        { "_id": "doc1", "title": "Updated title" },
        { "_id": "doc2", "_remove_fields": ["content"] }
      ]
    }'

  # EXAMPLE REQUEST 2: Update by metadata filter
  curl "https://$INDEX_HOST/namespaces/__default__/documents/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "filter": { "category": { "$eq": "news" } },
      "set_fields": { "category": "archive" },
      "remove_fields": ["content"]
    }'
  ```
</RequestExample>
