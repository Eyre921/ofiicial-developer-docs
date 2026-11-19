---
title: "List conversion jobs"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_conversion_jobs
path: reference/api/2026-07/control-plane/list_conversion_jobs
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /conversion-jobs
List the project's conversion jobs, newest first.

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/conversion-jobs?limit=10" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H 'accept: application/json'
```
