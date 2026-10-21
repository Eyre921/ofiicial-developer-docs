---
title: "Describe an operation"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/describe_operation
path: reference/api/2026-07/assistant/describe_operation
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml GET /operations/{assistant_name}/{operation_id}
Get the status of an operation.


```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

operation = pc.assistants.describe_operation(
    assistant_name="example-assistant",
    operation_id="op-1234-abcd-5678",
)
print(operation.status, operation.percent_complete)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const operation = await assistant.describeOperation('op-1234-abcd-5678');
console.log(operation);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"
OPERATION_ID="op-1234-abcd-5678"

curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME/$OPERATION_ID" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```

> [!NOTE]
>
> Operation responses may include `error_message`, but only when the operation status is `Failed`.
