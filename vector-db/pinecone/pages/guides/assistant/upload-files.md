---
title: "Upload files"
source: https://docs.pinecone.io/guides/assistant/upload-files
path: guides/assistant/upload-files
---

Upload local files to a Pinecone assistant with Python, JavaScript, or curl, track ingestion operations, and see how uploads are billed as ingestion units.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>

## Upload a local file

You can [upload a file to your assistant](/reference/api/latest/assistant/upload_file) from your local device, as in the following example.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  file = pc.assistants.upload_file(
      assistant_name="example-assistant",
      file_path="/Users/jdoe/Downloads/example_file.txt",
  )
  print(file.status)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = pc.assistant({ name: 'example-assistant' });

  const operation = await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt',
  });

  let { status } = await assistant.describeOperation(operation.id);
  while (status === 'Processing') {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    ({ status } = await assistant.describeOperation(operation.id));
  }
  console.log(status);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -F "file=@$LOCAL_FILE_PATH"
  ```
</CodeGroup>

File uploads are billed in [ingestion units](/guides/assistant/pricing-and-limits#ingestion). With [API version](/reference/api/versioning) `2026-04` or later, upload, upsert, and delete responses return an operation object. Poll [Describe an operation](/reference/api/2026-04/assistant/describe_operation) or [List operations](/reference/api/2026-04/assistant/list_operations) to track progress; when a file-ingestion operation completes, `ingestion_units` may be present on the operation. See [Track file operations](/guides/assistant/manage-files#track-file-operations).

Upload is asynchronous, and it may take several minutes for your assistant to process your file. The Python SDK waits until processing finishes before it returns. The Node.js SDK and the API return an operation, which you can [track](/guides/assistant/manage-files#track-file-operations) until it's no longer `Processing`, as the Node.js example does. You can also [check the status of your file](/guides/assistant/manage-files#get-the-status-of-a-file).

<Tip>
  You can upload a file to an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant you want to upload to and add the file in the Assistant playground.
</Tip>

## Upload a file with metadata

You can upload a file with metadata. Metadata is a dictionary of key-value pairs that you can use to store additional information about the file. For example, you can use metadata to store the file's name, document type, publish date, or any other relevant information.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  file = pc.assistants.upload_file(
      assistant_name="example-assistant",
      file_path="/Users/jdoe/Downloads/example_file.txt",
      metadata={"published": "2024-01-01", "document_type": "manuscript"},
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = pc.assistant({ name: 'example-assistant' });

  const operation = await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt',
    metadata: { published: '2024-01-01', document_type: 'manuscript' },
  });
  console.log(operation.id);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X POST "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -F "file=@$LOCAL_FILE_PATH" \
      -F 'metadata={"published": "2024-01-01", "document_type": "manuscript"}'
  ```
</CodeGroup>

When a file is uploaded with metadata, you can use the metadata to [filter a list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files) and [filter chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).

## Upsert a file

<Note>
  This feature requires [API version](/reference/api/versioning) `2026-04` or later.
</Note>

You can create or replace a file by providing a custom file ID using the [upsert file](/reference/api/2026-04/assistant/upsert_file) endpoint. If a file with the given ID already exists, it's replaced. If not, a new file is created.

File IDs must be 1-128 characters long and can contain alphanumeric characters, hyphens, and underscores.

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="my-custom-file-id"
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X PUT "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
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
    -H "X-Pinecone-Api-Version: 2026-07" \
    -F "file=@$LOCAL_FILE_PATH" \
    -F 'metadata={"published": "2024-01-01", "document_type": "manuscript"}'
  ```
</CodeGroup>

## Upload a PDF with multimodal context

Assistants can gather context from images contained in PDF files. To learn more about this feature, see [Multimodal context for assistants](/guides/assistant/multimodal).

## Upload from a binary stream

You can upload a file directly from an in-memory binary stream using the Python SDK and the [BytesIO class](https://docs.python.org/3/library/io.html#io.BytesIO). Pass the stream as `file_stream`, and set `file_name` to a name with a supported extension, such as `.md`, since the extension determines how the file is processed.

<Note>
  When uploading text-based files (like .txt, .md, .json, etc.) through BytesIO streams, make sure the content is encoded in UTF-8 format.
</Note>

```python Python theme={null}
from io import BytesIO

from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

md_text = "# Title\n\ntext"
stream = BytesIO(md_text.encode("utf-8"))

file = pc.assistants.upload_file(
    assistant_name="example-assistant",
    file_stream=stream,
    file_name="example_file.md",
)
```
