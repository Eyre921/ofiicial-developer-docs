---
title: "Configure an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/configure_index
path: reference/api/2026-07/control-plane/configure_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml patch /indexes/{index_name}
Configure an existing index. For guidance and examples, see [Manage indexes](https://docs.pinecone.io/guides/manage-data/manage-indexes).

Updates configuration on an existing index. You can update `deletion_protection`, `tags`, and `read_capacity` (for example, converting from `OnDemand` to `Dedicated`). The schema itself is immutable — to change field types or add new indexed fields, create a new index and re-upsert.

This is a partial update: only the fields you include in the request body are modified. Unspecified fields are left unchanged. To clear `tags`, send `"tags": {}`.

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

  # Enable deletion protection
  pc.indexes.configure(
      name="articles",
      deletion_protection="enabled",
  )

  # Convert read capacity from OnDemand to Dedicated
  pc.indexes.configure(
      name="articles",
      read_capacity={
          "mode": "Dedicated",
          "dedicated": {
              "node_type": "b1",
              "scaling": "Manual",
              "manual": {"shards": 1, "replicas": 1},
          },
      },
  )
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  # Enable deletion protection
  curl -X PATCH "https://api.pinecone.io/indexes/articles" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{ "deletion_protection": "enabled" }'

  # Convert read capacity from OnDemand to Dedicated
  curl -X PATCH "https://api.pinecone.io/indexes/articles" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "read_capacity": {
        "mode": "Dedicated",
        "dedicated": {
          "node_type": "b1",
          "scaling": "Manual",
          "manual": { "shards": 1, "replicas": 1 }
        }
      }
    }'
  ```
</RequestExample>
