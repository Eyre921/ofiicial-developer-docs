---
title: "List API keys"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/list_api_keys
path: reference/api/2026-04/admin-assistant/list_api_keys
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/projects/{project_id}/api-keys
List all API keys in a project.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const { data: apiKeys } = await admin.apiKeys.list('YOUR_PROJECT_ID');
  console.log(apiKeys);
  ```

  ```go Go theme={null}
  // Requires Go SDK v6.0.0 or later
  package main

  import (
      "context"
      "fmt"
      "log"
      "os"

      "github.com/pinecone-io/go-pinecone/v6/pinecone"
  )

  func main() {
      ctx := context.Background()

      adminClient, err := pinecone.NewAdminClientWithContext(ctx, pinecone.NewAdminClientParams{
          ClientId:     os.Getenv("PINECONE_CLIENT_ID"),
          ClientSecret: os.Getenv("PINECONE_CLIENT_SECRET"),
      })
      if err != nil {
          log.Fatalf("Failed to create AdminClient: %v", err)
      }

      apiKeys, err := adminClient.APIKey.List(ctx, "YOUR_PROJECT_ID")
      if err != nil {
          log.Fatalf("Failed to list API keys: %v", err)
      }
      for _, apiKey := range apiKeys {
          fmt.Printf("API key: %v (%v)\n", apiKey.Name, apiKey.Id)
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_PROJECT_ID="YOUR_PROJECT_ID"

  curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "roles": [
          "ProjectEditor"
        ]
      }
    ]
  }
  ```
</ResponseExample>
