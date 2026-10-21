---
title: "Describe a restore job"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_restore_job
path: reference/api/2026-07/control-plane/describe_restore_job
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /restore-jobs/{job_id}
Get a description of a restore job.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

restore_job = pc.restore_jobs.describe(job_id="9857add2-99d4-4399-870e-aa7f15d8d326")
print(restore_job)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const restoreJob = await pc.restoreJobs.describe('9857add2-99d4-4399-870e-aa7f15d8d326');
console.log(restoreJob);
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "os"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: os.Getenv("PINECONE_API_KEY"),
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    restoreJob, err := pc.DescribeRestoreJob(ctx, "9857add2-99d4-4399-870e-aa7f15d8d326")
    if err != nil {
        log.Fatalf("Failed to describe restore job: %v", err)
    }

    out, err := json.MarshalIndent(restoreJob, "", "  ")
    if err != nil {
        log.Fatalf("Failed to marshal response: %v", err)
    }
    fmt.Println(string(out))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'accept: application/json'
```
