---
title: "Search documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/search_documents
path: reference/api/2026-07/data-plane/search_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/search
Search for documents in a namespace using one or more scoring methods (dense vector, sparse vector, text, or query string similarity).

Returns the top-k most similar documents along with their scores and requested fields.

A request includes a `score_by` array selecting one of the following scoring types:

* **`type: "text"`**, BM25 token matching over one or more text fields named in `fields`; naming several scores the query against all of them. Multi-word queries use OR-style matching (case-insensitive). For exact-phrase ranking, use `query_string` with quoted terms.
* **`type: "query_string"`**, Lucene query syntax. Supports boolean operators, phrase prefix matching, boosting, fuzzy matching (`term~`, `term~N`), and cross-field queries. See the [query syntax reference](/guides/search/full-text-search/query-syntax). **Does not accept a `field` or `fields` parameter.** Target specific fields using Lucene field qualifiers in the query string itself: `fieldname:value` or `title:(alpha) OR body:(beta)`.
* **`type: "dense_vector"`**, dense vector similarity ranking against a `dense_vector` field.
* **`type: "sparse_vector"`**, sparse vector similarity ranking against a `sparse_vector` field.

Any scoring method can be combined with metadata filters (including text match operators `$match_phrase` / `$match_all` / `$match_any` and logical operators `$and` / `$or` / `$not`). Filters are applied **before** scoring: the search only considers documents that match the filter. Scoring-only operators are available in `query_string` scoring but cannot be used inside `filter`: phrase slop (`"phrase"~N`), term boosting (`^N`), and phrase prefix (`"phrase pre"*`).

`include_fields` defaults to `[]` (returns only `_id` and `_score`); use `["*"]` to return all stored fields.

<Note>
  A single search request ranks by one scoring type. Multi-field BM25 is supported: name several fields in one `text` clause's `fields` array, or pass multiple `text` clauses, which the server combines into one ranking; a `query_string` clause can also target several fields. Every contributing field weighs equally in `2026-07`; there is no per-field weight parameter. To combine BM25 ranking with `dense_vector` or `sparse_vector` ranking, restrict the dense (or sparse) search with a text-match filter (`$match_phrase`, `$match_all`, `$match_any`) on the full-text field, or run separate searches and merge the results client-side.
</Note>

<Warning>
  Text-match operators (`$match_phrase`, `$match_all`, `$match_any`) are supported on this endpoint and on [fetch](/reference/api/2026-07/data-plane/fetch_documents). A filtered [update](/reference/api/2026-07/data-plane/update_documents) or [delete](/reference/api/2026-07/data-plane/delete_documents) rejects them with a `400` and accepts plain metadata filters only. To update or delete by text match, search or fetch for the matching IDs first, then act on those IDs.
</Warning>

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  index = pc.Index(name="articles")

  NAMESPACE = "example-namespace"

  # BM25 token matching
  response = index.documents.search(
      namespace=NAMESPACE,
      top_k=10,
      score_by=[{"type": "text", "fields": ["body"], "query": "machine learning"}],
      include_fields=["title", "body", "category", "year"],
  )
  for match in response.matches:
      print(match._id, match._score, getattr(match, "title", ""))

  # Lucene query string
  response = index.documents.search(
      namespace=NAMESPACE,
      top_k=10,
      score_by=[{"type": "query_string", "query": "title:(quantum) OR body:(machine learning)"}],
      include_fields=["title", "body"],
  )

  # Dense vector ranking with phrase-match filter
  query_vector = [0.12, 0.34, 0.56]  # replace with your actual query vector
  response = index.documents.search(
      namespace=NAMESPACE,
      top_k=10,
      score_by=[{
          "type": "dense_vector",
          "fields": ["embedding"],
          "values": query_vector,
      }],
      filter={"body": {"$match_phrase": "machine learning"}},
      include_fields=["title", "body"],
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

  // BM25 token matching
  let response = await index.documents.search({
    topK: 10,
    scoreBy: [
      {
        type: 'text',
        fields: ['body'],
        query: 'machine learning',
      },
    ],
    includeFields: ['title', 'body', 'category', 'year'],
  });
  for (const match of response.matches) {
    console.log(match._id, match._score, match.title);
  }

  // Lucene query string
  response = await index.documents.search({
    topK: 10,
    scoreBy: [
      {
        type: 'query_string',
        query: 'title:(quantum) OR body:(machine learning)',
      },
    ],
    includeFields: ['title', 'body'],
  });

  // Dense vector ranking with phrase-match filter
  const queryVector = [0.12, 0.34, 0.56]; // replace with your actual query vector
  response = await index.documents.search({
    topK: 10,
    scoreBy: [
      {
        type: 'dense_vector',
        fields: ['embedding'],
        values: queryVector,
      },
    ],
    filter: {
      body: {
        $match_phrase: 'machine learning',
      },
    },
    includeFields: ['title', 'body'],
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

      // BM25 token matching
      textQuery := "machine learning"
      res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
          TopK: 10,
          ScoreBy: []pinecone.DocumentScoringMethod{
              {
                  Type:   "text",
                  Fields: []string{"body"},
                  Query:  &textQuery,
              },
          },
          IncludeFields: []string{"title", "body", "category", "year"},
      })
      if err != nil {
          log.Fatalf("Failed to search documents: %v", err)
      }
      for _, match := range res.Matches {
          fmt.Print(match.Id)
          if match.Score != nil {
              fmt.Printf(" %.3f", *match.Score)
          }
          fmt.Printf(" %v\n", match.Fields["title"])
      }

      // Lucene query string
      queryString := "title:(quantum) OR body:(machine learning)"
      res, err = idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
          TopK: 10,
          ScoreBy: []pinecone.DocumentScoringMethod{
              {
                  Type:  "query_string",
                  Query: &queryString,
              },
          },
          IncludeFields: []string{"title", "body"},
      })
      if err != nil {
          log.Fatalf("Failed to search documents: %v", err)
      }

      // Dense vector ranking with phrase-match filter
      queryVector := []float32{0.12, 0.34, 0.56} // replace with your actual query vector
      res, err = idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
          TopK: 10,
          ScoreBy: []pinecone.DocumentScoringMethod{
              {
                  Type:   "dense_vector",
                  Fields: []string{"embedding"},
                  Values: &queryVector,
              },
          },
          Filter: map[string]interface{}{
              "body": map[string]interface{}{
                  "$match_phrase": "machine learning",
              },
          },
          IncludeFields: []string{"title", "body"},
      })
      if err != nil {
          log.Fatalf("Failed to search documents: %v", err)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"

  # EXAMPLE REQUEST 1: BM25 token matching (type: "text")
  curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "include_fields": ["title", "body", "category", "year"],
      "score_by": [{
        "type": "text",
        "fields": ["body"],
        "query": "machine learning"
      }],
      "top_k": 10
    }'

  # EXAMPLE REQUEST 2: Cross-field boolean query (type: "query_string")
  curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "include_fields": ["title", "body"],
      "score_by": [{
        "type": "query_string",
        "query": "title:(quantum) OR body:(machine learning)"
      }],
      "top_k": 10
    }'

  # EXAMPLE REQUEST 3: Dense vector ranking with phrase-match filter
  curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "include_fields": ["title", "body"],
      "filter": { "body": { "$match_phrase": "machine learning" } },
      "score_by": [{
        "type": "dense_vector",
        "fields": ["embedding"],
        "values": [0.12, 0.34, 0.56]
      }],
      "top_k": 10
    }'

  # EXAMPLE REQUEST 4: Sparse vector ranking
  curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "include_fields": ["title", "body"],
      "score_by": [{
        "type": "sparse_vector",
        "fields": ["sparse_embedding"],
        "sparse_values": {
          "indices": [12, 287, 4096],
          "values": [0.41, 0.33, 0.18]
        }
      }],
      "top_k": 10
    }'

  # EXAMPLE REQUEST 5: Compound filter ($and + $match_all + metadata)
  curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "include_fields": ["body", "category", "year"],
      "filter": {
        "$and": [
          { "body": { "$match_all": "federal reserve" } },
          { "category": { "$eq": "finance" } },
          { "year": { "$gte": 2024 } }
        ]
      },
      "score_by": [{
        "type": "text",
        "fields": ["body"],
        "query": "monetary policy impact"
      }],
      "top_k": 10
    }'
  ```
</RequestExample>
