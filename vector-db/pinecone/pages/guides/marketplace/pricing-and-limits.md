---
title: "Marketplace pricing and limits"
source: https://docs.pinecone.io/guides/marketplace/pricing-and-limits
path: guides/marketplace/pricing-and-limits
---

How Pinecone Marketplace usage is billed and what limits apply.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This page describes how Pinecone Marketplace usage is billed and the limits that apply to a deployment.

## Pricing

Marketplace is bundled with your Pinecone usage. There is no separate Marketplace subscription. You pay for the Pinecone Assistant and index usage that your deployments generate, including:

* Assistant API usage from publishing, introspection, and end-user queries.
* Index storage and read or write units consumed by ingested documents.
* Pinecone Inference usage for any embedding or reranking your deployments perform.

For details on Pinecone Assistant pricing, see [Assistant pricing and limits](/guides/assistant/pricing-and-limits). For database pricing, see [Understanding cost](/guides/manage-cost/understanding-cost).

## Limits

The following limits apply to a deployment.

| Limit                             | Value                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Connectors per deployment         | Google Drive, manual upload                                                                             |
| Maximum file size per upload      | Matches Pinecone Assistant file limits                                                                  |
| Knowledge bases per deployment    | Multi-knowledge-base supported through the Knowledge Agent Toolkit (KAT)                                |
| Versions retained per deployment  | All published versions are retained for rollback                                                        |
| Consumer authentication providers | `link`, Google sign-in                                                                                  |
| Component types                   | 6 (comparison tables, content cards, timelines, progress trackers, coverage matrices, geolocation maps) |

For Pinecone Assistant file size and quantity limits, see [Assistant limits](/reference/api/assistant/assistant-limits).

## Access

Marketplace is available to all Pinecone organizations during public preview. Sign in at [marketplace.pinecone.io](https://marketplace.pinecone.io) with your Pinecone account.
