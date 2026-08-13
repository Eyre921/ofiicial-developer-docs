---
title: "Reciprocal rank fusion"
source: https://docs.pinecone.io/guides/search/reciprocal-rank-fusion
path: guides/search/reciprocal-rank-fusion
---

Combine the results of separate searches into a single ranking with reciprocal rank fusion (RRF), a client-side method that fuses rankings instead of raw scores.

<Note>
  The examples below use the [document API](/guides/search/full-text-search), which is in [public preview](/guides/search/full-text-search#public-preview). Reciprocal rank fusion itself is a client-side method and works with the results of any Pinecone search.
</Note>

When you rank the same set of documents two different ways, for example, a [full-text (BM25) search](/guides/search/full-text-search) and a [semantic (dense-vector) search](/guides/search/semantic-search), the scores live on different, incomparable scales. Adding or averaging the raw scores is not meaningful, and one signal usually dominates. **Reciprocal rank fusion (RRF)** combines them by fusing the *rankings* instead of the scores, so no normalization or per-signal weighting is required.

Today, you run each search separately, then apply RRF to their results in your client (server-side fusion is coming).

## When to use it

Reach for RRF whenever you combine results from separate searches and want each to contribute to the final ranking, most commonly full-text (BM25) with semantic (dense-vector). It's a robust default that works without normalizing scores or tuning per-signal weights.

## How it works

RRF scores each document by summing `1 / (k + rank)` across every ranking it appears in, where `rank` is the document's 1-based position in that ranking and `k` is a constant (the [original RRF paper](https://dl.acm.org/doi/10.1145/1571941.1572114) uses `k=60`). A document ranked highly in multiple searches accumulates the highest fused score. A document absent from a ranking gets nothing from it. Because only rank position matters, scores never need to be normalized.

```python Python theme={null}
def reciprocal_rank_fusion(rankings, k=60):
    """Fuse ranked lists of document IDs into one RRF-scored ranking.

    Each ranking is a list of `_id`s in rank order (best first).
    Returns a dict mapping `_id` to its fused score.
    """
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return scores
```

## Combine two searches

This assumes an index whose [schema](/guides/search/full-text-search#schema-definition) declares an FTS-enabled `string` field (`body`) and a `dense_vector` field (`embedding`).

Run each search independently, pass the ranked `_id`s to `reciprocal_rank_fusion`, then sort by the fused score. Here, a full-text search and a semantic search over the same index are fused into one top-10 ranking:

```python Python theme={null}
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.preview.index(name="docs-example")

query = "how do I reset my password?"
fetch_k = 50  # fetch deeper than the final top_k so weaker-but-present signals still count

# 1. Full-text (BM25) search.
text_hits = index.documents.search(
    namespace="__default__",
    top_k=fetch_k,
    score_by=[{"type": "text", "field": "body", "query": query}],
    include_fields=["*"],
).matches

# 2. Semantic (dense-vector) search. Embed the query with the same model as your documents.
query_embedding = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=[query],
    parameters={"input_type": "query"},
)
dense_hits = index.documents.search(
    namespace="__default__",
    top_k=fetch_k,
    score_by=[{"type": "dense_vector", "field": "embedding", "values": query_embedding[0]["values"]}],
    include_fields=["*"],
).matches

# 3. Fuse the two rankings client-side (reciprocal_rank_fusion is defined in "How it works" above).
fused = reciprocal_rank_fusion([
    [m._id for m in text_hits],
    [m._id for m in dense_hits],
])

# 4. Sort by fused score and keep the top results.
by_id = {m._id: m for m in text_hits}
for m in dense_hits:
    by_id.setdefault(m._id, m)

top_k = 10
for doc_id in sorted(fused, key=fused.get, reverse=True)[:top_k]:
    print(doc_id, fused[doc_id], getattr(by_id[doc_id], "body", ""))
```

## Tuning and extensions

* **`fetch_k`** (a variable in this example, not an API parameter) controls how deep each ranking is fetched before fusing. Raise it so a document that ranks well in one search but outside the top of the other still contributes. It should be at least your final `top_k`.
* **`k`** (default 60) controls how much a single ranking's top positions dominate the fused order. A larger `k` flattens the influence of any single top-ranked result.
* **Latency.** Run the searches in parallel (for example with `asyncio` or threads) so you pay the slowest search's latency, not the sum.
* **Weighting.** To favor one signal over another, weight each ranking's contribution (multiply its `1 / (k + rank)` terms by a per-ranking weight). It's a powerful relevance-tuning lever and can warrant its own guide; this page uses the unweighted default.

### Merge more than two rankings

RRF extends to any number of rankings. Pass more lists to `reciprocal_rank_fusion`; each additional search contributes another ranked list of `_id`s:

```python Python theme={null}
fused = reciprocal_rank_fusion([
    [m._id for m in text_hits],
    [m._id for m in dense_hits],
    [m._id for m in sparse_hits],  # e.g., a sparse-vector search
])
```
