---
title: "Create an API key"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/create_api_key
path: reference/api/2026-04/admin-assistant/create_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/projects/{project_id}/api-keys
Create an API key for a project to authenticate Data Plane and Control Plane requests.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  // `value` is returned only at creation time and cannot be retrieved later
  const apiKey = await admin.apiKeys.create('YOUR_PROJECT_ID', {
    name: 'Example API Key',
    roles: ['ProjectEditor'],
  });
  console.log(apiKey);
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

      adminClient, err := pinecone.NewAdminClientWithContext(ctx, pinecone.NewAdminClientParams{})
      if err != nil {
          log.Fatalf("Failed to create AdminClient: %v", err)
      }

      roles := []string{"ProjectEditor"}
      apiKey, err := adminClient.APIKey.Create(ctx, "YOUR_PROJECT_ID", &pinecone.CreateAPIKeyParams{
          Name:  "Example API Key",
          Roles: &roles,
      })
      if err != nil {
          log.Fatalf("Failed to create API key: %v", err)
      }
      // Value is returned only at creation time and cannot be retrieved later
      fmt.Printf("Successfully created API key: %v\n", apiKey.Key.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  resource "pinecone_api_key" "example" {
    name       = "Example API Key"
    project_id = "YOUR_PROJECT_ID"
    roles      = ["ProjectEditor"]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_PROJECT_ID="YOUR_PROJECT_ID"

  curl "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "Example API Key",
  		"roles": ["ProjectEditor"]
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Example API key",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "roles": [
        "ProjectEditor"
      ]
    },
    "value": "string"
  }
  ```
</ResponseExample>
