---
title: "Indexing overview"
source: https://docs.pinecone.io/guides/index-data/indexing-overview
path: guides/index-data/indexing-overview
---

Learn how indexing works in Pinecone: serverless indexes, document schemas, namespaces, integrated embedding, and metadata filtering.

## Indexes

In Pinecone, you store data in indexes. A serverless index holds your data as [documents](/guides/get-started/concepts#document) or [records](/guides/get-started/concepts#record), depending on how the index was created: an index created with a document schema holds documents, while an index created with a dense or sparse vector type holds records. A single index with a document schema can mix multiple ranking field types: a `dense_vector` field for [semantic search](/guides/search/semantic-search), a `sparse_vector` field for [sparse-vector retrieval](/guides/search/lexical-search), and one or more `string` fields with `full_text_search` enabled for [full-text search](/guides/search/full-text-search) with BM25 and Lucene queries. Any other fields you upsert are stored as metadata, automatically indexed for filtering — no schema declaration required.

One index per use case is the typical pattern. Because a document can combine vectors, text, and metadata in the same record, a single index often covers what previously required two — pick the ranking signal per query with `score_by`.

### Full-text search

Full-text search is **BM25 token matching with Lucene query syntax** over text fields in your schema — `string` fields you've declared with `full_text_search` enabled. No model required — Pinecone handles tokenization, IDF, and length normalization at index time and BM25 scoring at query time.

When you search, you rank results via `score_by`: `text` (BM25), `query_string` (Lucene), `dense_vector`, or `sparse_vector`. All scoring methods can be combined with metadata filters, including the text match operators (`$match_phrase`, `$match_all`, `$match_any`) for phrase and token matching. For example:

```json theme={null}
{
  "score_by": [{ "type": "text", "field": "body", "query": "machine learning" }],
  "top_k": 10
}
```

Reach for full-text search when relevance comes down to specific tokens appearing in both the query and the data: SKUs, error messages, code, named entities. For semantic similarity over natural-language queries, see [Indexes with dense vectors](#indexes-with-dense-vectors); for retrieval with a learned sparse encoder, see [Indexes with sparse vectors](#indexes-with-sparse-vectors).

Learn more:

* [Full-text search guide](/guides/search/full-text-search)
* [Schema definition](/guides/search/full-text-search#schema-definition)
* [Upsert documents](/guides/search/full-text-search#upsert-documents)

### Indexes with dense vectors

A dense vector encodes the meaning of text, images, or other data as a fixed-length list of numbers. Items with similar meaning sit close to each other in vector space, and a query returns the records closest to the query vector. This is **semantic search** (also called nearest neighbor search, similarity search, or vector search).

For the underlying concept, see [Dense vector](/guides/get-started/concepts#dense-vector).

Learn more:

* [Create an index for dense vectors](/guides/index-data/create-an-index#create-an-index-for-dense-vectors)
* [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors)
* [Semantic search](/guides/search/semantic-search)

### Indexes with sparse vectors

A sparse vector represents tokens (or token-like features) and their weights, with the vast majority of dimensions zero. A query returns records that share the most weighted tokens with the query vector — **sparse-vector lexical search**.

Sparse vectors come from a sparse embedding model. Pinecone hosts [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0); you can also bring your own. For the underlying concept and the distinction from full-text search, see [Index with sparse vectors](/guides/get-started/concepts#index-with-sparse-vectors).

Learn more:

* [Create an index for sparse vectors](/guides/index-data/create-an-index#create-an-index-for-sparse-vectors)
* [Upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors)
* [Lexical search](/guides/search/lexical-search)

#### Limitations

Indexes of sparse vectors have the following limitations:

* Max non-zero values per sparse vector: 1000
* Max upserts per second per index of sparse vectors: 10
* Max queries per second per index of sparse vectors: 100
* Max `top_k` value per query: 1000

  <Note>
    You may get fewer than `top_k` results if `top_k` is larger than the number of sparse vectors in your index that match your query. That is, any vectors where the dotproduct score is `0` will be discarded.
  </Note>
* Max query results size: 4MB

<Tip>
  Semantic search can miss exact keyword matches, while lexical search can miss semantically related results. To get the best of both, use [hybrid search](/guides/search/hybrid-search) — combine a lexical signal (BM25 or sparse) with a dense signal at query time, often with reranking.
</Tip>

## Namespaces

Within an index, records are partitioned into namespaces, and all [upserts](/guides/index-data/upsert-data), [queries](/guides/search/search-overview), and other data read and write operations always target one namespace. This has two main benefits:

* **Multitenancy:** When you need to isolate data between customers, you can use one namespace per customer and target each customer's writes and queries to their dedicated namespace. See [Implement multitenancy](/guides/index-data/implement-multitenancy) for end-to-end guidance.

* **Faster queries:** When you divide records into namespaces in a logical way, you speed up queries by ensuring only relevant records are scanned. The same applies to fetching records, listing record IDs, and other data operations.

Namespaces are created automatically during [upsert](/guides/index-data/upsert-data). If a namespace doesn't exist, it is created implicitly.

<Note>
  [Namespaces per serverless index](/reference/api/database-limits#namespaces-per-serverless-index) vary by plan. On the Standard and Enterprise plans, Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

<img />

<img />

## Vector embedding

[Dense vectors](/guides/get-started/concepts#dense-vector) and [sparse vectors](/guides/get-started/concepts#sparse-vector) are the basic units of data in Pinecone and what Pinecone was specially designed to store and work with. Dense vectors represents the semantics of data such as text, images, and audio recordings, while sparse vectors represent documents or queries in a way that captures keyword information.

To transform data into vector format, you use an embedding model. You can either use Pinecone's integrated embedding models to convert your source data to vectors automatically, or you can use an external embedding model and bring your own vectors to Pinecone.

### Integrated embedding

1. [Create an index](/guides/index-data/create-an-index) that is integrated with one of Pinecone's [hosted embedding models](/guides/index-data/create-an-index#embedding-models).
2. [Upsert](/guides/index-data/upsert-data) your source text. Pinecone uses the integrated model to convert the text to vectors automatically.
3. [Search](/guides/search/search-overview) with a query text. Again, Pinecone uses the integrated model to convert the text to a vector automatically.

<Note>
  Indexes with integrated embedding do not support [updating](/guides/manage-data/update-data) or [importing](/guides/index-data/import-data) with text.
</Note>

### Bring your own vectors

1. Use an embedding model to convert your text to vectors. The model can be [hosted by Pinecone](/reference/api/latest/inference/generate-embeddings) or an external provider.
2. [Create an index](/guides/index-data/create-an-index) that matches the characteristics of the model.
3. [Upsert](/guides/index-data/upsert-data) your vectors directly.
4. Use the same external embedding model to convert a query to a vector.
5. [Search](/guides/search/search-overview) with your query vector directly.

## Data ingestion

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

There are two ways to ingest data into an index:

* [Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective way to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

* [Upserting](/guides/index-data/upsert-data) is intended for ongoing writes to an index. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records (up to 1000 per batch) if you cannot work around import's current limitations.

## Metadata

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a vector. In addition, you can include metadata key-value pairs to store additional information or context. When you query the index, you can then include a [metadata filter](/guides/search/filter-by-metadata) to limit the search to records matching a filter expression. Searches without metadata filters do not consider metadata and search the entire namespace.

### Metadata format

* Metadata fields must be key-value pairs in a flat JSON object. Nested JSON objects are not supported.
* Keys must be strings and must not start with a `$`.
* Values must be one of the following data types:
  * String
  * Integer (converted to a 64-bit floating point by Pinecone)
  * Floating point
  * Boolean (`true`, `false`)
  * List of strings
* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.

**Examples**

<CodeGroup>
  ```json Valid metadata theme={null}
  {
    "document_id": "document1",
    "document_title": "Introduction to Vector Databases",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content...",
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": ["85", "92"]
  }
  ```

  ```json Invalid metadata theme={null}
  {
    "document": {       // Nested JSON objects are not supported
      "document_id": "document1",
      "document_title": "Introduction to Vector Databases",
    },
    "$chunk_number": 1, // Keys must not start with a `$`
    "chunk_text": null, // Null values are not supported
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": [85, 92]  // Lists of non-strings are not supported
  }
  ```
</CodeGroup>

### Metadata size

Pinecone supports 40KB of metadata per record.

### Metadata filter expressions

Pinecone's filtering language supports the following operators:

| Operator  | Function                                                                                                                   | Supported types         |
| :-------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `$eq`     | Matches  with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}`            | Number, string, boolean |
| `$ne`     | Matches  with metadata values that are not equal to a specified value. Example: `{"genre": {"$ne": "drama"}}`              | Number, string, boolean |
| `$gt`     | Matches  with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}`                  | Number                  |
| `$gte`    | Matches  with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}`      | Number                  |
| `$lt`     | Matches  with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}`                     | Number                  |
| `$lte`    | Matches  with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}`        | Number                  |
| `$in`     | Matches  with metadata values that are in a specified array. Example: `{"genre": {"$in": ["comedy", "documentary"]}}`      | String, number          |
| `$nin`    | Matches  with metadata values that are not in a specified array. Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number          |
| `$exists` | Matches  with the specified metadata field. Example: `{"genre": {"$exists": true}}`                                        | Number, string, boolean |
| `$and`    | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`     | -                       |
| `$or`     | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`       | -                       |

<Note>
  Only `$and` and `$or` are allowed at the top level of the query expression.
</Note>

<Note>
  Each `$in` or `$nin` operator accepts a maximum of 10,000 values. Exceeding this limit will cause the request to fail. For more information, see [Metadata filter limits](/reference/api/database-limits#metadata-filter-limits).
</Note>

For example, the following has a `"genre"` metadata field with a list of strings:

```JSON JSON theme={null}
{ "genre": ["comedy", "documentary"] }
```

This means `"genre"` takes on both values, and requests with the following filters will match:

```JSON JSON theme={null}
{"genre":"comedy"}

{"genre": {"$in":["documentary","action"]}}

{"$and": [{"genre": "comedy"}, {"genre":"documentary"}]}
```

However, requests with the following filter will **not** match:

```JSON JSON theme={null}
{ "$and": [{ "genre": "comedy" }, { "genre": "drama" }] }
```

Additionally, requests with the following filters will **not** match because they are invalid. They will result in a compilation error:

```json JSON theme={null}
# INVALID QUERY:
{"genre": ["comedy", "documentary"]}
```

```json JSON theme={null}
# INVALID QUERY:
{"genre": {"$eq": ["comedy", "documentary"]}}
```
