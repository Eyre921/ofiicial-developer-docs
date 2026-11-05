---
title: "Search overview"
source: https://docs.pinecone.io/guides/search/search-overview
path: guides/search/search-overview
---

Compare Pinecone search types and choose the right retrieval approach: full-text (BM25), semantic (dense vector), sparse-vector, and hybrid.

> [!TIP]
>
> Searches consume [read units (RUs)](/guides/cost/understand-cost#read-units). See [Understand Pinecone cost](/guides/cost/understand-cost#query) for how query cost is calculated, [Pricing](https://www.pinecone.io/pricing/) for rates, and [Query limits](/reference/api/database-limits/operation-limits) for `top_k` and result-size limits.

## Choosing a search approach

Pinecone supports four retrieval approaches. They differ in the signal they rank on and the index shape they require.

### Quick decision tree

Walk through these questions in order. Pick the first match.

1. **Do your queries share specific tokens with the data?** (Product names, error messages, source code, named entities, technical jargon, identifiers.) → **[Full-text search](/guides/search/full-text-search)**. BM25 ranks results that share tokens with the query; Lucene syntax adds boolean and phrase operators.

2. **Are your queries natural language where meaning matters more than exact wording?** (Synonyms, paraphrases, conceptual similarity.) → **[Semantic search](/guides/search/semantic-search)** with a dense vector field.

3. **Do you need both keyword and semantic signals on the same data?** → **[Hybrid search](/guides/search/hybrid-search)**. Declare a `dense_vector` field alongside one or more `string` fields with `full_text_search`, then add a text-match filter to a `dense_vector` query, or run two searches and merge the results client-side.

4. **Do you produce a learned sparse-vector representation upstream of Pinecone?** (For example, using [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) or your own sparse encoder.) → **[Sparse-vector search](/guides/search/sparse-vector-search)**.

### Approach details

A useful gradient: **dense** ranks on concept (semantic similarity), **full-text search** ranks on strict character-level token matching (BM25), and **sparse-vector search** sits between them — token-aware, but with learned per-token weights and term expansion.

* **[Full-text search](/guides/search/full-text-search)** — **recommended** for keyword and phrase search over text content. You upsert typed JSON documents and rank with `score_by`: BM25 token matching on a `string` field with `full_text_search`, Lucene query syntax (`query_string`), `dense_vector` similarity, or `sparse_vector` similarity. A single index with a document schema can mix all four field types, so it's also the recommended single-index path when a workload needs more than one signal (BM25 + dense, BM25 + sparse, etc.).

* **[Semantic search](/guides/search/semantic-search) (dense-vector)** — for queries where intent and meaning matter more than exact keyword matches (synonyms, paraphrases, conceptual similarity). Uses dense embeddings.

* **[Hybrid search](/guides/search/hybrid-search)** — combines a keyword signal with a semantic signal so one query benefits from both. There are two patterns: a text-match filter on a `dense_vector` query, or client-side RRF fusion of two searches. See [Hybrid search](/guides/search/hybrid-search) to choose.

* **[Sparse-vector search](/guides/search/sparse-vector-search)** — recommended for workflows that use a learned sparse-vector model (for example, [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0)) or where the application owns the sparse-vector representation directly. For general-purpose keyword and phrase retrieval over text, start with full-text search.

Once you've chosen an approach, see [Data modeling](/guides/indexes/data-modeling) to structure your documents or records, then [Create an index](/guides/indexes/create-an-index) to set it up.

## Optimization

* [Filter by metadata](/guides/search/filter-by-metadata)
* [Rerank results](/guides/search/rerank-results)
* [Parallel queries](/guides/optimize/increase-throughput#parallel-queries)
