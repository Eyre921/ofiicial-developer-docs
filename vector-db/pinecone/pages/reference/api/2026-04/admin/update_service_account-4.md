---
title: "Update a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/update_service_account
path: reference/api/2026-04/admin/update_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml patch /admin/service-accounts/{service_account_id}
Update a service account's name; role bindings are managed through the role-binding endpoints.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const serviceAccount = await admin.serviceAccounts.update('YOUR_SERVICE_ACCOUNT_ID', {
    name: 'ci-prod-renamed',
  });
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

      name := "ci-prod-renamed"
      sa, err := adminClient.ServiceAccount.Update(ctx, "YOUR_SERVICE_ACCOUNT_ID", &pinecone.UpdateServiceAccountParams{
          Name: &name,
      })
      if err != nil {
          log.Fatalf("Failed to update service account: %v", err)
      }
      fmt.Printf("Successfully updated service account: %v\n", sa.Name)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Change the name on an existing resource, then run `terraform apply`
  resource "pinecone_service_account" "ci_prod" {
    name = "ci-prod-renamed"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="YOUR_SERVICE_ACCOUNT_ID"

  curl -X PATCH "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "ci-prod-renamed"
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "name": "ci-prod-renamed",
    "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
