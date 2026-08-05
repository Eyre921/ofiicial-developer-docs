---
title: "List users in the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_users
path: reference/api/2026-04/admin/list_users
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/users
List users in the caller's organization, optionally filtered by email address.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const { data: users } = await admin.users.list();
  console.log(users);
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

      users, err := adminClient.User.List(ctx, &pinecone.ListUsersParams{})
      if err != nil {
          log.Fatalf("Failed to list users: %v", err)
      }
      for _, user := range users.Data {
          fmt.Printf("User: %v (%v)\n", user.Email, user.Id)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_users" "all" {}

  output "user_emails" {
    value = [for user in data.pinecone_users.all.users : user.email]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/users" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
        "email": "alice@example.com",
        "name": "Alice Example",
        "created_at": "2026-04-10T15:23:00Z",
        "updated_at": "2026-04-12T09:11:00Z"
      }
    ],
    "pagination": {
      "next": "eyJsYXN0X2lkIjoiZTJlOTI1MjMifQ=="
    }
  }
  ```
</ResponseExample>
