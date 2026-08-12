---
title: "Multimodal context for assistants"
source: https://docs.pinecone.io/guides/assistant/multimodal
path: guides/assistant/multimodal
---

Enable multimodal PDF context in Pinecone Assistant to analyze charts, images, and diagrams using OCR and visual understanding for RAG.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Pinecone assistants support multimodal context, allowing them to understand and respond to questions about images embedded in PDF documents.

This enables use cases like:

* Analyzing charts, graphs, and diagrams in financial reports
* Understanding infographics and visual data in research papers
* Interpreting visual layouts in technical documentation

When working with multimodal PDFs, assistants attempt to filter out purely decorative images (such as example logos, background graphics, generic stock photos), so they can focus on images that contain meaningful information.

Additionally, assistants use Optical Character Recognition (OCR) to extract text from images. This allows them to read and analyze scanned PDFs (PDFs that contain images of text, but no actual embedded text).

## How it works

When you enable multimodal context for a PDF:

1. Pinecone extracts text and images (raster or vector) from the file and analyzes their contents. For each image, the assistant generates a descriptive caption and set of keywords. Additionally, when it makes sense, the assistant captures data points found in the image (for example, values from a table or chart).
2. During chat or context queries, the assistant searches for relevant text and image context it captured when analyzing the PDF. Image context can include the original image data (base64-encoded).
3. The assistant passes this context to the LLM, which uses it to generate responses.

<Note>
  For an overview of how Pinecone Assistant works, see [Pinecone Assistant architecture](/reference/architecture/assistant-architecture).
</Note>

## Try it out

The following steps demonstrate how to create an assistant, provide it with a PDF that contains images, and then query that assistant using chat and context APIs.

<Note>
  All versions of Pinecone's Assistant API allow you to upload multimodal PDFs.
</Note>

### 1. Create an assistant

First, if you don't have one, [create an assistant](/reference/api/2025-10/assistant/create_assistant):

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant-multimodal", 
      instructions="You are a helpful assistant that can understand both text and images in documents.",
      region="us",
      timeout=30
  )

  print(f"Type: {type(assistant).__name__}")
  pprint(assistant)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
          "name": "example-assistant-multimodal",
          "instructions": "You are a helpful assistant that can understand both text and images in documents.",
          "region": "us"
        }'
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  Type: AssistantModel
  {'created_at': '2025-08-28T23:35:26.917953498Z',
    'host': 'https://prod-1-data.ke.pinecone.io',
    'instructions': 'You are a helpful assistant that can understand both text '
                    'and images in documents.',
    'metadata': {},
    'name': 'example-assistant-multimodal',
    'status': 'Ready',
    'updated_at': '2025-08-28T23:35:28.507639215Z'}
  ```

  ```json curl theme={null}
  {
    "name": "example-assistant-multimodal",
    "instructions": "You are a helpful assistant that can understand both text and images in documents.",
    "metadata": null,
    "status": "Initializing",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-08-18T23:18:52.858197495Z",
    "updated_at": "2025-08-18T23:18:52.858198077Z"
  }
  ```
</CodeGroup>

<Note>
  You don't need to create a new assistant to use multimodal context. Existing assistants can enable multimodal context for newly uploaded PDFs, as described in [the next section](#2-upload-a-multimodal-pdf).
</Note>

### 2. Upload a multimodal PDF

To enable multimodal context for a PDF, when [uploading the file](/reference/api/2025-10/assistant/upload_file), set the `multimodal` URL parameter to true (defaults to false).

<Tip>
  To improve retrieval accuracy for images found in uploaded PDFs, include relevant contextual text on the same page as each image. For example:

  * **Graphs and charts**: Include nearby text explaining the experiment, methodology, or data being visualized.
  * **Diagrams**: Add descriptive labels or explanations adjacent to technical diagrams.
  * **Tables**: Provide context about what the data represents and any relevant methodology.

  The assistant uses surrounding text when generating captions that are later passed to the LLM, so placing relevant context near images improves caption quality and retrieval accuracy.
</Tip>

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")

  # timeout=None allows the SDK to wait for file processing to complete before returning.
  # This parameter is only available in the SDK, not in direct API calls.
  file_model = assistant.upload_file(
      file_path="./document.pdf",
      multimodal=True,
      timeout=None
  )

  pprint(file_model)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"
  LOCAL_FILE_PATH="/path/to/your/document.pdf"

  curl -X POST "https://$ASSISTANT_HOST/assistant/files/$ASSISTANT_NAME?multimodal=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  FileModel(
    name='document.pdf',
    id='9c322597-58d6-4ebc-84b5-a398b620da01',
    metadata=None,
    created_on='2025-08-28T23:41:41.982805815Z',
    updated_on='2025-08-28T23:42:09.562949544Z',
    status='Available',
    signed_url=None,
    size=1236044.0
  )
  ```

  ```json curl theme={null}
  {
    "id": "op-1234-abcd-5678",
    "operation_type": "upload_file",
    "file_id": "9c322597-58d6-4ebc-84b5-a398b620da01",
    "status": "Processing",
    "created_on": "2025-08-28T23:41:41.982805815Z",
    "percent_complete": 0
  }
  ```
</CodeGroup>

<Note>
  * The `multimodal` parameter is only available for PDF files.
  * Upload is asynchronous. To check the status, use the [describe operation](/reference/api/2026-04/assistant/describe_operation) endpoint or [track file operations](/guides/assistant/manage-files#track-file-operations).
  * If upload processing fails, you'll need to re-upload the file.
</Note>

### 3. Chat with the assistant

Now, [chat with your assistant](/reference/api/2025-10/assistant/chat_assistant). To tell the assistant to provide image-related context to the LLM:

* Set the `multimodal` request parameter to true (default) in the `context_options` object. Setting `multimodal` to false means the LLM only receives text snippets.
* When `multimodal` is true, use `include_binary_content` to specify what image context the LLM should receive: base64 image data and captions (true) or captions only (false).

<Note>
  Sending image-related context to the LLM (whether captions, base64 data, or both) increases token usage. Learn about [monitoring spend and usage](/guides/assistant/admin/monitor-spend-and-usage).
</Note>

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone("YOUR_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")

  msg = Message(
      role="user", 
      content="Describe the symbol on the paper tray that indicates the maximum fill level."
  )

  chat_response = assistant.chat(
    messages=[msg],
    context_options={
        "multimodal": True,
        "include_binary_content": True,
        "top_k": 10,
        "snippet_size": 2048
    }
  )

  pprint(chat_response)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$ASSISTANT_HOST/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
          "messages": [
            {
              "role": "user",
              "content": "Describe the symbol on the paper tray that indicates the maximum fill level."
            }
          ],
          "context_options": {
            "multimodal": true,
            "include_binary_content": true,
            "top_k": 10,
            "snippet_size": 2048
          }
        }'
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  ChatResponse(
    id='00000000000000000fe49626f3ee5164', 
    model='gpt-4o-2024-11-20', 
    usage=Usage(
      prompt_tokens=8703, 
      completion_tokens=41, 
      total_tokens=8744
    ), 
    message=Message(
      content='The symbol on the paper tray that indicates...', 
      role='assistant'
    ), 
    finish_reason='stop', 
    citations=[
      Citation(
        position=209, 
        references=[
          Reference(
              file=FileModel(
                name='document.pdf', 
                id='9c322597-58d6-4ebc-84b5-a398b620da01', 
                metadata=None, 
                created_on='2025-08-28T23:41:41.982805815Z', 
                updated_on='2025-08-28T23:42:09.562949544Z', 
                status='Available', 
                signed_url='https://storage.googleapis.com/...',
                size=1236044.0,
                multimodal=True
            ), 
            pages=[3, 4, 5, 6, 7, 8, 9, 10, 11], 
            highlight=None
          )
        ]
      )
    ]
  )
  ```

  ```json curl theme={null}
  {
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "The symbol on the paper tray that indicates..."
    },
    "id": "0000000000000000d904dfd3dd4f4597"
    "model": "gpt-4o-2024-11-20",
    "usage": {
      "prompt_tokens": 8414,
      "completion_tokens": 42,
      "total_tokens": 8456
    },
    "citations": [
      {
        "position": 213,
        "references": [
          {
            "file": {
              "status": "Available",
              "id": "a89f678c-9ceb-40ec-8fc7-23913e560b37",
              "name": "document.pdf",
              "size": 1236044,
              "metadata": null,
              "multimodal": true,
              "updated_on": "2025-08-18T23:21:59.697988967Z",
              "created_on": "2025-08-18T23:21:36.498381046Z",
              "signed_url": "https://storage.googleapis.com/..."
            },
            "pages": [ 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
            "highlight": null
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

<Warning>
  If your assistant uses multimodal context snippets to generate a response, no [highlights](/guides/assistant/chat-with-assistant#include-citation-highlights-in-the-response) are returned—even when `include_highlights` is true.
</Warning>

### 4. Query for context

To query context for a custom RAG workflow, you can [retrieve context snippets](/reference/api/2025-10/assistant/context_assistant) directly. Then, you can pass these snippets to an LLM as context.

To fetch image-related context snippets (as well as text snippets), set the `multimodal` request parameter to true (default). When `multimodal` is true, use `include_binary_content` to specify what image context you'd like to receive: base64 image data and captions (true) or captions only (false).

<CodeGroup>
  ```Python Python theme={null}
  from pprint import pprint
  from pinecone import Pinecone

  pc = Pinecone("PINECONE_API_KEY") 
  assistant = pc.assistant.Assistant(assistant_name="example-assistant-multimodal")
  context_response = assistant.context(
      query="Describe the symbol on the paper tray that indicates the maximum fill level.",
      multimodal=True,
      include_binary_content=True
  )

  pprint(context_response)
  ```

  ```bash curl theme={null}
  ASSISTANT_HOST="YOUR_ASSISTANT_HOST"
  ASSISTANT_NAME="example-assistant-multimodal"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$ASSISTANT_HOST/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "Describe the symbol on the paper tray that indicates the maximum fill level.",
      "multimodal": true,
      "include_binary_content": true
    }'
  ```
</CodeGroup>

<Note>
  If you set `multimodal` to true and `include_binary_content` to false, image objects are not returned in the snippets. If you set `multimodal` to false, only text snippets are returned.
</Note>

Response:

<CodeGroup>
  ```shell Python theme={null}
  # Formatted for readability
  ContextResponse(
    id='00000000000000001e3ef84bd493e612', 
    snippets=[
      MultimodalSnippet(
        type='multimodal', 
        content=[
          TextBlock(type='text', text="..."), 
          ImageBlock(
            type='image', 
            caption='...', 
            image=Image(mime_type='image/jpeg', data='...', type='base64')), 
          // ...
        ], 
        score=0.16321887, 
        reference=PdfReference(
          type='pdf', 
          pages=[3, 4, 5, 6, 7, 8, 9, 10, 11], 
          file=FileModel(
            name='document.pdf', 
            id='9c322597-58d6-4ebc-84b5-a398b620da01', 
            metadata=None, 
            created_on='2025-08-28T23:41:41.982805815Z', 
            updated_on='2025-08-28T23:42:09.562949544Z', 
            status='Available', 
            signed_url='https://storage.googleapis.com/...',
            size=1236044,
            multimodal=True
          )
        )
      ), 
      // ...
    ], 
    usage=TokenCounts(
      prompt_tokens=7061, 
      completion_tokens=0, 
      total_tokens=7061
    )
  )
  ```

  ```json curl theme={null}
  {
    "snippets": [
      {
        "type": "multimodal",
        "content": [
          {
            "type": "text",
            "text": "# The Online User's Guide..."
          },
          {
            "type": "image",
            "caption": "An image of a control panel...",
            "image": {
              "type": "base64",
              "mime_type": "image/jpeg",
              "data": "..."
            }
          },
          // ...
        ],
        "score": 0.16775002,
        "reference": {
          "type": "pdf",
          "file": {
            "status": "Available",
            "id": "a89f678c-9ceb-40ec-8fc7-23913e560b37",
            "name": "document.pdf",
            "size": 1236044,
            "metadata": null,
            "multimodal": true,
            "updated_on": "2025-08-18T23:21:59.697988967Z",
            "created_on": "2025-08-18T23:21:36.498381046Z",
            "signed_url": "https://storage.googleapis.com/..."
          },
          "pages": [ 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
        }
      },
      // ...
    ],
    "usage": {
      "prompt_tokens": 6778,
      "completion_tokens": 0,
      "total_tokens": 6778
    },
    "id": "000000000000000005b9cd91b1c5446d"
  } 
  ```
</CodeGroup>

<Note>
  Snippets are returned based on their semantic relevance to the provided query. When you set `multimodal` to true, you'll receive the most relevant snippets, regardless of the types of content they contain. You can receive text snippets, multimodal snippets, or both.
</Note>

## Limits

Multimodal context for assistants is only available for PDF files. Additionally, the following limits apply:

Multimodal PDF processing uses the same [ingestion unit](/guides/assistant/pricing-and-limits#ingestion) as standard uploads; it is billed at about **twice** the standard per-unit rate (see [Pricing and limits](/guides/assistant/pricing-and-limits)). Object and rate limits for assistants also apply—see [#limits](/guides/assistant/pricing-and-limits#limits) and [#rate-limits](/guides/assistant/pricing-and-limits#rate-limits).

| Metric        | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------ | :----------- | :----------- | :------------ | :-------------- |
| Max file size | 10 MB        | 10 MB        | 50 MB         | 50 MB           |
| Page limit    | 100          | 100          | 100           | 100             |

To learn about other assistant-related limits, see [Pinecone Assistant limits](/guides/assistant/pricing-and-limits).
