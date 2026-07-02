---
title: "Upgrade your plan"
source: https://docs.pinecone.io/guides/assistant/admin/upgrade-billing-plan
path: guides/assistant/admin/upgrade-billing-plan
---

Upgrade to a paid plan to access advanced features and limits.

This page describes how to upgrade from the free Starter plan to the [Builder, Standard, or Enterprise plan](https://www.pinecone.io/pricing/), paying either with a credit/debit card or through a supported cloud marketplace.

<Note>
  To change your plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  To commit to annual spending, [contact Pinecone](https://www.pinecone.io/contact).
</Tip>

## Upgrade to the Builder plan

The Builder plan is a flat \$20/month plan with higher quotas than Starter and no usage overages. To upgrade from Starter to Builder:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Builder** plan section.
3. Enter your credit/debit card information.
4. Click **Upgrade**.

After upgrading, your organization is immediately on the Builder plan with the higher [Builder plan quotas](/reference/api/database-limits). If you need additional capacity or features not included in Builder, you can [upgrade to Standard or Enterprise](#upgrade-to-the-standard-or-enterprise-plan) at any time.

<Note>
  The [Builder plan](https://www.pinecone.io/pricing/) is available with credit/debit card billing only and is not supported through cloud marketplaces.
</Note>

## Upgrade to the Standard or Enterprise plan

### Pay with a credit/debit card

To upgrade your plan to Standard or Enterprise and pay with a credit/debit card, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Credit / Debit card**.
4. Enter your credit card information.
5. Click **Upgrade**.

After upgrading, you will immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).

### Pay through the Google Cloud Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Google Cloud Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through GCP**. This takes you to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone) in the Google Cloud Marketplace.
4. Click **Subscribe**.
5. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).

### Pay through the AWS Marketplace

To upgrade your plan to Standard or Enterprise and pay through the AWS Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through AWS**. This takes you to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
4. Click **View purchase options**.
5. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.

   <Warning>
     If the [Pinecone subscription page](https://aws.amazon.com/marketplace/saas/ordering?productId=738798c3-eeca-494a-a2a9-161bee9450b2) shows a message stating, “You are currently subscribed to this offer,” contact your team members to request an invitation to the existing AWS-linked organization. The **Set up your account** button is clickable, but Pinecone does not create a new AWS-linked organization.
   </Warning>
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).

### Pay through the Microsoft Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Microsoft Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through Azure**. This takes you to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas) in the Microsoft Marketplace.
4. Click **Get it now**.
5. Select the **Pinecone - Pay As You Go** plan.
6. Click **Subscribe**.
7. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
8. Click **Subscribe**.
9. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
10. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
11. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
12. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).
