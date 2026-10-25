---
title: "Data modeling"
source: https://docs.pinecone.io/guides/index-data/data-modeling
path: guides/index-data/data-modeling
---

Model data in Pinecone as documents in a document index or records in a vector index, choose a document schema, and plan IDs and metadata.

Pinecone stores your data as [documents](#documents) in a document index or as [records](#records) in a vector index, and you choose when you create the index. Use documents, the default, for new projects, full-text search, integrated embedding, or any workload that needs more than one ranking signal. Use records for vector-only workloads where you generate the vectors yourself.

> [!TIP]
>
> Deciding how tenants share indexes and namespaces? See [Design for multitenancy](/guides/index-data/design-for-multitenancy).

## Documents

A document is a JSON object in a document index, read and written through the Documents API. It has a required `_id`, values for the ranking fields declared in the index's schema, and any number of metadata fields. At query time, you choose which ranking field to search with `score_by`.

You declare the schema when you create the index, and you can't change it afterward. The schema supports these ranking field types:

* `string` with `full_text_search`: Indexed for [full-text search](/guides/search/full-text-search) with BM25 ranking and Lucene queries. `{}` uses the defaults, and the optional settings are `language`, `stemming`, `stop_words`, and `ngram`. Lowercasing and the token length cap are server-applied and can't be changed.
* `string` with `embed` (dense) or `sparse_embed` (learned-sparse): Uses [integrated embedding](/guides/search/integrated-embedding). Pinecone embeds the text with a hosted model on write and embeds the query text at search time, so you upsert and search with plain text. The stored text is also full-text searchable by default.
* `dense_vector`: An array of floats from your embedding model, indexed for approximate nearest neighbor (ANN) [semantic search](/guides/search/semantic-search).
* `sparse_vector`: An object with parallel `indices` (token positions) and `values` (token weights) arrays, indexed for [sparse-vector search](/guides/search/sparse-vector-search).

A schema can declare up to 100 full-text-searchable `string` fields, counting `embed` and `sparse_embed` fields that store their text, but at most one dense field (`dense_vector`, or a `string` field with `embed`) and one sparse field (`sparse_vector`, or a `string` field with `sparse_embed`).

Fields you don't declare in the schema are metadata. Pinecone stores them on the document, returns them via `include_fields`, and indexes them for filtering. For supported types and limits, see [Include metadata](#include-metadata).

For example, in an index whose schema declares `title` and `body` as full-text-search fields and `embedding` as a `dense_vector`, a document with a `category` metadata field looks like this:

```json theme={null}
{
  "_id": "document1#chunk1",
  "title": "Introduction to Vector Databases",
  "body": "First chunk of the document content...",
  "embedding": [0.0236, -0.0329, ..., -0.0104, 0.0086],
  "category": "tutorial"
}
```

Field names must be unique, non-empty, and at most 64 bytes. They can't start with `_` (reserved for system fields like `_id` and `_score`) or `$` (reserved for filter operators).

> [!NOTE]
>
> Pinecone scores and returns whole documents: `top_k` and `_score` apply per document, and Pinecone doesn't split a document into chunks. To retrieve parts of long content such as articles, PDFs, or transcripts, chunk it in your application before upsert and store each chunk as its own document, as shown in [Manage document chunks](/guides/manage-data/manage-document-chunks).

### Choose a schema

| To rank by | Declare | Guide |
| - | - | - |
| Keyword relevance (BM25) | One or more `string` fields with `full_text_search` | [Full-text search overview](/guides/search/full-text-search) |
| Meaning, with Pinecone generating the vectors | A `string` field with `embed` or `sparse_embed` | [Integrated embedding](/guides/search/integrated-embedding) |
| Your own dense or sparse vectors | A `dense_vector` or `sparse_vector` field | [Search with a dense vector](/guides/search/semantic-search#search-with-a-dense-vector), [Sparse-vector search](/guides/search/sparse-vector-search) |
| Keyword and semantic signals together | A dense field and `string` fields with `full_text_search` | [Hybrid search overview](/guides/search/hybrid-search) |

### Schema validation

Pinecone validates each document in an [upsert](/reference/api/latest/data-plane/upsert_documents) request against the schema. If any document fails, the whole request fails and nothing is written.

| Scenario | Result |
| - | - |
| A value doesn't match its schema field's declared type | Error |
| A document or request exceeds a size or count limit | Error |
| A field name starts with `_` or `$` | Error |
| A document is missing `_id` | Error |
| A document is missing a `dense_vector` field, or a `string` field with `embed`, that the schema declares | Error |
| A document has no schema fields, only `_id` and metadata | Error |
| A document is missing any other schema field | OK |
| A field isn't in the schema | Stored as metadata and indexed for filtering |

## Records

Records are the unit of data in a [vector index](/guides/index-data/create-an-index#create-a-vector-index), read and written through the Vectors API. You generate the vectors with an embedding model of your choice. Each record has these parts:

* **ID**: A unique string identifier.
* **Vector**: A dense vector for [semantic search](/guides/search/semantic-search), a sparse vector for [sparse-vector search](/guides/search/sparse-vector-search), or both for [hybrid search](/guides/search/hybrid-search) in a single index.
* **Metadata** (optional): Flat key-value pairs (nested objects aren't supported) that you can filter on when searching or deleting. See [Include metadata](#include-metadata).

```json Dense theme={null}
{
  "id": "document1#chunk1",
  "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875],
  "metadata": {
    "document_id": "document1",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content..."
  }
}
```

```json Sparse theme={null}
{
  "id": "document1#chunk1",
  "sparse_values": {
    "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
    "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
  },
  "metadata": {
    "document_id": "document1",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content..."
  }
}
```

```json Hybrid theme={null}
{
  "id": "document1#chunk1",
  "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875],
  "sparse_values": {
    "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
    "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
  },
  "metadata": {
    "document_id": "document1",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content..."
  }
}
```

To [import records from object storage](/guides/index-data/import-data#3-prepare-your-data), format them as Parquet.

> [!NOTE]
>
> A legacy integrated index, created with `create_index_for_model` and served by the Records API, also accepts records with raw text in place of a vector. For new projects, use a document index with [integrated embedding](/guides/search/integrated-embedding) instead, which can combine embedding and full-text search on the same field.

## Use structured IDs

Give IDs a structured, human-readable format, with prefixes that reflect the data, for example:

* **Document chunks**: `document_id#chunk_number`
* **User data**: `user_id#data_type#item_id`
* **Multitenant data**: `tenant_id#document_id#chunk_id`

Use a delimiter that doesn't appear elsewhere in your IDs, such as `#`, `_`, or `:`. Prefixes let you [fetch every chunk of a source document](/guides/manage-data/manage-document-chunks#fetch-all-chunks-of-a-document) by prefix, and they make IDs easier to read when you inspect your data.

## Include metadata

Include [metadata](/guides/index-data/indexing-overview#metadata) fields that support your application's key operations, for example:

* **Filter searches**: Add fields for time ranges, categories, or other criteria to [filter searches](/guides/search/filter-by-metadata).
* **Link related chunks**: Use fields like `document_id` and `chunk_number` to group a document's chunks, so you can [delete](/guides/manage-data/manage-document-chunks#delete-chunks) or [replace](/guides/manage-data/manage-document-chunks#replace-a-chunked-document) them together.
* **Link back to the source**: Include fields like `document_url` to display results or trace them back to the original content.

Metadata values must be one of these types:

* String
* Number (stored as a 64-bit float)
* Boolean
* List of strings

> [!NOTE]
>
> Each record or document can hold up to 40 KB of metadata. Schema fields on a document aren't metadata and don't count toward this limit. Each `string` schema field, including one with `embed` or `sparse_embed`, is limited to 100 KB, and stored text is limited to 10,000 tokens.
