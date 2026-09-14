---
title: "Scale a dedicated read nodes index"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/scale
path: guides/index-data/dedicated-read-nodes/scale
---

Scale a Pinecone dedicated read nodes index by adding replicas for query throughput and shards for storage capacity.

## When to scale

Dedicated read nodes don't yet scale automatically. You decide when to scale, guided by two signals:

| Scenario    | What to check  | What to do                              |
| :---------- | :------------- | :-------------------------------------- |
| Query load  | CPU usage      | [Add replicas](#add-or-remove-replicas) |
| Data volume | Index fullness | [Add shards](#add-or-remove-shards)     |

Diagnose which one you're facing before you scale. Adding shards won't relieve query latency that's driven by CPU saturation, and adding replicas won't create room on a shard that's running out of space.

## Add or remove replicas

CPU usage reflects query pressure. As query load outgrows what your replicas can serve, query latency climbs and throughput drops.

Pinecone exposes CPU usage as the `pinecone_db_drn_cpu_usage_percent` metric, reported per shard. To collect it, [monitor your index with Prometheus](/guides/production/monitoring#monitor-with-prometheus).

Alert on the highest value across your shards rather than the index-wide average, which can look healthy while a single shard is already saturated:

```shell theme={null}
max(avg_over_time(pinecone_db_drn_cpu_usage_percent{index_name="docs-example"}[5m]))
```

Add a replica when this exceeds 80%. Averaging over a window keeps a brief spike from triggering a scale-up, so shorten or lengthen the window to suit how quickly your traffic shifts.

Throughput scales approximately linearly with replicas. For high availability, allocate `n+1` replicas, where `n` is the minimum number of replicas required to serve your expected throughput at your target latency. See [Number of replicas](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-replicas).

<Tip>
  If you'd rather reduce per-query compute than add replicas, you can also tune [query-time search parameters](/guides/index-data/dedicated-read-nodes/tune-queries) to trade some recall for higher throughput.
</Tip>

To add or remove [replicas](/guides/index-data/dedicated-read-nodes/concepts#replicas), call [Configure an index](/reference/api/2025-10/control-plane/configure_index). This operation doesn't require downtime, but can take up to 30 minutes to complete. In the request body, set the following fields:

| Field                                                     | Value                                                                                   | Notes                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :---------------------------------------- |
| `spec.serverless.read_capacity.mode`                      | `Dedicated`                                                                             |                                           |
| `spec.serverless.read_capacity.dedicated.scaling`         | `Manual`                                                                                |                                           |
| `spec.serverless.read_capacity.dedicated.manual.replicas` | Desired number of [replicas](/guides/index-data/dedicated-read-nodes/concepts#replicas) | Add replicas to increase query throughput |

### Example

<CodeGroup>
  ```bash Request expandable theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
             "spec": {
               "serverless": {
                 "read_capacity": {
                   "mode": "Dedicated",
                   "dedicated": {
                     "scaling": "Manual",
                     "manual": {
                       "replicas": 2
                     }
                   }
                 }
               }
             }
           }'
  ```
</CodeGroup>

<CodeGroup>
  ```jsonc Response expandable theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2 // <---- desired state
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1 // <---- current state
          }
        }
      }
    },
    "deletion_protection": "disabled",
    "tags": null,
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "END"
      },
      "vector_type": "dense"
    }
  }
  ```
</CodeGroup>

<Note>
  Configuration change limits:

  * You can make one configuration change every ten minutes, but you can batch multiple changes (node type, shards, and replicas) in a single request.
  * A new configuration change can only be initiated after the previous configuration change has completed.
  * Each configuration change can take up to 30 minutes to complete.
  * Read and write operations continue normally during configuration changes.
</Note>

## Add or remove shards

[Index fullness](/guides/index-data/dedicated-read-nodes/concepts#index-fullness) reflects data volume. Writes are blocked once the index reaches capacity, while reads continue normally.

<Note>
  [Add shards](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-shards) when [index fullness](/guides/index-data/dedicated-read-nodes/concepts#index-fullness) reaches 70-80%, especially if you expect continued growth. Adding shards reduces storage fullness (index data is spread across shards, so each stores less) and memory fullness (with less data per shard, there's less to cache in memory), helping you avoid write failures.
</Note>

To check the current value, see [Monitor index fullness](/guides/index-data/dedicated-read-nodes/manage#monitor-index-fullness).

To add or remove [shards](/guides/index-data/dedicated-read-nodes/concepts#shards), call [Configure an index](/reference/api/2025-10/control-plane/configure_index). This operation doesn't require downtime, but can take up to 30 minutes to complete. In the request body, set the following fields:

| Field                                                   | Value                                                                               | Notes                                 |
| :------------------------------------------------------ | :---------------------------------------------------------------------------------- | :------------------------------------ |
| `spec.serverless.read_capacity.mode`                    | `Dedicated`                                                                         |                                       |
| `spec.serverless.read_capacity.dedicated.scaling`       | `Manual`                                                                            |                                       |
| `spec.serverless.read_capacity.dedicated.manual.shards` | Desired number of [shards](/guides/index-data/dedicated-read-nodes/concepts#shards) | Each shard provides 250 GB of storage |

### Example

<CodeGroup>
  ```bash Request expandable theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
             "spec": {
               "serverless": {
                 "read_capacity": {
                   "mode": "Dedicated",
                   "dedicated": {
                     "scaling": "Manual",
                     "manual": {
                       "shards": 3
                     }
                   }
                 }
               }
             }
           }'
  ```
</CodeGroup>

<CodeGroup>
  ```jsonc Response expandable theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 3, // <---- desired state
              "replicas": 1
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 2, // <---- current state
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "disabled",
    "tags": null,
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "END"
      },
      "vector_type": "dense"
    }
  }
  ```
</CodeGroup>

<Note>
  Configuration change limits:

  * You can make one configuration change every ten minutes, but you can batch multiple changes (node type, shards, and replicas) in a single request.
  * A new configuration change can only be initiated after the previous configuration change has completed.
  * Each configuration change can take up to 30 minutes to complete.
  * Read and write operations continue normally during configuration changes.
</Note>
