---
title: "Versions and publishing"
source: https://docs.pinecone.io/reference/api/marketplace/versions
path: reference/api/marketplace/versions
---

Marketplace Versions API reference for publishing building versions, listing version history, and rolling back deployments programmatically.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Versions API lets you publish building versions, list version history, and roll back to a previous version programmatically.

## Operations

| Operation         | Description                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------- |
| List versions     | Return the version history of a deployment.                                                 |
| Get a version     | Return configuration, status, and evaluation result for a single version.                   |
| Publish a version | Promote a building version to active. Returns immediately and provisions in the background. |
| Roll back         | Promote a previous version to active.                                                       |

For the operator-facing guides, see [Publish a deployment](/guides/marketplace/publish-a-deployment) and [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).
