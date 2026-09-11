---
title: "Describe backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_backup_schedule
path: reference/api/2026-07/control-plane/describe_backup_schedule
---

GET https://api.pinecone.io/backup-schedules/{schedule_id}
Retrieve details for a Pinecone backup schedule by schedule ID, including frequency, retention days, next scheduled run, and enabled status.

<Note>
  This endpoint requires `X-Pinecone-Api-Version: 2026-07`.
</Note>

Get the details of a specific backup schedule by its ID.

### Path parameters

<ParamField type="string">
  The ID of the backup schedule.
</ParamField>

<RequestExample>
  ```bash curl theme={null}
  curl -sS "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}" \
    -H "api-key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
