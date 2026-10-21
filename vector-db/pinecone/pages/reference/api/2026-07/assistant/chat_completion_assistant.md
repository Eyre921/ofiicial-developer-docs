---
title: "Chat through an OpenAI-compatible interface"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/chat_completion_assistant
path: reference/api/2026-07/assistant/chat_completion_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml POST /chat/{assistant_name}/chat/completions
Chat with an assistant. This endpoint is based on the OpenAI Chat Completion API, a commonly used and adopted API. 

It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the standard chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

```python Python | Default theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

response = pc.assistants.chat_completions(
    assistant_name="example-assistant",
    messages=[{"role": "user", "content": "What is the maximum height of a red pine?"}],
)
print(response.choices[0].message.content)
```

```python Python | Streaming theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

stream = pc.assistants.chat_completions(
    assistant_name="example-assistant",
    messages=[{"role": "user", "content": "What is the maximum height of a red pine?"}],
    stream=True,
)
for chunk in stream:
    for choice in chunk.choices:
        if choice.delta.content:
            print(choice.delta.content, end="", flush=True)
```

```javascript JavaScript | Default theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const response = await assistant.chatCompletion({
  messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
});
console.log(response.choices?.[0]?.message?.content);
```

```javascript JavaScript | Streaming theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const stream = await assistant.chatCompletionStream({
  messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
});
for await (const chunk of stream) {
  for (const choice of chunk.choices) {
    if (choice.delta.content) {
      process.stdout.write(choice.delta.content);
    }
  }
}
```

```bash curl | Default theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is the maximum height of a red pine?"
    }
  ]
}'
```

```bash curl | Streaming theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is the maximum height of a red pine?"
    }
  ],
  "stream": true
}'
```
