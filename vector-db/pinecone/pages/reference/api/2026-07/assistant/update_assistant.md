---
title: "Update an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/update_assistant
path: reference/api/2026-07/assistant/update_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_control_2026-07.oas.yaml PATCH /assistants/{assistant_name}
Update an existing assistant. You can modify the assistant's instructions.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#add-instructions-to-an-assistant).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

assistant = pc.assistants.update(
    name="example-assistant",
    instructions="Use American English for spelling and grammar.",
    metadata={"team": "customer-support", "version": "1.1"},
)
print(assistant)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = await pc.assistants.update({
  name: 'example-assistant',
  instructions: 'Use American English for spelling and grammar.',
  metadata: { team: 'customer-support', version: '1.1' },
});
console.log(assistant);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl -X PATCH "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
  "instructions": "Use American English for spelling and grammar.",
  "metadata": {"team": "customer-support", "version": "1.1"}
}'
```
