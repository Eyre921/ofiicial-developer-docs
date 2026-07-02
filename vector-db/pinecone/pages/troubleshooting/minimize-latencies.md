---
title: "Minimize latencies"
source: https://docs.pinecone.io/troubleshooting/minimize-latencies
path: troubleshooting/minimize-latencies
---

Troubleshoot “Minimize latencies” in Pinecone: There are many aspects to consider to minimize latencies:

There are many aspects to consider to minimize latencies:

## Slow uploads or high latencies

To minimize latency when accessing Pinecone:

* Switch to a cloud environment. For example: EC2, GCE, [Google Colab](https://colab.research.google.com), [GCP AI Platform Notebook](https://cloud.google.com/ai-platform-notebooks), or [SageMaker Notebook](https://docs.aws.amazon.com/sagemaker/dg/nbi.html). If you experience slow uploads or high query latencies, it might be because you are accessing Pinecone from your home network.
* Consider deploying your application in the same environment as your Pinecone service.
* See [Decrease latency](/guides/optimize/decrease-latency) for more tips.

## High query latencies with batching

If you're batching queries, try reducing the number of queries per call to 1 query vector. You can make these [calls in parallel](/troubleshooting/parallel-queries) and expect roughly the same performance as with batching.

## High latencies with fetch or include\_values

For on-demand indexes, since vector values are retrieved from object storage, operations that return vector values (`fetch` operations or queries with `include_values=true`) may have increased latency. If you don't need the vector values, set `include_values=false` when querying, or use the [`query`](/reference/api/latest/data-plane/query) operation instead of `fetch` if you only need metadata or IDs. See [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed) for more details.
