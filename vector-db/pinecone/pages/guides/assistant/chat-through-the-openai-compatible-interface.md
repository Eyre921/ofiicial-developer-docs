---
title: "Chat through the OpenAI-compatible interface"
source: https://docs.pinecone.io/guides/assistant/chat-through-the-openai-compatible-interface
path: guides/assistant/chat-through-the-openai-compatible-interface
---

Integrate OpenAI-compatible chat interface with Pinecone Assistant.

After [uploading files](/guides/assistant/manage-files) to an assistant, you can chat with the assistant.

This page shows you how to chat with an assistant using the [OpenAI-compatible chat interface](/reference/api/latest/assistant/chat_completion_assistant). This interface is based on the OpenAI Chat Completion API, a commonly used and adopted API. It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the [standard chat interface](/guides/assistant/chat-with-assistant).

<Tip>
  The [standard chat interface](/guides/assistant/chat-with-assistant) is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references.
</Tip>

## Chat with an assistant

The [OpenAI-compatible chat interface](/reference/api/latest/assistant/chat_completion_assistant) can return responses in two different formats:

* [Default response](#default-response): The assistant returns a response in a single string field, which includes citation information.
* [Streaming response](#streaming-response): The assistant returns the response as a text stream.

### Default response

The following example sends a message and requests a response in the default format:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content='What is the maximum height of a red pine?')]
  response = assistant.chat_completions(messages=chat_context)

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';

  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
        messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
      });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ]
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```JSON theme={null}
{"chat_completion":
  {
    "id":"chatcmpl-9OtJCcR0SJQdgbCDc9JfRZy8g7VJR",
    "choices":[
      {
        "finish_reason":"stop",
        "index":0,
        "message":{
          "role":"assistant",
          "content":"The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
        }
      }
    ],
    "model":"my_assistant"
  }
}
```

### Streaming response

Streaming responses can improve perceived latency by allowing users to see content as it's generated, rather than waiting for the complete response. This creates a more responsive chat experience, especially for longer responses.

The following example sends a message and requests a streaming response:

<Note>
  The `content` parameter in the request cannot be empty.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant" 
  )

  # Streaming chat with the Assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(messages=[chat_context], stream=True)

  for data in response:
      if data:
          print(data)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletionStream({
      messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }]
  });

  for await (const response of chatResp) {
      if (response) {
          console.log(response);
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
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
</CodeGroup>

The example above returns a result like the following:

```json theme={null}
{
  'id': '000000000000000009de65aa87adbcf0', 
  'choices': [
      {
      'index': 0, 
      'delta': 
        {
        'role': 'assistant', 
        'content': 'The'
        }, 
      'finish_reason': None
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}

...

{
  'id': '00000000000000007a927260910f5839',
  'choices': [
      {
      'index': 0,
      'delta':
        {
          'role': '', 
          'content': 'The'
        }, 
      'finish_reason': None
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}

...

{
  'id': '00000000000000007a927260910f5839', 
  'choices': [
    {
      'index': 0, 
      'delta': 
        {
        'role': None, 
        'content': None
        }, 
      'finish_reason': 'stop'
      }
    ], 
  'model': 'gpt-4o-2024-05-13'
}
```

There are three types of messages in a chat completion response:

* **Message start**: Includes `"role":"assistant"`, which indicates that the assistant is responding to the user's message.
* **Content**: Includes a value in the `content` field (e.g., `"content":"The"`), which is part of the assistant's streamed response to the user's message.
* **Message end**: Includes `"finish_reason":"stop"`, which indicates that the assistant has finished responding to the user's message.

## Extract the response content

In the assistant's response, the message string is contained in the following JSON object:

* `choices.[0].message.content` for the default chat response
* `choices[0].delta.content` for the streaming chat response

You can extract the message content and print it to the console:

<Tabs>
  <Tab title="Default response">
    <CodeGroup>
      ```python Python theme={null}
      print(str(response.choices[0].message.content))
      ```

      ```bash curl theme={null}
      | jq '.choices.[0].message.content'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash theme={null}
    A red pine, scientifically known as *Pinus resinosa*, is a medium-sized tree that can grow up to 25 meters high and 75 centimeters in diameter. [1, pp. 1]
    ```
  </Tab>

  <Tab title="Streaming response">
    <CodeGroup>
      ```python Python theme={null}
      for data in response:
          if data:
              print(str(data.choices[0].delta.content))
      ```

      ```bash curl theme={null}
      |  sed -u 's/.*"content":"\([^"]*\)".*/\1/'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash Streaming response theme={null}
    The
     maximum
     height
     of
     a
     red
     pine
     (
    Pin
    us
     resin
    osa
    )
     is
     up
     to
     twenty
    -five
     meters

     [1, pp. 1]
    .
    ```
  </Tab>
</Tabs>

## Choose a model

Pinecone Assistant supports the following models:

* `gpt-4o` (default)
* `gpt-4.1`
* `gpt-5`
* `o4-mini`
* `claude-sonnet-4-5`
* `gemini-2.5-pro`

<Note>
  Anthropic has [deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations) the Claude 3.5 Sonnet and Claude 3.7 Sonnet models. Assistant automatically routes chat requests that specify `claude-3-5-sonnet` or `claude-3-7-sonnet` to `claude-sonnet-4-5` at the same price.
</Note>

<Tip>
  For chat applications, we recommend using GPT models (`gpt-4o`, `gpt-4.1`, `gpt-5`, or `o4-mini`) as they typically provide faster response times compared to other models.
</Tip>

To choose a non-default model for your assistant, set the `model` parameter in the request:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(
      messages=chat_context, 
      model="gpt-4.1"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    model: 'gpt-4.1',
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "model": "gpt-4.1"
  }'
  ```
</CodeGroup>

## Filter chat with metadata

You can [filter which documents to use for chat completions](/guides/assistant/files-overview#file-metadata). The following example filters the responses to use only documents that include the metadata `"resource": "encyclopedia"`.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(messages=chat_context, stream=True, filter={"resource": "encyclopedia"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    filter: {
      'resource': 'encyclopedia'
    }
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true,
    "filter": 
      {
      "resource": "encyclopedia"
      }
    }'
  ```
</CodeGroup>

## Set the sampling temperature

<Note>
  This is available in API versions `2025-04` and later.
</Note>

Temperature is a parameter that controls the randomness of a model's predictions during text generation. Lower temperatures (\~0.0) yield more consistent, predictable answers, while higher temperatures increase the model's explanatory power and is generally better for creative tasks.

To control the sampling temperature for a model, set the `temperarture` parameter in the request. If a model does not support a temperature parameter, the parameter is ignored.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat_completions(
      messages=[msg], 
      temperature=0.8
  )

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    temperature: 0.8,
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO of Netflix?"
      }
    ],
    "temperature": 0.8
  }'
  ```
</CodeGroup>
