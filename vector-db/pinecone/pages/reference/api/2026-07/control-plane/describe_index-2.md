---
title: "Describe an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_index
path: reference/api/2026-07/control-plane/describe_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /indexes/{index_name}
Get a description of an index.

Returns detailed information about a specific index, including its schema, status, host URL, and read capacity. Poll this endpoint after [`POST /indexes`](/reference/api/2026-07/control-plane/create_index) until `status.ready: true` (and, for `Dedicated` read capacity, `read_capacity.status.state: "Ready"`) before performing data plane operations.

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

  index_model = pc.indexes.describe(name="articles")
  print(index_model.status, index_model.schema)

  host = index_model.host
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  curl "https://api.pinecone.io/indexes/articles" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
