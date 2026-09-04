---
title: "Get service account details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_service_account
path: reference/api/2026-04/admin/fetch_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/service-accounts/{service_account_id}
Get a service account by ID; the client secret is returned only from create and rotate-secret requests.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const serviceAccount = await admin.serviceAccounts.describe('YOUR_SERVICE_ACCOUNT_ID');
  console.log(serviceAccount);
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

      sa, err := adminClient.ServiceAccount.Describe(ctx, "YOUR_SERVICE_ACCOUNT_ID")
      if err != nil {
          log.Fatalf("Failed to describe service account: %v", err)
      }
      fmt.Printf("Service account: %v (%v)\n", sa.Name, sa.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_service_account" "example" {
    id = "YOUR_SERVICE_ACCOUNT_ID"
  }

  output "service_account_name" {
    value = data.pinecone_service_account.example.name
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c"

  curl -X GET "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "name": "My Service Account",
    "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
