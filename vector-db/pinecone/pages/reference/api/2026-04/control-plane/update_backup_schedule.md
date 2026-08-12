---
title: "Update backup schedule"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/update_backup_schedule
path: reference/api/2026-04/control-plane/update_backup_schedule
---

PATCH https://api.pinecone.io/backup-schedules/{schedule_id}
Update a Pinecone backup schedule using the API, including pausing with enabled, changing frequency, and adjusting the retention expire_after_days.

<Note>
  This endpoint requires `X-Pinecone-API-Version: unstable`.
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
    -H "X-Pinecone-API-Version: unstable" \
    -H "Content-Type: application/json" \
    -d '{
      "enabled": false,
      "frequency": "weekly",
      "retention": { "expire_after_days": 14 }
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "schedule_id": "c688ed12-5a39-4254-9518-bd394b7f4886",
    "name": "my-nightly-backup",
    "index_id": "d40265e4-a492-402b-9cf1-973b4908b7a0",
    "project_id": "cc95c601-bf08-4973-9a1d-a65a1b528759",
    "schedule_type": "time-based",
    "frequency": "weekly",
    "retention_expire_after_days": 14,
    "enabled": false,
    "next_scheduled_run": "2026-04-24T06:00:00+00:00",
    "created_at": "2026-04-23T16:36:51.267528+00:00"
  }
  ```
</ResponseExample>
