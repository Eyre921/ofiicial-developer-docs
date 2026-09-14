---
title: "Create a dedicated read nodes index"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/create
path: guides/index-data/dedicated-read-nodes/create
---

Create a Pinecone dedicated read nodes index from scratch or from a backup of an existing index.

## From scratch

<Steps>
  <Step title="Create the index">
    Call [Create an index](/reference/api/2025-10/control-plane/create_index). In the request body, in the `spec.serverless.read_capacity` object, set the following fields:

    | Field                       | Value                                                                                                 | Notes                                                                                              |
    | :-------------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
    | `mode`                      | `Dedicated`                                                                                           |                                                                                                    |
    | `dedicated.node_type`       | `b1` or `t1`                                                                                          | See [node types](/guides/index-data/dedicated-read-nodes/concepts#node-types)                      |
    | `dedicated.scaling`         | `Manual`                                                                                              | The only supported value                                                                           |
    | `dedicated.manual.shards`   | Number of [shards](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-shards) needed     | Minimum 1 shard; each shard provides 250 GB of storage                                             |
    | `dedicated.manual.replicas` | Number of [replicas](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-replicas) needed | Minimum 0 (this [pauses](/guides/index-data/dedicated-read-nodes/manage#pause-an-index) the index) |

    <Note>
      To learn how to determine the number of shards and replicas your index requires, see [Calculate the size of your index](/guides/index-data/dedicated-read-nodes/size-and-test#calculate-the-size-of-your-index).
    </Note>

    This example creates an index with two shards and one replica:

    <CodeGroup>
      ```bash Request expandable theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl "https://api.pinecone.io/indexes" \
           -H "Accept: application/json" \
           -H "Content-Type: application/json" \
           -H "Api-Key: $PINECONE_API_KEY" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -d '{
                 "name": "example-dedicated-index",
                 "dimension": 1024,
                 "metric": "cosine",
                 "deletion_protection": "enabled",
                 "tags": {
                   "environment": "production"
                 },
                 "vector_type": "dense",
                 "spec": {
                   "serverless": {
                     "cloud": "aws",
                     "region": "us-east-1",
                     "read_capacity": {
                       "mode": "Dedicated",
                       "dedicated": {
                         "node_type": "b1",
                         "scaling": "Manual",
                         "manual": {
                           "shards": 2,
                           "replicas": 1
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
          "ready": false,
          "state": "Initializing"
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
                  "shards": 2, // <---- desired state
                  "replicas": 1
                }
              },
              "status": {
                "state": "Migrating",
                "current_shards": null, // <---- current state
                "current_replicas": null
              }
            }
          }
        },
        "deletion_protection": "enabled",
        "tags": {
          "environment": "production"
        }
      }
      ```
    </CodeGroup>

    The response includes two status fields:

    | Field                                            | Description                                                                |
    | :----------------------------------------------- | :------------------------------------------------------------------------- |
    | **`status.state`**                               | Overall index status (for example, `Initializing`, `Ready`, `Terminating`) |
    | **`spec.serverless.read_capacity.status.state`** | Read capacity status (`Migrating`, `Scaling`, `Ready`, `Error`)            |

    <Note>
      When creating a dedicated read nodes index, `status.state` transitions to `Ready` as soon as the index is ready for reads and writes.

      However, `spec.serverless.read_capacity.status.state` remains `Migrating` until the index scales to its full read capacity, at which point it transitions to `Ready`.
    </Note>
  </Step>

  <Step title="Add your data">
    After the index is created, [upsert](/guides/index-data/upsert-data) or [import](/guides/index-data/import-data) your data.

    <Tip>
      To upsert and search with text instead of vectors, you can configure your index to use a [hosted embedding model](/guides/index-data/create-an-index#embedding-models). Call [Configure an index](/reference/api/2025-10/control-plane/configure_index) and specify the `embed` object in the request body.
    </Tip>
  </Step>
</Steps>

## From a backup

<Steps>
  <Step title="Restore the backup">
    [Restore the backup](/guides/manage-data/restore-an-index) to a new on-demand index with the same data as the original.
  </Step>

  <Step title="Delete extra namespaces">
    If the restored index has multiple namespaces, [delete](/reference/api/latest/data-plane/deletenamespace) all of them except the one you want to keep. Dedicated read nodes support only [one namespace](/guides/index-data/dedicated-read-nodes/overview#namespace-limits).
  </Step>

  <Step title="Migrate to dedicated read nodes">
    Convert the restored on-demand index by following [Migrate to dedicated read nodes](/guides/index-data/dedicated-read-nodes/migrate).
  </Step>
</Steps>
