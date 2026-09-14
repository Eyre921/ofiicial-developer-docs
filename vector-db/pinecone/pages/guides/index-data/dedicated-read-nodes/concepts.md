---
title: "Dedicated read nodes concepts"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/concepts
path: guides/index-data/dedicated-read-nodes/concepts
---

Node types, shards, replicas, and index fullness are the building blocks of a Pinecone dedicated read nodes index.

Before creating a dedicated read nodes index, understand the configuration options that determine capacity and performance.

## Node types

A node is the basic unit of compute and cache storage capacity for a dedicated read nodes index. Each shard runs on one node, so the node type you choose determines the performance characteristics and cost of your index. The total number of nodes in your index is calculated as `shards × replicas`. For example, an index with two shards and two replicas uses four nodes.

There are two node types: `b1` and `t1`. Both are suitable for large-scale and demanding workloads, but they differ in processing power and memory capacity, and they cache different data.

|                  | b1 (Balanced)                                                                   | t1 (Performance)                                                                                                |
| ---------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Memory caching   | Vector index stored in memory                                                   | Vector index + vector projections cached in memory                                                              |
| Use case         | Predictable performance for sustained query rates with balanced cost efficiency | Highest performance for the most demanding workloads with extreme query volumes and strict latency requirements |
| Storage          | 250 GB per shard                                                                | 250 GB per shard                                                                                                |
| Compute & memory | Base-level compute and memory resources                                         | \~4x more compute and memory than `b1`                                                                          |
| Cost             | Lower-cost option                                                               | \~3x the cost of `b1`                                                                                           |

Consider using `t1` nodes if your performance requirements aren't met by `b1` nodes, or if `t1` nodes are more cost-effective than `b1` nodes for your workload.

<Note>
  When choosing a node type, remember that:

  * Both types of nodes provide 250 GB of storage per shard. The difference is in compute and memory, which affects query performance.
  * Because `t1` nodes cache more data in memory than `b1` nodes, an index may require more shards on `t1` than on `b1` (for the same data).
  * You can [change node types](/guides/index-data/dedicated-read-nodes/manage#change-node-types) after creating your index.
</Note>

## Shards

Shards determine the storage capacity of an index. Each shard provides 250 GB of storage, and data is split across all the shards in an index. To respond to a query, the index gathers data from all shards as needed. To determine how many shards you need, [calculate your index size](/guides/index-data/dedicated-read-nodes/size-and-test#calculate-the-size-of-your-index) and then [calculate the number of shards](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-shards).

<Warning>
  It's your responsibility to allocate enough shards for your index size. If you run out of shard capacity, writes are blocked (reads continue). Track how close you are with [index fullness](#index-fullness).
</Warning>

## Replicas

Replicas multiply the compute resources and data of an index, allowing for higher query throughput and availability. Each replica is a complete copy of your index data and has its own dedicated compute resources.

* Throughput scales approximately linearly with replicas. For example, if one replica handles 50 QPS at your target latency, two replicas should handle approximately 100 QPS.
* You can scale replicas up or down with no downtime using the API. See [Add or remove replicas](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-replicas).
* For high availability, use at least two replicas. The recommended approach is to allocate `n+1` replicas where `n` is your minimum for throughput. Pinecone distributes replicas across availability zones (up to three per region), so if one zone fails, remaining replicas continue serving queries.

To determine how many replicas you need, [test your workload](/guides/index-data/dedicated-read-nodes/size-and-test#test-your-workload) and then [calculate the number of replicas](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-replicas).

<Note>
  Actual performance varies based on workload characteristics (query complexity, vector dimensions, metadata characteristics), [metadata filter](/guides/search/filter-by-metadata) selectivity, and [node type](#node-types) (`b1` vs `t1`). Always test with your specific workload.
</Note>

## Index fullness

Index fullness measures how much of an index's allocated capacity is in use. Dedicated read nodes cache all of your data in memory and on local SSD, so fullness tracks both dimensions:

* `memoryFullness`: how full the memory cache is.
* `storageFullness`: how full the local SSD is.
* `indexFullness`: the greater of the two, on a scale of 0 to 1.

Storage usually fills first, but memory can be the limiting factor with `b1` nodes holding many low-dimension vectors, or `t1` nodes holding high-dimension vectors and lots of metadata. When `indexFullness` reaches 1.0 (100%), writes are blocked while reads continue.

To check these values on demand, see [Monitor index fullness](/guides/index-data/dedicated-read-nodes/manage#monitor-index-fullness). To track them over time, use the [`pinecone_db_index_fullness` metrics](/guides/production/monitoring#available-metrics) via the [Prometheus or Datadog integration](/guides/production/monitoring#monitor-with-datadog). To decide when to add capacity, see [Add or remove shards](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-shards).
