---
title: "Create an index in BYOC"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud/create-an-index
path: guides/production/bring-your-own-cloud/create-an-index
---

Create an index in your Pinecone BYOC environment using the standard Pinecone API.

Once your BYOC environment is [deployed](/guides/production/bring-your-own-cloud/deploy), you can create indexes and read/write data using the standard Pinecone API.

Control plane operations like [creating](/reference/api/latest/control-plane/create_index), [listing](/reference/api/latest/control-plane/list_indexes), and [deleting](/reference/api/latest/control-plane/delete_index) indexes work via the standard Pinecone API regardless of your [network access mode](/guides/production/bring-your-own-cloud/connect-and-manage#connect-to-your-index).

> [!NOTE]
>
> BYOC supports both on-demand and [dedicated read nodes (DRN)](/guides/index-data/dedicated-read-nodes/overview) indexes.
>
> * On-demand indexes and their namespaces share one pool of nodes in your BYOC environment.
> * DRN indexes each get their own nodes, which you size with shards and replicas when you create the index.
>
> Both index types support vector search and [full-text search](/guides/search/full-text-search).

To create an index in your BYOC environment, set these fields in the create request:

* `deployment.deployment_type`: `byoc`
* `deployment.environment`: The environment name from the [deployment output](/guides/production/bring-your-own-cloud/deploy)
* `read_capacity.mode`: `OnDemand` for an on-demand index, or `Dedicated` for a DRN index

The following examples use the API and SDKs.

> [!TIP]
>
> You can also create either index type in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/): select the **BYOC** tab under **Capacity mode**, set **Read capacity** to **On-demand** or **Dedicated read nodes**, and enter your **Environment ID**.

## Create a DRN index

A DRN index runs on its own set of nodes. Set the node type, shards, and replicas in `read_capacity`.

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07" \
     -d '{
           "name": "example-byoc-index",
           "deployment": {
             "deployment_type": "byoc",
             "environment": "aws-us-east-1-26bf.byoc"
           },
           "schema": {
             "fields": {
               "title": { "type": "string", "full_text_search": {} },
               "body": { "type": "string", "full_text_search": {} },
               "embedding": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
             }
           },
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
           },
           "deletion_protection": "disabled"
         }'
```

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

pc.indexes.create(
    name="example-byoc-index",
    schema={
        "fields": {
            "title": {"type": "string", "full_text_search": {}},
            "body": {"type": "string", "full_text_search": {}},
            "embedding": {"type": "dense_vector", "dimension": 1536, "metric": "cosine"},
        }
    },
    deployment={
        "deployment_type": "byoc",
        "environment": "aws-us-east-1-26bf.byoc",
    },
    read_capacity={
        "mode": "Dedicated",
        "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
                "shards": 1,
                "replicas": 1,
            },
        },
    },
    deletion_protection="disabled",
)
```

## Create an on-demand index

An on-demand index sets no shards or replicas, because it runs on the shared on-demand pool.

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07" \
     -d '{
           "name": "example-byoc-on-demand-index",
           "deployment": {
             "deployment_type": "byoc",
             "environment": "aws-us-east-1-26bf.byoc"
           },
           "schema": {
             "fields": {
               "title": { "type": "string", "full_text_search": {} },
               "body": { "type": "string", "full_text_search": {} },
               "embedding": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
             }
           },
           "read_capacity": {
             "mode": "OnDemand"
           },
           "deletion_protection": "disabled"
         }'
```

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

pc.indexes.create(
    name="example-byoc-on-demand-index",
    schema={
        "fields": {
            "title": {"type": "string", "full_text_search": {}},
            "body": {"type": "string", "full_text_search": {}},
            "embedding": {"type": "dense_vector", "dimension": 1536, "metric": "cosine"},
        }
    },
    deployment={
        "deployment_type": "byoc",
        "environment": "aws-us-east-1-26bf.byoc",
    },
    read_capacity={"mode": "OnDemand"},
    deletion_protection="disabled",
)
```

## Next steps

* [Connect to and manage your BYOC indexes](/guides/production/bring-your-own-cloud/connect-and-manage)
