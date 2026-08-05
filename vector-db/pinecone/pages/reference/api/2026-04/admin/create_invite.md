---
title: "Invite a user to the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_invite
path: reference/api/2026-04/admin/create_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/invites
Invite a user to the organization by email and grant their initial role bindings.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const invite = await admin.invites.create({
    email: 'newhire@example.com',
    roleBindings: [
      { resourceType: 'organization', role: 'OrgMember' },
      {
        resourceType: 'project',
        resourceId: 'a2f7dddb-1597-4eff-9f71-535fde243f58',
        role: 'ProjectMember',
      },
    ],
  });
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

      projectId := "a2f7dddb-1597-4eff-9f71-535fde243f58"
      invite, err := adminClient.Invite.Create(ctx, &pinecone.CreateInviteParams{
          Email: "newhire@example.com",
          RoleBindings: []pinecone.RoleBindingInput{
              {ResourceType: pinecone.ResourceTypeOrganization, Role: "OrgMember"},
              {ResourceType: pinecone.ResourceTypeProject, ResourceId: &projectId, Role: "ProjectMember"},
          },
      })
      if err != nil {
          log.Fatalf("Failed to create invite: %v", err)
      }
      fmt.Printf("Invited %v (status: %v)\n", invite.Email, invite.Status)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  resource "pinecone_invite" "newhire" {
    email = "newhire@example.com"

    role_bindings = [
      {
        resource_type = "organization"
        role          = "OrgMember"
      },
      {
        resource_type = "project"
        resource_id   = "a2f7dddb-1597-4eff-9f71-535fde243f58"
        role          = "ProjectMember"
      }
    ]
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/invites" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
    -d '{
      "email": "newhire@example.com",
      "role_bindings": [
        {
          "resource_type": "organization",
          "role": "OrgMember"
        },
        {
          "resource_type": "project",
          "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
          "role": "ProjectMember"
        }
      ]
    }'
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
