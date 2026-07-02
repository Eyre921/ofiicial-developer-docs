---
title: "Downgrade your plan"
source: https://docs.pinecone.io/guides/assistant/admin/downgrade-billing-plan
path: guides/assistant/admin/downgrade-billing-plan
---

Downgrade from a paid plan to the free Starter plan.

<Note>
  To change your billing plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  If you are on the Standard plan with credit/debit card billing and want to reduce spend without returning to the free Starter plan, consider [switching to the Builder plan](#switch-from-standard-to-builder) for a flat \$20/month.
</Tip>

## Requirements

Before you can downgrade, your organization must be under the [Starter plan quotas](/reference/api/database-limits):

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

## Downgrade to the Starter plan

The downgrade process is different depending on how you are paying for Pinecone.

<Warning>
  It is important to start the downgrade process in the Pinecone console, as described below. When you do so, Pinecone checks that you are under the [Starter plan quotas](#requirements) before allowing you to downgrade. In contrast, if you start the downgrade process in one of the cloud marketplaces, Pinecone cannot check that you are under these quotas before allowing you to downgrade. If you are over the quotas, Pinecone will deactivate your account, and you will need to [contact support](https://www.pinecone.io/contact/support/).
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
