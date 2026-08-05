---
title: "Get user details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_user
path: reference/api/2026-04/admin/fetch_user
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/users/{user_id}
Get a user in the caller's organization by ID.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const user = await admin.users.describe('YOUR_USER_ID');
  console.log(user);
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

      user, err := adminClient.User.Describe(ctx, "YOUR_USER_ID")
      if err != nil {
          log.Fatalf("Failed to describe user: %v", err)
      }
      fmt.Printf("User: %v (%v)\n", user.Email, user.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Look up a user by id or by email
  data "pinecone_user" "example" {
    id = "YOUR_USER_ID"
  }

  output "user_name" {
    value = data.pinecone_user.example.name
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_USER_ID="e2e92523-85dc-4142-b8c2-e681be8b78df"

  curl -X GET "https://api.pinecone.io/admin/users/$PINECONE_USER_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
    "email": "alice@example.com",
    "name": "Alice Example",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
