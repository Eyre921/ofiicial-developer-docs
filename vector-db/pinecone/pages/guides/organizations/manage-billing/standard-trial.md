---
title: "Pinecone Standard plan trial"
source: https://docs.pinecone.io/guides/organizations/manage-billing/standard-trial
path: guides/organizations/manage-billing/standard-trial
---

Evaluate the Pinecone Standard plan with $300 in credits over 21 days, including bulk import, backup and restore, RBAC, and higher scale limits.

The Standard trial lets you evaluate Pinecone without requiring any up-front payment. You get \$300 in credits over 21 days with access to Standard plan [features](https://www.pinecone.io/pricing/) and [limits](/reference/api/database-limits) that are suitable for testing Pinecone at scale.

<Note>
  If you're building a small or personal project, consider the free [Starter plan](https://www.pinecone.io/pricing/) or the flat-rate [Builder plan](https://www.pinecone.io/pricing/) instead.
</Note>

## Key features

* \$300 in credits
* 21 days of access to Standard plan [features](https://www.pinecone.io/pricing/), including:
  * [Bulk import](/guides/index-data/import-data)
  * [Backup and restore](/guides/manage-data/backups-overview)
  * [RBAC (role-based access control)](/guides/production/security-overview#role-based-access-controls-rbac)
* [Higher limits](/reference/api/database-limits) for testing at scale
* Access to all [cloud regions](/guides/index-data/create-an-index#cloud-regions)
* Access to [Developer Support](https://www.pinecone.io/pricing/?plans=support)

## Expiration

When your Standard trial ends, or when you use all of your credits, your quotas are blocked and console access is limited to the billing page. You don't automatically return to your previous plan; to restore full access, take one of the following actions:

* Add a payment method and continue on the Standard plan.
* Upgrade to the Enterprise plan.
* [Downgrade to the Starter plan](#downgrade-to-the-starter-plan) (you can also do this any time before the trial expires).

If you started the trial from the Builder plan, you aren't charged the \$20/month Builder fee during the trial.

<Note>
  Learn more about [pricing](https://www.pinecone.io/pricing/).
</Note>

## Downgrade to the Starter plan

You can downgrade from a Standard trial to the Starter plan at any time.

When you downgrade to the Starter plan in the Pinecone console, you choose which projects, indexes, assistants, and members to keep, up to the [Starter plan limits](/reference/api/database-limits): 1 project, 5 serverless indexes in the `us-east-1` region of AWS, 5 assistants, and 2 members. Pinecone deletes everything you don't keep, along with all backups, backup schedules, and collections.

The downgrade doesn't reduce your data or change your configuration, so do this first:

* **Move any serverless indexes outside the `us-east-1` region of AWS that you want to keep.** [Create a new index](/guides/index-data/create-an-index) in `us-east-1`, [re-upsert your data](/guides/index-data/upsert-data), and delete the old index before you start the downgrade. Indexes in other [regions](/guides/index-data/create-an-index#cloud-regions) can't be kept on Starter.
* **Migrate any dedicated read node indexes** whose data you want to keep. They can't run on Starter and there's no self-serve conversion. If the index is in `us-east-1`, [back it up](/guides/manage-data/back-up-an-index) and [restore it](/guides/manage-data/restore-an-index) (this creates a new on-demand serverless index in the same region), then delete the original and keep the restored index during the downgrade. If it's in another region, create a new `us-east-1` index and re-upsert your data as described above. You can also [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to migrate back.
* **Migrate any pod-based indexes** whose data you want to keep. [Migrate each one to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless) and finish creating the new serverless index **before** you start the downgrade: the migration saves your index as a collection, and the downgrade deletes all collections.
* **Move any `eu`-region assistants you want to keep to `us`.** [Recreate them in `us`](/guides/assistant/create-assistant) and re-upload their files. `eu` assistants you don't move are deleted.
* **Disconnect your organization's [SSO connection](/guides/organizations/understanding-organizations#organization-single-sign-on-sso).**
* **Reassign or remove members** whose [organization role](/guides/organizations/understanding-organizations#organization-roles) isn't available on the Starter plan.
* **Get under the Starter storage limits.** Do this last, after the migrations above, which can briefly leave a second copy of an index: no more than 2 GB of data across your serverless indexes and 1 GB of assistant storage. [Delete records](/guides/manage-data/delete-data) and [assistant files](/guides/assistant/manage-files#delete-a-file) to fit.

<Note>
  You don't need to bring [Assistant usage](/guides/assistant/pricing-and-limits) (ingestion units, chat tokens, and context tokens) under Starter caps before downgrading. If you exceed Starter limits after downgrading, new requests may be blocked until usage is within limits.
</Note>

<Note>
  **Switching from Standard to Builder instead of Starter?** Your organization must be under the [Builder plan quotas](/reference/api/database-limits), backups must be deleted, and any features not available on Builder, such as bulk import, pod-based indexes, storage integrations, RBAC, and SSO, must be removed or stopped.
</Note>

## Limits

* Each organization is allowed only one trial.
* Organizations already on a Standard or Enterprise plan can't activate a Standard plan trial.
* Organizations that initially subscribed to Pinecone through marketplace partners can't activate a Standard plan trial.

If you have questions, [contact Support](https://www.pinecone.io/contact/support/).
