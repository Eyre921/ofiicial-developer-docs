---
title: "Delete backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/delete_backup_schedule
path: reference/api/2026-07/control-plane/delete_backup_schedule
---

DELETE https://api.pinecone.io/backup-schedules/{schedule_id}
Delete a backup schedule for a Pinecone serverless index using the API by schedule ID, while preserving all previously created backup snapshots.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

Delete a backup schedule. This does **not** delete any backups that were previously created by the schedule.

### Path parameters

**schedule\_id** `string` *required*

The ID of the backup schedule to delete.

```bash curl theme={null}
curl -sS -o /dev/null -w "%{http_code}\n" -X DELETE \
  "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
