---
title: "Search overview"
source: https://docs.pinecone.io/guides/search/search-overview
path: guides/search/search-overview
---

Compare Pinecone search types and choose the right retrieval approach: full-text (BM25), semantic (dense vector), sparse-vector, and hybrid.

Pinecone supports four retrieval approaches. Three of them rank on a signal the index declares a field for, and hybrid search combines two or more of them. One document index can declare fields for all three, so the choice is mostly about which signal should order your results.

## Choose an approach

| Approach | Ranks on | Index declares | Reach for it when |
| - | - | - | - |
| [Full-text search](/guides/search/full-text-search) | BM25 token overlap, with optional Lucene query syntax | A `string` field with `full_text_search` | Queries mostly share exact words with the data, such as product names, error strings, source code, or identifiers |
| [Semantic search](/guides/search/semantic-search) | Dense-vector similarity, which captures meaning rather than wording | A `dense_vector` field, or a `string` field with [`embed`](/guides/search/integrated-embedding) | Queries are natural language, and a synonym or a paraphrase should still match |
| [Sparse-vector search](/guides/search/sparse-vector-search) | Per-token weights | A `sparse_vector` field, or a `string` field with [`sparse_embed`](/guides/search/integrated-embedding) | A sparse model such as [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) produces the representation, or your application produces its own sparse vectors |

Full-text search and sparse-vector search both rank on tokens. Full-text search matches tokens exactly, unless a field opts into [stemming or other text processing](/guides/search/full-text-search/text-processing). Sparse-vector search weights each token in your documents, which puts it between full-text search and semantic search. For general keyword retrieval, start with full-text search.

## Hybrid search

Hybrid search combines two or more signals in a single workflow. It isn't a field type, so an index declares nothing extra for it, and any index whose schema covers at least two signals can serve it. Reach for it when no single signal orders results well, as in a catalog where part numbers and descriptive phrases are both relevant.

Full-text with dense is the common pairing on a document index, and sparse with dense is what a [legacy vector index](/guides/legacy/vectors-api/hybrid-search-single-index) runs, but any combination works, including all three at once. A [metadata or text-match filter](/guides/search/filter-by-metadata) can also serve as one of the signals, narrowing the pool before another one ranks what's left.

See [Hybrid search](/guides/search/hybrid-search) for the patterns that combine them.

## Tune search

Each of these works with any approach:

* [Filter by metadata](/guides/search/filter-by-metadata) narrows the candidate pool before ranking, so an out-of-scope document can't take a result slot. [Text-match filters](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) do the same on full-text fields.
* [Rerank results](/guides/search/rerank-results) reorders what a search returns, using a model that reads the query and the document together.
* [Parallel queries](/guides/optimize/increase-throughput#parallel-queries) raise throughput when you run many searches at once.

Once you've chosen an approach, see [Data modeling](/guides/indexes/data-modeling) to structure your documents or records, then [Create an index](/guides/indexes/create-an-index) to set it up.

> [!TIP]
>
> Searches consume [read units (RUs)](/guides/cost/understand-cost#read-units). See [Understand Pinecone cost](/guides/cost/understand-cost#query) for how query cost is calculated, [Pricing](https://www.pinecone.io/pricing/) for rates, and [Query limits](/reference/api/database-limits/operation-limits) for `top_k` and result-size limits.
