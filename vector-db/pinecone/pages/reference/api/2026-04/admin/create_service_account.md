---
title: "Create a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_service_account
path: reference/api/2026-04/admin/create_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/service-accounts
Create a service account with optional initial role bindings; the client secret is returned only once.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  // `clientSecret` is returned only once and cannot be retrieved later
  const { serviceAccount, clientSecret } = await admin.serviceAccounts.create({
    name: 'ci-prod',
    roleBindings: [
      {
        resourceType: 'project',
        resourceId: 'a2f7dddb-1597-4eff-9f71-535fde243f58',
        role: 'DataPlaneEditor',
      },
    ],
  });
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

      projectId := "a2f7dddb-1597-4eff-9f71-535fde243f58"
      sa, err := adminClient.ServiceAccount.Create(ctx, &pinecone.CreateServiceAccountParams{
          Name: "ci-prod",
          RoleBindings: []pinecone.RoleBindingInput{
              {
                  ResourceType: pinecone.ResourceTypeProject,
                  ResourceId:   &projectId,
                  Role:         "DataPlaneEditor",
              },
          },
      })
      if err != nil {
          log.Fatalf("Failed to create service account: %v", err)
      }
      // ClientSecret is returned only once — store it securely and never log it
      fmt.Printf("Successfully created service account: %v\n", sa.ServiceAccount.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # Roles are assigned with separate pinecone_role_binding resources
  resource "pinecone_service_account" "ci_prod" {
    name = "ci-prod"
  }

  resource "pinecone_role_binding" "ci_prod_data_plane_editor" {
    principal_id   = pinecone_service_account.ci_prod.id
    principal_type = "service_account"
    resource_type  = "project"
    resource_id    = "a2f7dddb-1597-4eff-9f71-535fde243f58"
    role           = "DataPlaneEditor"
  }

  output "ci_prod_client_secret" {
    value     = pinecone_service_account.ci_prod.client_secret
    sensitive = true
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/service-accounts" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "ci-prod",
  		"role_bindings": [
  			{
  				"resource_type": "project",
  				"resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
  				"role": "DataPlaneEditor"
  			}
  		]
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "service_account": {
      "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
      "name": "ci-prod",
      "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
      "created_at": "2026-04-10T15:23:00Z",
      "updated_at": "2026-04-10T15:23:00Z"
    },
    "client_secret": "8p-kkC23XOWvkCosKq-BOn3G74qp__rBcDMxc82iB4gfzRvuhSCRBKM7C5Q7TAzj"
  }
  ```
</ResponseExample>
