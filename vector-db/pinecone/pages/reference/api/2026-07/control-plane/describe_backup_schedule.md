---
title: "Describe backup schedule"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_backup_schedule
path: reference/api/2026-07/control-plane/describe_backup_schedule
---

GET https://api.pinecone.io/backup-schedules/{schedule_id}
Retrieve details for a Pinecone backup schedule by schedule ID, including frequency, retention days, next scheduled run, and enabled status.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

Get the details of a specific backup schedule by its ID.

### Path parameters

**schedule\_id** `string` *required*

The ID of the backup schedule.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schedule = pc.backup_schedules.describe(schedule_id="SCHEDULE_ID")
print(schedule)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const schedule = await pc.backupSchedules.describe('SCHEDULE_ID');
console.log(schedule);
```

```bash curl theme={null}
curl -sS "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
