---
title: "Delete a project"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/delete_project
path: reference/api/2026-04/admin-assistant/delete_project
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/projects/{project_id}
Delete a project and all its configuration; delete its indexes, assistants, backups, and collections first.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
  const admin = new AdminClient();

  await admin.projects.delete('YOUR_PROJECT_ID');
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

      if err := adminClient.Project.Delete(ctx, "YOUR_PROJECT_ID"); err != nil {
          log.Fatalf("Failed to delete project: %v", err)
      }
  }
  ```

  ```hcl Terraform theme={null}
  # Requires Terraform provider v4.0.0 or later
  # This block defines the project. To delete it, either remove the block and run
  # `terraform apply`, or run:
  #   terraform destroy -target=pinecone_project.example
  resource "pinecone_project" "example" {
    name = "example-project"
  }
  ```

  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="YOUR_PROJECT_ID"

  curl -X DELETE "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
