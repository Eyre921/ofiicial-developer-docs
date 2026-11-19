---
title: "Describe a conversion job"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_conversion_job
path: reference/api/2026-07/control-plane/describe_conversion_job
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /conversion-jobs/{job_id}
Get the status and progress of a conversion job.

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
JOB_ID="670e8400-e29b-41d4-a716-446655440001"

curl "https://api.pinecone.io/conversion-jobs/$JOB_ID" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H 'accept: application/json'
```
