---
title: "Get role binding details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_role_binding
path: reference/api/2026-04/admin/fetch_role_binding
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/role-bindings/{role_binding_id}
Get a role binding in the caller's organization by ID.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const roleBinding = await admin.roleBindings.describe('YOUR_ROLE_BINDING_ID');
  console.log(roleBinding);
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

      roleBinding, err := adminClient.RoleBinding.Describe(ctx, "YOUR_ROLE_BINDING_ID")
      if err != nil {
          log.Fatalf("Failed to describe role binding: %v", err)
      }
      fmt.Printf("Role binding: %v (%v)\n", roleBinding.Role, roleBinding.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_role_binding" "example" {
    id = "YOUR_ROLE_BINDING_ID"
  }

  output "role" {
    value = data.pinecone_role_binding.example.role
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_ROLE_BINDING_ID="9a8e3528-b9c0-4358-84ce-84c28e91b566"

  curl -X GET "https://api.pinecone.io/admin/role-bindings/$PINECONE_ROLE_BINDING_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9a8e3528-b9c0-4358-84ce-84c28e91b566",
    "principal_type": "service_account",
    "principal_id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "DataPlaneEditor",
    "created_at": "2026-04-10T15:23:00Z"
  }
  ```
</ResponseExample>
