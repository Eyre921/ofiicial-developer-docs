---
title: "Manage a dedicated read nodes index"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/manage
path: guides/index-data/dedicated-read-nodes/manage
---

Add a hosted embedding model, monitor fullness, change node types, pause, or convert a Pinecone dedicated read nodes index back to on-demand.

## Add a hosted embedding model

To upsert and search with text instead of vectors, you can configure your index to use a [hosted embedding model](/guides/index-data/create-an-index#embedding-models). To do this, call [Configure an index](/reference/api/2025-10/control-plane/configure_index) and provide an `embed` object in the request body. In this object:

* For the `text` field, specify the name of the field in your data that contains the text to be embedded.
* Specify a model whose dimension requirements match the dimensions of your index.

### Example

<CodeGroup>
  ```bash Request expandable theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
             "embed": {
               "field_map": {
                 "text": "chunk_text"
               },
               "model": "llama-text-embed-v2",
               "read_parameters": {
                 "input_type": "query",
                 "truncate": "NONE"
               },
               "write_parameters": {
                 "input_type": "passage"
               }
             }
           }'
  ```
</CodeGroup>

<CodeGroup>
  ```json Response expandable theme={null}
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
              "shards": 2,
              "replicas": 1
            }
          },
          "status": {
            "state": "Ready",
            "current_shards": 2,
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "environment": "testing"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "chunk_text"
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
        "truncate": "NONE"
      },
      "vector_type": "dense"
    }
  }
  ```
</CodeGroup>

<Note>
  You can also create a dedicated read nodes index when calling [Create an index with integrated embedding](/reference/api/2025-10/control-plane/create_for_model). In the request body, use the `read_capacity` object to configure node type, shards, and replicas for dedicated read nodes.
</Note>

## Monitor index fullness

To check [index fullness](/guides/index-data/dedicated-read-nodes/concepts#index-fullness), call [Get index stats](/reference/api/2025-10/data-plane/describeindexstats).

### Example

<CodeGroup>
  ```bash Request theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/describe_index_stats" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

<CodeGroup>
  ```json Response expandable theme={null}
  {
    "namespaces": {
      "__default__": {
        "vectorCount": 705000
      }
    },
    "indexFullness": 0.01,
    "totalVectorCount": 705000,
    "dimension": 1536,
    "metric": "cosine",
    "vectorType": "dense",
    "memoryFullness": 0.01,
    "storageFullness": 0.01
  }
  ```
</CodeGroup>

In the response, `indexFullness` describes how full the index is, on a scale of 0 to 1. It's set to the greater of `memoryFullness` and `storageFullness`.

Pinecone also [emits these values](/guides/production/monitoring#available-metrics). Use them to track fullness over time in Prometheus or Datadog, and to alert before your index reaches capacity.

## Change node types

You can change node types in either direction (`b1` → `t1` or `t1` → `b1`). This operation doesn't require downtime, but can take up to 30 minutes to complete.

<Note>
  The most predictable way to increase throughput is by increasing [replicas](/guides/index-data/dedicated-read-nodes/concepts#replicas).
</Note>

<Warning>
  `t1` nodes [cache more data in memory](/guides/index-data/dedicated-read-nodes/concepts#node-types) than `b1` nodes. Because of this, switching from `b1` to `t1` may require more shards.

  If your new configuration doesn't have enough shards, the configuration change will fail with an error telling you how many shards are required. Update the request and retry.

  In the meantime, your index will continue to function normally in its original configuration.
</Warning>

To change node types, call [Configure an index](/reference/api/2025-10/control-plane/configure_index). In the request body, set the following fields:

| Field                                               | Value        | Notes                                                                         |
| :-------------------------------------------------- | :----------- | :---------------------------------------------------------------------------- |
| `spec.serverless.read_capacity.mode`                | `Dedicated`  |                                                                               |
| `spec.serverless.read_capacity.dedicated.node_type` | `b1` or `t1` | See [node types](/guides/index-data/dedicated-read-nodes/concepts#node-types) |

### Example

This example changes the node type from `b1` to `t1`:

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
                     "node_type": "t1"
                   }
                 }
               }
             }
           }'
  ```
</CodeGroup>

<CodeGroup>
  ```json Response expandable theme={null}
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
            "node_type": "t1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 1
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
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

## Pause an index

To pause an index, [set the number of replicas](/guides/index-data/dedicated-read-nodes/scale#add-or-remove-replicas) to 0. This operation can take up to 30 minutes to complete.

<Note>
  While an index is paused, you can't write to it or read from it. For a paused index, you're billed for storage, but not for node costs, reads, or writes.
</Note>

## Check the status of a configuration change

After making a configuration change to a dedicated read nodes index (changing shards, replicas, or node type), check the status of the change by calling [Describe an index](/reference/api/2025-10/control-plane/describe_index).

### Example

<CodeGroup>
  ```bash Request theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -X GET "https://api.pinecone.io/indexes/$INDEX_NAME" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

<CodeGroup>
  ```jsonc Response expandable theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
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
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    }
  }
  ```
</CodeGroup>

The response includes two status fields:

| Field                                            | Description                                                                |
| :----------------------------------------------- | :------------------------------------------------------------------------- |
| **`status.state`**                               | Overall index status (for example, `Initializing`, `Ready`, `Terminating`) |
| **`spec.serverless.read_capacity.status.state`** | Read capacity status (`Migrating`, `Scaling`, `Ready`, `Error`)            |

When changing node types, shards, or replicas, monitor the read capacity status (`spec.serverless.read_capacity.status.state`). Possible values:

| State       | Description                                                                                                                                                                                   |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Ready`     | The change is complete and the index is ready to serve queries at full capacity.                                                                                                              |
| `Scaling`   | A change to the number of shards or replicas is in progress.                                                                                                                                  |
| `Migrating` | A change to the node type or read capacity <Tooltip>mode</Tooltip> is in progress.                                                                                                            |
| `Error`     | The operation failed. For migrations to dedicated, this typically means you didn't allocate enough shards for your index size. Check `error_message` for details, and retry with more shards. |

<Note>
  During changes to shards, replicas, and node type, the index-level status (`status.state`) remains `Ready`. This is because the index can handle reads and writes while its dedicated read capacity scales.
</Note>

## Convert to on-demand

To convert a dedicated read nodes index back to on-demand, call [Configure an index](/reference/api/2025-10/control-plane/configure_index) and set `spec.serverless.read_capacity.mode` to `OnDemand`. This converts the index in place, keeping the same index name and host.

<CodeGroup>
  ```bash Request theme={null}
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
                   "mode": "OnDemand"
                 }
               }
             }
           }'
  ```
</CodeGroup>

<CodeGroup>
  ```jsonc Response expandable theme={null}
  {
    "name": "example-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-index-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "OnDemand",
          "status": {
            "state": "Ready",
            "current_shards": null,
            "current_replicas": null
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

If you'd rather return to on-demand on a fresh index, use the backup and restore path instead:

1. [Create a backup](/guides/manage-data/back-up-an-index) of your dedicated read nodes index.
2. [Create a new index from the backup](/guides/manage-data/restore-an-index), without specifying dedicated read node configuration.
3. Verify the new on-demand index and update your application to use it.
4. Delete the old dedicated read nodes index.

If you have concerns or need assistance, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
