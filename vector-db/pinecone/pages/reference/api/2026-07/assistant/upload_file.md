---
title: "Upload a file"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/upload_file
path: reference/api/2026-07/assistant/upload_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml POST /files/{assistant_name}
Upload a file to the specified assistant.

An identifier will be generated. To specify a file identifier or to replace file content, use the upsert endpoint (`PUT /files/{assistant_name}/{assistant_file_id}`).

This operation is asynchronous. The response includes an operation ID that can be used to poll for completion via the describe operation endpoint.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#upload-a-local-file).

<RequestExample>
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
</RequestExample>
