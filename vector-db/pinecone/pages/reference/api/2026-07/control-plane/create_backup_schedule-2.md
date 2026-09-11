---
title: "Create backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_backup_schedule
path: reference/api/2026-07/control-plane/create_backup_schedule
---

POST https://api.pinecone.io/indexes/{index_name}/backup-schedules
Create a recurring backup schedule for a Pinecone serverless or BYOC index using the API, including daily, weekly, or monthly frequency and retention policy.

<Note>
  This endpoint requires `X-Pinecone-Api-Version: 2026-07`.
</Note>

Create a recurring backup schedule for a serverless or BYOC index. Backups are created automatically based on the specified frequency and expired according to the retention policy. Each index supports one active schedule at a time.

### Path parameters

<ParamField type="string">
  The name of the index to create a backup schedule for.
</ParamField>

### Body parameters

<ParamField type="string">
  A human-readable name for the backup schedule. Backups created by the schedule are automatically named `{name}-{ISO8601_timestamp}`.
</ParamField>

<ParamField type="object">
  The schedule configuration.

  <Expandable title="schedule properties">
    <ParamField type="string">
      The type of schedule. Currently only `time-based` is supported.
    </ParamField>

    <ParamField type="string">
      How often backups are created. One of `daily`, `weekly`, or `monthly`.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField type="object">
  The retention policy for backups created by this schedule.

  <Expandable title="retention properties">
    <ParamField type="integer">
      The number of days after which backups created by this schedule are automatically deleted.
    </ParamField>
  </Expandable>
</ParamField>

### Error responses

| Status | Description                                                                    |
| :----- | :----------------------------------------------------------------------------- |
| 403    | Scheduled backups are not available for your plan.                             |
| 404    | Index not found.                                                               |
| 409    | This index already has an enabled backup schedule. Disable or delete it first. |

<RequestExample>
  ```bash curl theme={null}
  curl -sS -X POST "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
    -H "api-key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "my-nightly-backup",
      "schedule": {
        "type": "time-based",
        "frequency": "daily"
      },
      "retention": {
        "expire_after_days": 7
      }
    }'
  ```
</RequestExample>
