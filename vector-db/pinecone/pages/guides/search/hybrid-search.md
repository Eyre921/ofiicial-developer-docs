---
title: "Hybrid search overview"
source: https://docs.pinecone.io/guides/search/hybrid-search
path: guides/search/hybrid-search
---

Combine two or more retrieval signals in Pinecone with a filter that narrows a ranking, or by fusing separate searches with reciprocal rank fusion.

Hybrid search combines two or more retrieval signals so your results benefit from each. Full-text search (BM25) and sparse-vector search match specific terms like product codes, error strings, and names. Semantic search (dense vectors) matches on meaning, so a query still finds an answer phrased with different words. Each method misses what the others catch, and hybrid search closes that gap.

## Combine signals

The following patterns differ in where the signals meet. A filter can serve as one of them: [metadata filtering](/guides/search/filter-by-metadata) narrows the candidate pool before ranking, so an out-of-scope document can't compete for a result slot.

| Pattern | How it works | When to use it |
| - | - | - |
| Filter, then rank | A filter narrows the candidates, then any ranking clause scores what remains, all in one request. The filter can be a [metadata filter](/guides/search/filter-by-metadata) on any filterable field, or a [text-match filter](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) on a full-text field. The ranking clause can score the same `string` field with `embed`, or score a `dense_vector`, `sparse_vector`, or full-text field. | Document and text workloads on the Documents API. One index, one call, and no score normalization. |
| Client-side fusion | Run separate searches, then merge any number of their ranked lists with [reciprocal rank fusion (RRF)](/guides/search/reciprocal-rank-fusion). | When you want every signal to contribute to the ranking rather than only narrow the pool. |

RRF is a fusion method, not a synonym for hybrid search. It's one way to merge ranked lists, while "hybrid search" is the broader approach of combining signals. See [Reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).

## Set up an index

For a new document or text workload, use the [Documents API](/guides/get-started/documents-api). Declare one or more `string` fields with `full_text_search`, then add the dense side:

* **Integrated embedding**: Add `embed` to a `string` field, so Pinecone indexes the text for full-text search and embeds it for semantic search. See [Integrated embedding](/guides/search/integrated-embedding).
* **Your own vectors**: Declare a `dense_vector` field alongside the full-text fields. See [Bring your own vectors](/guides/search/bring-your-own-vectors) and the full-text search [example schemas](/guides/search/full-text-search#example-schemas).

If you [converted a legacy vector index](/guides/indexes/convert-an-index) that held both dense and sparse vectors, the new index has a separate field for each, plus any `string` field you gave `full_text_search`. The legacy combined dense and sparse query doesn't carry over, because a document search ranks by one scoring type per request. Combine them with one of the patterns above.

For a legacy vector index, see [Hybrid search on a single index](/guides/legacy/vectors-api/hybrid-search-single-index) and [Hybrid search on separate indexes](/guides/legacy/vectors-api/hybrid-search-separate-indexes).
