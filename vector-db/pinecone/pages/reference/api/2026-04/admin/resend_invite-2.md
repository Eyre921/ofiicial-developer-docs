---
title: "Resend an invite email"
source: https://docs.pinecone.io/reference/api/2026-04/admin/resend_invite
path: reference/api/2026-04/admin/resend_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/invites/{invite_id}/resend
Resend the invite email and extend its expiration to 7 days from now; limited to 100 emails per hour per organization.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const invite = await admin.invites.resend('YOUR_INVITE_ID');
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

      invite, err := adminClient.Invite.Resend(ctx, "YOUR_INVITE_ID")
      if err != nil {
          log.Fatalf("Failed to resend invite: %v", err)
      }
      fmt.Printf("Resent invite to %v (status: %v)\n", invite.Email, invite.Status)
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="9c8e3528-b9c0-4358-84ce-84c28e91b566"

  curl -X POST "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID/resend" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9c8e3528-b9c0-4358-84ce-84c28e91b566",
    "email": "newhire@example.com",
    "status": "pending",
    "expires_at": "2026-05-28T20:14:00Z",
    "processed_at": null,
    "created_at": "2026-04-14T20:00:00Z"
  }
  ```
</ResponseExample>
