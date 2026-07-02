---
title: "Delete a project"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_project
path: reference/api/2026-04/admin/delete_project
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/projects/{project_id}
Delete a project and all its associated configuration.
Before deleting a project, you must delete all indexes, assistants, backups, and collections associated with the project. Other project resources, such as API keys, are automatically deleted when the project is deleted.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="YOUR_PROJECT_ID"

  curl -X DELETE "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
