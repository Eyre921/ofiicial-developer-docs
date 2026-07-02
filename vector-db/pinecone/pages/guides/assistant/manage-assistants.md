---
title: "Manage assistants"
source: https://docs.pinecone.io/guides/assistant/manage-assistants
path: guides/assistant/manage-assistants
---

View, update, and delete, and check the status of assistants.

## List assistants for a project

You can [get the name, status, and metadata for each assistant](/reference/api/latest/assistant/list_assistants) in your project as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistants = pc.assistant.list_assistants()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistants = await pc.listAssistants();
  console.log(assistants);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON theme={null}
{
  "assistants": [
    {
      "name": "example-assistant",
      "instructions": "Use American English for spelling and grammar.",
      "metadata": {"team": "customer-support", "version": "1.0"},
      "status": "Initializing",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z"
    }
  ]
}
```

You can use the `name` value to [check the status of an assistant](/guides/assistant/manage-assistants#get-the-status-of-an-assistant).

<Tip>
  You can list assistants using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant/-/files).
</Tip>

## Get the status of an assistant

You can [get the status and metadata for your assistant](/reference/api/latest/assistant/describe_assistant) as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.describe_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.describeAssistant('example-assistant');
  console.log(assistant);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON theme={null}
{
  "name": "example-assistant",
  "instructions": "Use American English for spelling and grammar.",
  "metadata": {"team": "customer-support", "version": "1.0"},
  "status": "Initializing",
  "created_at": "2023-11-07T05:31:56Z",
  "updated_at": "2023-11-07T05:31:56Z"
}
```

The `status` field has the following possible values:

* Initializing
* Failed
* Ready
* Terminating

<Tip>
  You can check the status of an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>

## Change an assistant's chat model

The chat model is the underlying large language model (LLM) that powers the assistant's responses. You can change the chat model for an existing assistant through the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant):

1. On the **Assistants** page, select the assistant you want to update.
2. In the sidebar on the right, select **Settings** (gear icon).
3. Select the **Chat model**.

## Add instructions to an assistant

You can [add or update the instructions](/reference/api/latest/assistant/update_assistant) for an existing assistant. Instructions are a short description or directive for the assistant to apply to all of its responses. For example, you can update the instructions to reflect the assistant's role or purpose.

<Note>
  Instructions (maximum size 16 KB) are included in every chat API call. Longer instructions increase input token costs for each request and consume more of the LLM's context window, reducing available space for retrieved context and conversation history.
</Note>

For example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key=YOUR_API_KEY)

  assistant = pc.assistant.update_assistant(
      assistant_name="example-assistant", 
      instructions="Use American English for spelling and grammar.",
      metadata={"team": "customer-support", "version": "1.1"} # Optional metadata (max 16KB) for organizing assistants.
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.updateAssistant('example-assistant', {
    instructions: 'Use American English for spelling and grammar.',
    metadata: { team: 'customer-support', version: '1.1' }, // Optional metadata (max 16KB) for organizing assistants.
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X PATCH "https://api.pinecone.io/assistant/assistants/example-assistant" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.1"}
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```JSON theme={null}
{
    "name":"example-assistant",
    "instructions":"Use American English for spelling and grammar.",
    "metadata":{"team": "customer-support", "version": "1.1"},
    "status":"Ready",
    "created_at":"2024-06-14T14:58:06.573004549Z",
    "updated_at":"2024-10-01T19:44:32.813235817Z"
}
```

<Tip>
  You can add or update instructions for an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>

## Delete an assistant

You can [delete an assistant](/reference/api/latest/assistant/delete_assistant) as in the following example:

<Warning>
  Deleting an assistant also deletes all files uploaded to the assistant.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.assistant.delete_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.deleteAssistant('example-assistant');
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X DELETE "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

<Tip>
  You can delete an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant).
</Tip>
