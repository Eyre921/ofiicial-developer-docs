---
title: "Fetch documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/fetch_documents
path: reference/api/2026-07/data-plane/fetch_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/fetch
Fetch documents from a namespace. Returns the specified fields for each document. Exactly one of `ids` or `filter` must be specified.

- `ids`: Fetch the documents with the given IDs.
- `filter`: Fetch every document matching a metadata filter expression. Results are returned a page at a time, holding `limit` documents per page (100 by default, 10000 at most). When there are more documents to return, the response includes a `pagination` token you can pass back as `pagination_token` to retrieve the next page. When no `pagination` token is returned, there are no more documents to fetch.

<Note>
  Text match operators (`$match_phrase`, `$match_all`, `$match_any`) aren't supported in a filtered fetch; they're only available in [search](/reference/api/2026-07/data-plane/search_documents).
</Note>

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  # Fetch by IDs
  response = index.documents.fetch(
      namespace=NAMESPACE,
      ids=["doc1", "doc2"],
      include_fields=["title", "body", "category"],
  )
  for doc_id, doc in response.documents.items():
      print(doc_id, getattr(doc, "title", ""))

  # Fetch by metadata filter, paging through all matches
  pagination_token = None
  while True:
      response = index.documents.fetch(
          namespace=NAMESPACE,
          filter={"category": {"$eq": "news"}},
          include_fields=["title", "body", "category"],
          pagination_token=pagination_token,
      )
      for doc_id, doc in response.documents.items():
          print(doc_id, getattr(doc, "title", ""))
      pagination = getattr(response, "pagination", None)
      if not pagination or not getattr(pagination, "next", None):
          break
      pagination_token = pagination.next
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"

  # EXAMPLE REQUEST 1: Fetch by IDs
  curl "https://$INDEX_HOST/namespaces/__default__/documents/fetch" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "ids": ["doc1", "doc2"],
      "include_fields": ["title", "body", "category"]
    }'

  # EXAMPLE REQUEST 2: Fetch by metadata filter
  curl "https://$INDEX_HOST/namespaces/__default__/documents/fetch" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "filter": { "category": { "$eq": "news" } },
      "include_fields": ["title", "body", "category"]
    }'
  ```
</RequestExample>
