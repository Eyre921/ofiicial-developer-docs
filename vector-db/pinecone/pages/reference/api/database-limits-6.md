---
title: "Pinecone Database limits"
source: https://docs.pinecone.io/reference/api/database-limits
path: reference/api/database-limits
---

Pinecone Database limits: This page describes different types of limits for Pinecone Database.

This page describes different types of limits for Pinecone Database.

<Note>
  **Looking for a specific limit?**

  * To compare monthly included usage by plan, start with [read units](#read-units-per-month-per-org), [write units](#write-units-per-month-per-org), and [model usage limits](#monthly-usage-limits).
  * If you received a `429` error, check [rate limits](#rate-limits), especially request-per-second limits for query, upsert, update, delete, fetch, and list.
  * For projects, users, indexes, namespaces, storage, backups, and collections, see [object limits](#object-limits).
  * For batch sizes, metadata filters, and identifier lengths, see [operation limits](#operation-limits) and [identifier limits](#identifier-limits).
</Note>

## Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared serverless infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case. Pinecone is committed to supporting your growth and can often accommodate higher throughput requirements.

Rate limits vary based on [pricing plan](https://www.pinecone.io/pricing/) and apply to [serverless indexes](/guides/index-data/indexing-overview) only.

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### Data plane operations: request-per-second limits

Pinecone enforces rate limits on the number of API requests per second at the namespace level for data plane operations (query, upsert, delete, and update). These limits provide protection against excessive request rates.

#### Affected operations

The following operations are subject to request-per-second rate limiting:

| Operation | Scope         | Limit |
| --------- | ------------- | ----- |
| Query     | Per namespace | 100   |
| Upsert    | Per namespace | 100   |
| Delete    | Per namespace | 100   |
| Update    | Per namespace | 100   |

#### Error response

When you exceed the request-per-second limit, you'll receive an HTTP `429 - TOO_MANY_REQUESTS` response. The error message indicates which operation exceeded the limit and includes the namespace name and limit value. See the individual limit sections below for specific error message formats.

#### How request-per-second limits work with limits on read and write units

Request-per-second limits are enforced in addition to existing read unit and write unit limits. Requests must not exceed any applicable limits:

* Index-level limits - read and write unit limits, per index
* Namespace-level limits - read and write unit limits, per namespace
* Request-per-second limits - requests per second, per namespace

If any limit is exceeded, the request fails with a 429 error.

#### Recommendations

If you're hitting request-per-second limits:

1. Implement retry logic. Use exponential backoff to handle rate limit errors gracefully. See [Error Handling Guide](/guides/production/error-handling#implement-retry-logic).
2. Pace your requests. Add client-side rate limiting to stay under limits.
3. Consider [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes), which don't have request-per-second limits and provide dedicated capacity for high-throughput workloads.
4. If you need higher limits, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

### All rate limits

#### Monthly usage limits

| Metric                                                                        | Starter plan   | Builder plan   | Standard plan  | Enterprise plan |
| :---------------------------------------------------------------------------- | :------------- | :------------- | :------------- | :-------------- |
| [Read units per month per org](#read-units-per-month-per-org)                 | 1,000,000      | 2,000,000      | Unlimited      | Unlimited       |
| [Write units per month per org](#write-units-per-month-per-org)               | 2,000,000      | 5,000,000      | Unlimited      | Unlimited       |
| [Embedding tokens per month per model](#embedding-tokens-per-month-per-model) | 5,000,000      | 10,000,000     | Unlimited      | Unlimited       |
| [Rerank requests per month per model](#rerank-requests-per-month-per-model)   | Model-specific | Model-specific | Model-specific | Model-specific  |

#### Data operation throughput limits

| Metric                                                                                                        | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------------------------------------------------------------------------------------------------------ | :----------- | :----------- | :------------ | :-------------- |
| [Upsert size per second per namespace](#upsert-size-per-second-per-namespace)                                 | 50 MB        | 50 MB        | 50 MB         | 50 MB           |
| [Query read units per second per index](#query-read-units-per-second-per-index)                               | 2,000        | 2,000        | 2,000         | 2,000           |
| [Query requests per second per namespace](#query-requests-per-second-per-namespace)                           | 100          | 100          | 100           | 100             |
| [Update records per second per namespace](#update-records-per-second-per-namespace)                           | 100          | 100          | 100           | 100             |
| [Update requests per second per namespace](#update-requests-per-second-per-namespace)                         | 100          | 100          | 100           | 100             |
| [Update by metadata requests per second per namespace](#update-by-metadata-requests-per-second-per-namespace) | 5            | 5            | 5             | 5               |
| [Update by metadata requests per second per index](#update-by-metadata-requests-per-second-per-index)         | 500          | 500          | 500           | 500             |
| [Upsert requests per second per namespace](#upsert-requests-per-second-per-namespace)                         | 100          | 100          | 100           | 100             |
| [Fetch requests per second per index](#fetch-requests-per-second-per-index)                                   | 100          | 100          | 100           | 100             |
| [List requests per second per index](#list-requests-per-second-per-index)                                     | 200          | 200          | 200           | 200             |
| [Describe index stats requests per second per index](#describe-index-stats-requests-per-second-per-index)     | 100          | 100          | 100           | 100             |
| [Delete requests per second per namespace](#delete-requests-per-second-per-namespace)                         | 100          | 100          | 100           | 100             |
| [Delete records per second per namespace](#delete-records-per-second-per-namespace)                           | 5,000        | 5,000        | 5,000         | 5,000           |
| [Delete records per second per index](#delete-records-per-second-per-index)                                   | 5,000        | 5,000        | 5,000         | 5,000           |
| [Delete by metadata requests per second per namespace](#delete-by-metadata-requests-per-second-per-namespace) | 5            | 5            | 5             | 5               |
| [Delete by metadata requests per second per index](#delete-by-metadata-requests-per-second-per-index)         | 500          | 500          | 500           | 500             |

#### Model throughput limits

| Metric                                                                          | Starter plan   | Builder plan   | Standard plan  | Enterprise plan |
| :------------------------------------------------------------------------------ | :------------- | :------------- | :------------- | :-------------- |
| [Embedding tokens per minute per model](#embedding-tokens-per-minute-per-model) | Model-specific | Model-specific | Model-specific | Model-specific  |
| [Rerank requests per minute per model](#rerank-requests-per-minute-per-model)   | Model-specific | Model-specific | Model-specific | Model-specific  |

### Read units per month per org

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 1,000,000    | 2,000,000    | Unlimited     | Unlimited       |

[Read units](/guides/manage-cost/understanding-cost#read-units) measure the compute, I/O, and network resources used by [fetch](/guides/manage-data/fetch-data), [query](/guides/search/search-overview), and [list](/guides/manage-data/list-record-ids) requests to serverless indexes. When you reach the monthly read unit limit for an organization, fetch, query, and list requests to serverless indexes in the organization will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached your read unit limit for the current month limit. 
  To continue reading data, upgrade your plan. 
  ```
</Accordion>

To continue reading from serverless indexes in the organization, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

To check how close you are to the monthly read unit limit for your organization, do the following:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project.
3. Select any index in the project.
4. Look under **Usage**.

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### Write units per month per org

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 2,000,000    | 5,000,000    | Unlimited     | Unlimited       |

[Write units](/guides/manage-cost/understanding-cost#write-units) measure the storage and compute resources used by [upsert](/guides/index-data/upsert-data), [update](/guides/manage-data/update-data), and [delete](/guides/manage-data/delete-data) requests to serverless indexes. When you reach the monthly write unit limit for an organization, upsert, update, and delete requests to serverless indexes in the organization will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached your write unit limit for the current month. 
  To continue writing data, upgrade your plan.
  ```
</Accordion>

To continue writing data to serverless indexes in the organization, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

To check how close you are to the monthly write unit limit for your organization, do the following:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project.
3. Select any index in the project.
4. Look under **Usage**.

### Upsert size per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 50 MB        | 50 MB        | 50 MB         | 50 MB           |

When you reach the per second [upsert](/guides/index-data/upsert-data) size for a namespace in an index, additional upserts will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max upsert size limit per second for index <index name>. 
  Pace your upserts or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Query read units per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 2,000        | 2,000        | 2,000         | 2,000           |

Pinecone measures [query](/guides/search/search-overview) usage in [read units](/guides/manage-cost/understanding-cost#read-units). When you reach the per second limit for queries across all namespaces in an index, additional queries will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max query read units per second for index <index name>. 
  Pace your queries or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

To check how many read units a query consumes, [check the query response](/guides/manage-cost/monitor-usage-and-costs#read-units).

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### Query requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [query](/guides/search/search-overview) limit for a namespace in an index, additional queries will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the query QPS limit for namespace {namespace_name} ({limit} QPS). Pace your queries,
  consider Dedicated Read Nodes for your index, or contact Pinecone Support
  (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### Update records per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [update](/guides/manage-data/update-data) limit for a namespace in an index, additional updates will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max update records per second for namespace <namespace name>. 
  Pace your update requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Update requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [update](/guides/manage-data/update-data) request limit for a namespace in an index, additional update requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the update QPS limit for namespace {namespace_name} ({limit} QPS). Pace your update requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

<Tip>
  If you need to update most of the records in a large namespace, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) for help creating an export to enable a faster and more cost-effective approach.
</Tip>

### Update by metadata requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5            | 5            | 5             | 5               |

When you reach the per second [update by metadata](/guides/manage-data/update-data#update-metadata-across-multiple-records) request limit for a namespace in an index, additional update by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max update by metadata requests per second for namespace <namespace name>. Pace your update by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Update by metadata requests per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 500          | 500          | 500           | 500             |

When you reach the per second [update by metadata](/guides/manage-data/update-data#update-metadata-across-multiple-records) request limit across all namespaces in an index, additional update by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max update by metadata requests per second for index <index name>. Pace your update by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Upsert requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [upsert](/guides/index-data/upsert-data) request limit for a namespace in an index, additional upsert requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the upsert QPS limit for namespace {namespace_name} ({limit} QPS). Pace your upsert requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Fetch requests per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [fetch](/guides/manage-data/fetch-data) limit across all namespaces in an index, additional fetch requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max fetch requests per second for index <index name>.
  Pace your fetch requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### List requests per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 200          | 200          | 200           | 200             |

When you reach the per second [list](/guides/manage-data/list-record-ids) limit across all namespaces in an index, additional list requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max list requests per second for index <index name>.
  Pace your list requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

### Describe index stats requests per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [describe index stats](/reference/api/2024-10/data-plane/describeindexstats) limit across all namespaces in an index, additional describe index stats requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max describe_index_stats requests per second for index <index>. 
  Pace your describe_index_stats requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 100          | 100           | 100             |

When you reach the per second [delete](/guides/manage-data/delete-data) request limit for a namespace in an index, additional delete requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the delete QPS limit for namespace {namespace_name} ({limit} QPS). Pace your delete requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete records per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5000         | 5000         | 5000          | 5000            |

When you reach the per second [delete](/guides/manage-data/delete-data) limit for a namespace in an index, additional deletes will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max delete records per second for namespace <namespace name>. 
  Pace your delete requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete records per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5000         | 5000         | 5000          | 5000            |

When you reach the per second [delete](/guides/manage-data/delete-data) limit across all namespaces in an index, additional deletes will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max delete records per second for index <index name>. 
  Pace your delete requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete by metadata requests per second per namespace

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5            | 5            | 5             | 5               |

When you reach the per second [delete by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) request limit for a namespace in an index, additional delete by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max delete by metadata requests per second for namespace <namespace name>. Pace your delete by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Delete by metadata requests per second per index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 500          | 500          | 500           | 500             |

When you reach the per second [delete by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) request limit across all namespaces in an index, additional delete by metadata requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max delete by metadata requests per second for index <index name>. Pace your delete by metadata requests or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). If you need a higher limit for your use case, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Embedding tokens per minute per model

| Embedding model              | Input type | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :--------------------------- | :--------- | :----------- | :----------- | :------------ | :-------------- |
| `llama-text-embed-v2`        | Passage    | 250,000      | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 50,000       | 250,000       | 250,000         |
| `multilingual-e5-large`      | Passage    | 250,000      | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 50,000       | 250,000       | 250,000         |
| `pinecone-sparse-english-v0` | Passage    | 250,000      | 250,000      | 3,000,000     | 3,000,000       |
|                              | Query      | 250,000      | 250,000      | 3,000,000     | 3,000,000       |

When you reach the per minute token limit for an [embedding model](/guides/index-data/create-an-index#embedding-models) hosted by Pinecone, additional embeddings will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max embedding tokens per minute (<limit>) model '<model name>'' and input type '<passage|query>' for the current project. 
  To increase this limit, upgrade your plan.
  ```
</Accordion>

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan). Otherwise, you can handle this limit by [implementing retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).

### Embedding tokens per month per model

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5,000,000    | 10,000,000   | Unlimited     | Unlimited       |

When you reach the monthly token limit for an [embedding model](/guides/index-data/create-an-index#embedding-models) hosted by Pinecone, additional embeddings will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the embedding token limit (<limit>) for model <model name> for the current month. 
  To continue using this model, upgrade your plan.
  ```
</Accordion>

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Rerank requests per minute per model

| Reranking model        | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :--------------------- | :------------ | :------------ | :------------ | :-------------- |
| `cohere-rerank-4-fast` | Not available | Not available | 300           | 300             |
| `cohere-rerank-3.5`    | Not available | Not available | 300           | 300             |
| `bge-reranker-v2-m3`   | 60            | 60            | 60            | 60              |
| `pinecone-rerank-v0`   | 60            | Not available | 60            | 60              |

When you reach the per minute request limit for a [reranking model](/guides/search/rerank-results#reranking-models) hosted by Pinecone, additional reranking requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max rerank requests per minute (<limit>) for model '<model name>' for the current project. 
  To increase this limit, upgrade your plan.
  ```
</Accordion>

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Rerank requests per month per model

| Reranking model        | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :--------------------- | :------------ | :------------ | :------------ | :-------------- |
| `cohere-rerank-4-fast` | Not available | Not available | Unlimited     | Unlimited       |
| `cohere-rerank-3.5`    | Not available | Not available | Unlimited     | Unlimited       |
| `bge-reranker-v2-m3`   | 500           | 1,000         | Unlimited     | Unlimited       |
| `pinecone-rerank-v0`   | 500           | Not available | Unlimited     | Unlimited       |

When you reach the monthly request limit for a [reranking model](/guides/search/rerank-results#reranking-models) hosted by Pinecone, additional reranking requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the rerank request limit (<limit>) for model <model name> for the current month. 
  To continue using this model, upgrade your plan.
  ```
</Accordion>

To increase this limit, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Inference requests per second or minute, per project

| Metric                        | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :---------------------------- | :----------- | :----------- | :------------ | :-------------- |
| Inference requests per second | 100          | 100          | 100           | 100             |
| Inference requests per minute | 2000         | 2000         | 2000          | 2000            |

When you reach the per second or per minute request limit, inference requests will fail and return a `429 - TOO_MANY_REQUESTS` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max inference requests per second (<limit>) for the current project.
  ```
</Accordion>

<Note>
  This error indicates per second or per minute, as applicable.
</Note>

To handle this limit, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).

## Object limits

Object limits are restrictions on the number or size of objects in Pinecone. Object limits vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Metric                                                                         | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :----------------------------------------------------------------------------- | :----------- | :----------- | :------------ | :-------------- |
| [Projects per organization](#projects-per-organization)                        | 1            | 5            | 20            | 100             |
| [Users per organization](#users-per-organization)                              | 2            | 5            | Unlimited     | Unlimited       |
| [Serverless indexes per project](#serverless-indexes-per-project) <sup>1</sup> | 5            | 10           | 20            | 200             |
| [Serverless index storage per org](#serverless-index-storage-per-org)          | 2 GB         | 10 GB        | N/A           | N/A             |
| [Namespaces per serverless index](#namespaces-per-serverless-index)            | 100          | 1,000        | 100,000       | 100,000         |
| [Serverless backups per project](#serverless-backups-per-project)              | N/A          | N/A          | 500           | 1000            |
| [Collections per project](#collections-per-project)                            | 100          | N/A          | N/A           | N/A             |

<sup>1 On the Starter plan, all serverless indexes must be in the `us-east-1` region of AWS. Builder, Standard, and Enterprise plans can create indexes in any [supported region](/guides/index-data/create-an-index#cloud-regions).</sup><br />

### Projects per organization

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 1            | 5            | 20            | 100             |

When you reach this quota for an organization, trying to [create projects](/guides/projects/create-a-project) will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max projects allowed in organization <org name>. 
  To add more projects, upgrade your plan.
  ```
</Accordion>

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### Users per organization

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 2            | 5            | Unlimited     | Unlimited       |

When you reach this quota for an organization, trying to add users to the organization will fail. To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Serverless indexes per project

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 5            | 10           | 20            | 200             |

When you reach this quota for a project, trying to [create serverless indexes](/guides/index-data/create-an-index#create-a-serverless-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max serverless indexes allowed in project <project>. 
  Use namespaces to partition your data into logical groups, or upgrade your plan to add more serverless indexes.
  ```
</Accordion>

To stay under this quota, consider using [namespaces](/guides/index-data/create-an-index#namespaces) instead of creating multiple indexes. Namespaces let you partition your data into logical groups within a single index. This approach not only helps you stay within index limits, but can also improve query performance and lower costs by limiting searches to relevant data subsets.

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Serverless index storage per org

<Note>This limit applies to organizations on the Starter and Builder plans only.</Note>

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 2 GB         | 10 GB        | N/A           | N/A             |

When you've reached this quota for an organization, updates and upserts into serverless indexes will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max storage allowed for organization <org name>. 
  To update or upsert new data, delete records or upgrade your plan.
  ```
</Accordion>

To continue writing data into your serverless indexes, [delete records](/guides/manage-data/delete-data) to bring your organization under the limit or [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

### Namespaces per serverless index

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | 1,000        | 100,000       | 100,000         |

When you reach this quota for a serverless index, trying to [upsert records into a new namespace](/guides/index-data/upsert-data) in the index will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max namespaces allowed in serverless index <index name>. 
  To add more namespaces, upgrade your plan.
  ```
</Accordion>

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

<Note>
  [Namespaces per serverless index](/reference/api/database-limits#namespaces-per-serverless-index) vary by plan. On the Standard and Enterprise plans, Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

### Serverless backups per project

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| N/A          | N/A          | 500           | 1000            |

Backups are not available on the Starter or Builder plans. On the Standard and Enterprise plans, when you reach this quota for a project, trying to [create serverless backups](/guides/manage-data/back-up-an-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Backup failed to create. Quota for number of backups per index exceeded.
  ```
</Accordion>

### Collections per project

| Starter plan | Builder plan | Standard plan | Enterprise plan |
| ------------ | ------------ | ------------- | --------------- |
| 100          | N/A          | N/A           | N/A             |

When you reach this quota for a project, trying to [create collections](/guides/manage-data/back-up-an-index) in the project will fail and return a `403 - QUOTA_EXCEEDED` status with the following error:

<Accordion title="Error response">
  ```
  Request failed. You've reached the max collections allowed in project <project name>. 
  To add more collections, upgrade your plan.
  ```
</Accordion>

To increase this quota, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).

## Operation limits

Operation limits are restrictions on the size, number, or other characteristics of operations in Pinecone. Operation limits are fixed and do not vary based on pricing plan.

### Upsert limits

| Metric                                                             | Limit                                                         |
| :----------------------------------------------------------------- | :------------------------------------------------------------ |
| Max [batch size](/guides/index-data/upsert-data#upsert-in-batches) | 2 MB or 1000 records with vectors <br /> 96 records with text |
| Max documents per upsert request                                   | 1000                                                          |
| Max document upsert request size                                   | 2 MB                                                          |
| Max document size                                                  | 2 MB                                                          |
| Max `full_text_search` string fields per schema                    | 100                                                           |
| Max size per `full_text_search` string field                       | 100 KB                                                        |
| Max tokens per `full_text_search` string field                     | 10,000                                                        |
| Max bytes per token                                                | 256 bytes                                                     |
| Max filterable metadata size per document                          | 40 KB                                                         |
| Max length for a record ID                                         | 512 characters                                                |
| Max dimensionality for dense vectors                               | 20,000                                                        |
| Max non-zero values for sparse vectors                             | 2048                                                          |
| Max dimensionality for sparse vectors                              | 4.2 billion                                                   |

The 40 KB filterable metadata limit does not apply to `full_text_search` text fields.

### Import limits

<Note>
  If your import exceeds these limits, you'll get an error specifying the limit exceeded. See [Troubleshooting](/guides/index-data/import-data#troubleshooting) for details.
</Note>

| Metric                                        | Limit     |
| :-------------------------------------------- | :-------- |
| Max namespaces per import                     | 10,000    |
| Max total input data size (on-demand indexes) | 1 TB      |
| Max total input data size (DRN indexes)       | Unlimited |
| Max files per import                          | 100,000   |
| Max size per file                             | 10 GB     |

The total input data size limit does not apply to indexes with [dedicated read nodes](/guides/index-data/dedicated-read-nodes).

Bulk import is supported only for indexes without a schema definition. It is not supported for indexes with schemas, including full-text search indexes with document schemas and semantic-text-only integrated embedding indexes.

### Query limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them.
</Tip>

### Fetch limits

**Fetch by ID limits:**

| Metric                           | Limit |
| :------------------------------- | :---- |
| Max record IDs per fetch request | 1,000 |

**Fetch by metadata limits:**

| Metric                   | Limit                               |
| :----------------------- | :---------------------------------- |
| Max records per response | 10,000                              |
| Max response size        | 4 MB                                |
| Max request rate         | 5 requests per second per namespace |

To retrieve more than 10,000 matching records, paginate through results using the `paginationToken` parameter. See [Fetch records by metadata](/guides/manage-data/fetch-data#fetch-records-by-metadata).

### Delete limits

| Metric                            | Limit |
| :-------------------------------- | :---- |
| Max record IDs per delete request | 1,000 |

### Metadata filter limits

The following limits apply to [metadata filter expressions](/guides/search/filter-by-metadata#metadata-filter-expressions) used in query, delete, update, and fetch operations.

| Limit                                       | Value  | Description                                                                                                                                                                                                      |
| :------------------------------------------ | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum values per `$in` or `$nin` operator | 10,000 | Each `$in` or `$nin` operator accepts up to 10,000 values in its array. This limit applies per operator—if you have multiple `$in` operators in a single filter, each is independently limited to 10,000 values. |

When you exceed this limit, the request will fail and return a `400 - BAD_REQUEST` error.

#### Rationale

Large `$in` operators can impact query performance and cost. Filters with thousands of values increase request payload size and end-to-end latency. Additionally, using large filters typically indicates a shared namespace architecture, which increases query costs—queries scan the entire namespace regardless of filters.

#### Alternative approaches

If you need to filter by more than 10,000 values, consider these alternatives:

* **Use namespaces for tenant isolation**: Instead of filtering by tenant IDs within a single namespace, create separate namespaces for each tenant or tenant group. This can also reduce query costs. See [Design for multi-tenancy](/guides/index-data/data-modeling#design-for-multi-tenancy).
* **Use broader access control groups**: Instead of filtering by individual user IDs, filter by organization, project, or role. This reduces the number of values in your `$in` filter. See [Design for multi-tenancy](/guides/index-data/data-modeling#use-access-control-groups-instead-of-individual-ids).
* **Post-filter client-side**: Retrieve a larger top K without filtering (for example, top 1000), then filter results client-side.
* **Run multiple queries**: Split your filter into multiple queries with smaller `$in` operators and combine the results client-side.

<Tip>
  To avoid hitting this limit in production, validate the size of your `$in` and `$nin` arrays in your application code before making the request to Pinecone.
</Tip>

## Identifier limits

An identifier is a string of characters used to identify "named" [objects in Pinecone](/guides/get-started/concepts). The following Pinecone objects use strings as identifiers:

| Object                                                    | Field       | Max # characters | Allowed characters                                                                                                                        |
| --------------------------------------------------------- | ----------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](/guides/get-started/concepts#organization) | `name`      | 512              | <ul><li>UTF-8 except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
| [Project](/guides/get-started/concepts#project)           | `name`      | 512              | <ul><li>UTF-8 except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
| [Index](/guides/get-started/concepts#index)               | `name`      | 45               | <ul><li>`a-z`, `0-9`, and `-`</li><li>Must be lowercase</li><li>Cannot start or end with `-`</li><li>Cannot be empty</li></ul>            |
| [Namespace](/guides/get-started/concepts#namespace)       | `namespace` | 512              | <ul><li>ASCII except `\0`</li><li>For the default namespace, use `""` (or `"__default__"`, in API versions `2025-04` and later)</li></ul> |
| [Record](/guides/get-started/concepts#record)             | `id`        | 512              | <ul><li>ASCII except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
