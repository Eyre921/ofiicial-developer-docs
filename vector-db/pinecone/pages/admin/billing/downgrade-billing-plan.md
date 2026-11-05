---
title: "Downgrade your billing plan"
source: https://docs.pinecone.io/admin/billing/downgrade-billing-plan
path: admin/billing/downgrade-billing-plan
---

Downgrade your Pinecone organization from a paid plan to the free Starter plan, including plan requirements, index limits, and billing impact.

> [!NOTE]
>
> To change your billing plan, you must be an [organization owner or billing admin](/admin/organizations/organizations-overview#organization-roles).

> [!TIP]
>
> If you're on the Standard plan with credit/debit card billing and want to reduce spend without returning to the free Starter plan, consider [switching to the Builder plan](#switch-from-standard-to-builder) for a flat \$20/month.

## Before you downgrade

When you downgrade to the Starter plan in the Pinecone console, you choose which projects, indexes, assistants, and members to keep. You can keep up to the [Starter plan limits](/reference/api/database-limits/object-limits): 1 project, 5 serverless indexes in the `us-east-1` region of AWS, 5 assistants, and 2 members. Pinecone deletes everything you don't keep, along with all backups, backup schedules, and collections.

The downgrade doesn't reduce your data or change your configuration, so do this first:

* **Indexes outside `us-east-1`**: Indexes in other [regions](/guides/indexes/index-configuration#cloud-regions) can't be kept on Starter. To keep one, [create a new index](/guides/indexes/create-an-index) in `us-east-1`, [re-upsert your data](/guides/data/upsert-data), and delete the old index.
* **Gemini and `us` processing indexes**: Indexes with embedded fields that use `gemini-embedding-2` or the `us` [processing location](/guides/indexes/processing-locations) can't be kept on Starter. To keep one, create a new index that uses a model available on Starter in place of `gemini-embedding-2`, or that sets `processing_location` to `global`. Then re-upsert your data and delete the old index.
* **Dedicated read node indexes**: These can't run on Starter, and there's no self-serve conversion. To keep one in `us-east-1`, [back it up](/guides/indexes/back-up-an-index) and [restore it](/guides/indexes/restore-an-index), which creates a new on-demand serverless index in the same region. Delete the original and keep the restored index during the downgrade. For one in another region, create a new `us-east-1` index and re-upsert your data. You can also [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to migrate back.
* **Pod-based indexes**: To keep one, [migrate it to serverless](/guides/legacy/pod-based-indexes/migrate-a-pod-based-index-to-serverless) and finish creating the new serverless index first. The migration saves your index as a collection, and the downgrade deletes all collections.
* **`eu` assistants**: These are deleted unless you move them. To keep one, [recreate it in `us`](/guides/assistant/create-assistant) and re-upload its files.
* **SSO**: Disconnect your organization's [SSO connection](/admin/organizations/organizations-overview#organization-single-sign-on-sso).
* **Member roles**: Reassign or remove members whose [organization role](/admin/organizations/organizations-overview#organization-roles) isn't available on Starter.
* **Storage**: Starter allows no more than 2 GB of data across your serverless indexes and 1 GB of assistant storage. [Delete records](/guides/data/delete-data) and [assistant files](/guides/assistant/manage-files#delete-a-file) to fit. Do this last, because the migrations above can briefly leave a second copy of an index.

> [!NOTE]
>
> You don't need to bring [Assistant usage](/guides/assistant/pricing-and-limits) (ingestion units, chat tokens, and context tokens) under Starter caps before downgrading. If you exceed Starter limits after downgrading, new requests may be blocked until usage is within limits.

> [!NOTE]
>
> If you're switching from Standard to Builder instead of Starter, your organization must be under the [Builder plan quotas](/reference/api/database-limits/object-limits). You must also delete all backups and remove or stop any features not available on Builder, such as bulk import, pod-based indexes, storage integrations, RBAC, and SSO.

## Downgrade to the Starter plan

The downgrade process is different depending on how you're paying for Pinecone.

> [!WARNING]
>
> Start the downgrade in the Pinecone console, as described below. The console walks you through what to keep and cleans up the rest. If you start the downgrade in a cloud marketplace instead, that cleanup doesn't run, so Pinecone deactivates your account and you'll need to [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

> [tab] Credit card
>
> 1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
> 2. Click **Downgrade** in the **Starter** plan section.
>
> Your billing ends immediately, but you'll receive a final invoice for any charges accrued in the current month.

> [tab] Google Cloud Marketplace
>
> 1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
> 2. In the **Starter** section, click **Downgrade**.
> 3. Click **Confirm downgrade**.
> 4. On the **Continue your downgrade on GCP Marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
> 5. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your Pinecone subscription.
>
>    > [!TIP]
>    >
>    > If you don't see the order, check that the correct billing account is selected.
>
> Your billing ends immediately, but you'll receive a final invoice for any charges accrued in the current month.

> [tab] AWS Marketplace
>
> 1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
> 2. In the **Starter** section, click **Downgrade**.
> 3. Click **Confirm downgrade**.
> 4. On the **Continue your downgrade on AWS Marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
> 5. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.
>
> Your billing ends immediately, but you'll receive a final invoice for any charges accrued in the current month.

> [tab] Microsoft Marketplace
>
> 1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
> 2. In the **Starter** section, click **Downgrade**.
> 3. Click **Confirm downgrade**.
> 4. On the **Continue your downgrade on Azure Marketplace** modal, click **Continue to marketplace**.
> 5. On the **SaaS** page, click your subscription to Pinecone.
> 6. Click **Cancel subscription**.
> 7. Confirm the cancellation.
>
> Your billing ends immediately, but you'll receive a final invoice for any charges accrued in the current month.

## Switch from Standard to Builder

If you're on the Standard plan and pay by credit/debit card, you can switch to the [Builder plan](/reference/api/database-limits/object-limits) for a flat \$20/month:

1. Bring your organization under the [Builder plan quotas](/reference/api/database-limits). In particular, you must be within the Builder plan limits for projects, indexes, namespaces, storage, users, and monthly usage units.
2. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
3. Click **Switch to Builder** in the **Builder** plan section.
4. Confirm the change.

After switching, overages are no longer billed. Instead, requests that exceed Builder quotas are blocked. If you need more capacity, [upgrade back to Standard or Enterprise](/admin/billing/upgrade-billing-plan) at any time.

> [!NOTE]
>
> The [Builder plan](https://www.pinecone.io/pricing/) is available with credit/debit card billing only and isn't supported through cloud marketplaces.

If you pay through a cloud marketplace, you can't switch to the Builder plan at this time. [Contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to be notified when this migration becomes available.
