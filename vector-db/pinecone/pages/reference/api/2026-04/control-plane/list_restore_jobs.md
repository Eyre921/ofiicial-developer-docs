---
title: "List restore jobs"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_restore_jobs
path: reference/api/2026-04/control-plane/list_restore_jobs
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /restore-jobs
List all restore jobs for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/restore-jobs" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Api-Key: $PINECONE_API_KEY"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
        "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
        "target_index_name": "restored-index",
        "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
        "status": "Completed",
        "created_at": "2025-04-25T18:14:05.227526Z",
        "completed_at": "2025-04-25T18:14:11.074618Z",
        "percent_complete": 100
      },
      {
        "restore_job_id": "69acc1d0-9105-4fcb-b1db-ebf97b285c5e",
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "target_index_name": "restored-index2",
        "target_index_id": "e6c0387f-33db-4227-9e91-32181106e56b",
        "status": "Completed",
        "created_at": "2025-05-14T17:25:59.378989Z",
        "completed_at": "2025-05-14T17:26:23.997284Z",
        "percent_complete": 100
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>
