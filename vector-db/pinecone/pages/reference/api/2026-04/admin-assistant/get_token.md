---
title: "Create an access token"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/get_token
path: reference/api/2026-04/admin-assistant/get_token
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/oauth_2026-04.oas.yaml post /oauth/token
Obtain an access token for a service account using the OAuth2 client credentials flow. An access token is needed to authorize requests to the Pinecone Admin API.
The host domain for OAuth endpoints is `login.pinecone.io`.


<RequestExample>
  ```bash curl theme={null}
  curl "https://login.pinecone.io/oauth/token" \ # Note: Base URL is login.pinecone.io
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
