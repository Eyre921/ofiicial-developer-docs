---
title: "Hybrid search overview"
source: https://docs.pinecone.io/guides/search/hybrid-search
path: guides/search/hybrid-search
---

Combine keyword and semantic retrieval in Pinecone with a text-match filter on a dense search, or by fusing separate searches with reciprocal rank fusion.

Hybrid search combines a keyword signal with a semantic signal so your results benefit from both. Full-text search (BM25) and sparse-vector search match specific terms like product codes, error strings, and names. Semantic search (dense vectors) matches on meaning, so a query still finds an answer phrased with different words. Each method misses what the other catches, and hybrid search closes that gap.

> [!NOTE]
>
> "Hybrid" covers several combinations: full-text (BM25) plus dense, sparse plus dense, or a text-match filter plus dense.

## Combine signals

Pinecone gives you two ways to combine a keyword signal with a dense signal. [Metadata filtering](/guides/search/filter-by-metadata) is a separate lever that composes with both: it narrows the candidate pool before ranking, so an out-of-scope document can't compete for a result slot.

| Pattern | How it works | When to use it |
| - | - | - |
| Filter, then rank | A [text-match filter](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) on a full-text field narrows the candidates, then a dense search ranks what remains, all in one request. The dense search can score the same `string` field with `embed`, or score a `dense_vector` field. | Document and text workloads on the Documents API. One index, one call, and no score normalization. |
| Client-side fusion | Run a keyword search and a dense search separately, then merge the two ranked lists with [reciprocal rank fusion (RRF)](/guides/search/reciprocal-rank-fusion). | When you want both signals to contribute to the ranking, not just to filter. |

RRF is a fusion method, not a synonym for hybrid search. It's one way to merge ranked lists, while "hybrid search" is the broader approach of combining signals. See [Reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).

## Choose an approach

For a new document or text workload, use the [Documents API](/guides/get-started/documents-api). Declare one `string` field with both `full_text_search` and `embed`, so Pinecone indexes its text for full-text search and embeds it for semantic search. Then either filter an `embed` search with a text-match filter on that field, or run a `text` search and an `embed` search and fuse them with RRF. See [Integrated embedding](/guides/search/integrated-embedding).

If you generate your own embeddings, declare a `dense_vector` field alongside one or more full-text `string` fields instead. See the full-text search [example schemas](/guides/search/full-text-search#example-schemas).

For hybrid search on a legacy vector index, see [Hybrid search on a single index](/guides/legacy/vectors-api/hybrid-search-single-index) and [Hybrid search on separate indexes](/guides/legacy/vectors-api/hybrid-search-separate-indexes).
