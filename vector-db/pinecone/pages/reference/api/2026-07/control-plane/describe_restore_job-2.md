---
title: "Describe a restore job"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_restore_job
path: reference/api/2026-07/control-plane/describe_restore_job
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /restore-jobs/{job_id}
Get a description of a restore job.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json'
  ```
</RequestExample>
