---
title: "Integrated embedding"
source: https://docs.pinecone.io/guides/search/integrated-embedding
path: guides/search/integrated-embedding
---

Declare embed or sparse_embed on a string field so Pinecone embeds your text on a document index, and upsert and search with plain text instead of vectors.

Embedding converts text into a vector that captures its meaning. Instead of generating those vectors yourself, you can have Pinecone embed a `string` field's text for you. Add an `embed` (dense) or `sparse_embed` (learned-sparse) object to the field, and Pinecone embeds the text when you upsert or update a [document](/guides/core-concepts/key-terms#document), and embeds the query text when you search that field. You send and search with plain text and never handle vectors.

This is the same integrated embedding that the [Create an index with integrated embedding](/reference/api/2026-07/control-plane/create_for_model) operation provides for the legacy Records API, brought to document indexes, where it composes with full-text search on the same field.

Integrated embedding requires API version `2026-07`. Send `X-Pinecone-Api-Version: 2026-07` on REST requests, or use an SDK that supports it: Python `10.1.0` or later, Node.js `9.1.0` or later, or Go `7.1.0` or later.

> [!NOTE]
>
> Bring Your Own Cloud (BYOC) indexes can't declare `embed` or `sparse_embed`.

## Declare an embedded field

Add `embed`, `sparse_embed`, or both to a `string` field, inside `schema.fields` in the [create-index request](/guides/search/full-text-search#example-schemas). Every key inside them is optional: an empty `{}` uses the platform default model at its default dimension and metric. Pinecone resolves and fixes the model, dimension, and metric at creation, and returns them when you describe the index.

> [!TIP]
>
> You can also create an index with integrated embedding in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/schema-create-index).

```json Default models theme={null}
{
  "chunk_text": {
    "type": "string",
    "embed": {},
    "sparse_embed": {}
  }
}
```

```json Chosen model and dimension theme={null}
{
  "chunk_text": {
    "type": "string",
    "embed": { "model": "llama-text-embed-v2", "dimension": 512 }
  }
}
```

* `embed` takes a hosted dense model (default `llama-text-embed-v2`) and optional `dimension`, `metric`, and `write_parameters`/`read_parameters` (model parameters applied when embedding on write and on query, such as `truncate`).
* `sparse_embed` takes a hosted sparse model (default `pinecone-sparse-english-v0`) and optional `write_parameters`/`read_parameters`. Sparse embeddings have no dimension or metric.
* An `embed` field uses the index's single dense slot, and a `sparse_embed` field uses its single sparse slot. So an index has at most one of each, and an embedded field can't coexist with a `dense_vector` or `sparse_vector` field of the same type (dense or sparse).

For available models and their supported dimensions, see the [model guide](/guides/index-data/index-configuration#embedding-models). The embedding configuration is fixed at creation: you can't add, remove, or change `embed` or `sparse_embed` on an existing index.

## Text storage and full-text search

By default (`store_text: true`), Pinecone stores the field's text and returns it via `include_fields`. It also indexes the text for full-text search, so a `string` field with `embed` is BM25-searchable unless you opt out.

Set `store_text: false` to embed the text without storing it. A field with `store_text: false`:

* can't declare `full_text_search`.
* can't be scored with `text` or `query_string`, or matched with `$match_phrase`, `$match_all`, or `$match_any`.
* still supports `embed` and `sparse_embed` scoring.
* returns a `400` if named in `include_fields` on search or fetch. `["*"]` leaves it out.

To search one chunk field by dense, learned-sparse, and BM25, declare all three aspects:

```json All three aspects theme={null}
{
  "chunk_text": {
    "type": "string",
    "embed": {},
    "sparse_embed": {},
    "full_text_search": {}
  }
}
```

### Limits

* A document and a single request are each limited to 2 MB. On an index that embeds text, that request limit also counts the vectors Pinecone derives from the text.
* An embedded value can be up to 100 KB, whether or not the text is stored. A stored value is also limited to 10,000 tokens after tokenization.
* Each model embeds only its first N tokens (507 for `multilingual-e5-large`, 2,048 for `llama-text-embed-v2`, 512 by default for `pinecone-sparse-english-v0`). Longer values are truncated by default. For a dense `embed` field, setting `truncate: NONE` rejects an over-length value with a `400` instead. The full value is still stored and returned when `store_text` is `true`.

## Upsert and search embedded fields

### Upsert

Upsert documents with plain text on the embedded field. You don't supply vectors, and Pinecone embeds the text on write. A few rules apply:

* When the schema declares `embed` or `sparse_embed`, each upsert or by-ID update is embedded in one call, so it's capped at 96 documents instead of 1,000, even when a request sets only metadata.
* A dense `embed` field must appear in every document. Omitting it, or removing it in an update, is rejected with a `400`. A `sparse_embed`-only field is optional, so you can omit or remove it.
* A vector or an empty string on an embedded field is rejected with a `400`.
* Update is a partial patch, so a field you don't set is left unchanged. A by-filter update can't set an embedded field; patch it by document ID.
* An upsert or update that embeds text reports the tokens it consumed as `usage.embed_total_tokens`.

```python Python theme={null}
index.documents.upsert(
    namespace="example-namespace",
    documents=[
        {"_id": "doc1", "chunk_text": "Vitamin D supports bone health and immune function."},
    ],
)
```

```javascript JavaScript theme={null}
const index = pc.index({ name: 'INDEX_NAME', namespace: 'example-namespace' });

await index.documents.upsert({
  documents: [
    { _id: 'doc1', chunk_text: 'Vitamin D supports bone health and immune function.' },
  ],
});
```

```go Go theme={null}
idx, _ := pc.DescribeIndex(ctx, "INDEX_NAME")
conn, _ := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "example-namespace"})

_, err := conn.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
	Documents: []pinecone.Document{
		{"_id": "doc1", "chunk_text": "Vitamin D supports bone health and immune function."},
	},
})
if err != nil {
	log.Fatal(err)
}
```

> [!NOTE]
>
> You can't [bulk import](/guides/index-data/import-data) into an index with an `embed` or `sparse_embed` field. Add text through upsert or update instead.

### Search

To search, pick the `embed` or `sparse_embed` scoring method and pass query text. Pinecone embeds the query with the field's frozen model and ranks by similarity.

```python Python theme={null}
response = index.documents.search(
    namespace="example-namespace",
    top_k=5,
    score_by=[
        {"type": "embed", "fields": ["chunk_text"], "query": "how does vitamin D help the body"}
    ],
    include_fields=["chunk_text"],
)
```

```javascript JavaScript theme={null}
const index = pc.index({ name: 'INDEX_NAME', namespace: 'example-namespace' });

const response = await index.documents.search({
  topK: 5,
  scoreBy: [
    { type: 'embed', fields: ['chunk_text'], query: 'how does vitamin D help the body' },
  ],
  includeFields: ['chunk_text'],
});
```

```go Go theme={null}
idx, _ := pc.DescribeIndex(ctx, "INDEX_NAME")
conn, _ := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "example-namespace"})

query := "how does vitamin D help the body"
response, err := conn.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
	TopK: 5,
	ScoreBy: []pinecone.DocumentScoringMethod{
		{Type: pinecone.DocumentScoringTypeEmbed, Fields: []string{"chunk_text"}, Query: &query},
	},
	IncludeFields: []string{"chunk_text"},
})
if err != nil {
	log.Fatal(err)
}
fmt.Println(response)
```

```bash curl theme={null}
curl -X POST "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 5,
    "score_by": [
      { "type": "embed", "fields": ["chunk_text"], "query": "how does vitamin D help the body" }
    ],
    "include_fields": ["chunk_text"]
  }'
```

Pinecone returns the stored text and any metadata you request with `include_fields`. The vectors it derives from your text are internal and aren't returned. The search response reports the query's embedding usage as `usage.embed_total_tokens`. A `sparse_embed` query is embedded in-process, so it reports `0`.

An `embed` or `sparse_embed` clause must be the only clause in `score_by`. You can still combine signals, because a stored embedded field is also full-text-searchable. Rank with an `embed` `score_by`, then narrow the results with a `$match_phrase`, `$match_all`, or `$match_any` filter on the same field (see [Full-text search](/guides/search/full-text-search#search-examples)). To fuse two full rankings instead, run separate searches and merge them with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).
