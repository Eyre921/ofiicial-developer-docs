---
title: "List assistants"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/list_assistants
path: reference/api/2026-07/assistant/list_assistants
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_control_2026-07.oas.yaml GET /assistants
List of all assistants in a project.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#list-assistants-for-a-project).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

for assistant in pc.assistants.list():
    print(assistant.name, assistant.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const { assistants } = await pc.assistants.list();
console.log(assistants);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X GET "https://api.pinecone.io/assistant/assistants" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
