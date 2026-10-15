---
title: "Upgrade your plan"
source: https://docs.pinecone.io/admin/billing/upgrade-billing-plan
path: admin/billing/upgrade-billing-plan
---

Upgrade your Pinecone organization to the Builder, Standard, or Enterprise plan and pay by card or through a cloud marketplace.

This page describes how to upgrade to a paid [Builder, Standard, or Enterprise plan](https://www.pinecone.io/pricing/), either from the free Starter plan or from Builder to Standard or Enterprise. You can pay with a credit or debit card, or through a supported cloud marketplace if your organization is on the Starter plan.

<Note>
  To change your plan, you must be an [organization owner or billing admin](/admin/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  To evaluate the Standard plan before you start paying, see the [Standard plan trial](/admin/billing/standard-trial). You get 21 days and \$300 in credits. Each organization can activate one trial, and [some organizations aren't eligible](/admin/billing/standard-trial#limits).
</Tip>

<Tip>
  To commit to annual spending, [contact Pinecone](https://www.pinecone.io/contact).
</Tip>

## Upgrade to the Builder plan

The Builder plan is a flat \$20/month plan with higher quotas than Starter and no usage overages. To upgrade from Starter to Builder:

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Builder** plan section.
3. If you have a promo code, click **Add discount code** and enter it. For details, see [Redeem a promo code](/admin/billing/redeem-a-promo-code).
4. Click **Continue**.
5. Enter your credit or debit card information.
6. Click **Upgrade**.

After upgrading, your organization is immediately on the Builder plan with the higher [Builder plan quotas](/reference/api/database-limits/object-limits). If you need additional capacity or features not included in Builder, you can [upgrade to Standard or Enterprise](#upgrade-to-the-standard-or-enterprise-plan) at any time.

<Note>
  The [Builder plan](https://www.pinecone.io/pricing/) is available with credit/debit card billing only and isn't supported through cloud marketplaces.
</Note>

## Upgrade to the Standard or Enterprise plan

### Pay with a credit/debit card

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Credit / Debit card**.
4. Enter your credit card information.
5. Click **Upgrade**.

After upgrading, you'll immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost).

### Pay through the Google Cloud Marketplace

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through GCP**. This takes you to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone) in the Google Cloud Marketplace.
4. Click **Subscribe**.
5. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

   <Note>The billing unit listed doesn't reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). You can also create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

After your organization is connected and upgraded, you'll receive a confirmation message. You'll then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost).

### Pay through the AWS Marketplace

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through AWS**. This takes you to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
4. Click **View purchase options**.
5. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

   <Note>The billing unit listed doesn't reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.

   <Warning>
     If the [Pinecone subscription page](https://aws.amazon.com/marketplace/saas/ordering?productId=738798c3-eeca-494a-a2a9-161bee9450b2) shows a message stating, “You are currently subscribed to this offer,” contact your team members to request an invitation to the existing AWS-linked organization. The **Set up your account** button is clickable, but Pinecone doesn't create a new AWS-linked organization.
   </Warning>
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). You can also create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

After your organization is connected and upgraded, you'll receive a confirmation message. You'll then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost).

### Pay through the Microsoft Marketplace

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through Azure**. This takes you to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas) in the Microsoft Marketplace.
4. Click **Get it now**.
5. Select the **Pinecone - Pay As You Go** plan.
6. Click **Subscribe**.
7. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

   <Note>The billing unit listed doesn't reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
8. Click **Subscribe**.
9. After the subscription is approved, click **Configure account now**. This redirects you to a Microsoft-specific Pinecone login page.
10. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
11. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). You can also create a new organization.
12. Click **Connect to Pinecone** and follow the prompts.

After your organization is connected and upgraded, you'll receive a confirmation message. You'll then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost).
