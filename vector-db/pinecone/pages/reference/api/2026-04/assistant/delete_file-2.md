---
title: "Delete a file"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/delete_file
path: reference/api/2026-04/assistant/delete_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml DELETE /files/{assistant_name}/{assistant_file_id}
[Delete an uploaded file](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file) from an assistant.

This operation is asynchronous. The response includes an operation ID that can be used to poll for completion via the describe operation endpoint.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="070513b3-022f-4966-b583-a9b12e0290ff"

  curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "op-7777-ffff-0000",
    "operation_type": "delete_file",
    "file_id": "my-file-id-123",
    "status": "Processing",
    "created_on": "2025-10-01T12:30:00Z",
    "percent_complete": 0
  }
  ```
</ResponseExample>

<Note>
  This example shows a `Processing` operation. The `error_message` field is present only when the operation status is `Failed`.
</Note>
