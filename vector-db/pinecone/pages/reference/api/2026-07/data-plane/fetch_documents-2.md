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
  Text-match operators (`$match_phrase`, `$match_all`, `$match_any`) are supported in a filtered fetch, as they are in [search](/reference/api/2026-07/data-plane/search_documents). A filtered [update](/reference/api/2026-07/data-plane/update_documents) or [delete](/reference/api/2026-07/data-plane/delete_documents) rejects them with a `400`.
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

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';

  // Reads PINECONE_API_KEY from the environment
  const pc = new Pinecone();

  const index = pc.index({
    name: 'articles',
    namespace: 'example-namespace',
  });

  // Fetch by IDs
  const response = await index.documents.fetch({
    ids: ['doc1', 'doc2'],
    includeFields: ['title', 'body', 'category'],
  });
  for (const [id, doc] of Object.entries(response.documents)) {
    console.log(id, doc.title);
  }

  // Fetch by metadata filter, paging through all matches
  let paginationToken;
  do {
    const page = await index.documents.fetch({
      filter: {
        category: {
          $eq: 'news',
        },
      },
      includeFields: ['title', 'body', 'category'],
      paginationToken,
    });
    for (const [id, doc] of Object.entries(page.documents)) {
      console.log(id, doc.title);
    }
    paginationToken = page.pagination?.next;
  } while (paginationToken);
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"
      "os"

      "github.com/pinecone-io/go-pinecone/v7/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: os.Getenv("PINECONE_API_KEY"),
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      idx, err := pc.DescribeIndex(ctx, "articles")
      if err != nil {
          log.Fatalf("Failed to describe index: %v", err)
      }

      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
          Host:      idx.Host,
          Namespace: "example-namespace",
      })
      if err != nil {
          log.Fatalf("Failed to create IndexConnection: %v", err)
      }

      // Fetch by IDs
      res, err := idxConnection.FetchDocuments(ctx, &pinecone.FetchDocumentsRequest{
          Ids:           []string{"doc1", "doc2"},
          IncludeFields: []string{"title", "body", "category"},
      })
      if err != nil {
          log.Fatalf("Failed to fetch documents: %v", err)
      }
      for id, doc := range res.Documents {
          fmt.Println(id, doc["title"])
      }

      // Fetch by metadata filter, paging through all matches
      var paginationToken *string
      for {
          res, err := idxConnection.FetchDocuments(ctx, &pinecone.FetchDocumentsRequest{
              Filter: map[string]interface{}{
                  "category": map[string]interface{}{
                      "$eq": "news",
                  },
              },
              IncludeFields:   []string{"title", "body", "category"},
              PaginationToken: paginationToken,
          })
          if err != nil {
              log.Fatalf("Failed to fetch documents: %v", err)
          }
          for id, doc := range res.Documents {
              fmt.Println(id, doc["title"])
          }
          if res.Pagination == nil || res.Pagination.Next == "" {
              break
          }
          paginationToken = &res.Pagination.Next
      }
  }
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
