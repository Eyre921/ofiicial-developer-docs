---
title: "List restore jobs"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_restore_jobs
path: reference/api/2026-07/control-plane/list_restore_jobs
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /restore-jobs
List all restore jobs for a project.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

restore_jobs = pc.restore_jobs.list()
print(restore_jobs)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const restoreJobs = await pc.restoreJobs.list();
console.log(restoreJobs);
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

    restoreJobs, err := pc.ListRestoreJobs(ctx, nil)
    if err != nil {
        log.Fatalf("Failed to list restore jobs: %v", err)
    }

    out, err := json.MarshalIndent(restoreJobs, "", "  ")
    if err != nil {
        log.Fatalf("Failed to marshal response: %v", err)
    }
    fmt.Println(string(out))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/restore-jobs" \
	-H "X-Pinecone-Api-Version: 2026-07" \
	-H "Api-Key: $PINECONE_API_KEY"
```
