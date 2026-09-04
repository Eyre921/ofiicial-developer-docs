---
title: "Get invite details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_invite
path: reference/api/2026-04/admin/fetch_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/invites/{invite_id}
Get an invite in the caller's organization by ID.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const invite = await admin.invites.describe('YOUR_INVITE_ID');
  console.log(invite);
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

      invite, err := adminClient.Invite.Describe(ctx, "YOUR_INVITE_ID")
      if err != nil {
          log.Fatalf("Failed to describe invite: %v", err)
      }
      fmt.Printf("Invite: %v (status: %v)\n", invite.Email, invite.Status)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_invite" "example" {
    id = "YOUR_INVITE_ID"
  }

  output "invite_status" {
    value = data.pinecone_invite.example.status
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="9c8e3528-b9c0-4358-84ce-84c28e91b566"

  curl -X GET "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9c8e3528-b9c0-4358-84ce-84c28e91b566",
    "email": "newhire@example.com",
    "status": "pending",
    "expires_at": "2026-05-21T03:00:00Z",
    "processed_at": null,
    "created_at": "2026-04-14T20:00:00Z"
  }
  ```
</ResponseExample>
