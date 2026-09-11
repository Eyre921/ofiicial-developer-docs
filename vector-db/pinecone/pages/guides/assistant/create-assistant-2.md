---
title: "Create an assistant"
source: https://docs.pinecone.io/guides/assistant/create-assistant
path: guides/assistant/create-assistant
---

Create a Pinecone Assistant with custom instructions, metadata, and region settings using the API, Python SDK, Node.js SDK, or console.

This page shows you how to create an [assistant](/guides/assistant/overview).

You can [create an assistant](/reference/api/latest/assistant/create_assistant), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant", 
      instructions="Use American English for spelling and grammar.", # Description or directive for the assistant to apply to all responses.
      metadata={"team": "customer-support", "version": "1.0"}, # Optional metadata (max 16KB) for organizing assistants.
      region="us", # Region to deploy assistant. Options: "us" (default) or "eu".
      timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.createAssistant({
    name: 'example-assistant',
    instructions: 'Use American English for spelling and grammar.',
    metadata: { team: 'customer-support', version: '1.0' }, // Optional metadata (max 16KB) for organizing assistants.
    region: 'us'
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "region":"us"
  }'
  ```
</CodeGroup>

<Note>
  Instructions (maximum size 16 KB) are included in every chat API call. Longer instructions increase input token costs for each request and consume more of the LLM's context window, reducing available space for retrieved context and conversation history.
</Note>

<Tip>
  You can create an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant/-/files).
</Tip>
