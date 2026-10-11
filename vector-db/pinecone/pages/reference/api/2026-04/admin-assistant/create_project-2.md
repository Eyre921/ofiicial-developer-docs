---
title: "Create a new project"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/create_project
path: reference/api/2026-04/admin-assistant/create_project
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/projects
Create a new project.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const project = await admin.projects.create({ name: 'example-project' });
  console.log(project);
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

      project, err := adminClient.Project.Create(ctx, &pinecone.CreateProjectParams{
          Name: "example-project",
      })
      if err != nil {
          log.Fatalf("Failed to create project: %v", err)
      }
      fmt.Printf("Successfully created project: %v\n", project.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  resource "pinecone_project" "example" {
    name = "example-project"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/projects" \
      -H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
          "name":"example-project"
          }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "example-project",
    "max_pods": 0,
    "force_encryption_with_cmek": false,
    "organization_id": "string",
    "created_at": "2025-03-16T22:46:45.030Z"
  }
  ```
</ResponseExample>
