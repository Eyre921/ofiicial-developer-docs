---
title: "List operations"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/list_operations
path: reference/api/2026-07/assistant/list_operations
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml GET /operations/{assistant_name}
List all operations for an assistant. Returns operations that are in progress, as well as recently completed or failed operations.

Both successful and failed operations are retained for 30 days after completion.

Use the `operation_type` and `status` query parameters to filter results.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

for operation in pc.assistants.list_operations(assistant_name="example-assistant"):
    print(operation.operation_id, operation.operation_type, operation.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const { operations } = await assistant.listOperations();
console.log(operations);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

# List all operations
curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"

# Filter by status
# curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME?status=Processing" \
#   -H "Api-Key: $PINECONE_API_KEY" \
#   -H "X-Pinecone-Api-Version: 2026-07"
```
