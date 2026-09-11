---
title: "Rate limits"
source: https://docs.pinecone.io/reference/api/database-limits/rate-limits
path: reference/api/database-limits/rate-limits
---

Request-per-second, monthly usage, and model throughput limits for Pinecone Database serverless indexes, and the 429 errors returned when you exceed them.

Rate limits help protect your applications from misuse and maintain the health of our shared serverless infrastructure. They vary by [pricing plan](https://www.pinecone.io/pricing/) and apply to [serverless indexes](/guides/index-data/indexing-overview) only.

Request-per-second limits are enforced per namespace or per index, as noted in the [Data operation throughput limits](#data-operation-throughput-limits) table, in addition to your read and write unit limits, so a request fails if it exceeds any applicable limit. When you exceed a limit, the request returns a `429 - TOO_MANY_REQUESTS` and the error message names the limit, scope, and value.

**Most rate limits can be adjusted upon request.** If you need higher limits, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

## Monthly usage limits

[Read units](/guides/manage-cost/understanding-cost#read-units) and [write units](/guides/manage-cost/understanding-cost#write-units) measure resource consumption. To check your current usage, see [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs).

| Metric                               | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :----------------------------------- | :----------- | :----------- | :------------ | :-------------- |
| Read units per month per org         | 1,000,000    | 2,000,000    | Unlimited     | Unlimited       |
| Write units per month per org        | 2,000,000    | 5,000,000    | Unlimited     | Unlimited       |
| Embedding tokens per month per model | 5,000,000    | 10,000,000   | Unlimited     | Unlimited       |

Monthly rerank request limits vary by model:

| Reranking model        | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :--------------------- | :------------ | :------------ | :------------ | :-------------- |
| `cohere-rerank-4-fast` | Not available | Not available | Unlimited     | Unlimited       |
| `cohere-rerank-3.5`    | Not available | Not available | Unlimited     | Unlimited       |
| `bge-reranker-v2-m3`   | 500           | 1,000         | Unlimited     | Unlimited       |
| `pinecone-rerank-v0`   | 500           | Not available | Unlimited     | Unlimited       |

Reaching a monthly usage limit returns a `429 - TOO_MANY_REQUESTS`. [Upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) to continue.

<Accordion title="Example error">
  ```
  Request failed. You've reached your read unit limit for the current month.
  To continue reading data, upgrade your plan.
  ```
</Accordion>

## Data operation throughput limits

| Metric                                               | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :--------------------------------------------------- | :----------- | :----------- | :------------ | :-------------- |
| Upsert size per second per namespace                 | 50 MB        | 50 MB        | 50 MB         | 50 MB           |
| Query read units per second per index                | 2,000        | 2,000        | 2,000         | 2,000           |
| Query requests per second per namespace              | 100          | 100          | 100           | 100             |
| Update records per second per namespace              | 100          | 100          | 100           | 100             |
| Update requests per second per namespace             | 100          | 100          | 100           | 100             |
| Update by metadata requests per second per namespace | 5            | 5            | 5             | 5               |
| Update by metadata requests per second per index     | 500          | 500          | 500           | 500             |
| Upsert requests per second per namespace             | 100          | 100          | 100           | 100             |
| Fetch requests per second per index                  | 100          | 100          | 100           | 100             |
| List requests per second per index                   | 200          | 200          | 200           | 200             |
| Describe index stats requests per second per index   | 100          | 100          | 100           | 100             |
| Delete requests per second per namespace             | 100          | 100          | 100           | 100             |
| Delete records per second per namespace              | 5,000        | 5,000        | 5,000         | 5,000           |
| Delete records per second per index                  | 5,000        | 5,000        | 5,000         | 5,000           |
| Delete by metadata requests per second per namespace | 5            | 5            | 5             | 5               |
| Delete by metadata requests per second per index     | 500          | 500          | 500           | 500             |

Exceeding a per-second throughput limit returns a `429 - TOO_MANY_REQUESTS`. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic), pace your requests, consider [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) (which aren't subject to per-second read limits) for high-throughput reads, or [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to raise a limit.

<Accordion title="Example error">
  ```
  Request failed. You've reached the query QPS limit for namespace {namespace_name} ({limit} QPS). Pace your queries, consider Dedicated Read Nodes for your index, or contact Pinecone Support (https://app.pinecone.io/organizations/-/settings/support/ticket) to request a higher limit.
  ```
</Accordion>

## Model throughput limits

Per-minute token limits for embedding models:

| Embedding model              | Input type | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :--------------------------- | :--------- | :----------- | :----------- | :------------ | :-------------- |
| `llama-text-embed-v2`        | Passage    | 250,000      | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 50,000       | 250,000       | 250,000         |
| `multilingual-e5-large`      | Passage    | 250,000      | 250,000      | 1,000,000     | 1,000,000       |
|                              | Query      | 50,000       | 50,000       | 250,000       | 250,000         |
| `pinecone-sparse-english-v0` | Passage    | 250,000      | 250,000      | 3,000,000     | 3,000,000       |
|                              | Query      | 250,000      | 250,000      | 3,000,000     | 3,000,000       |

Per-minute request limits for reranking models:

| Reranking model        | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :--------------------- | :------------ | :------------ | :------------ | :-------------- |
| `cohere-rerank-4-fast` | Not available | Not available | 300           | 300             |
| `cohere-rerank-3.5`    | Not available | Not available | 300           | 300             |
| `bge-reranker-v2-m3`   | 60            | 60            | 60            | 60              |
| `pinecone-rerank-v0`   | 60            | Not available | 60            | 60              |

Reaching a per-minute model limit returns a `429 - TOO_MANY_REQUESTS`. [Upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) to increase it, or [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).

<Accordion title="Example error">
  ```
  Request failed. You've reached the max embedding tokens per minute (<limit>) model '<model name>' and input type '<passage|query>' for the current project.
  To increase this limit, upgrade your plan.
  ```
</Accordion>

## Inference request limits

| Metric                                    | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :---------------------------------------- | :----------- | :----------- | :------------ | :-------------- |
| Inference requests per second per project | 100          | 100          | 100           | 100             |
| Inference requests per minute per project | 2,000        | 2,000        | 2,000         | 2,000           |

Exceeding the per-second or per-minute limit returns a `429 - TOO_MANY_REQUESTS`. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle it.

<Accordion title="Example error">
  ```
  Request failed. You've reached the max inference requests per second (<limit>) for the current project.
  ```

  The message names the per-second or per-minute limit, whichever you exceeded.
</Accordion>
