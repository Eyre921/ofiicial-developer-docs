---
title: "Retrieve context from an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/context_assistant
path: reference/api/2026-07/assistant/context_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml POST /chat/{assistant_name}/context
Retrieve context snippets from an assistant to use as part of RAG or any agentic flow.

For guidance and examples, see [Retrieve context snippets](https://docs.pinecone.io/guides/assistant/retrieve-context-snippets).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

response = pc.assistants.context(
    assistant_name="example-assistant",
    query="Who is the CFO of Netflix?",
)
for snippet in response.snippets:
    print(snippet.score, snippet.content)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const response = await assistant.context({
  query: 'Who is the CFO of Netflix?',
});
console.log(response.snippets);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "query": "Who is the CFO of Netflix?"
}'
```
