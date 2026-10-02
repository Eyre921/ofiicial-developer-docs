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
      remove_fields=["year"],
  )
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

  // Patch specific documents by ID
  await index.documents.update({
    documents: [
      {
        _id: 'doc1',
        title: 'Updated title',
      },
      {
        _id: 'doc2',
        _remove_fields: ['content'], // Reserved document key, sent as-is
      },
    ],
  });

  // Apply the same patch to every document matching a metadata filter
  const response = await index.documents.update({
    filter: {
      category: {
        $eq: 'news',
      },
    },
    setFields: {
      category: 'archive',
    },
    removeFields: ['year'],
  });
  console.log(`Matched ${response.matchedRecords} documents`);
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

      // Patch specific documents by ID
      _, err = idxConnection.UpdateDocuments(ctx, &pinecone.UpdateDocumentsRequest{
          Documents: []pinecone.Document{
              {
                  "_id":   "doc1",
                  "title": "Updated title",
              },
              {
                  "_id":            "doc2",
                  "_remove_fields": []string{"content"},
              },
          },
      })
      if err != nil {
          log.Fatalf("Failed to update documents: %v", err)
      }

      // Apply the same patch to every document matching a metadata filter
      res, err := idxConnection.UpdateDocuments(ctx, &pinecone.UpdateDocumentsRequest{
          Filter: map[string]interface{}{
              "category": map[string]interface{}{
                  "$eq": "news",
              },
          },
          SetFields: map[string]interface{}{
              "category": "archive",
          },
          RemoveFields: []string{"year"},
      })
      if err != nil {
          log.Fatalf("Failed to update documents: %v", err)
      }
      if res.MatchedRecords != nil {
          fmt.Printf("Matched %d documents\n", *res.MatchedRecords)
      }
  }
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
      "remove_fields": ["year"]
    }'
  ```
</RequestExample>
