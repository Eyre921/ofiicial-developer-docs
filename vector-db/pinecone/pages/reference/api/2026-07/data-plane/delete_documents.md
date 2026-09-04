---
title: "Delete documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/delete_documents
path: reference/api/2026-07/data-plane/delete_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/delete
Delete documents from a namespace. Exactly one of `ids`, `filter`, or `delete_all` must be specified.

- `ids`: Delete documents with the given IDs.
- `filter`: Delete every document matching a metadata filter expression. Text-match operators (`$match_phrase`, `$match_all`, `$match_any`) are not supported in a filtered delete; they are only supported in search. The response reports `matched_records`, the number of documents the filter matched.
- `delete_all`: Delete all documents in the namespace.

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  # Delete by IDs
  index.documents.delete(namespace=NAMESPACE, ids=["doc1", "doc2"])

  # Delete by metadata filter
  index.documents.delete(namespace=NAMESPACE, filter={"category": {"$eq": "news"}})

  # Delete every document in the namespace
  index.documents.delete(namespace=NAMESPACE, delete_all=True)
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"

  # EXAMPLE REQUEST 1: Delete by IDs
  curl "https://$INDEX_HOST/namespaces/__default__/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{ "ids": ["doc1", "doc2"] }'

  # EXAMPLE REQUEST 2: Delete by metadata filter
  curl "https://$INDEX_HOST/namespaces/__default__/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{ "filter": { "category": { "$eq": "news" } } }'

  # EXAMPLE REQUEST 3: Delete all documents in a namespace
  curl "https://$INDEX_HOST/namespaces/__default__/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{ "delete_all": true }'
  ```
</RequestExample>
