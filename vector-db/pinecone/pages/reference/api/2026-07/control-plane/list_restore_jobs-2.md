---
title: "List restore jobs"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_restore_jobs
path: reference/api/2026-07/control-plane/list_restore_jobs
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /restore-jobs
List all restore jobs for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/restore-jobs" \
  	-H "X-Pinecone-Api-Version: 2026-07" \
  	-H "Api-Key: $PINECONE_API_KEY"
  ```
</RequestExample>
