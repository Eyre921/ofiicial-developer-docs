---
title: "Evaluations"
source: https://docs.pinecone.io/reference/api/marketplace/evaluations
path: reference/api/marketplace/evaluations
---

Marketplace Evaluations API reference for triggering evaluation runs, retrieving scores, and inspecting per-question detail per version.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Evaluations API lets you trigger evaluations and retrieve results per version.

## Operations

| Operation             | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| List evaluations      | Return all evaluation runs for a deployment.                             |
| Get an evaluation     | Return aggregate scores and per-question detail for a single evaluation. |
| Trigger an evaluation | Run an evaluation against the active version on demand.                  |

For the operator-facing guides, see [Evaluations](/guides/marketplace/evaluations).
