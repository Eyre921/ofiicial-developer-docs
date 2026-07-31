---
title: "List backups for an index"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_index_backups
path: reference/api/2026-04/control-plane/list_index_backups
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /indexes/{index_name}/backups
When `include_deleted` is false (or omitted), `index_name` must resolve to an active index in the project. If no active index by that name exists—including the case where only deleted indexes have used the name—the API returns **404**, not an empty list.
When `include_deleted` is true, the API returns backups from every index in the project that has ever used this name (active and deleted). The `source_index_deleted_at` field is present only when the backup is from a deleted index. **404** is returned only when no index by that name has ever existed in the project (active or deleted).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl -X GET "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -H "accept: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data":
    [
      {
        "backup_id":"9947520e-d5a1-4418-a78d-9f464c9969da",
        "source_index_id":"8433941a-dae7-43b5-ac2c-d3dab4a56b2b",
        "source_index_name":"docs-example",
        "tags":{},
        "name":"example-backup",
        "description":"Monthly backup of production index",
        "status":"Pending",
        "cloud":"aws",
        "region":"us-east-1",
        "dimension":1024,
        "record_count":98,
        "namespace_count":3,
        "size_bytes":1069169,
        "created_at":"2025-03-11T18:29:50.549505Z"
        }
      ],
    "pagination":null
  }
  ```
</ResponseExample>
