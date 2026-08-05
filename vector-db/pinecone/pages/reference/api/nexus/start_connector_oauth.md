---
title: "Start the OAuth link flow for a provider"
source: https://docs.pinecone.io/reference/api/nexus/start_connector_oauth
path: reference/api/nexus/start_connector_oauth
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /connectors/oauth/{provider}/start
Returns an `authorize_url` for the user to open in a browser. The connector is persisted by the provider's OAuth redirect callback once the user approves access.
