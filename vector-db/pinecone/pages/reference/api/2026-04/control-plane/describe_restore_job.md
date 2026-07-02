---
title: "Describe a restore job"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/describe_restore_job
path: reference/api/2026-04/control-plane/describe_restore_job
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /restore-jobs/{job_id}
Get a description of a restore job.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
      -H "X-Pinecone-Api-Version: 2026-04" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```
</ResponseExample>
