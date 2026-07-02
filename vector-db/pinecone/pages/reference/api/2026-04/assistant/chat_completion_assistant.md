---
title: "Chat through an OpenAI-compatible interface"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/chat_completion_assistant
path: reference/api/2026-04/assistant/chat_completion_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml POST /chat/{assistant_name}/chat/completions
Chat with an assistant. This endpoint is based on the OpenAI Chat Completion API, a commonly used and adopted API. 

It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the standard chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
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
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
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
</RequestExample>

<ResponseExample>
  ```JSON Default response theme={null}
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

  ```text Streaming response theme={null}
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
</ResponseExample>
