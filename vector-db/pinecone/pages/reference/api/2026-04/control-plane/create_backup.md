---
title: "Create a backup of an index"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/create_backup
path: reference/api/2026-04/control-plane/create_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml post /indexes/{index_name}/backups
Create a backup of an index.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -d '{
        "name": "example-backup", 
        "description": "Monthly backup of production index"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "backup_id":"8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "source_index_id":"f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name":"docs-example",
    "tags":{},
    "name":"example-backup",
    "description":"Monthly backup of production index",
    "status":"Ready",
    "cloud":"aws",
    "region":"us-east-1",
    "dimension":1024,
    "record_count":96,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-05-14T16:37:25.625540Z"
    }
  ```
</ResponseExample>
