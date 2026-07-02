---
title: "Describe a backup"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/describe_backup
path: reference/api/2026-04/control-plane/describe_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /backups/{backup_id}
Get a description of a backup.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="8c85e612-ed1c-4f97-9f8c-8194e07bcf71"

  curl -X GET "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -H "accept: application/json"
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
    "record_count":98,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-03-11T18:29:50.549505Z"
  }
  ```
</ResponseExample>
