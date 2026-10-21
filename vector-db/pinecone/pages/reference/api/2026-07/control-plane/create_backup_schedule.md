---
title: "Create backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_backup_schedule
path: reference/api/2026-07/control-plane/create_backup_schedule
---

POST https://api.pinecone.io/indexes/{index_name}/backup-schedules
Create a recurring backup schedule for a Pinecone serverless or BYOC index using the API, including daily, weekly, or monthly frequency and retention policy.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

Create a recurring backup schedule for a serverless or BYOC index. Backups are created automatically based on the specified frequency and expired according to the retention policy. Each index supports one active schedule at a time.

### Path parameters

**index\_name** `string` *required*

The name of the index to create a backup schedule for.

### Body parameters

**name** `string` *required*

A human-readable name for the backup schedule. Backups created by the schedule are automatically named `{name}-{ISO8601_timestamp}`.

**schedule** `object` *required*

The schedule configuration.

**schedule properties**

**type** `string` *required*

The type of schedule. Currently only `time-based` is supported.

**frequency** `string` *required*

How often backups are created. One of `daily`, `weekly`, or `monthly`.

**retention** `object` *required*

The retention policy for backups created by this schedule.

**retention properties**

**expire\_after\_days** `integer` *required*

The number of days after which backups created by this schedule are automatically deleted.

### Error responses

| Status | Description |
| :- | :- |
| 403 | Scheduled backups are not available for your plan. |
| 404 | Index not found. |
| 409 | This index already has an enabled backup schedule. Disable or delete it first. |

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schedule = pc.backup_schedules.create(
    index_name="docs-example",
    name="example-backup-schedule",
    frequency="daily",
    retention_days=7,
)
print(schedule)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const schedule = await pc.backupSchedules.create('docs-example', {
  name: 'example-backup-schedule',
  frequency: 'daily',
  retentionDays: 7,
});
console.log(schedule);
```

```bash curl theme={null}
curl -sS -X POST "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "example-backup-schedule",
    "schedule": {
      "type": "time-based",
      "frequency": "daily"
    },
    "retention": {
      "expire_after_days": 7
    }
  }'
```
