---
title: "Authentication"
source: https://docs.pinecone.io/reference/api/marketplace/authentication
path: reference/api/marketplace/authentication
---

Authenticate to the Pinecone Marketplace API using project-scoped API keys, including the Api-Key header, key scoping, and deployment permissions.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Pinecone Marketplace API uses Pinecone API keys for authentication. You can use the same API key you use for Pinecone Assistant and the Pinecone Vector Database.

## API key header

Include your API key in the `Api-Key` header on every request:

```bash curl theme={null}
curl https://api.pinecone.io/marketplace/deployments \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json"
```

## Scoping

API keys are scoped to a Pinecone project. Marketplace deployments are scoped to a project as well. An API key can manage deployments in the project it belongs to.

For details on how to create and manage Pinecone API keys, see [Manage API keys](/guides/assistant/admin/manage-api-keys).
