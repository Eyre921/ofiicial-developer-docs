---
title: "Size and test a dedicated read nodes index"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/size-and-test
path: guides/index-data/dedicated-read-nodes/size-and-test
---

Calculate how many shards and replicas a Pinecone dedicated read nodes index needs, and load-test your workload to validate the configuration.

## Calculate the size of your index

To determine how many [shards](/guides/index-data/dedicated-read-nodes/concepts#shards) your index requires, calculate your index size and then apply the [number of shards](#number-of-shards) formula.

### Index size

A record can include a dense vector, a sparse vector, or both. Use the formula that matches your data to calculate total size:

<div>
  <Tabs>
    <Tab title="Index of dense vectors">
      An [index of dense vectors](/guides/index-data/indexing-overview#indexes-with-dense-vectors) contains records with one dense vector each.

      <Note>
        Records can also contain sparse vectors (when the index metric is set to `dotproduct`), which can be useful for [hybrid search](/guides/search/hybrid-search/single-index). To learn how to calculate size in that case, see [Index with both dense and sparse vectors](#index-with-both-dense-and-sparse-vectors).
      </Note>

      **Calculate size (assuming no sparse vectors)**

      ```
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Dense vector dimensions × 4 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * Each `Dense vector dimension` uses 4 bytes.

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Dense vector dimensions | Avg metadata size | Index size |
      | :--------- | :---------------------- | :---------------- | :--------- |
      | 500,000    | 768                     | 500 bytes         | 1.79 GB    |
      | 1,000,000  | 1536                    | 1,000 bytes       | 7.15 GB    |
      | 5,000,000  | 1024                    | 15,000 bytes      | 95.5 GB    |
      | 10,000,000 | 1536                    | 1,000 bytes       | 71.5 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + 500 bytes of metadata) = 1.79 GB
      </Note>
    </Tab>

    <Tab title="Index of sparse vectors">
      An [index of sparse vectors](/guides/index-data/indexing-overview#indexes-with-sparse-vectors) contains records with one sparse vector each.

      **Calculate size**

      ```
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * `Number of non-zero sparse values`: Average number across all records. To find the count for a single record, check the length of the sparse vector's `indices` or `values` array. Each non-zero value uses 8 bytes.

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :--------- | :----------------------------------- | :---------------- | :--------- |
      | 500,000    | 10                                   | 500 bytes         | 0.29 GB    |
      | 1,000,000  | 50                                   | 1,000 bytes       | 1.41 GB    |
      | 5,000,000  | 100                                  | 15,000 bytes      | 79.0 GB    |
      | 10,000,000 | 50                                   | 1,000 bytes       | 14.1 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 0.29 GB
      </Note>
    </Tab>

    <Tab title="Index with both dense and sparse vectors">
      An [index with both dense and sparse vectors](/guides/search/hybrid-search/single-index) contains records that each have one dense vector and an optional sparse vector.

      **Calculate size**

      ```
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Dense vector dimensions × 4 bytes + 
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * Each `Dense vector dimension` uses 4 bytes.
      * `Number of non-zero sparse values`: Average number across all records, including those without sparse vectors. To find the count for a single record, check the length of the sparse vector's `indices` or `values` array. Each non-zero value uses 8 bytes.

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Dense vector dimensions | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :--------- | :---------------------- | :----------------------------------- | :---------------- | :--------- |
      | 500,000    | 768                     | 10                                   | 500 bytes         | 1.83 GB    |
      | 1,000,000  | 1536                    | 50                                   | 1,000 bytes       | 7.54 GB    |
      | 5,000,000  | 1024                    | 100                                  | 15,000 bytes      | 99.5 GB    |
      | 10,000,000 | 1536                    | 50                                   | 1,000 bytes       | 75.4 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 1.83 GB
      </Note>
    </Tab>
  </Tabs>
</div>

### Number of shards

To calculate the number of shards your index requires, divide the size of your index by 250 GB and round up:

```
Minimum shards = (Index size) / (250 GB per shard)
```

To maintain optimal performance, provision additional shards to keep your index at 70-80% capacity. For example, a 500 GB index should have three shards (750 GB capacity = 67% full), not two shards (500 GB capacity = 100% full).

#### Example shard calculations

| Index size | Minimum shards       | Recommended shards   |
| :--------- | :------------------- | :------------------- |
| \~71 GB    | 1 (250 GB; 28% full) | 1 (250 GB; 28% full) |
| \~300 GB   | 2 (500 GB; 60% full) | 2 (500 GB; 60% full) |
| \~400 GB   | 2 (500 GB; 80% full) | 3 (750 GB; 53% full) |

#### Other considerations

* Every index must have at least one shard. However, you can [pause an index](/guides/index-data/dedicated-read-nodes/manage#pause-an-index) by reducing its replicas to 0.
* After you've created your index, [monitor its fullness](/guides/index-data/dedicated-read-nodes/manage#monitor-index-fullness).

<Note>
  [Add shards](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-shards) when [index fullness](/guides/index-data/dedicated-read-nodes/concepts#index-fullness) reaches 70-80%, especially if you expect continued growth. Adding shards reduces storage fullness (index data is spread across shards, so each stores less) and memory fullness (with less data per shard, there's less to cache in memory), helping you avoid write failures.
</Note>

### Number of replicas

To calculate the number of replicas your index requires, first [test your workload](#test-your-workload) to find the QPS a single replica can handle at your target latency. Then, use this formula, and round up:

```
Minimum replicas = (Required QPS) / (QPS per replica)
```

For example, if one replica handles 50 QPS at your target latency and you need 150 QPS, you need three replicas.

For how throughput scales with replicas and how to size for high availability, see [Replicas](/guides/index-data/dedicated-read-nodes/concepts#replicas).

## Test your workload

To choose between on-demand and dedicated read nodes, or to optimize your dedicated read nodes configuration, test with your actual workload. Performance varies based on factors such as the size of your index, vector dimensionality, metadata characteristics, and query patterns.

<Steps>
  <Step title="Calculate the size of your index">
    Determine how many shards your index requires. See [Calculate the size of your index](#calculate-the-size-of-your-index).
  </Step>

  <Step title="Create and populate a test index">
    Populate a [dedicated read nodes index](/guides/index-data/dedicated-read-nodes/create) with data representative of your workload.

    <Tip>
      If you don't restore your test index from a backup, you can [upsert](/guides/index-data/upsert-data) or [import](/guides/index-data/import-data) your data.
    </Tip>
  </Step>

  <Step title="Migrate your test index to dedicated read nodes (if necessary)">
    If your test index is on-demand, [migrate it](/guides/index-data/dedicated-read-nodes/migrate) with a single `b1` replica to start.

    <Warning>
      Don't migrate your production index yet. At this point, you're just testing your workload.
    </Warning>
  </Step>

  <Step title="Run a load test">
    Send realistic query patterns against your test index, gradually increasing QPS. For example, start at 10 QPS for about 30 minutes, then step up in 10-QPS increments while monitoring latency. Note the QPS where latency crosses your target threshold.
  </Step>

  <Step title="Calculate replicas">
    From the QPS a single replica sustained, [determine how many replicas](#number-of-replicas) you need for your target throughput.
  </Step>

  <Step title="Adjust and re-test">
    If you haven't hit your performance and cost goals, change the configuration and test again:

    * [Add or remove shards](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-shards) for storage capacity
    * [Add or remove replicas](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-replicas) for throughput
    * [Change node types](/guides/index-data/dedicated-read-nodes/manage#change-node-types) for different performance characteristics

    Continue iterating until you meet your requirements with room for growth.
  </Step>
</Steps>
