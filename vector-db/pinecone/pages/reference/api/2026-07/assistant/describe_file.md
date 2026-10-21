---
title: "Describe a file"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/describe_file
path: reference/api/2026-07/assistant/describe_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml GET /files/{assistant_name}/{assistant_file_id}
[Get the current status and metadata of a file](https://docs.pinecone.io/guides/assistant/manage-files#get-the-status-of-a-file) uploaded to an assistant.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

file = pc.assistants.describe_file(
    assistant_name="example-assistant",
    file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a",
    include_url=True,
)
print(file)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const assistant = pc.assistant({ name: 'example-assistant' });
const file = await assistant.describeFile('3c90c3cc-0d44-4b50-8888-8dd25736052a', true);
console.log(file);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
ASSISTANT_NAME="example-assistant"
FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

# Describe a file.
# To get a signed URL in the response, set `include_url` to `true`.
curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
