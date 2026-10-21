---
title: "List Files"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/list_files
path: reference/api/2026-07/assistant/list_files
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml GET /files/{assistant_name}
List all files in an assistant, with an option to filter files with metadata.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#list-files-in-an-assistant).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

for file in pc.assistants.list_files(assistant_name="example-assistant"):
    print(file.id, file.name, file.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const { files } = await assistant.listFiles();
console.log(files);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"

curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
