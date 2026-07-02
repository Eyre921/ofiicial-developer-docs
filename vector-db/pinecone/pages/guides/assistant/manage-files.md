---
title: "Manage files"
source: https://docs.pinecone.io/guides/assistant/manage-files
path: guides/assistant/manage-files
---

List, check status, and delete files from your assistant.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>

## List files in an assistant

### View all files

You can [get the status, ID, and metadata for each file in your assistant](/reference/api/latest/assistant/list_files), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant.
  files = assistant.list_files()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles();
  console.log(files);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON theme={null}
{
  "files": [
    {
      "status": "Available",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "example_file.txt",
      "size": 1073470,
      "metadata": {},
      "updated_on": "2025-07-16T16:46:40.787204651Z",
      "created_on": "2025-07-16T16:45:59.414273474Z",
      "signed_url": null
    }
  ]
}
```

You can use the `id` value to [check the status of an individual file](#get-the-status-of-a-file).

<Tip>
  You can list file in an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant and view the files in the Assistant playground.
</Tip>

### View a filtered list of files

Metadata filter expressions can be included when listing files. This will limit the list of files to only those matching the filter expression. Use the `filter` parameter to specify the metadata filter expression.

For more information about filtering with metadata, see [Understanding files](/guides/assistant/files-overview#metadata-query-language).

The following example lists files that are a manuscript:

<CodeGroup>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant that match the metadata filter.
  files = assistant.list_files(filter={"document_type":"manuscript"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles({
    filter: { document_type: 'manuscript' },
  });
  console.log(files);

  // You can also use filter operators:
  // const files = await assistant.listFiles({
  //   filter: { document_type: { '$ne': 'manuscript' } },
  // });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  ENCODED_METADATA="%7B%22document_type%22%3A%20%22manuscript%22%7D" # URL encoded metadata - See w3schools.com/tags/ref_urlencode.ASP

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME?filter=$ENCODED_METADATA" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

## Get the status of a file

You can [get the status and metadata for your assistant](/reference/api/latest/assistant/describe_file), as in the following example:

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

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `True`.
  file = assistant.describe_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a", include_url=True)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const fileId = "3c90c3cc-0d44-4b50-8888-8dd25736052a";

  // Describe a file. Returns a signed URL by default. 
  const file = await assistant.describeFile(fileId)
  // To exclude signed URL, set `includeUrl` to `false`.
  // const includeUrl = false;
  // const file = await assistant.describeFile(fileId, includeUrl)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `true`.
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON theme={null}
{
  "status": "Available",
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "example_file.txt",
  "size": 1073470,
  "metadata": {},
  "updated_on": "2025-07-16T16:46:40.787204651Z",
  "created_on": "2025-07-16T16:45:59.414273474Z",
  "signed_url": "https://storage.googleapis.com/..."
}
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>

<Tip>
  You can check the status a file using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, click the file for more details.
</Tip>

## Track file operations

<Note>
  This feature requires [API version](/reference/api/versioning) `2026-04` or later.
</Note>

File uploads, upserts, and deletes are asynchronous. Each action returns an **operation** object that you can poll for status and progress.

Use [List operations](/reference/api/2026-04/assistant/list_operations) and [Describe an operation](/reference/api/2026-04/assistant/describe_operation) for the HTTP API. Example requests:

<CodeGroup>
  ```bash List operations theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```

  ```bash Describe operation theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  OPERATION_ID="op-1234-abcd-5678"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME/$OPERATION_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</CodeGroup>

Operation status values include **Processing** (use `percent_complete` for progress), **Completed**, and **Failed** (the response may include `error_message`). The `percent_complete` field on operations replaces `percent_done` on the file model; ingestion usage for completed file work may appear as **`ingestion_units`** on the operation.

## Delete a file

You can [delete a file](/reference/api/latest/assistant/delete_file) from an assistant.

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Delete a file from your assistant.
  assistant.delete_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);

  const file = await assistant.deleteFile("070513b3-022f-4966-b583-a9b12e0290ff")
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

* Once a file is deleted, you cannot recover it.
* With [API version](/reference/api/versioning) `2026-04` or later, delete is asynchronous and returns an operation ID. You can [track file operations](#track-file-operations) to monitor progress.
* You cannot delete a file while it is still processing.
* You can also delete a file from an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, find the file and click the **ellipsis (...) menu > Delete**.

## Track file operations

<Note>
  This feature requires [API version](/reference/api/versioning) `2026-04` or later.
</Note>

File uploads, upserts, and deletes are asynchronous operations. Each of these actions returns an operation object that you can poll for status and progress.

### List operations

You can [list all operations](/reference/api/2026-04/assistant/list_operations) for an assistant:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</CodeGroup>

This returns a list of operations:

```JSON theme={null}
{
  "operations": [
    {
      "id": "op-1234-abcd-5678",
      "operation_type": "upload_file",
      "file_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "status": "Completed",
      "created_on": "2025-10-01T12:00:00Z",
      "completed_on": "2025-10-01T12:05:00Z",
      "percent_complete": 100
    },
    {
      "id": "op-8765-dcba-4321",
      "operation_type": "upsert_file",
      "file_id": "my-custom-file-id",
      "status": "Processing",
      "created_on": "2025-10-01T12:30:00Z",
      "percent_complete": 45
    }
  ]
}
```

### Describe an operation

You can [get the status of a specific operation](/reference/api/2026-04/assistant/describe_operation):

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  OPERATION_ID="op-1234-abcd-5678"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME/$OPERATION_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</CodeGroup>

```JSON theme={null}
{
  "id": "op-1234-abcd-5678",
  "operation_type": "upload_file",
  "file_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "status": "Completed",
  "created_on": "2025-10-01T12:00:00Z",
  "completed_on": "2025-10-01T12:05:00Z",
  "percent_complete": 100
}
```

### Operation status values

Operations can have the following status values:

* **Processing**: The operation is in progress. Use `percent_complete` to track progress.
* **Completed**: The operation finished successfully.
* **Failed**: The operation failed. In this case, the operation response includes `error_message`.

<Note>
  The `percent_complete` field on operations replaces the `percent_done` field that was previously on the file model. Similarly, `error_message` appears on failed operations, not on the file model.
</Note>
