---
title: "Update backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/update_backup_schedule
path: reference/api/2026-07/control-plane/update_backup_schedule
---

PATCH https://api.pinecone.io/backup-schedules/{schedule_id}
Update a Pinecone backup schedule using the API, including pausing with enabled, changing frequency, and adjusting the retention expire_after_days.

<Note>
  This endpoint requires `X-Pinecone-Api-Version: 2026-07`.
</Note>

Update a backup schedule. Send only the fields you want to change. All body fields are optional.

### Path parameters

<ParamField type="string">
  The ID of the backup schedule to update.
</ParamField>

### Body parameters

<ParamField type="boolean">
  Whether the schedule is enabled. Set to `false` to pause the schedule without deleting it.
</ParamField>

<ParamField type="string">
  How often backups are created. One of `daily`, `weekly`, or `monthly`.
</ParamField>

<ParamField type="object">
  The retention policy for backups created by this schedule.

  <Expandable title="retention properties">
    <ParamField type="integer">
      The number of days after which backups created by this schedule are automatically deleted.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
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
</RequestExample>
