---
title: "Update backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/update_backup_schedule
path: reference/api/2026-07/control-plane/update_backup_schedule
---

PATCH https://api.pinecone.io/backup-schedules/{schedule_id}
Update a Pinecone backup schedule using the API, including pausing with enabled, changing frequency, and adjusting the retention expire_after_days.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

Update a backup schedule. Send only the fields you want to change. All body fields are optional.

### Path parameters

**schedule\_id** `string` *required*

The ID of the backup schedule to update.

### Body parameters

**enabled** `boolean`

Whether the schedule is enabled. Set to `false` to pause the schedule without deleting it.

**frequency** `string`

How often backups are created. One of `daily`, `weekly`, or `monthly`.

**retention** `object`

The retention policy for backups created by this schedule.

**retention properties**

**expire\_after\_days** `integer`

The number of days after which backups created by this schedule are automatically deleted.

```bash curl theme={null}
curl -sS -X PATCH "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": false,
    "frequency": "weekly",
    "retention": { "expire_after_days": 14 }
  }'
```
