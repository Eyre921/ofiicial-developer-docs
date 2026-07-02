---
title: "Increase search relevance"
source: https://docs.pinecone.io/guides/optimize/increase-relevance
path: guides/optimize/increase-relevance
---

Learn techniques to improve search result quality.

This page describes helpful techniques for improving search accuracy and relevance.

## Rerank results

[Reranking](/guides/search/rerank-results) is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](/guides/search/rerank-results#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

## Filter by metadata

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a dense or sparse vector, depending on the [type of index](/guides/index-data/indexing-overview#indexes). In addition, you can include metadata key-value pairs to store related information or context. When you search the index, you can then include a metadata filter to limit the search to records matching a filter expression.

For example, if an index contains records about books, you could use a metadata field to associate each record with a genre, like `"genre": "fiction"` or `"genre": "poetry"`. When you query the index, you could then use a metadata filter to limit your search to records related to a specific genre.

For more details, see [Filter by metadata](/guides/search/filter-by-metadata).

## Use full-text search for keyword matching

When relevance depends on exact keyword or phrase matches over text content — for example, product names, technical IDs, named entities, or jargon — we recommend [full-text search](/guides/search/full-text-search). It uses **BM25** ranking on `string` fields you've declared with `full_text_search` enabled and supports Lucene query syntax (`query_string`), including phrase, boolean, and proximity operators, plus the `$match_phrase` filter for exact phrase matching against text fields.

An index with a document schema can also include `dense_vector` and `sparse_vector` fields in the same schema, so you can combine BM25 token matching with semantic or sparse-vector ranking on a single index. A single search request ranks by one scoring type — restrict a `dense_vector` or `sparse_vector` search with a text-match filter (`$match_phrase`, `$match_all`, `$match_any`) on an FTS-enabled `string` field, or run BM25 and dense (or sparse) searches separately and merge the results client-side.

For more details, see [Full-text search](/guides/search/full-text-search).

## Match the query and passage embedding paths

When you use [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding) with a model like [`llama-text-embed-v2`](/models/llama-text-embed-v2) or [`multilingual-e5-large`](/models/multilingual-e5-large), Pinecone embeds upserted data with the `passage` input type and embeds query text with the `query` input type. The encoder is the same, but the input type changes the resulting vector, so the *same* string embedded as a query and as a passage produces two different vectors. This is intentional in E5- and Llama-style models: the asymmetry is what makes a short query match a longer, semantically related passage.

A common consequence is that searching by text for the exact string you upserted does not return a similarity score near `1.0`. For example, querying for the exact text `"JetBlue Flights and Extras"` against a record containing that same text can score around `0.58`, while searching by the raw passage vector for the same record scores near `1.0`. The text query takes the `query` path and the stored record was embedded via the `passage` path, so the two vectors are not identical.

**Is a low score expected for identical short strings?** Yes. The query/passage split has the largest effect on short, low-semantic text such as exact names, error codes, SKUs, and IDs, where there is little meaning for the model to align across the two paths. Scores in roughly the `0.5`–`0.8` range for identical short strings are normal. The asymmetry helps on true semantic search (a short question matched to a longer answer passage) and only looks like a problem on exact-token-match workloads.

**When should you query through the passage path?** Only when the workload is exact or near-exact lookup (IDs, error logs, product names) rather than semantic search, and you want exact matches to score near `1.0`. You can override the read-time input type at the index level with [`configure_index`](/reference/api/latest/control-plane/configure_index). Set `model` and `field_map` to the index's existing values, and set `read_parameters.input_type` to `passage`:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

pc.configure_index(
    name="docs-example",
    embed={
        "model": "llama-text-embed-v2",
        "field_map": {"text": "chunk_text"},
        "read_parameters": {"input_type": "passage"}
    }
)
```

Note the trade-offs:

* This setting degrades true semantic search, since queries no longer use the input type the model was trained to expect.
* It applies to the whole index. With integrated inference you cannot choose `query` or `passage` per request. If you need that control, embed text yourself with the [Inference API](/reference/api/latest/inference/generate-embeddings) and search with the [`query`](/reference/api/latest/data-plane/query) operation using your own vectors.

For pure exact-match retrieval, a [sparse index](/guides/index-data/indexing-overview#indexes-with-sparse-vectors) or [full-text search](/guides/search/full-text-search) is usually a better fit than forcing dense embeddings through the passage path. See [Use full-text search for keyword matching](#use-full-text-search-for-keyword-matching) above for when keyword and phrase matching is the right tool.

## Use hybrid search

When you have both dense and sparse vectors for the same records and want to combine semantic and lexical signals at query time, you can use hybrid search. [Semantic search](/guides/search/semantic-search) can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while sparse-vector [lexical search](/guides/search/lexical-search) can miss results based on relationships, such as synonyms and paraphrases. Hybrid search combines the two.

There are two ways to do this:

* [Use a single index for dense and sparse vectors](/guides/search/hybrid-search#use-a-single-index-for-dense-and-sparse-vectors). This is the **recommended** approach for most use cases because you make requests to a single index, the linkage between dense and sparse vectors is implicit, and you can perform hybrid queries with a single request. Note that you'll need to [normalize sparse and dense values](/guides/search/hybrid-search#normalize-sparse-and-dense-values) at query time so the unbounded sparse component doesn't dominate the combined score.
* [Use separate indexes for dense and sparse vectors](/guides/search/hybrid-search#use-separate-indexes-for-dense-and-sparse-vectors). This approach provides more flexibility but requires managing two indexes, maintaining linkages between vectors, and querying each index separately before merging results.

If you'd rather not tune sparse and dense weights at all, an [index with a document schema](/guides/get-started/concepts#document) with a multi-field schema is a simpler single-index alternative: declare FTS-enabled `string` fields alongside a `dense_vector` or `sparse_vector` field on the same index, then either restrict the dense (or sparse) search with a text-match filter on the lexical field, or run separate searches and merge the results client-side.

For more details, including guidance on choosing the right approach, see [Hybrid search](/guides/search/hybrid-search).

## Explore chunking strategies

You can chunk your content in different ways to get better results. Consider factors like the length of the content, the complexity of queries, and how results will be used in your application.

For more details, see [Chunking strategies](https://www.pinecone.io/learn/chunking-strategies/).
