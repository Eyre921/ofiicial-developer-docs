---
title: "List backups for all indexes in a project"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_project_backups
path: reference/api/2026-04/control-plane/list_project_backups
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /backups
List all backups for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -H "accept: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json curl  theme={null}
  {
    "data": [
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "tags": null,
        "name": "example-backup",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 0,
        "record_count": 96,
        "namespace_count": 1,
        "size_bytes": 86393,
        "created_at": "2025-05-14T17:00:45.803146Z"
      },
      {
        "backup_id": "d686451d-1ede-4004-9f72-7d22cc799b6e",
        "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
        "source_index_name": "docs-example2",
        "tags": null,
        "name": "example-backup2",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 50,
        "namespace_count": 1,
        "size_bytes": 545171,
        "created_at": "2025-05-14T17:00:34.814371Z"
      },
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example3",
        "tags": {},
        "name": "example-backup3",
        "description": "Monthly backup of production index",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 98,
        "namespace_count": 3,
        "size_bytes": 1069169,
        "created_at": "2025-05-14T16:37:25.625540Z"
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>
