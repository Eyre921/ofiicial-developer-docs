---
title: "Downgrade your plan"
source: https://docs.pinecone.io/guides/assistant/admin/downgrade-billing-plan
path: guides/assistant/admin/downgrade-billing-plan
---

Downgrade your Pinecone subscription from a paid tier back to the free Starter plan, including steps to review usage limits before switching.

<Note>
  To change your billing plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  If you are on the Standard plan with credit/debit card billing and want to reduce spend without returning to the free Starter plan, consider [switching to the Builder plan](#switch-from-standard-to-builder) for a flat \$20/month.
</Tip>

## Before you downgrade

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

## Downgrade to the Starter plan

The downgrade process is different depending on how you are paying for Pinecone.

<Warning>
  Start the downgrade in the Pinecone console, as described below. The console walks you through what to keep and cleans up the rest. If you start the downgrade in a cloud marketplace instead, that cleanup doesn't run, so Pinecone deactivates your account and you'll need to [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Warning>

<Tabs>
  <Tab title="Credit card">
    If you are paying with a credit card, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. Click **Downgrade** in the **Starter** plan section.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Google Cloud Marketplace">
    If you are paying through the Google Cloud Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the GCP marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
    5. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your Pinecone subscription.

       <Tip>
         If you don't see the order, check that the correct billing account is selected.
       </Tip>

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="AWS Marketplace">
    If you are paying through the AWS Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the AWS marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
    5. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Microsoft Marketplace">
    If you are paying through the Microsoft Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on Microsoft marketplace** modal, click **Continue to marketplace**.
    5. On the **SaaS** page, click your subscription to Pinecone.
    6. Click **Cancel subscription**.
    7. Confirm the cancellation.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>
</Tabs>

## Switch from Standard to Builder

If you are on the **Standard plan** with credit/debit card billing and would like to switch to the [Builder plan](/reference/api/database-limits) (flat \$20/month), do the following:

1. Bring your organization under the [Builder plan quotas](/reference/api/database-limits). In particular, you must be within the Builder plan limits for projects, indexes, namespaces, storage, users, and monthly usage units.
2. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
3. Click **Switch to Builder** in the **Builder** plan section.
4. Confirm the change.

After switching, overages are no longer billed—requests that exceed Builder quotas are blocked instead. If you need more capacity, [upgrade back to Standard or Enterprise](/guides/organizations/manage-billing/upgrade-billing-plan) at any time.

<Note>
  The [Builder plan](https://www.pinecone.io/pricing/) is available with credit/debit card billing only and is not supported through cloud marketplaces.
</Note>

If you pay through a cloud marketplace, you cannot switch to the Builder plan at this time. [Contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to be notified when this migration becomes available.
