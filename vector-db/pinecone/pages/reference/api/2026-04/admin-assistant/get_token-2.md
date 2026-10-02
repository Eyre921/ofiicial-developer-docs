---
title: "Create an access token"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/get_token
path: reference/api/2026-04/admin-assistant/get_token
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/oauth_2026-04.oas.yaml post /oauth/token
Obtain an access token for a service account using the OAuth2 client credentials flow. An access token is needed to authorize requests to the Pinecone Admin API.
The host domain for OAuth endpoints is `login.pinecone.io`.


<RequestExample>
  ```javascript JavaScript theme={null}
  // Requires Node.js SDK v8.2.0 or later
  import { AdminClient } from '@pinecone-database/pinecone';

  // You don't call this endpoint directly when using the SDK. The AdminClient
  // exchanges your service account credentials for an access token on the first
  // admin request and reuses it for subsequent calls.
  const admin = new AdminClient({
    clientId: 'YOUR_CLIENT_ID',
    clientSecret: 'YOUR_CLIENT_SECRET',
  });

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

      "github.com/pinecone-io/go-pinecone/v6/pinecone"
  )

  func main() {
      ctx := context.Background()

      // You don't call this endpoint directly when using the SDK. The AdminClient
      // exchanges your service account credentials for an access token.
      adminClient, err := pinecone.NewAdminClientWithContext(ctx, pinecone.NewAdminClientParams{
          ClientId:     "YOUR_CLIENT_ID",
          ClientSecret: "YOUR_CLIENT_SECRET",
      })
      if err != nil {
          log.Fatalf("Failed to create AdminClient: %v", err)
      }

      projects, err := adminClient.Project.List(ctx)
      if err != nil {
          log.Fatalf("Failed to list projects: %v", err)
      }
      fmt.Printf("Found %v projects\n", len(projects))
  }
  ```

  ```bash curl theme={null}
  curl "https://login.pinecone.io/oauth/token" \ # Note: Base URL is login.pinecone.io
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Content-Type: application/json" \
  	-d '{
  		"grant_type": "client_credentials",
  		"client_id": "YOUR_CLIENT_ID",
  		"client_secret": "YOUR_CLIENT_SECRET",
  		"audience": "https://api.pinecone.io/"
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "access_token":"YOUR_ACCESS_TOKEN",
      "expires_in":86400,
      "token_type":"Bearer"
  }
  ```
</ResponseExample>
