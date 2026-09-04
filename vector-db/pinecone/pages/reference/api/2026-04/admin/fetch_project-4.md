---
title: "Get project details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_project
path: reference/api/2026-04/admin/fetch_project
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/projects/{project_id}
Get a project's details.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const project = await admin.projects.describe('YOUR_PROJECT_ID');
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

      project, err := adminClient.Project.Describe(ctx, "YOUR_PROJECT_ID")
      if err != nil {
          log.Fatalf("Failed to describe project: %v", err)
      }
      fmt.Printf("Project: %v (%v)\n", project.Name, project.Id)
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_project" "example" {
    id = "YOUR_PROJECT_ID"
  }

  output "project_name" {
    value = data.pinecone_project.example.name
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="3fa85f64-5717-4562-b3fc-2c963f66afa6"

  curl -X GET "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
      -H "accept: application/json"
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
    "created_at": "2025-03-17T00:30:23.262Z"
  }
  ```
</ResponseExample>
