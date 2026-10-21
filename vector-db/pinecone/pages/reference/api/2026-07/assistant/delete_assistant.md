---
title: "Delete an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/delete_assistant
path: reference/api/2026-07/assistant/delete_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_control_2026-07.oas.yaml DELETE /assistants/{assistant_name}
Delete an existing assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#delete-an-assistant)

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

pc.assistants.delete(name="example-assistant")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

await pc.assistants.delete('example-assistant');
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl -X DELETE "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
