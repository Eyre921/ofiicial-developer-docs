---
title: "Create a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_service_account
path: reference/api/2026-04/admin/create_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/service-accounts
Create a service account with optional initial role bindings. The `client_secret` in the response is shown only once; store it securely.
Grant roles with `role_bindings`: `organization`-scoped bindings omit `resource_id`, while `project`-scoped bindings include the project `resource_id`. Service accounts may receive any organization- or project-scoped role (see Role). Bindings are not returned in the response.
Repeating the same request may create duplicate service accounts.


<RequestExample>
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
