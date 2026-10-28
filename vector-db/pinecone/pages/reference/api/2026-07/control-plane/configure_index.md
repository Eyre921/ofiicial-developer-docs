---
title: "Configure an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/configure_index
path: reference/api/2026-07/control-plane/configure_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml patch /indexes/{index_name}
Configure an existing index. For guidance and examples, see [Manage indexes](https://docs.pinecone.io/guides/manage-data/manage-indexes).

Updates configuration on an existing index. You can update `deletion_protection`, `tags`, and `read_capacity` (for example, converting from `OnDemand` to `Dedicated`). The schema itself is immutable — to change field types or add new indexed fields, create a new index and re-upsert.

This is a partial update: only the fields you include in the request body are modified. Unspecified fields are left unchanged. To clear `tags`, send `"tags": {}`.

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

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

// Enable deletion protection
await pc.indexes.configure('articles', {
  deletionProtection: 'enabled',
});

// Convert read capacity from OnDemand to Dedicated
await pc.indexes.configure('articles', {
  readCapacity: {
    mode: 'Dedicated',
    dedicated: {
      nodeType: 'b1',
      scaling: 'Manual',
      manual: { shards: 1, replicas: 1 },
    },
  },
});
```

```go Go theme={null}
package main

import (
    "context"
    "log"
    "os"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: os.Getenv("PINECONE_API_KEY"),
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    // Enable deletion protection
    _, err = pc.ConfigureIndex(ctx, "articles", pinecone.ConfigureIndexParams{
        DeletionProtection: pinecone.DeletionProtectionEnabled,
    })
    if err != nil {
        log.Fatalf("Failed to configure index: %v", err)
    }

    // Convert read capacity from OnDemand to Dedicated
    nodeType := "b1"
    shards := int32(1)
    replicas := int32(1)

    _, err = pc.ConfigureIndex(ctx, "articles", pinecone.ConfigureIndexParams{
        ReadCapacity: &pinecone.ReadCapacityParams{
            Dedicated: &pinecone.ReadCapacityDedicatedConfig{
                NodeType: &nodeType,
                Scaling: &pinecone.ReadCapacityScaling{
                    Manual: &pinecone.ReadCapacityManualScaling{
                        Shards:   &shards,
                        Replicas: &replicas,
                    },
                },
            },
        },
    })
    if err != nil {
        log.Fatalf("Failed to configure index: %v", err)
    }
}
```

```hcl Terraform theme={null}
# Requires Terraform provider v5.0.0 or later
# To configure an index, change deletion_protection, tags, or read_capacity in its
# resource block and run `terraform apply`. Terraform updates the index in place.
# An index can't switch from dedicated read capacity back to on-demand.
resource "pinecone_index" "articles" {
  name = "articles"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      title = { string = { full_text_search = {} } }
      body  = { string = { full_text_search = { language = "en", stemming = true, stop_words = true } } }
    }
  }

  # Enable deletion protection
  deletion_protection = "enabled"

  # Add or change tags
  tags = {
    environment = "production"
  }

  # Convert read capacity from on-demand to dedicated. The apply waits until the
  # dedicated read nodes are ready.
  read_capacity = {
    dedicated = {
      node_type = "b1"
      replicas  = 1
      shards    = 1
    }
  }
}
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
