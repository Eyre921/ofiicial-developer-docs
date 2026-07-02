---
title: "Chat with an assistant"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/chat_assistant
path: reference/api/2026-04/assistant/chat_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml POST /chat/{assistant_name}
Chat with an assistant and get back citations in structured form. 

This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references than the OpenAI-compatible chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
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
    -H "X-Pinecone-Api-Version: 2026-04" \
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
</RequestExample>

<ResponseExample>
  ```json Default response theme={null}
  {
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "The inciting incident of \"Pride and Prejudice\" occurs when Mrs. Bennet informs Mr. Bennet that Netherfield Park has been let at last, and she is eager to share the news about the new tenant, Mr. Bingley, who is wealthy and single. This sets the stage for the subsequent events of the story, including the introduction of Mr. Bingley and Mr. Darcy to the Bennet family and the ensuing romantic entanglements."
    },
    "id": "00000000000000004ac3add5961aa757",
    "model": "gpt-4o-2024-05-13",
    "usage": {
      "prompt_tokens": 9736,
      "completion_tokens": 105,
      "total_tokens": 9841
    },
    "citations": [
      {
        "position": 406,
        "references": [
          {
            "file": {
              "status": "Available",
              "id": "ae79e447-b89e-4994-994b-3232ca52a654",
              "name": "Pride-and-Prejudice.pdf",
              "size": 2973077,
              "metadata": null,
              "updated_on": "2024-06-14T15:01:57.385425746Z",
              "created_on": "2024-06-14T15:01:02.910452398Z",
              "signed_url": "https://storage.googleapis.com/..."
            },
            "pages": [
              1
            ]
          }
        ]
      }
    ]
  }

  ```

  ```text Streaming response theme={null}
  data:{
    "type":"message_start",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "role":"assistant"
  }

  data:
  {
    "type":"content_chunk",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "delta":
    {
      "content":"The"
      }
  }

  ...

  data:
  {
    "type":"citation",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "citation":
    {
      "position":406,
      "references":
      [
        {
          "file":{
            "status":"Available",
            "id":"ae79e447-b89e-4994-994b-3232ca52a654",
            "name":"Pride-and-Prejudice.pdf",
            "size":2973077,
            "metadata":null,
            "updated_on":"2024-06-14T15:01:57.385425746Z",
            "created_on":"2024-06-14T15:01:02.910452398Z",
            "signed_url":"https://storage.googleapis.com/..."
            },
        "pages":[1]
        }
      ]
    }
  }

  data:
  {
    "type":"message_end",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "finish_reason":"stop",
    "usage":
    {
      "prompt_tokens":9736,
      "completion_tokens":102,
      "total_tokens":9838
      }
  }
  ```
</ResponseExample>
