---
title: "Search overview"
source: https://docs.pinecone.io/guides/search/search-overview
path: guides/search/search-overview
---

Compare Pinecone search types and choose the right retrieval approach: full-text (BM25), semantic (dense vector), sparse lexical, and hybrid.

<Tip>
  Searches consume [read units (RUs)](/guides/manage-cost/understanding-cost#read-units). See [Understanding cost](/guides/manage-cost/understanding-cost#query) for how query cost is calculated.
</Tip>

## Search types

* [Full-text search](/guides/search/full-text-search)
* [Semantic search](/guides/search/semantic-search) (dense-vector)
* [Sparse-vector search (also called sparse-vector lexical search)](/guides/search/lexical-search)
* [Hybrid search](/guides/search/hybrid-search)

## Choosing a search approach

Pinecone supports four retrieval approaches. They differ in the signal they rank on and the index shape they require.

### Quick decision tree

Walk through these questions in order — pick the first match.

1. **Do your queries share specific tokens with the data?** (Product names, error messages, source code, named entities, technical jargon, identifiers.) → **[Full-text search](/guides/search/full-text-search)**. BM25 ranks results that share tokens with the query; Lucene syntax adds boolean and phrase operators.

2. **Are your queries natural language where meaning matters more than exact wording?** (Synonyms, paraphrases, conceptual similarity.) → **[Semantic search](/guides/search/semantic-search)** with a dense vector field.

3. **Do you produce a learned sparse-vector representation upstream of Pinecone?** (For example, using [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) or your own sparse encoder.) → **[Sparse-vector lexical search](/guides/search/lexical-search)**.

4. **Do you need both semantic and keyword signals on the same data?**
   * **On a JSON-document workload** → **[Full-text search](/guides/search/full-text-search)** with a multi-field schema. Declare a `dense_vector` field alongside one or more FTS-enabled `string` fields. A single search request ranks by one signal; combine them by adding a text-match filter to a `dense_vector` query, or by running two searches and merging results client-side.
   * **On a vector-only records workload** → **[Hybrid search](/guides/search/hybrid-search)**. Store a dense vector and a sparse vector on each record in a single index (vector API).

### Approach details

A useful gradient: **dense** ranks on concept (semantic similarity), **full-text search** ranks on strict character-level token matching (BM25), and **sparse-vector lexical search** sits between them — token-aware, but with learned per-token weights and term expansion.

* **[Full-text search](/guides/search/full-text-search)** — **recommended** for keyword and phrase search over text content. You upsert typed JSON documents and rank with `score_by`: BM25 token matching on an FTS-enabled `string` field, Lucene query syntax (`query_string`), `dense_vector` similarity, or `sparse_vector` similarity. A single index with a document schema can mix all four field types, so it's also the recommended single-index path when a workload needs more than one signal (BM25 + dense, BM25 + sparse, etc.).

* **[Semantic search](/guides/search/semantic-search) (dense-vector)** — for queries where intent and meaning matter more than exact keyword matches (synonyms, paraphrases, conceptual similarity). Uses dense embeddings.

* **[Sparse-vector search (also called sparse-vector lexical search)](/guides/search/lexical-search)** — recommended for workflows that use a learned sparse-vector model (for example, [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0)) or where the application owns the sparse-vector representation directly. For general-purpose keyword and phrase retrieval over text, start with full-text search.

* **[Hybrid search](/guides/search/hybrid-search)** — combines dense and sparse vectors in a single index (vector API) for vector-centric workflows that need both semantic and lexical signals. For document-centric workflows that combine keyword matching with vector ranking, the most common pattern is dense (or sparse) ranking restricted by a text-match filter on an FTS-enabled `string` field — for example, semantic search across a corpus narrowed to documents containing an exact phrase. To weight BM25 and dense rankings against each other, run separate searches and merge the results client-side.

Once you've chosen an approach, see [Data modeling](/guides/index-data/data-modeling) to structure your documents or records, then [Create an index](/guides/index-data/create-an-index) to set it up.

## Optimization

* [Filter by metadata](/guides/search/filter-by-metadata)
* [Rerank results](/guides/search/rerank-results)
* [Parallel queries](/guides/search/semantic-search#parallel-queries)

## Limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them.
</Tip>

## Cost

* To understand how cost is calculated for queries, see [Understanding cost](/guides/manage-cost/understanding-cost#query).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).
