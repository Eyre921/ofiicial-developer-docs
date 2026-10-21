---
title: "List backup schedules"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_backup_schedules
path: reference/api/2026-07/control-plane/list_backup_schedules
---

GET https://api.pinecone.io/indexes/{index_name}/backup-schedules
List all backup schedules configured for a Pinecone serverless index, including schedule IDs, frequency, retention, and next scheduled run times.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

List all backup schedules configured for a specific index.

### Path parameters

**index\_name** `string` *required*

The name of the index to list backup schedules for.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schedules = pc.backup_schedules.list(index_name="docs-example")
print(schedules)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const schedules = await pc.backupSchedules.list('docs-example');
console.log(schedules);
```

```bash curl theme={null}
curl -sS "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
