---
title: "Rotate a service account's OAuth client secret"
source: https://docs.pinecone.io/reference/api/2026-04/admin/rotate_service_account_secret
path: reference/api/2026-04/admin/rotate_service_account_secret
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/service-accounts/{service_account_id}/rotate-secret
Rotate a service account's OAuth client secret; the previous secret and its tokens are revoked within seconds and the new secret is returned only once.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  // The previous secret is invalidated, and the new one is returned only once
  const { serviceAccount, clientSecret } = await admin.serviceAccounts.rotateSecret(
    'YOUR_SERVICE_ACCOUNT_ID'
  );
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

      sa, err := adminClient.ServiceAccount.RotateSecret(ctx, "YOUR_SERVICE_ACCOUNT_ID")
      if err != nil {
          log.Fatalf("Failed to rotate service account secret: %v", err)
      }
      // ClientSecret is returned only once — store it securely and never log it
      fmt.Printf("Successfully rotated secret for service account: %v\n", sa.ServiceAccount.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Change rotate_trigger to any new value to issue and store a new secret
  resource "pinecone_service_account" "ci_prod" {
    name           = "ci-prod"
    rotate_trigger = "2026-04-10"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c"

  curl -X POST "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID/rotate-secret" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "service_account": {
      "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
      "name": "My Service Account",
      "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
      "created_at": "2026-04-10T15:23:00Z",
      "updated_at": "2026-04-10T15:23:00Z"
    },
    "client_secret": "8p-kkC23XOWvkCosKq-BOn3G74qp__rBcDMxc82iB4gfzRvuhSCRBKM7C5Q7TAzj"
  }
  ```
</ResponseExample>
