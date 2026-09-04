---
title: "Authentication"
source: https://docs.pinecone.io/reference/api/nexus/authentication
path: reference/api/nexus/authentication
---

Authenticate to the Nexus API with your Pinecone API key, sent directly or exchanged for a short-lived session token.

All requests to the [Pinecone Nexus API](/reference/api/nexus/introduction) authenticate with a valid [Pinecone API key](/guides/production/security-overview#api-keys) for the target project. The Pinecone project is the tenancy boundary. How you send the key depends on the plane:

* **Control plane** (workspace management, `https://api.pinecone.io`): send the key directly in the `Api-Key` header.
* **Data plane** (contexts, curation, and queries, your workspace host): exchange the key for a short-lived session token with `POST /auth/login`, or send it directly in the `Api-Key` header.

## Get an API key

[Create an API key](https://app.pinecone.io/organizations/-/projects/-/keys) in the Pinecone console.

```bash theme={null}
export PINECONE_API_KEY="YOUR_API_KEY"
```

## Control plane

The control plane is served at `https://api.pinecone.io`. Send your Pinecone API key directly in the `Api-Key` header, with no login exchange.

```bash curl theme={null}
curl -fsS "https://api.pinecone.io/workspaces" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'X-Pinecone-Api-Version: 2026-07'
```

## Data plane

The data plane is served at your deployment's workspace host, from the `nexus_default_workspace_data_console_url` output of the [install](/guides/nexus/byoc/deploy):

```bash theme={null}
export NEXUS_BASE_URL="https://YOUR_WORKSPACE_HOST/api"
```

### Session token

The primary method for data-plane requests. Exchange your API key for a short-lived bearer token with `POST /auth/login`, then send that token as `Authorization: Bearer <token>` on every request.

```bash curl theme={null}
export NEXUS_TOKEN="$(
  curl -fsS "$NEXUS_BASE_URL/auth/login" \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-Api-Version: 2026-07' \
    -d "{\"api_key\":\"$PINECONE_API_KEY\"}" \
  | jq -r '.token'
)"

curl -fsS "$NEXUS_BASE_URL/contexts" \
  -H "Authorization: Bearer $NEXUS_TOKEN" \
  -H 'X-Pinecone-Api-Version: 2026-07'
```

### API key

Alternatively, send your Pinecone API key directly in the `Api-Key` header, with no login exchange.

```bash curl theme={null}
curl -fsS "$NEXUS_BASE_URL/contexts" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'X-Pinecone-Api-Version: 2026-07'
```
