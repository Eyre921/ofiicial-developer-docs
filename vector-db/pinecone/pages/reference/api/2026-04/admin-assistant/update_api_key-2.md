---
title: "Update an API key"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/update_api_key
path: reference/api/2026-04/admin-assistant/update_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml patch /admin/api-keys/{api_key_id}
Update an API key's name and roles.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const apiKey = await admin.apiKeys.update('YOUR_API_KEY_ID', {
    name: 'New API key name',
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

      adminClient, err := pinecone.NewAdminClientWithContext(ctx, pinecone.NewAdminClientParams{
          ClientId:     os.Getenv("PINECONE_CLIENT_ID"),
          ClientSecret: os.Getenv("PINECONE_CLIENT_SECRET"),
      })
      if err != nil {
          log.Fatalf("Failed to create AdminClient: %v", err)
      }

      name := "New API key name"
      roles := []string{"ProjectEditor"}
      apiKey, err := adminClient.APIKey.Update(ctx, "YOUR_API_KEY_ID", &pinecone.UpdateAPIKeyParams{
          Name:  &name,
          Roles: &roles,
      })
      if err != nil {
          log.Fatalf("Failed to update API key: %v", err)
      }
      fmt.Printf("Successfully updated API key: %v\n", apiKey.Name)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Change the name or roles on an existing resource, then run `terraform apply`
  resource "pinecone_api_key" "example" {
    name       = "New API key name"
    project_id = "YOUR_PROJECT_ID"
    roles      = ["ProjectEditor"]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_API_KEY_ID="YOUR_API_KEY_ID"

  curl -X PATCH "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "New API key name",
  		"roles": ["ProjectEditor"]
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "New API key name",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "roles": [
        "ProjectEditor"
      ]
    },
    "value": "string"
  }
  ```
</ResponseExample>
