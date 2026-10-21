---
title: "Delete a file"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/delete_file
path: reference/api/2026-07/assistant/delete_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml DELETE /files/{assistant_name}/{assistant_file_id}
[Delete an uploaded file](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file) from an assistant.

This operation is asynchronous. The response includes an operation ID that can be used to poll for completion via the describe operation endpoint.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

pc.assistants.delete_file(
    assistant_name="example-assistant",
    file_id="070513b3-022f-4966-b583-a9b12e0290ff",
)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const operation = await assistant.deleteFile('070513b3-022f-4966-b583-a9b12e0290ff');
console.log(operation);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"
FILE_ID="070513b3-022f-4966-b583-a9b12e0290ff"

curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
