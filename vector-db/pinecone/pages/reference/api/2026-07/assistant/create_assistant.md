---
title: "Create an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/create_assistant
path: reference/api/2026-07/assistant/create_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_control_2026-07.oas.yaml POST /assistants
Create an assistant. This is where you specify the underlying training model, which cloud provider you would like to deploy with, and more.

For guidance and examples, see [Create an assistant](https://docs.pinecone.io/guides/assistant/create-assistant)

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

assistant = pc.assistants.create(
    name="example-assistant",
    instructions="Use American English for spelling and grammar.",
    metadata={"team": "customer-support", "version": "1.0"},
    region="us",
)
print(assistant.name, assistant.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = await pc.assistants.create({
  name: 'example-assistant',
  instructions: 'Use American English for spelling and grammar.',
  metadata: { team: 'customer-support', version: '1.0' },
  region: 'us',
});
console.log(assistant);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/assistant/assistants" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
  "name": "example-assistant",
  "instructions": "Use American English for spelling and grammar.",
  "metadata": {"team": "customer-support", "version": "1.0"},
  "region":"us"
}'
```
