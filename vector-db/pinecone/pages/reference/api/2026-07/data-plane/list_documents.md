---
title: "List documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/list_documents
path: reference/api/2026-07/data-plane/list_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/list
List documents in a namespace.

Returns up to 100 documents per page by default, in sorted order (bitwise "C" collation). Use the optional `prefix` parameter to limit results to documents whose IDs start with a given prefix. When there are more documents to return, the response includes a `pagination` token you can pass to retrieve the next page. When no `pagination` token is returned, there are no more documents to list.

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  # List every document ID in the namespace.
  # The SDK returns a paginator, so iterating it walks every page.
  for document in index.documents.list(namespace=NAMESPACE):
      print(document._id)

  # List only the IDs beginning with a prefix.
  for document in index.documents.list(namespace=NAMESPACE, prefix="report-2026#"):
      print(document._id)
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"

  # EXAMPLE REQUEST 1: List the first page of document IDs
  curl "https://$INDEX_HOST/namespaces/__default__/documents/list" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "limit": 20
    }'

  # EXAMPLE REQUEST 2: List only the IDs beginning with a prefix
  curl "https://$INDEX_HOST/namespaces/__default__/documents/list" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "prefix": "report-2026#"
    }'

  # EXAMPLE REQUEST 3: Retrieve the next page
  curl "https://$INDEX_HOST/namespaces/__default__/documents/list" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "pagination_token": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }'
  ```
</RequestExample>
