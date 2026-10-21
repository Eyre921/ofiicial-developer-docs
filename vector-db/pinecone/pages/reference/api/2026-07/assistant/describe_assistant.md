---
title: "Check assistant status"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/describe_assistant
path: reference/api/2026-07/assistant/describe_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_control_2026-07.oas.yaml GET /assistants/{assistant_name}
Get the status of an assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#get-the-status-of-an-assistant)

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

assistant = pc.assistants.describe(name="example-assistant")
print(assistant)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = await pc.assistants.describe('example-assistant');
console.log(assistant);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
