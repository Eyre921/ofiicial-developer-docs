---
title: "Upsert a file"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/upsert_file
path: reference/api/2026-07/assistant/upsert_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml PUT /files/{assistant_name}/{assistant_file_id}
Create or replace a file in the specified assistant. If a file with the given `assistant_file_id` already exists, it will be replaced with the new file. If it doesn't exist, a new file will be created with that identifier.

This operation is asynchronous. The file processing will occur in the background.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#upload-a-local-file).

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
