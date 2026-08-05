---
title: "Pinecone Nexus API"
source: https://docs.pinecone.io/reference/api/nexus/introduction
path: reference/api/nexus/introduction
---

Programmatic access to Nexus: manage contexts and sources, curate, and query with KnowQL.

The Pinecone Nexus API gives you programmatic access to the same operations available in the Nexus console: managing contexts and sources, curating, and querying with KnowQL. Anything you can do in the console you can do through the API.

## Base URL

Your deployment's workspace host, from the `nexus_default_workspace_data_console_url` output of the [install](/guides/nexus/byoc/deploy), with the `/api` path:

```
https://YOUR_WORKSPACE_HOST/api
```

## Versioning

Nexus uses date-based versioning through the `X-Pinecone-Api-Version` header. Send the version you built against, for example `2026-07`. Omit it to use the default version. The older `/api/v0` path stays functional as a legacy alias.
