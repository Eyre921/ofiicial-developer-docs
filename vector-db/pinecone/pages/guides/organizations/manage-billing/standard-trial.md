---
title: "Standard trial"
source: https://docs.pinecone.io/guides/organizations/manage-billing/standard-trial
path: guides/organizations/manage-billing/standard-trial
---

Get $300 credits for 21 days with the Standard plan trial.

The Standard trial lets you evaluate Pinecone without requiring any up-front payment. You get \$300 in credits over 21 days with access to Standard plan [features](https://www.pinecone.io/pricing/) and [limits](/reference/api/database-limits) that are suitable for testing Pinecone at scale.

<Note>
  If you're building a small or personal project, consider the free [Starter plan](https://www.pinecone.io/pricing/) or the flat-rate [Builder plan](https://www.pinecone.io/pricing/) instead.
</Note>

## Key features

* \$300 in credits
* 21 days of access to Standard plan [features](https://www.pinecone.io/pricing/), including:
  * [Bulk import](/guides/index-data/import-data)
  * [Backup and restore](/guides/manage-data/backups-overview)
  * [RBAC (role-based access control)](/guides/production/security-overview#role-based-access-control)
* [Higher limits](/reference/api/database-limits) for testing at scale
* Access to all [cloud regions](/guides/index-data/create-an-index#cloud-regions)
* Access to [Developer Support](https://www.pinecone.io/pricing/?plans=support)

## Expiration

At the end of a Standard trial, or when you've used all of your credits, you can take one of the following actions:

* Add a payment method and continue on with the Standard plan.
* Upgrade to the Enterprise plan.
* [Downgrade to the Starter plan](#downgrading-to-the-starter-plan) (you can also do this before your trial expires, if you choose).

<Note>
  Learn more about [pricing](https://www.pinecone.io/pricing/).
</Note>

## Downgrading to the Starter plan

To downgrade from a Standard trial to the Starter plan, you'll need to bring your usage within Starter plan limits.

* No more than 5 indexes, all serverless and in the `us-east-1` region of AWS
  * If you have serverless indexes in a region other than `us-east-1`, [create a new serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in `us-east-1`, [re-upsert your data](/guides/index-data/upsert-data) into the new index, and [delete the old index](/guides/manage-data/manage-indexes#delete-an-index).
  * If you have more than 5 serverless indexes, [delete indexes](/guides/manage-data/manage-indexes#delete-an-index) until you have 5 or fewer.
  * If you have pod-based indexes, [delete them](/guides/manage-data/manage-indexes#delete-an-index).
* No more than 1 project
  * If you have more than 1 project, [delete all but 1 project](/guides/projects/manage-projects#delete-a-project).
  * Before you can delete a project, you must [delete all indexes](/guides/manage-data/manage-indexes#delete-an-index) and [delete all collections](/guides/manage-data/back-up-an-index#delete-a-collection) in the project.
* No more than 2 GB of data across all of your serverless indexes
  * If you are storing more than 2 GB of data, [delete records](/guides/manage-data/delete-data) until you're storing less than 2 GB.
* No more than 100 namespaces per serverless index
  * If any serverless index has more than 100 namespaces, [delete namespaces](/guides/manage-data/delete-data#delete-all-records-from-a-namespace) until it has 100 or fewer remaining.
* No more than 3 [assistants](/guides/assistant/overview)
  * If you have more than 3 assistants, [delete assistants](/guides/assistant/manage-assistants#delete-an-assistant) until you have 3 or fewer.
* Within the Starter plan's monthly [ingestion](/guides/assistant/pricing-and-limits#ingestion) and token limits
  * Your usage must fit within the Starter plan limits for [ingestion units](/guides/assistant/pricing-and-limits#ingestion), chat tokens, context tokens, and storage. Reduce files or usage until you are within those limits.
* No more than 1 GB of assistant storage
  * If you have more than 1 GB of assistant storage, [delete files](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file) until you're storing less than 1 GB.
* No more than 2 users
* No collections or backups (these are automatically deleted as part of the downgrade process)

<Note>
  You do not need to bring [Assistant usage](/guides/assistant/pricing-and-limits) (ingestion, tokens, and so on) under Starter caps before downgrading. If you exceed Starter limits after downgrading, new requests may be blocked until usage is within limits.
</Note>

<Note>
  **Switching from Standard to Builder instead of Starter?** Your organization must be under the [Builder plan quotas](/reference/api/database-limits), backups must be deleted, and any features not available on Builder—such as bulk import, pod-based indexes, storage integrations, RBAC, and SSO—must be removed or stopped.
</Note>

If you have questions, [contact Support](https://www.pinecone.io/contact/support/).

## Limits

* Each organization is allowed only one trial.
* Organizations already on a Builder, Standard, or Enterprise plan cannot activate a Standard plan trial.
* Organizations that initially subscribed to Pinecone through marketplace partners cannot activate a Standard plan trial.

If you have any questions, [contact Support](https://www.pinecone.io/contact/support/).
