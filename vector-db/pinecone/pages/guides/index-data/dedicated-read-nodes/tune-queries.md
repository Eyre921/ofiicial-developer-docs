---
title: "Tune queries on dedicated read nodes"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/tune-queries
path: guides/index-data/dedicated-read-nodes/tune-queries
---

Tune scan_factor and max_candidates on a Pinecone dedicated read nodes index to trade recall for lower latency and higher throughput.

Dedicated read nodes support two optional query-time parameters, `scan_factor` and `max_candidates`, that let you trade off recall (search quality) for lower latency and higher throughput. By default, queries use internal heuristics that favor recall. If your application is latency-sensitive or needs higher QPS, you can tune these parameters to reduce the work done per query, or increase them for higher recall.

These parameters only take effect on dedicated read nodes indexes with dense vectors. On-demand indexes accept the parameters but ignore them. On indexes that store only sparse vectors, specifying either parameter returns an error. Using these parameters requires API version `2025-10` or later.

## How scan\_factor and max\_candidates work

Dense vector search on dedicated read nodes uses a two-stage pipeline:

1. **Scanning**: Controlled by `scan_factor`. For IVF-based indexes, the system scans a fraction of partitions determined by `scan_factor / sqrt(num_partitions)`. A lower `scan_factor` scans fewer partitions, producing fewer candidates faster. This parameter only affects IVF-based slabs; for other index architectures (e.g., smaller indexes using flat search), `scan_factor` has no effect.
2. **Reranking**: Controlled by `max_candidates`. The top candidates from the scanning stage are reranked by computing exact distances. More reranking improves recall but increases latency. This parameter applies to all index architectures.

The two parameters affect different stages and their effects are additive, so you can set both to optimize each stage independently.

| Parameter        | Type    | Range                                | Default                                                         | Description                                                                                                                                |
| :--------------- | :------ | :----------------------------------- | :-------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `scan_factor`    | Float   | 0.5–4.0                              | 4.0                                                             | Controls how much of the IVF index is scanned to find vector candidates. Lower values scan fewer partitions and return results faster.     |
| `max_candidates` | Integer | Your query's `top_k` value – 100,000 | 2500 (see [default behavior](#default-max_candidates-behavior)) | Maximum number of candidate vectors to rerank with exact distance computation. Higher values improve recall; lower values improve latency. |

You can set one or both per query. Omitting both preserves the current default behavior, so existing applications are unaffected.

### Default `max_candidates` behavior

When `max_candidates` isn't set, the system calculates an effective value using the following formula:

* If `top_k` \<= 1000: `min(top_k * 10, 1000)`
* If `top_k` > 1000: `top_k`
* Then, a floor of 2500 is applied (the effective value is at least 2500)

For most queries (where `top_k` \<= 2500), the effective default is **2500**. This isn't the maximum possible value. You can raise `max_candidates` (up to 100,000) to increase recall, or lower it (down to your query's `top_k`) to reduce latency.

When you explicitly set `max_candidates`, the value you provide is used directly, bypassing the formula and the floor.

## Impact on recall and performance

Lower `scan_factor` or `max_candidates` values reduce the work done per query, which improves latency and throughput but may reduce recall. The tables below summarize benchmarked behavior on a 2.68M-vector index (1536 dimensions, cosine similarity). Actual results are dataset-dependent.

### `scan_factor` benchmarks

Starting from the default (4.0), lowering `scan_factor` reduces the fraction of IVF partitions scanned:

| scan\_factor  | Approximate recall (p50) | Relative throughput |
| :------------ | :----------------------- | :------------------ |
| 4.0 (default) | \~96%                    | 1x (baseline)       |
| 2.0           | \~94%                    | \~1.5x              |
| 1.0           | \~91%                    | \~2x                |
| 0.5           | \~84%                    | \~4x                |

Testing shows that lower `scan_factor` values can reduce p50 and p99 latency by 30–50% or more.

### Tuning `max_candidates`

Higher `max_candidates` improves recall by reranking more candidates but increases latency and reduces throughput; lower values favor speed. For guidance on choosing values, see [Tuning guidance](#tuning-guidance). We recommend benchmarking on your own dataset and workload to find the right balance. Use the [Test your workload](/guides/index-data/dedicated-read-nodes/size-and-test#test-your-workload) process to validate latency and recall.

## Tuning guidance

Start with the defaults and adjust based on your workload requirements:

* **To optimize for throughput/latency:** Lower `scan_factor` first (from the default of 4.0). This has the most impact on IVF-based indexes. If you need further improvement, lower `max_candidates` below the default of 2500 (down to your query's `top_k` value).
* **To optimize for recall:** Raise `max_candidates` above the default of 2500 (up to 100,000). This reranks more candidate vectors at the cost of higher latency.

### Trade-offs to consider

* **One parameter at a time:** `scan_factor` controls the scanning stage (IVF only) and `max_candidates` controls the reranking stage (all index types). Tuning them independently makes it easier to isolate the effect.
* **Safe defaults:** Omitting both parameters preserves existing behavior, so existing queries aren't affected.
* **Cost reduction:** By achieving higher throughput per node, you may be able to serve the same query rate with fewer replicas.

## Behavior by vector type

| Index / query type                           | Behavior                                                                                                                                                                                                      |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dense vectors, dense query                   | `scan_factor` and `max_candidates` apply normally.                                                                                                                                                            |
| Dense vectors, hybrid query (dense + sparse) | Both parameters apply to the dense component only; the sparse component is unaffected.                                                                                                                        |
| Sparse vectors only                          | Specifying `scan_factor` or `max_candidates` returns an error.                                                                                                                                                |
| On-demand index                              | Both parameters are accepted but have no effect on search behavior. You can use the same query code against on-demand (e.g., for development) and dedicated read nodes (for production) without modification. |

## API and SDK examples

Both parameters are optional fields on the `POST /query` request.

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "namespace": "example-namespace",
      "topK": 10,
      "vector": [0.1, 0.2, 0.3],
      "scanFactor": 1.0,
      "maxCandidates": 1000
    }'
  ```

  ```python Python theme={null}
  # Both parameters — balanced recall and latency
  index.query(
      namespace="example-namespace",
      vector=[0.1, 0.2, 0.3],
      top_k=10,
      scan_factor=1.0,
      max_candidates=1000
  )

  # scan_factor only — faster queries, lower recall
  index.query(
      namespace="example-namespace",
      vector=[0.1, 0.2, 0.3],
      top_k=10,
      scan_factor=0.5
  )

  # Omit both for maximum recall (default behavior)
  index.query(
      namespace="example-namespace",
      vector=[0.1, 0.2, 0.3],
      top_k=10
  )
  ```

  ```typescript TypeScript theme={null}
  // Both parameters — balanced recall and latency
  await index.query({
    namespace: "example-namespace",
    vector: [0.1, 0.2, 0.3],
    topK: 10,
    scanFactor: 1.0,
    maxCandidates: 1000
  });

  // scan_factor only — faster queries, lower recall
  await index.query({
    namespace: "example-namespace",
    vector: [0.1, 0.2, 0.3],
    topK: 10,
    scanFactor: 0.5
  });
  ```
</CodeGroup>

### Validation errors

| Condition                                                                               | Error message                                                                                         |
| :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| API version earlier than `2025-10`                                                      | `scan_factor and max_candidates parameters require API version 2025-10 or later`                      |
| `scan_factor` outside 0.5–4.0                                                           | `scan_factor must be between 0.5 and 4.0, got &lcub;value&rcub;`                                      |
| `max_candidates` below your query's `top_k` or above 100,000                            | `max_candidates must be between &lcub;top_k&rcub; (top_k) and &lcub;max&rcub;, got &lcub;value&rcub;` |
| Used on an index that stores only sparse vectors (API error text says "sparse indexes") | `scan_factor and max_candidates parameters are not supported for sparse indexes`                      |

<Note>
  `scan_factor` and `max_candidates` don't affect billing. Read costs for dedicated read nodes are based on provisioned capacity (node type, shards, and replicas), not per-query effort. By tuning these parameters to achieve higher throughput, you may be able to serve the same query rate with fewer provisioned replicas, reducing your overall cost.
</Note>
