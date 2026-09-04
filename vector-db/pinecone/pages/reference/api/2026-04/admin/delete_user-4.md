---
title: "Remove a user from the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_user
path: reference/api/2026-04/admin/delete_user
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/users/{user_id}
Remove a user from the organization and revoke their role bindings; their Pinecone account is not deleted.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  await admin.users.delete('YOUR_USER_ID');
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

      if err := adminClient.User.Delete(ctx, "YOUR_USER_ID"); err != nil {
          log.Fatalf("Failed to delete user: %v", err)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Users join by accepting an invite, so import the existing member first:
  #   terraform import pinecone_user.teammate YOUR_USER_ID
  # Then remove the resource block and run `terraform apply` to remove them
  # from the organization.
  resource "pinecone_user" "teammate" {
    id = "YOUR_USER_ID"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_USER_ID="YOUR_USER_ID"

  curl -X DELETE "https://api.pinecone.io/admin/users/$PINECONE_USER_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
