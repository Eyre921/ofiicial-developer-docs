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

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone';

  // Reads PINECONE_API_KEY from the environment
  const pc = new Pinecone();

  const index = pc.index({
    name: 'articles',
    namespace: 'example-namespace',
  });

  // Delete by IDs
  await index.documents.delete({
    ids: ['doc1', 'doc2'],
  });

  // Delete by metadata filter
  const response = await index.documents.delete({
    filter: {
      category: {
        $eq: 'news',
      },
    },
  });
  console.log(`Matched ${response.matchedRecords} documents`);

  // Delete every document in the namespace
  await index.documents.delete({
    deleteAll: true,
  });
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

      // Delete by IDs
      _, err = idxConnection.DeleteDocuments(ctx, &pinecone.DeleteDocumentsRequest{
          Ids: []string{"doc1", "doc2"},
      })
      if err != nil {
          log.Fatalf("Failed to delete documents: %v", err)
      }

      // Delete by metadata filter
      res, err := idxConnection.DeleteDocuments(ctx, &pinecone.DeleteDocumentsRequest{
          Filter: map[string]interface{}{
              "category": map[string]interface{}{
                  "$eq": "news",
              },
          },
      })
      if err != nil {
          log.Fatalf("Failed to delete documents: %v", err)
      }
      if res.MatchedRecords != nil {
          fmt.Printf("Matched %d documents\n", *res.MatchedRecords)
      }

      // Delete every document in the namespace
      _, err = idxConnection.DeleteDocuments(ctx, &pinecone.DeleteDocumentsRequest{
          DeleteAll: true,
      })
      if err != nil {
          log.Fatalf("Failed to delete documents: %v", err)
      }
  }
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
