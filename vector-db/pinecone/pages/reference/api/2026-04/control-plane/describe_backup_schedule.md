---
title: "Describe backup schedule"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/describe_backup_schedule
path: reference/api/2026-04/control-plane/describe_backup_schedule
---

GET https://api.pinecone.io/backup-schedules/{schedule_id}
Retrieve details for a Pinecone backup schedule by schedule ID, including frequency, retention days, next scheduled run, and enabled status.

<Note>
  This endpoint requires `X-Pinecone-API-Version: unstable`.
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
    -H "X-Pinecone-API-Version: unstable"
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
    "frequency": "daily",
    "retention_expire_after_days": 7,
    "enabled": true,
    "next_scheduled_run": "2026-04-24T06:00:00+00:00",
    "created_at": "2026-04-23T16:36:51.267528+00:00"
  }
  ```
</ResponseExample>
