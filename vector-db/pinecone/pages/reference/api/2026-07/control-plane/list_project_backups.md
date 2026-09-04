---
title: "List backups for all indexes in a project"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_project_backups
path: reference/api/2026-07/control-plane/list_project_backups
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /backups
List all backups for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -H "accept: application/json"
  ```
</RequestExample>
