---
title: "Delete a role binding"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_role_binding
path: reference/api/2026-04/admin/delete_role_binding
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/role-bindings/{role_binding_id}
Delete a role binding; permissions are revoked when the deletion completes.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  await admin.roleBindings.delete('YOUR_ROLE_BINDING_ID');
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

      if err := adminClient.RoleBinding.Delete(ctx, "YOUR_ROLE_BINDING_ID"); err != nil {
          log.Fatalf("Failed to delete role binding: %v", err)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # This block defines the role binding. To revoke the role, either remove the
  # block and run `terraform apply`, or run:
  #   terraform destroy -target=pinecone_role_binding.ci_data_plane_editor
  resource "pinecone_role_binding" "ci_data_plane_editor" {
    principal_type = "service_account"
    principal_id   = "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c"
    resource_type  = "project"
    resource_id    = "a2f7dddb-1597-4eff-9f71-535fde243f58"
    role           = "DataPlaneEditor"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_ROLE_BINDING_ID="YOUR_ROLE_BINDING_ID"

  curl -X DELETE "https://api.pinecone.io/admin/role-bindings/$PINECONE_ROLE_BINDING_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
