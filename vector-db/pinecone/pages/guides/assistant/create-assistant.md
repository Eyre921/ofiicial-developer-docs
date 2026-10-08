---
title: "Create an assistant"
source: https://docs.pinecone.io/guides/assistant/create-assistant
path: guides/assistant/create-assistant
---

Create a Pinecone Assistant with custom instructions, metadata, and region settings using the API, Python SDK, Node.js SDK, or console.

This page shows you how to create an [assistant](/guides/assistant/overview).

You can [create an assistant](/reference/api/latest/assistant/create_assistant) with the following parameters:

* `name`: A name for the assistant, unique within the project.
* `instructions`: A directive the assistant applies to every response it gives.
* `metadata`: Optional key-value pairs, up to 16 KB, that help you organize assistants.
* `region`: Where the assistant is deployed, `us` (default) or `eu`. You can't change it later.

The Python SDK waits until the assistant is ready before it returns. The Node.js SDK and the API return right away, while the assistant's status is still `Initializing`. To find out when it's ready, [get the status of the assistant](/guides/assistant/manage-assistants#get-the-status-of-an-assistant).

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistants.create(
      name="example-assistant",
      instructions="Use American English for spelling and grammar.",
      metadata={"team": "customer-support", "version": "1.0"},
      region="us",
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.assistants.create({
    name: 'example-assistant',
    instructions: 'Use American English for spelling and grammar.',
    metadata: { team: 'customer-support', version: '1.0' },
    region: 'us',
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
