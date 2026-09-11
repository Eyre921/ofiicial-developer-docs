---
title: "Production checklist"
source: https://docs.pinecone.io/guides/production/production-checklist
path: guides/production/production-checklist
---

Prepare Pinecone indexes for production with best practices for project structure, security, scaling, API keys, and reliability across your workloads.

This page provides recommendations and best practices for preparing your Pinecone indexes for production, anticipating production issues, and enabling reliability and growth.

## Prepare your project structure

One of the first steps towards building a production-ready Pinecone index is configuring your project correctly.

* Consider [creating a separate project](/guides/projects/create-a-project) for your development and production indexes, to allow for testing changes to your index before deploying them to production.
* Ensure that you have properly [configured user access](/guides/projects/understanding-projects#project-roles) to the Pinecone console, so that only those users who need to access the production index can do so.
* Ensure that you have properly configured access through the API by [managing API keys](/guides/projects/manage-api-keys) and using API key permissions.

Consider how best to [manage the API keys](/guides/projects/manage-api-keys) associated with your production project. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

## Enforce security

Use Pinecone's [security features](/guides/production/security-overview) to protect your production data:

* Data security
  * Private endpoints
  * Customer-managed encryption keys (CMEK) for hosted projects; for BYOC, use KMS on your own resources ([Bring Your Own Cloud](/guides/production/bring-your-own-cloud))
* Authorization
  * API keys
  * Role-based access control (RBAC)
  * Organization single sign-on (SSO)
* Audit logs
* Bring Your Own Cloud

## Design your indexes for scale

Follow these best practices when designing and populating your indexes:

* **Data ingestion**: For large datasets (10M+ records), [import from object storage](/guides/index-data/import-data) for the most efficient and cost-effective ingestion. For ongoing ingestion, [upsert in batches](/guides/index-data/upsert-data#upsert-in-batches) to optimize speed and efficiency. See the [data ingestion overview](/guides/index-data/data-ingestion-overview) for details.
* **Dimensionality**: Consider the dimensionality of your vectors. Higher dimensions can offer more accuracy but require more resources.
* **Data modeling**: Use [structured IDs](/guides/index-data/data-modeling#use-structured-ids) (e.g., `document_id#chunk_number`) for efficient operations. Design [metadata](/guides/index-data/data-modeling#include-metadata) to support filtering, linking related chunks, and traceability. See the [data modeling guide](/guides/index-data/data-modeling) for details.
* **Namespaces**: When indexing, try to [use namespaces to keep your data among tenants separate](/guides/index-data/implement-multitenancy), and do not use multiple indexes for this purpose. Namespaces are more efficient and more affordable in the long run.

## Understand database limits

Architect your application to work within Pinecone's [database limits](/reference/api/database-limits):

* **Rate limits**: Serverless indexes have per-second operation limits for queries, upserts, updates, and deletes. [Implement error handling with exponential backoff](/guides/production/error-handling) to handle rate limit errors gracefully.
* **Size limits**: Be aware of constraints on vector dimensionality, metadata size per record, record ID length, maximum `top_k` values, and query result sizes. Design your [data model](/guides/index-data/data-modeling) accordingly.
* **Index limits**: Plan for index capacity based on your [plan tier](https://www.pinecone.io/pricing/). Use [namespaces](/guides/index-data/implement-multitenancy) to partition data within indexes rather than creating multiple indexes.
* **Plan limits**: The Starter and Builder plans have monthly read/write unit limits. Upgrade to Standard or Enterprise for unlimited read/write units and higher throughput needs.

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

## Test your query results

Before you move your index to production, make sure that your index is returning accurate results in the context of your application by [identifying the appropriate metrics](https://www.pinecone.io/learn/offline-evaluation/) for evaluating your results.

## Optimize performance

Before serving production workloads, optimize your Pinecone implementation:

* **Increase search relevance**: Use techniques like reranking, metadata filtering, hybrid search, and chunking strategies to improve result quality. See [increase search relevance](/guides/optimize/increase-relevance) for details.
* **Increase throughput**: Import from object storage, upsert in batches, use parallel operations, and leverage Python SDK optimizations like gRPC. See [increase throughput](/guides/optimize/increase-throughput) for details.
* **Decrease latency**: Use namespaces, filter by metadata, target indexes by host, reuse connections, and deploy in the same cloud region as your index. See [decrease latency](/guides/optimize/decrease-latency) for details.
* **Save on costs**: Prefer bulk import for large initial loads, use namespaces for multitenancy, and avoid unnecessary data in query responses. See [save on costs](/guides/optimize/save-on-costs) for details.

## Backup up your indexes

In order to enable long-term retention, compliance archiving, and deployment of new indexes, consider backing up your production indexes by [creating a backup or collection](/guides/manage-data/back-up-an-index).

## Implement error handling

Prepare your application to handle errors gracefully:

* Implement [error handling and retry logic](/guides/production/error-handling) with exponential backoff
* Handle different error types appropriately (4xx vs 5xx)
* Monitor error rates and set up alerts
* Check [status.pinecone.io](https://status.pinecone.io) before escalating issues

## Configure monitoring

Prepare to [monitor the production performance and availability of your indexes](/guides/production/monitoring).

## Configure CI/CD

Use [Pinecone in CI/CD](/guides/production/automated-testing) to safely test changes before deploying them to production.

## Know how to get support

If you need help, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket), or talk to the [Pinecone community](https://www.pinecone.io/community/). Ensure that your [plan tier](https://www.pinecone.io/pricing/) matches the support and availability SLAs you need. This may require you to upgrade to Enterprise.
