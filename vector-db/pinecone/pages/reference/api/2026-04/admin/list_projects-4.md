---
title: "List projects"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_projects
path: reference/api/2026-04/admin/list_projects
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/projects
List all projects in an organization.

<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  const { data: projects } = await admin.projects.list();
  console.log(projects);
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

      projects, err := adminClient.Project.List(ctx)
      if err != nil {
          log.Fatalf("Failed to list projects: %v", err)
      }
      for _, project := range projects {
          fmt.Printf("Project: %v (%v)\n", project.Name, project.Id)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  data "pinecone_projects" "all" {}

  output "project_names" {
    value = [for project in data.pinecone_projects.all.projects : project.name]
  }
  ```

  ```bash curl theme={null}
  curl -X GET "https://api.pinecone.io/admin/projects" \
      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "example-project",
        "max_pods": 0,
        "force_encryption_with_cmek": true,
        "organization_id": "<string>",
        "created_at": "2023-11-07T05:31:56Z"
      }
    ]
  }
  ```
</ResponseExample>
