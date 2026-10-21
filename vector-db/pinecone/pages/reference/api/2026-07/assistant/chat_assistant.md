---
title: "Chat with an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/chat_assistant
path: reference/api/2026-07/assistant/chat_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml POST /chat/{assistant_name}
Chat with an assistant and get back citations in structured form. 

This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references than the OpenAI-compatible chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

```python Python | Default theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

response = pc.assistants.chat(
    assistant_name="example-assistant",
    messages=[{"role": "user", "content": "What is the inciting incident of Pride and Prejudice?"}],
    model="gpt-4o",
)
print(response.message.content)
```

```python Python | Streaming theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

stream = pc.assistants.chat(
    assistant_name="example-assistant",
    messages=[{"role": "user", "content": "What is the inciting incident of Pride and Prejudice?"}],
    model="gpt-4o",
    stream=True,
)
for fragment in stream.text():
    print(fragment, end="", flush=True)
```

```javascript JavaScript | Default theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const response = await assistant.chat({
  messages: [{ role: 'user', content: 'What is the inciting incident of Pride and Prejudice?' }],
  model: 'gpt-4o',
});
console.log(response.message?.content);
```

```javascript JavaScript | Streaming theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const stream = await assistant.chatStream({
  messages: [{ role: 'user', content: 'What is the inciting incident of Pride and Prejudice?' }],
  model: 'gpt-4o',
});
for await (const chunk of stream) {
  if (chunk.type === 'content_chunk') {
    process.stdout.write(chunk.delta.content);
  }
}
```

```bash curl | Default theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is the inciting incident of Pride and Prejudice?"
    }
  ],
  "stream": false,
  "model": "gpt-4o"
}'
```

```bash curl | Streaming theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is the inciting incident of Pride and Prejudice?"
    }
  ],
  "stream": true,
  "model": "gpt-4o"
}'
```
