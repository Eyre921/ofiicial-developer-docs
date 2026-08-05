---
title: "Delete an invite"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_invite
path: reference/api/2026-04/admin/delete_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/invites/{invite_id}
Delete a pending or expired invite and its role bindings; to remove an accepted user, delete the user instead.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  await admin.invites.delete('YOUR_INVITE_ID');
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

      if err := adminClient.Invite.Delete(ctx, "YOUR_INVITE_ID"); err != nil {
          log.Fatalf("Failed to delete invite: %v", err)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # This block defines the invite. To revoke a pending invite, either remove the
  # block and run `terraform apply`, or run:
  #   terraform destroy -target=pinecone_invite.newhire
  resource "pinecone_invite" "newhire" {
    email = "newhire@example.com"

    role_bindings = [
      {
        resource_type = "organization"
        role          = "OrgMember"
      }
    ]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="YOUR_INVITE_ID"

  curl -X DELETE "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
