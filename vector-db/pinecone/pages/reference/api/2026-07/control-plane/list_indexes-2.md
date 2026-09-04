---
title: "List indexes"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_indexes
path: reference/api/2026-07/control-plane/list_indexes
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /indexes
List all indexes in a project.

Returns all indexes in the project, including their current status and configuration. Each item in the response has the same shape as [`GET /indexes/{index_name}`](/reference/api/2026-07/control-plane/describe_index).

<RequestExample>
  ```python Python theme={null}
  # pip install --upgrade pinecone
  import os
  from pinecone import Pinecone

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

  for index_model in pc.indexes.list():
      print(index_model.name, index_model.host, index_model.status.state)
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  curl "https://api.pinecone.io/indexes" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
