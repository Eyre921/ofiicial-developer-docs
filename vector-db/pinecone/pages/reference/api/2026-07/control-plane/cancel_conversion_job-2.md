---
title: "Cancel a conversion job"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/cancel_conversion_job
path: reference/api/2026-07/control-plane/cancel_conversion_job
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /conversion-jobs/{job_id}/cancel
Cancel a conversion job that is `Pending` or `InProgress`. The job stops, and the index it was filling is left in the `InitializationFailed` state; delete it to free its name.

Cancelling a job that has already ended has no effect. The response is the job as it stands after the request, so a repeated cancel returns the same result.

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
JOB_ID="670e8400-e29b-41d4-a716-446655440001"

curl -X POST "https://api.pinecone.io/conversion-jobs/$JOB_ID/cancel" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H 'accept: application/json'
```
