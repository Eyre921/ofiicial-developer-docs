---
title: "Object limits"
source: https://docs.pinecone.io/reference/api/database-limits/object-limits
path: reference/api/database-limits/object-limits
---

Limits on the number and size of Pinecone Database projects, indexes, namespaces, storage, backups, and collections, by plan.

Object limits are restrictions on the number or size of objects in Pinecone. They vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Metric                                      | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------------------------------------ | :----------- | :----------- | :------------ | :-------------- |
| Projects per organization                   | 1            | 5            | 20            | 100             |
| Users per organization                      | 2            | 5            | Unlimited     | Unlimited       |
| Serverless indexes per project <sup>1</sup> | 5            | 10           | 20            | 200             |
| Serverless index storage per org            | 2 GB         | 10 GB        | N/A           | N/A             |
| Namespaces per serverless index             | 100          | 1,000        | 100,000       | 100,000         |
| Serverless backups per project              | N/A          | N/A          | 500           | 1,000           |
| Collections per project                     | 100          | N/A          | N/A           | N/A             |

<sup>1 On the Starter plan, all serverless indexes must be in the `us-east-1` region of AWS. Builder, Standard, and Enterprise plans can create indexes in any [supported region](/guides/index-data/create-an-index#cloud-regions).</sup><br />

When you exceed an object limit, API operations return a `403 - QUOTA_EXCEEDED`. [Upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan) to increase the limit. If a higher plan still doesn't cover what you need, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case, since most object limits can be raised on request.

<Accordion title="Example error">
  ```
  Request failed. You've reached the max projects allowed in organization <org name>.
  To add more projects, upgrade your plan.
  ```
</Accordion>

For the serverless storage limit, you can also [delete records](/guides/manage-data/delete-data) to get back under it.

<Tip>
  To stay under the serverless index limit, use [namespaces](/guides/index-data/create-an-index#namespaces) to partition data within a single index instead of creating multiple indexes. This can also improve query performance and lower costs by limiting searches to relevant data subsets.
</Tip>

<Note>
  [Namespaces per serverless index](/reference/api/database-limits/object-limits) vary by plan. On the Standard and Enterprise plans, Pinecone can accommodate million-scale namespaces and beyond for specific use cases. If your application requires more than 100,000 namespaces, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>
