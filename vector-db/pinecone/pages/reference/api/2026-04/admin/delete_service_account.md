---
title: "Delete a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_service_account
path: reference/api/2026-04/admin/delete_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/service-accounts/{service_account_id}
Delete a service account and its role bindings; tokens it minted are revoked within a few seconds.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  await admin.serviceAccounts.delete('YOUR_SERVICE_ACCOUNT_ID');
  ```

  ```go Go theme={null}
  // Requires Go SDK v6.0.0 or later
  package main

  import (
      "context"
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

      if err := adminClient.ServiceAccount.Delete(ctx, "YOUR_SERVICE_ACCOUNT_ID"); err != nil {
          log.Fatalf("Failed to delete service account: %v", err)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # This block defines the service account. To delete it, either remove the block
  # and run `terraform apply`, or run:
  #   terraform destroy -target=pinecone_service_account.ci_prod
  resource "pinecone_service_account" "ci_prod" {
    name = "ci-prod"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="YOUR_SERVICE_ACCOUNT_ID"

  curl -X DELETE "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
