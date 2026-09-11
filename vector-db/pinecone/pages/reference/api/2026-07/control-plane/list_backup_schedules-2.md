---
title: "List backup schedules"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_backup_schedules
path: reference/api/2026-07/control-plane/list_backup_schedules
---

GET https://api.pinecone.io/indexes/{index_name}/backup-schedules
List all backup schedules configured for a Pinecone serverless index, including schedule IDs, frequency, retention, and next scheduled run times.

<Note>
  This endpoint requires `X-Pinecone-Api-Version: 2026-07`.
</Note>

List all backup schedules configured for a specific index.

### Path parameters

<ParamField type="string">
  The name of the index to list backup schedules for.
</ParamField>

<RequestExample>
  ```bash curl theme={null}
  curl -sS "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
    -H "api-key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
