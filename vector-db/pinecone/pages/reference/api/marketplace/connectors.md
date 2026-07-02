---
title: "Connectors"
source: https://docs.pinecone.io/reference/api/marketplace/connectors
path: reference/api/marketplace/connectors
---

Manage source connectors for Pinecone Marketplace deployments.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Connectors API lets you configure source connectors and review sync status for deployments.

## Operations

| Operation          | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| List connectors    | Return the connectors attached to a deployment.             |
| Attach a connector | Attach a source connector to a knowledge base.              |
| Update a connector | Update connector configuration, such as the selected scope. |
| Detach a connector | Remove a connector from a knowledge base.                   |
| Get sync status    | Return the latest sync status per file.                     |
| Trigger a sync     | Force an immediate sync run.                                |

For the operator-facing guides, see [Connectors overview](/guides/marketplace/connectors-overview).
