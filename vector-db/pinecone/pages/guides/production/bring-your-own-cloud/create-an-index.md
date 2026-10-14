---
title: "Create an index in BYOC"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud/create-an-index
path: guides/production/bring-your-own-cloud/create-an-index
---

Create an index in your Pinecone BYOC environment using the standard Pinecone API.

Once your BYOC environment is [deployed](/guides/production/bring-your-own-cloud/deploy), you can create indexes and read/write data using the standard Pinecone API.

Control plane operations like [creating](/reference/api/latest/control-plane/create_index), [listing](/reference/api/latest/control-plane/list_indexes), and [deleting](/reference/api/latest/control-plane/delete_index) indexes work via the standard Pinecone API regardless of your [network access mode](/guides/production/bring-your-own-cloud/connect-and-manage#connect-to-your-index).

<Note>
  BYOC supports [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) indexes, but not on-demand indexes.
</Note>

## Create an index

Use the environment name from the [deployment output](/guides/production/bring-your-own-cloud/deploy) to create an index in your BYOC environment.

<CodeGroup>
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
                 "_values": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
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
  from pinecone.db_control.models import ByocSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.db.index.create(
      name="example-byoc-index",
      dimension=1536,
      metric="cosine",
      vector_type="dense",
      spec=ByocSpec(
          environment="aws-us-east-1-26bf.byoc",
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
      ),
      deletion_protection="disabled",
  )
  ```
</CodeGroup>

## Next steps

* [Connect to and manage your BYOC indexes](/guides/production/bring-your-own-cloud/connect-and-manage)
