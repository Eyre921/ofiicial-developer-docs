---
title: "Upload files"
source: https://docs.pinecone.io/guides/assistant/upload-files
path: guides/assistant/upload-files
---

Upload local files to an assistant.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>

## Upload a local file

You can [upload a file to your assistant](/reference/api/latest/assistant/upload_file) from your local device, as in the following example.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get an assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Upload a file.
  response = assistant.upload_file(
      file_path="/Users/jdoe/Downloads/example_file.txt",
      timeout=None
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt'
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

File uploads are billed in [ingestion units](/guides/assistant/pricing-and-limits#ingestion). With [API version](/reference/api/versioning) `2026-04` or later, upload, upsert, and delete responses return an operation object. Poll [Describe an operation](/reference/api/2026-04/assistant/describe_operation) or [List operations](/reference/api/2026-04/assistant/list_operations) to track progress; when a file-ingestion operation completes, `ingestion_units` may be present on the operation. See [Track file operations](/guides/assistant/manage-files#track-file-operations).

Upload is asynchronous and returns an operation ID. It may take several minutes for your assistant to process your file. You can [track file operations](/guides/assistant/manage-files#track-file-operations) to monitor progress, or [check the status of your file](/guides/assistant/manage-files#get-the-status-of-a-file) to determine if it is ready to use.

<Tip>
  You can upload a file to an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant you want to upload to and add the file in the Assistant playground.
</Tip>

## Upload a file with metadata

You can upload a file with metadata. Metadata is a dictionary of key-value pairs that you can use to store additional information about the file. For example, you can use metadata to store the file's name, document type, publish date, or any other relevant information.

<CodeGroup>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get the assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Upload a file.
  response = assistant.upload_file(
      file_path="/Users/jdoe/Downloads/example_file.txt",
      metadata={"published": "2024-01-01", "document_type": "manuscript"},
      timeout=None
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt',
    metadata: { 'published': '2024-01-01', 'document_type': 'manuscript' },
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -F "file=@$LOCAL_FILE_PATH" \
      -F 'metadata={"published": "2024-01-01", "document_type": "manuscript"}'
  ```
</CodeGroup>

When a file is uploaded with metadata, you can use the metadata to [filter a list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files) and [filter chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).

## Upsert a file

<Note>
  This feature requires [API version](/reference/api/versioning) `2026-04` or later.
</Note>

You can create or replace a file by providing a custom file ID using the [upsert file](/reference/api/2026-04/assistant/upsert_file) endpoint. If a file with the given ID already exists, it is replaced. If not, a new file is created.

File IDs must be 1-128 characters long and can contain alphanumeric characters, hyphens, and underscores.

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="my-custom-file-id"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X PUT "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

Upsert is asynchronous and returns an operation ID. You can [track file operations](/guides/assistant/manage-files#track-file-operations) to monitor progress.

## Upsert a file with metadata

You can upsert a file with metadata by including it as a field in the multipart form:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="my-custom-file-id"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X PUT "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -F "file=@$LOCAL_FILE_PATH" \
    -F 'metadata={"published": "2024-01-01", "document_type": "manuscript"}'
  ```
</CodeGroup>

## Upload a PDF with multimodal context

Assistants can gather context from images contained in PDF files. To learn more about this feature, see [Multimodal context for assistants](/guides/assistant/multimodal).

## Upload from a binary stream

You can upload a file directly from an in-memory binary stream using the Python SDK and the [BytesIO class](https://docs.python.org/3/library/io.html#io.BytesIO).

<Note>
  When uploading text-based files (like .txt, .md, .json, etc.) through BytesIO streams, make sure the content is encoded in UTF-8 format.
</Note>

```python Python theme={null}
from pinecone import Pinecone
from io import BytesIO

pc = Pinecone(api_key="YOUR_API_KEY")

# Get an assistant
assistant = pc.assistant.Assistant(
    assistant_name="example-assistant", 
)

# Create a BytesIO stream with some content
md_text = "# Title\n\ntext"
# Note: Assistant currently supports only utf-8 for text-based files
stream = BytesIO(md_text.encode("utf-8"))

# Upload the stream
response = assistant.upload_bytes_stream(
    stream=stream,
    file_name="example_file.md",
    timeout=None
)
```
