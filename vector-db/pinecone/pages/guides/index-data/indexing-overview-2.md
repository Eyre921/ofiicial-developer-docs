---
title: "Indexing overview"
source: https://docs.pinecone.io/guides/index-data/indexing-overview
path: guides/index-data/indexing-overview
---

Learn how indexing works in Pinecone: serverless indexes, schemas, namespaces, integrated embedding, and metadata filtering.

## Indexes

In Pinecone, you store data in an index, typically one per use case. Every index is defined by a **schema** that declares its fields. What the schema can hold, and which API reads and writes the index, is set when you create it. There are two kinds: new indexes are document indexes by default, and vector indexes remain fully supported.

### Document index

You define a `schema` with `pc.indexes.create` (or `POST /indexes`).

* One schema can combine `dense_vector`, `sparse_vector`, and `full_text_search`-enabled `string` fields.
* A single index can serve [full-text search](/guides/search/full-text-search) (BM25 with Lucene queries), [semantic search](/guides/search/semantic-search), and [sparse-vector search](/guides/search/lexical-search) together, often covering what previously required two indexes.
* Holds [documents](/guides/core-concepts/key-terms#document), read and written through the Documents API. Pick the ranking signal per query with `score_by`.

### Vector index

Created with `pc.create_index(dimension=..., metric=..., vector_type=...)`. You don't declare fields yourself; the SDK builds the schema from the dimension, metric, and vector type you provide.

* Holds [records](/guides/core-concepts/key-terms#record), read and written through the Vectors API.
* Serves [semantic search](/guides/search/semantic-search) and [sparse-vector search](/guides/search/lexical-search).

<Note>
  As of API version `2026-07`, `POST /indexes` in the REST API is schema-only. The SDKs still accept `dimension`, `metric`, and `vector_type` and create a vector index. Existing indexes keep working unchanged on the API they were created with. See [Adopt the Documents API](/guides/index-data/adopt-the-documents-api) for what changed and whether it affects your code.
</Note>

## Search approaches

How you rank results depends on the fields your index declares.

### Full-text search

Full-text search is **BM25 token matching with Lucene query syntax** over text fields in your schema, `string` fields you've declared with `full_text_search` enabled. No model required: Pinecone handles tokenization, IDF, and length normalization at index time and BM25 scoring at query time.

When you search, you rank results via `score_by`: `text` (BM25), `query_string` (Lucene), `dense_vector`, or `sparse_vector`. All scoring methods can be combined with metadata filters, including the text match operators (`$match_phrase`, `$match_all`, `$match_any`) for phrase and token matching. For example:

```json theme={null}
{
  "score_by": [{ "type": "text", "fields": ["body"], "query": "machine learning" }],
  "top_k": 10
}
```

Reach for full-text search when relevance comes down to specific tokens appearing in both the query and the data, such as SKUs, error messages, code, and named entities. For semantic similarity over natural-language queries, see [Semantic search](#semantic-search). For retrieval with a learned sparse encoder, see [Sparse-vector search](#sparse-vector-search).

Learn more:

* [Full-text search guide](/guides/search/full-text-search)
* [Schema definition](/guides/search/full-text-search#schema-definition)
* [Upsert documents](/reference/api/latest/data-plane/upsert_documents)

### Semantic search

A dense vector encodes the meaning of text, images, or other data as a fixed-length list of numbers. Items with similar meaning sit close to each other in vector space, and a query returns the records closest to the query vector. This is **semantic search** (also called nearest neighbor search, similarity search, or vector search).

For the underlying concept, see [Dense vector](/guides/core-concepts/key-terms#dense-vector).

Learn more:

* [Create an index for dense vectors](/guides/index-data/create-an-index#create-an-index-for-dense-vectors)
* [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors)
* [Semantic search](/guides/search/semantic-search)

### Sparse-vector search

A sparse vector represents tokens (or token-like features) and their weights, with the vast majority of dimensions zero. A query returns records that share the most weighted tokens with the query vector, which is called **sparse-vector search**.

Sparse vectors come from a sparse embedding model. Pinecone hosts [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0); you can also bring your own. For the underlying concept and the distinction from full-text search, see [Index with sparse vectors](/guides/core-concepts/key-terms#index-with-sparse-vectors).

Learn more:

* [Create an index for sparse vectors](/guides/index-data/create-an-index#create-an-index-for-sparse-vectors)
* [Upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors)
* [Sparse-vector search](/guides/search/lexical-search)

#### Limitations

Indexes of sparse vectors have the following limitations:

* Max non-zero values per sparse vector: 2048
* Max upserts per second per index of sparse vectors: 10
* Max queries per second per index of sparse vectors: 100
* Max `top_k` value per query: 10,000

  <Note>
    You may get fewer than `top_k` results if `top_k` is larger than the number of sparse vectors in your index that match your query. That is, any vectors where the dotproduct score is `0` will be discarded.
  </Note>
* Max query results size: 4 MB

<Tip>
  Semantic search can miss exact keyword matches, while keyword search can miss semantically related results. To get the best of both, use [hybrid search](/guides/search/hybrid-search) — combine a keyword signal (BM25 or sparse) with a dense signal at query time, often with reranking.
</Tip>

## Namespaces

Within an index, records or documents are partitioned into namespaces, and all [upserts](/guides/index-data/upsert-data), [queries](/guides/search/search-overview), and other data read and write operations always target one namespace. This has two main benefits:

* **Multitenancy:** When you need to isolate data between customers, you can use one namespace per customer and target each customer's writes and queries to their dedicated namespace. See [Implement multitenancy](/guides/index-data/implement-multitenancy) for end-to-end guidance.

* **Faster queries:** When you divide your data into namespaces in a logical way, you speed up queries by ensuring only relevant records or documents are scanned. The same applies to fetching them, listing their IDs, and other data operations.

Namespaces are created automatically during [upsert](/guides/index-data/upsert-data). If a namespace doesn't exist, it's created implicitly.

<Note>
  [Namespaces per serverless index](/reference/api/database-limits/object-limits) vary by plan. On the Standard and Enterprise plans, Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

<img />

<img />

## Vector embedding

A schema declares the vector fields your index uses: a [dense vector](/guides/core-concepts/key-terms#dense-vector) field, a [sparse vector](/guides/core-concepts/key-terms#sparse-vector) field, or both. Dense vectors represent the semantics of data such as text, images, and audio; sparse vectors capture keyword information.

To turn your source data into vectors, you use an embedding model. You can either use Pinecone's integrated embedding models to convert your data to vectors automatically, or use an external embedding model and bring your own vectors to Pinecone.

### Integrated embedding

Integrated-embedding indexes are created with `pc.create_index_for_model` and read and written through the Records API. Pinecone generates the vectors from your text automatically, both when you upsert and when you search.

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

* [Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective way to load large numbers of records or documents into an index. You store your data in object storage (Parquet for vector indexes, [JSON Lines (JSONL)](https://jsonlines.org/) for document indexes), integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your data.

* [Upserting](/guides/index-data/upsert-data) is intended for ongoing writes to an index. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records or documents (up to 1000 per batch) if you can't work around import's current limitations.

## Metadata

Every record has an ID and a vector, and every document has an `_id` and the fields its schema declares. Either can also carry metadata: extra key-value fields you filter on at query time. In a vector index, you pass metadata as an explicit object with each vector. With integrated embedding or in a document index, extra fields you upsert are stored as metadata automatically. Pinecone indexes metadata for filtering, so a query can include a [metadata filter](/guides/search/filter-by-metadata) to limit the search. Searches without a metadata filter don't consider metadata and search the entire namespace.

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

Pinecone supports 40 KB of metadata per record or document. `full_text_search` string fields aren't metadata and don't count toward this limit. Each `full_text_search` string field is limited to 100 KB and 10,000 tokens.

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
| `$not`    | Matches  that do not match the wrapped clause. Example: `{"genre": {"$not": {"$eq": "drama"}}}`                            | -                       |

<Note>
  At the top level, list one or more fields (combined with implicit AND) or combine clauses with the logical operators `$and` and `$or`. Use `$not` to negate a clause, as shown in the table. A bare comparison operator (like `$gt`) can't appear at the top level; nest it under a field.
</Note>

<Note>
  Each `$in` or `$nin` operator accepts a maximum of 10,000 values. Exceeding this limit will cause the request to fail. For more information, see [Metadata filter limits](/reference/api/database-limits/operation-limits#metadata-filter-limits).
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
