---
title: "List role bindings"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_role_bindings
path: reference/api/2026-04/admin/list_role_bindings
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/role-bindings
List role bindings in the caller's organization, optionally filtered by principal, resource, and role.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const { data: roleBindings } = await admin.roleBindings.list({
    principalType: 'user',
    principalId: 'e2e92523-85dc-4142-b8c2-e681be8b78df',
  });
  console.log(roleBindings);
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

      principalType := pinecone.PrincipalTypeUser
      principalId := "e2e92523-85dc-4142-b8c2-e681be8b78df"
      roleBindings, err := adminClient.RoleBinding.List(ctx, &pinecone.ListRoleBindingsParams{
          PrincipalType: &principalType,
          PrincipalId:   &principalId,
      })
      if err != nil {
          log.Fatalf("Failed to list role bindings: %v", err)
      }
      for _, roleBinding := range roleBindings.Data {
          fmt.Printf("Role binding: %v (%v)\n", roleBinding.Role, roleBinding.Id)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_role_bindings" "user_roles" {
    principal_type = "user"
    principal_id   = "e2e92523-85dc-4142-b8c2-e681be8b78df"
  }

  output "user_roles" {
    value = [for b in data.pinecone_role_bindings.user_roles.role_bindings : b.role]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/role-bindings?principal_type=user&principal_id=e2e92523-85dc-4142-b8c2-e681be8b78df" \
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
        "id": "5a86ed21-daf1-448d-a9ca-f92a0fd839d3",
        "principal_type": "user",
        "principal_id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
        "resource_type": "organization",
        "resource_id": "-ExampleOrgId0000000",
        "role": "OrgMember",
        "created_at": "2026-04-10T15:23:00Z"
      }
    ],
    "pagination": {
      "next": "eyJsYXN0X2lkIjoiNWE4NmVkMjEifQ=="
    }
  }
  ```
</ResponseExample>
