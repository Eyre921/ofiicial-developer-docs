---
title: "Pinecone Assistant limits"
source: https://docs.pinecone.io/reference/api/assistant/assistant-limits
path: reference/api/assistant/assistant-limits
---

Pinecone REST API:

Pinecone Assistant limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

### Object limits

Object limits are restrictions on the number or size of assistant-related objects. Limits below are scoped **per organization** except for **Assistants per project**, which is scoped per project.

| Metric                              | Starter plan      | Builder plan      | Standard plan | Enterprise plan |
| :---------------------------------- | :---------------- | :---------------- | :------------ | :-------------- |
| Assistants per project              | 5                 | 200               | Unlimited     | Unlimited       |
| File storage per org                | 1 GB              | 3 GB              | Unlimited     | Unlimited       |
| Chat input tokens per org           | 500,000 / month\* | 2,000,000 / month | Unlimited     | Unlimited       |
| Chat output tokens per org          | 300,000 / month   | 1,000,000 / month | Unlimited     | Unlimited       |
| Context retrieval tokens per org    | 500,000 / month   | 2,000,000 / month | Unlimited     | Unlimited       |
| Ingestion units per org             | 1,000 / month     | 10,000 / month    | Unlimited     | Unlimited       |
| File size (.docx, .json, .md, .txt) | 10 MB             | 10 MB             | 10 MB         | 10 MB           |
| File size (.pdf)                    | 10 MB             | 50 MB             | 100 MB        | 100 MB          |
| Metadata size per file              | 16 KB             | 16 KB             | 16 KB         | 16 KB           |

*\*1,000,000 input tokens/month to explore [Marketplace apps](/guides/marketplace) until June 30, 2026.*

Additionally, the following limits apply to [multimodal PDFs](/guides/assistant/multimodal) (currently in [public preview](/release-notes/feature-availability)):

Multimodal PDF processing uses the same [ingestion unit](/guides/assistant/pricing-and-limits#ingestion) as standard uploads; it is billed at about **twice** the standard per-unit rate (see [Pricing and limits](/guides/assistant/pricing-and-limits)). Object and rate limits for assistants also apply—see [#limits](/guides/assistant/pricing-and-limits#limits) and [#rate-limits](/guides/assistant/pricing-and-limits#rate-limits).

| Metric        | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------ | :----------- | :----------- | :------------ | :-------------- |
| Max file size | 10 MB        | 10 MB        | 50 MB         | 50 MB           |
| Page limit    | 100          | 100          | 100           | 100             |

### Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

Requests that exceed a rate limit fail and return a `429 - TOO_MANY_REQUESTS` status.

<Tip>To handle rate limits, implement [retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).</Tip>

| Metric                                      | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :------------------------------------------ | :------------ | :------------ | :------------ | :-------------- |
| Assistant list/get requests per minute      | 40            | 50            | 100           | 500             |
| Assistant create/update requests per minute | 20            | 25            | 50            | 100             |
| Assistant delete requests per minute        | 20            | 25            | 50            | 100             |
| File get requests per minute                | 100           | 150           | 300           | 6,000           |
| File list requests per minute               | 50            | 75            | 150           | 3,000           |
| File upload requests per minute             | 5             | 15            | 20            | 300             |
| Multimodal PDF upload requests per minute   | 5             | 10            | 20            | 40              |
| File delete requests per minute             | 5             | 15            | 20            | 300             |
| Chat input tokens per minute                | 100,000       | 200,000       | 300,000       | 1,000,000       |
| Chat history tokens per query               | 64,000        | 64,000        | 64,000        | 64,000          |
| Evaluation input tokens per minute          | Not available | Not available | 150,000       | 500,000         |
