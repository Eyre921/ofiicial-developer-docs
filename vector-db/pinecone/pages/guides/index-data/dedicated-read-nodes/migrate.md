---
title: "Migrate to dedicated read nodes"
source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes/migrate
path: guides/index-data/dedicated-read-nodes/migrate
---

Migrate an existing on-demand or pod-based Pinecone index to dedicated read nodes.

## From a pod-based index

You can't migrate a pod-based index directly to dedicated read nodes. First complete [Migrate a pod-based index to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless), which creates a new on-demand index with your data.

If that index has multiple namespaces, consolidate to one namespace, or plan a different architecture. Dedicated read nodes support only a [single namespace](/guides/index-data/dedicated-read-nodes/overview#namespace-limits).

## From an on-demand (serverless) index

To migrate an existing on-demand index to dedicated read nodes (including one you created by [migrating from pods](#from-a-pod-based-index)), follow these steps:

<Steps>
  <Step title="Create a backup of your index">
    Before migrating, [back up your index](/guides/manage-data/back-up-an-index) so you can return to on-demand later, either by [converting back](/guides/index-data/dedicated-read-nodes/manage#convert-to-on-demand) or by restoring the backup to a new on-demand index.
  </Step>

  <Step title="Delete extra namespaces">
    If your index has multiple namespaces, [delete](/reference/api/latest/data-plane/deletenamespace) all of them except the one you want to keep. Dedicated read nodes support only a [single namespace](/guides/index-data/dedicated-read-nodes/overview#namespace-limits).

    <Warning>
      If this is a production index, be sure to make a [backup](/guides/manage-data/back-up-an-index) before deleting namespaces. Or, if you need multiple namespaces, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket) to discuss early access to multi-namespace support for dedicated read nodes.
    </Warning>
  </Step>

  <Step title="Calculate your index size">
    Determine how many [shards](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-shards) you need by [sizing your index](/guides/index-data/dedicated-read-nodes/size-and-test#index-size).
  </Step>

  <Step title="Migrate the index">
    Call [Configure an index](/reference/api/2025-10/control-plane/configure_index). In the request body, in the `spec.serverless.read_capacity` object, set the following fields:

    | Field                       | Value                                                                                                 | Notes                                                                                              |
    | :-------------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
    | `mode`                      | `Dedicated`                                                                                           |                                                                                                    |
    | `dedicated.node_type`       | `b1` or `t1`                                                                                          | See [node types](/guides/index-data/dedicated-read-nodes/concepts#node-types)                      |
    | `dedicated.scaling`         | `Manual`                                                                                              | The only supported value                                                                           |
    | `dedicated.manual.shards`   | Number of [shards](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-shards) needed     | Minimum 1 shard; each shard provides 250 GB of storage                                             |
    | `dedicated.manual.replicas` | Number of [replicas](/guides/index-data/dedicated-read-nodes/size-and-test#number-of-replicas) needed | Minimum 0 (this [pauses](/guides/index-data/dedicated-read-nodes/manage#pause-an-index) the index) |

    This example migrates an index to dedicated read nodes using `b1` nodes, one shard, and one replica:

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
                         "node_type": "b1",
                         "scaling": "Manual",
                         "manual": {
                           "shards": 1,
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
        "name": "example-index-to-migrate",
        "vector_type": "dense",
        "metric": "cosine",
        "dimension": 1024,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "example-index-to-migrate-1c6ab6aa.svc.aped-4627-b74a.pinecone.io",
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
                  "shards": 1, // <---- desired state
                  "replicas": 1
                }
              },
              "status": {
                "state": "Migrating",
                "current_shards": null, //<---- current state
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

    The response includes two status fields:

    | Field                                            | Description                                                                |
    | :----------------------------------------------- | :------------------------------------------------------------------------- |
    | **`status.state`**                               | Overall index status (for example, `Initializing`, `Ready`, `Terminating`) |
    | **`spec.serverless.read_capacity.status.state`** | Read capacity status (`Migrating`, `Scaling`, `Ready`, `Error`)            |

    <Warning>
      If `status.state` is set to `Error`, the allocated number of shards was insufficient for the size of the index. Try again, adding more shards as needed.
    </Warning>
  </Step>

  <Step title="Monitor the migration">
    [Check the status](/guides/index-data/dedicated-read-nodes/manage#check-the-status-of-a-configuration-change) until `spec.serverless.read_capacity.status.state` is `Ready`.
  </Step>

  <Step title="Verify performance">
    Confirm the index meets your latency and throughput targets.
  </Step>
</Steps>
