---
title: "Delete backup schedule"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/delete_backup_schedule
path: reference/api/2026-04/control-plane/delete_backup_schedule
---

DELETE https://api.pinecone.io/backup-schedules/{schedule_id}
Delete a backup schedule for a Pinecone serverless index using the API by schedule ID, while preserving all previously created backup snapshots.

<Note>
  This endpoint requires `X-Pinecone-API-Version: unstable`.
</Note>

Delete a backup schedule. This does **not** delete any backups that were previously created by the schedule.

### Path parameters

<ParamField type="string">
  The ID of the backup schedule to delete.
</ParamField>

<RequestExample>
  ```bash curl theme={null}
  curl -sS -o /dev/null -w "%{http_code}\n" -X DELETE \
    "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}" \
    -H "api-key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-API-Version: unstable"
  ```
</RequestExample>

<ResponseExample>
  ```text curl theme={null}
  204
  ```
</ResponseExample>
