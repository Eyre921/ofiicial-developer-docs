---
title: "Chat through the standard interface"
source: https://docs.pinecone.io/guides/assistant/chat-with-assistant
path: guides/assistant/chat-with-assistant
---

Chat with your assistant using the standard interface and API.

After [uploading files](/guides/assistant/manage-files) to an assistant, you can chat with the assistant.

<Tip>
  You can chat with an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant to chat with, and use the Assistant playground.
</Tip>

## Chat through the standard interface

The [standard chat interface](/reference/api/latest/assistant/chat_assistant) can return responses in three different formats:

* [Default response](#default-response): The assistant returns a structured response and separate citation information.
* [Streaming response](#streaming-response): The assistant returns the response as a text stream.
* [JSON response](#json-response): The assistant returns the response as JSON key-value pairs.

<Tip>
  This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references. However, if you need your assistant to be OpenAI-compatible or need inline citations, use the [OpenAI-compatible chat interface](#chat-through-the-openai-compatible-interface).
</Tip>

### Default response

The following example sends a message and requests a default response:

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
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat(messages=[msg])

  # Alternatively, you can provide a dictionary as the message:
  # msg = {"role": "user", "content": "Who is the CFO of Netflix?"}
  # response = assistant.chat(messages=[msg])

  print(response)

  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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
    "stream": false,
    "model": "gpt-4o"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```json JSON theme={null}
{
    "finish_reason": "stop",
    "message": {
        "role": "assistant",
        "content": "The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
    },
    "id": "00000000...",
    "model": "gpt-4o-2024-11-20",
    "usage": {
        "prompt_tokens": 23633,
        "completion_tokens": 24,
        "total_tokens": 23657
    },
    "citations": [
        {
            "position": 63,
            "references": [
                {
                    "file": {
                        "status": "Available",
                        "id": "76a11dd1...",
                        "name": "Netflix-10-K-01262024.pdf",
                        "size": 1073470,
                        "metadata": {
                            "company": "netflix",
                            "document_type": "form 10k"
                        },
                        "updated_on": "2025-07-16T16:46:40.787204651Z",
                        "created_on": "2025-07-16T16:45:59.414273474Z",
                        "signed_url": "https://storage.googleapis.com/..."
                    },
                    "pages": [
                        78,
                        79,
                        80
                    ],
                    "highlight": null
                }
            ]
        }
    ]
}
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>

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

  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="What is the inciting incident of Pride and Prejudice?")

  response = assistant.chat(messages=[msg], stream=True)

  for data in response:
      if data:
          print(data)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';

  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatStream({
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

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
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
</CodeGroup>

The example above returns a result like the following:

```shell theme={null}
data:{"type":"message_start","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","role":"assistant"}

data:{"type":"content_chunk","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","delta":{"content":"The"}}

...

data:{"type":"citation","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","citation":{"position":406,"references":[{"file":{"status":"Available","id":"ae79e447-b89e-4994-994b-3232ca52a654","name":"Pride-and-Prejudice.pdf","size":2973077,"metadata":null,"updated_on":"2024-06-14T15:01:57.385425746Z","created_on":"2024-06-14T15:01:02.910452398Z","signed_url":"https://storage.googleapis.com/..."},"pages":[1]}]}}

data:{"type":"message_end","id":"0000000000000000111b35de85e8a8f9","model":"gpt-4o-2024-05-13","finish_reason":"stop","usage":{"prompt_tokens":9736,"completion_tokens":102,"total_tokens":9838}}
```

There are four types of messages in a streaming chat response:

* **Message start**: Includes `"role":"assistant"`, which indicates that the assistant is responding to the user's message.
* **Content**: Includes a value in the `content` field (e.g., `"content":"The"`), which is part of the assistant's streamed response to the user's message.
* **Citation**: Includes a citation to the document that the assistant used to generate the response.
* **Message end**: Includes `"finish_reason":"stop"`, which indicates that the assistant has finished responding to the user's message.

### JSON response

The following example uses the `json_response` parameter to instruct the assistant to return the response as JSON key-value pairs. This is useful if you need to parse the response programmatically.

<Note>
  JSON response cannot be used with the `stream` parameter.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  import json
  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO and CEO of Netflix?")

  response = assistant.chat(messages=[msg], json_response=True)

  print(json.loads(response))
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO and CEO of Netflix?', json_response: true }],
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "Who is the CFO and CEO of Netflix?"
      }
    ],
    "json_response": true,
    "model": "gpt-4o"
  }'
  ```
</CodeGroup>

The example above returns a result like the following:

```json theme={null}
{
  "finish_reason": "stop",
  "message": {
    "role": "assistant",
    "content": "{\"CFO\": \"Spencer Neumann\", \"CEO\": \"Ted Sarandos and Greg Peters\"}"
  },
  "id": "0000000000000000680c95d2faab7aad",
  "model": "gpt-4o-2024-11-20",
  "usage": {
    "prompt_tokens": 14298,
    "completion_tokens": 42,
    "total_tokens": 14340
  },
  "citations": [
    {
      "position": 24,
      "references": [
        {
          "file": {
            "status": "Available",
            "id": "cbecaa37-2943-4030-b4d6-ce4350ab774a",
            "name": "Netflix-10-K-01262024.pdf",
            "size": 1073470,
            "metadata": {
              "test-key": "test-value"
            },
            "updated_on": "2025-01-24T16:53:17.148820770Z",
            "created_on": "2025-01-24T16:52:44.851577534Z",
            "signed_url": "https://storage.googleapis.com/knowledge-prod-files/bf0dcf22..."
          },
          "pages": [
            79
          ],
          "highlight": null
        },
    ...
  ]
}
```

## Extract the response content

In the assistant's response, the message string is contained in the following JSON object:

* `message.content` for the default chat response
* `delta.content` for the streaming chat response
* `message.content` for the JSON response

You can extract the message content and print it to the console:

<Tabs>
  <Tab title="Default response">
    <CodeGroup>
      ```python Python theme={null}
      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg])

      print(str(response.message.content))
      ```

      ```javascript JavaScript theme={null}
      const assistant = pc.Assistant(assistantName);
      const chatResp = await assistant.chat({
        messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
      });
      console.log(chatResp.message.content);
      ```

      ```bash curl theme={null}
      | jq '.message.content'
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
      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg], stream=True)

      for data in response:
          if hasattr(data, "delta"):
              print(data.delta.content)
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

  <Tab title="JSON response">
    <CodeGroup>
      ```python Python theme={null}
      import json

      msg = Message(role="user", content="What is the maximum height of a red pine?")

      response = assistant.chat(messages=[msg], json_response=True)

      print(json.loads(response.message.content))
      ```

      ```bash curl theme={null}
      |  sed -u 's/.*"content":"\([^"]*\)".*/\1/'
      ```
    </CodeGroup>

    This creates output like the following:

    ```bash JSON response theme={null}
    {'red pine': 'A red pine, scientifically known as *Pinus resinosa*, is a medium-sized tree that can grow up to 25 meters high and 75 centimeters in diameter.'}
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
  response = assistant.chat(
      messages=chat_context, 
      model="gpt-4.1"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }],
    model: 'gpt-4.1',
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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

## Provide conversation history

Models lack memory of previous requests, so any relevant messages from earlier in the conversation must be present in the `messages` object.

In the following example, the `messages` object includes prior messages that are necessary for interpreting the newest message.

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
  chat_context = [
      Message(content="What is the maximum height of a red pine?", role="user"),
      Message(content="The maximum height of a red pine (Pinus resinosa) is up to 25 meters.", role="assistant"),
      Message(content="What is its maximum diameter?", role="user")
  ]
  response = assistant.chat(messages=chat_context)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY " \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      },
      {
        "role": "assistant",
        "content": "The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
      },
      {
        "role": "user",
        "content": "What is its maximum diameter?"
      }
    ]
  }'
  ```
</CodeGroup>

The example returns a response like the following:

```JSON theme={null}
{
  "finish_reason":"stop",
  "message":{
    "role":"assistant",
    "content":"The maximum diameter of a red pine (Pinus resinosa) is up to 1 meter."
    },
    "id":"0000000000000000236a24a17e55309a",
    "model":"gpt-4o-2024-05-13",
    "usage":{
      "prompt_tokens":21377,
      "completion_tokens":20,
      "total_tokens":21397
      },
      "citations":[...]
}
```

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
  response = assistant.chat(messages=chat_context, stream=True, filter={"resource": "encyclopedia"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
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

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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

## Control the context size

<Note>
  This is available in API versions `2025-04` and later.
</Note>

To limit the number of [input tokens](/guides/assistant/pricing-and-limits#token-usage) used, you can control the context size by tuning `top_k * snippet_size`. These parameters can be adjusted by setting [`context_options`](/reference/api/latest/assistant/chat_assistant#body-context-options) in the request:

* `snippet_size`: Controls the max size of a snippet (default is 2048 tokens). Note that snippet size can vary and, in rare cases, may be bigger than the set `snippet_size`. Snippet size controls the amount of context the model is given for each chunk of text.
* `top_k`: Controls the max number of context snippets sent to the LLM (default is 16). `top_k` controls the diversity of information sent to the model.

While additional tokens will be used for other parameters (e.g., the system prompt, chat input), adjusting the `top_k` and `snippet_size` can help manage token consumption.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="Who is the CFO of Netflix?")
  response = assistant.chat(messages=[msg], context_options={"snippet_size": 2500, "top_k": 10})

  print(response)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    contextOptions: { topK: 10, snippetSize: 2500 },
  });

  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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
    "context_options": {
      "top_k":10,
      "snippet_size":2500
      }
  }'
  ```
</CodeGroup>

The example will return up to 10 snippets and each snippet will be up to 2500 tokens in size.

<Tip>
  To better understand the context retrieved using these parameters, you can [retrieve context from an assistant](/reference/api/latest/assistant/context_assistant).
</Tip>

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
  response = assistant.chat(
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
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
    temperature: 0.8,
  });
  console.log(chatResp);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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

## Include citation highlights in the response

<Note>
  Citation highlights are available in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant) or API versions `2025-04` and later.
</Note>

When using the [standard chat interface](/reference/api/latest/assistant/chat_assistant), every response includes a `citation` object. The object includes a reference to the document that the assistant used to generate the response. Additionally, you can include highlights, which are the specific parts of the document that the assistant used to generate the response, by setting the `include_highlights` parameter to `true` in the request:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
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
  "stream": false,
  "model": "gpt-4o",
  "include_highlights": true
}'
```

The example returns response like the following:

```json theme={null}
{
  "finish_reason":"stop",
  "message":{
    "role":"assistant",
    "content":"The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
    },
    "id":"00000000000000006685b07087b1ad42",
    "model":"gpt-4o-2024-05-13",
    "usage":{
      "prompt_tokens":12490,
      "completion_tokens":33,
      "total_tokens":12523
      },
      "citations":[{
        "position":63,
        "references":[{
          "file":{
            "status":"Available",
            "id":"cbecaa37-2943-4030-b4d6-ce4350ab774a",
            "name":"Netflix-10-K-01262024.pdf",
            "size":1073470,
            "metadata":{"test-key":"test-value"},
            "updated_on":"2025-01-24T16:53:17.148820770Z",
            "created_on":"2025-01-24T16:52:44.851577534Z",
            "signed_url":"https://storage.googleapis.com/knowledge-prod-files/b..."
            },
            "pages":[78],
            "highlight":{
              "type":"text",
              "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that:"
              }
            },
            {
              "file":{
                "status":"Available",
                "id":"cbecaa37-2943-4030-b4d6-ce4350ab774a",
                "name":"Netflix-10-K-01262024.pdf",
                "size":1073470,
                "metadata":{"test-key":"test-value"},
                "updated_on":"2025-01-24T16:53:17.148820770Z",
                "created_on":"2025-01-24T16:52:44.851577534Z",
                "signed_url":"https://storage.googleapis.com/knowledge-prod-files/bf..."
                },
                "pages":[79],
                "highlight":{
                  "type":"text",
                  "content":"operations of\nNetflix, Inc.\nDated: January 26, 2024  By:  /S/ SPENCER NEUMANN\n  Spencer Neumann\n  Chief Financial Officer"
                }
            }
          ]
        }
      ]
}
```

<Note>
  Enabling highlights will increase token usage.
</Note>
