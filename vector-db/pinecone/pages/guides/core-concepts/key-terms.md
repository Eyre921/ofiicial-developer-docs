---
title: "Pinecone key terms"
source: https://docs.pinecone.io/guides/core-concepts/key-terms
path: guides/core-concepts/key-terms
---

The key terms and objects in Pinecone and how they relate to each other.

This page defines the key terms and objects in Pinecone. For how these objects nest together, see [Architecture](/guides/core-concepts/architecture#resource-hierarchy).

## Account and billing

### Organization

An organization is a group of one or more [projects](#project) that use the same billing. Organizations allow one or more [users](/admin/organizations/manage-organization-members) to control billing and permissions for all of the projects belonging to the organization.

For more information, see [Organizations overview](/admin/organizations/understanding-organizations).

### Project

A project belongs to an [organization](#organization) and contains one or more [indexes](#index). Each project belongs to exactly one organization, but only [users](/admin/projects/manage-project-members) who belong to the project can access the indexes in that project. [API keys](#api-key) and [assistants](/guides/assistant/overview) are project-specific.

For more information, see [Projects overview](/admin/projects/understanding-projects).

### API key

An API key is a unique token that [authenticates](/reference/api/authentication) and authorizes access to the [Pinecone APIs](/reference/api/introduction). API keys are project-specific.

### Read unit (RU)

A read unit (RU) is the unit Pinecone uses to measure and price the cost of read requests to a serverless index, including [query](/guides/manage-cost/understanding-cost#query), [fetch](/guides/manage-cost/understanding-cost#fetch), and [list](/guides/manage-cost/understanding-cost#list).

For how read units are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost#read-units).

### Write unit (WU)

A write unit (WU) is the unit Pinecone uses to measure and price the cost of write requests to a serverless index, including [upsert](/guides/manage-cost/understanding-cost#upsert), [update](/guides/manage-cost/understanding-cost#update), and [delete](/guides/manage-cost/understanding-cost#delete).

For how write units are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost#write-units).

## Index

Pinecone [serverless indexes](/guides/index-data/indexing-overview) hold your data as [documents](#document) or [records](#record), depending on how the index was created. One index per use case is the typical pattern.

### Document index

A document index is an index created with a document schema. It holds [documents](#document) and is served by the Documents API. Because a document can combine vectors, text, and metadata, a single document index often covers what previously required two indexes. Pick the ranking signal per query with `score_by`.

### Vector index

A vector index is an index created with a dense or sparse vector type. It holds [records](#record) and is served by the Vectors API.

* In an index with dense vectors, each record has one [dense vector](#dense-vector). Records can also carry a [sparse vector](#sparse-vector) for single-index [hybrid search](/guides/search/hybrid-search/single-index).
* In an index with sparse vectors, each record has one sparse vector.

### Namespace

A namespace is a partition within an index. It divides [documents](#document) or [records](#record) into separate groups so that each query scans only one namespace (faster lookups) and each customer's data can be isolated from another customer's (multitenant isolation).

All [upserts](/guides/index-data/upsert-data), [queries](/guides/search/search-overview), and other data read and write operations always target one namespace.

For more information, see [Use namespaces](/guides/index-data/indexing-overview#namespaces).

### Backup

A backup is a static copy of an index, including its schema. Backups only consume storage and can't be queried. You can create a backup from an index, and you can create a new index from that backup. The new index inherits the source index's schema, so it has the same fields, dimensions, and similarity metric, but it can have a different name.

For more information, see [Understanding backups](/guides/manage-data/backups-overview).

## Data

### Document

A document is a JSON object with a required `_id` field, the ranking fields declared in the index's schema, and any number of metadata fields. It's the unit of data in a [document index](#document-index). A document can combine these ranking fields:

* `string` fields with `full_text_search` enabled, for [full-text search](#full-text-search).
* A `dense_vector` field, or a `string` field with `embed`, for [semantic search](#semantic-search).
* A `sparse_vector` field, or a `string` field with `sparse_embed`, for [sparse-vector search](#sparse-vector-search).

With `embed` and `sparse_embed`, Pinecone generates the vectors from your text using [integrated embedding](/guides/search/integrated-embedding). You choose the [scoring method](#scoring-methods) per query with `score_by`.

Documents are the recommended shape for new multi-field and full-text workloads. Vector-only indexes continue to use [records](#record). The Documents API and the Vectors API are both fully supported.

For more information, see [Full-text search](/guides/search/full-text-search).

#### Document fields

* **Schema limits**: Up to 100 `string` fields with `full_text_search` enabled, at most one dense field (a `dense_vector` field or a `string` field with `embed`), and at most one sparse field (a `sparse_vector` field or a `string` field with `sparse_embed`) per index.
* **Value shapes**: A `dense_vector` field holds an array of floats. A `sparse_vector` field is an object with two parallel arrays, `indices` (token positions) and `values` (token weights). A metadata `string_list` field holds an array of strings.
* **Metadata fields**: Any field on an upserted document that's not declared in the schema is stored, returned via `include_fields`, and automatically indexed for filtering. Pinecone infers metadata field types (string, number, boolean, array of strings) from the values you upsert.
* **Field names**: Names must be unique, non-empty strings of 64 bytes or less. They can't start with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators).

### Record

A record is the unit of data in a [vector index](#vector-index). It contains:

* A [record ID](#record-id).
* One vector, or a dense and a sparse vector for single-index [hybrid search](/guides/search/hybrid-search).
* Optional [metadata](#metadata).

In a [legacy integrated index](/guides/index-data/indexing-overview#integrated-embedding) created with `create_index_for_model`, you can upsert raw text instead of a vector, and Pinecone embeds it at index time. When an item has more than one searchable field, such as a text field ranked by BM25 and a `dense_vector` field for similarity, model it as a [document](#document).

For more information, see [Upsert data](/guides/index-data/upsert-data).

#### Record ID

A record ID is a record's unique ID. [Use ID prefixes](/guides/index-data/data-modeling#use-structured-ids) that reflect the type of data you're storing.

### Dense vector

A dense vector, also referred to as a vector embedding or simply a vector, is a series of numbers that represent the meaning and relationships of data. Each vector is a point in a multidimensional space, and each number is a coordinate in that space. Vectors that are closer together in that space are semantically similar.

Dense vectors power [semantic search](#semantic-search).

You use a dense embedding model to convert data to dense vectors. The embedding model can be external to Pinecone or [hosted on Pinecone infrastructure](/guides/index-data/index-configuration#embedding-models) and integrated with an index.

For more information about dense vectors, see [What are vector embeddings?](https://www.pinecone.io/learn/vector-embeddings/).

### Sparse vector

Sparse vectors are often used to represent documents or queries in a way that captures keyword information. Each dimension in a sparse vector typically represents a word from a dictionary, and the non-zero values represent the importance of these words in the document.

Sparse vectors have a large number of dimensions, but a small number of those values are non-zero. Because most values are zero, Pinecone stores sparse vectors efficiently by keeping only the non-zero values along with their corresponding indices.

Sparse vectors power [sparse-vector search](#sparse-vector-search), and they can coexist with dense vectors in a single vector index for [hybrid search](/guides/search/hybrid-search/single-index) on the Vectors API. To convert data to sparse vectors, use a sparse embedding model. The embedding model can be external to Pinecone or [hosted on Pinecone infrastructure](/guides/index-data/index-configuration#embedding-models) and integrated with an index.

For more information about sparse vectors, see [Sparse retrieval](https://www.pinecone.io/learn/sparse-retrieval/).

### Metadata

Metadata is additional information included in a document or record to provide more context and enable additional [filtering capabilities](/guides/index-data/indexing-overview#metadata). For example, the original text that was embedded can be stored in the metadata.

## Search

### Full-text search

Full-text search ranks documents by BM25 token matching, with optional Lucene query syntax, over `string` fields declared with `full_text_search`. These are often called text fields. Full-text search doesn't need a model.

* **At index time**: Pinecone tokenizes text and records term frequencies and field lengths.
* **At query time**: Pinecone computes BM25 scores, including inverse document frequency (IDF).
* **Tokens**: A token is a unit produced by Pinecone's text analyzer (split on whitespace and punctuation, lowercased by default, and optionally stemmed), not the subword unit an embedding model uses internally. See [Tokens and analyzers](/guides/search/full-text-search/text-processing#tokens-and-analyzers) for the full pipeline.

Use full-text search for keyword and phrase search over text content — product names, identifiers, technical terms, code, and other cases where queries and documents share specific tokens.

For more information, see [Full-text search](/guides/search/full-text-search).

### Semantic search

When you search with a [dense vector](#dense-vector), Pinecone retrieves the documents or records whose dense vectors are most semantically similar to the query. This is also called nearest neighbor search, similarity search, or vector search.

### Sparse-vector search

When you search with a [sparse vector](#sparse-vector), Pinecone retrieves the documents or records whose sparse vectors share the most weighted tokens with the query vector. This is also called sparse-vector retrieval.

Sparse vectors are produced by a sparse embedding model. Pinecone hosts [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0), a learned-sparse encoder that predicts per-token weights and includes term expansion (related concepts that don't appear in the source text). You can also bring your own sparse model.

Sparse-vector search and [full-text search](#full-text-search) both retrieve on token-level signals, but they weight tokens differently:

* **Full-text search**: Uses BM25, a statistical function with no model. Use it when you want a strong baseline with nothing to manage.
* **Sparse-vector search**: Uses a learned encoder that weights tokens at index time and can expand to related terms. Use it when a learned encoder better captures your domain's term importance and synonyms.

### Scoring methods

On a document index, you choose a scoring method per query with `score_by`. The value of `type` selects the method:

* `text`: BM25 token matching over one or more text fields.
* `query_string`: [Lucene query syntax](/guides/search/full-text-search/query-syntax) across one or more text fields, including cross-field boolean queries.
* `dense_vector`: Vector similarity.
* `sparse_vector`: Sparse-vector similarity.
* `embed`: Vector similarity, with Pinecone embedding the query text using the field's `embed` model.
* `sparse_embed`: Sparse-vector similarity, with Pinecone embedding the query text using the field's `sparse_embed` model.

You can combine several `text` and `query_string` clauses in one query. Any other type must be the only clause. To combine a keyword signal with a dense signal, restrict a dense search with a text-match [filter](#metadata-filters), or run separate searches and merge the results client-side.

### Metadata filters

You can combine any scoring method with a metadata filter. Filters support:

* **Logical operators**: `$and`, `$or`, and `$not`.
* **Existence checks**: `$exists`.
* **Text-match operators**: `$match_phrase`, `$match_all`, and `$match_any` match phrases and tokens in text fields.

For more information, see [Metadata filter expressions](/guides/index-data/indexing-overview#metadata-filter-expressions).

### Standalone embedding and reranking

Standalone embedding and reranking let you call [embedding models](/guides/index-data/index-configuration#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone's infrastructure directly, separately from index operations.
