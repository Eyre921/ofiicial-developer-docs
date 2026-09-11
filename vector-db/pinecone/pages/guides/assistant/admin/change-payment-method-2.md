---
title: "Change your payment method"
source: https://docs.pinecone.io/guides/assistant/admin/change-payment-method
path: guides/assistant/admin/change-payment-method
---

Update the credit card or payment method on file for your Pinecone organization to keep billing details current and avoid failed charges.

You can pay for the [Standard and Enterprise plans](https://www.pinecone.io/pricing/) with a credit/debit card or through the AWS Marketplace, Microsoft Marketplace, or Google Cloud Marketplace. This page describes how to switch between these payment methods.

<Note>
  To change your payment method, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Note>
  The [Builder plan](https://www.pinecone.io/pricing/) is available with credit/debit card billing only and is not supported through cloud marketplaces.
</Note>

To switch a Builder-plan organization to marketplace billing, first [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan) using the marketplace subscription flow.

## Credit card → marketplace

To change from credit card to marketplace billing, you'll need to:

1. Create a new Pinecone organization through the marketplace
2. Migrate your existing projects to the new Pinecone organization
3. Add your team members to the new Pinecone organization
4. Downgrade your original Pinecone organization once migration is complete

<Tabs>
  <Tab title="Credit card → Google Cloud">
    To change from paying with a credit card to paying through the Google Cloud Marketplace, do the following:

    1. Subscribe to Pinecone in the Google Cloud Marketplace:

       1. In the Google Cloud Marketplace, go to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone).
       2. Click **Subscribe**.
       3. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone sign-up page.
       5. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your Google Cloud Marketplace account:

       1. On the **Connect GCP to Pinecone** page, choose **Select an organization > + Create New Organization**.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. Enter the name of the new organization and click **Connect to Pinecone**.
       3. On the **Confirm GCP marketplace Connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Google Cloud Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the Google Cloud Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Credit card → AWS">
    To change from paying with a credit card to paying through the AWS Marketplace, do the following:

    1. Subscribe to Pinecone in the AWS Marketplace:

       1. In the AWS Marketplace, go to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk).
       2. Click **View purchase options**.
       3. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone sign-up page.
       5. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your AWS account:

       1. On the **Connect AWS to Pinecone** page, choose **Select an organization > + Create New Organization**.

       <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>

       1. Enter the name of the new organization and click **Connect to Pinecone**.
       2. On the **Confirm AWS Marketplace Connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Google Cloud Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the AWS Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Credit card → Microsoft">
    To change from paying with a credit card to paying through the Microsoft Marketplace, do the following:

    1. Subscribe to Pinecone in the Microsoft Marketplace:

       1. In the Microsoft Marketplace, go to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas).
       2. Click **Get it now**.
       3. Select the **Pinecone - Pay As You Go** plan.
       4. Click **Subscribe**.
       5. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       6. Click **Subscribe**.
       7. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
       8. Sign up using the same authentication method as your existing Pinecone organization.

    2. Create a new Pinecone organization and connect it to your Microsoft Marketplace account:

       1. On the **Connect Azure to Pinecone** page, choose **Select an organization > + Create New Organization**.

       <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>

       1. Enter the name of the new organization and click **Connect to Pinecone**.
       2. On the **Connect Azure marketplace connection** modal, click **Connect**. This takes you to your new organization in the Pinecone console.

    3. Migrate your projects to the new Pinecone organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. Make sure the **Owner** email address for your original organization is set as an **Owner** or **Billing Admin** for your new organization. This allows Pinecone to verify that both the original and new organizations are owned by the same person.
       3. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       4. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       5. For **Ticket category**, select **Project or Organization Management**.
       6. For **Subject**, enter "Migrate projects to a new organization".
       7. For **Description**, enter the following:

          ```
          I am changing my payment method from credit card to Microsoft Marketplace. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       8. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to **Settings > Billing > Plans**.
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.

    Going forward, your usage of Pinecone will be billed through the Microsoft Marketplace.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>
</Tabs>

## Marketplace → credit card

To change from marketplace billing to credit card, you'll need to:

1. Create a new organization in your Pinecone account
2. Upgrade the new organization to the Standard or Enterprise plan
3. Migrate your existing projects to the new organization
4. Add your team members to the new organization
5. Downgrade your original organization once migration is complete

<Tabs>
  <Tab title="Google Cloud → credit card">
    To change from paying through the Google Cloud Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from Google Cloud Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on the GCP marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
       6. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your original organization.

          <Tip>
            If you don't see the order, check that the correct billing account is selected.
          </Tip>

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="AWS → credit card">
    To change from paying through the AWS Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from AWS Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on the AWS marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
       6. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>

  <Tab title="Microsoft → credit card">
    To change from paying through the Microsoft Marketplace to paying with a credit card, do the following:

    1. Create a new organization in your Pinecone account:

       1. In the Pinecone console, go to [**Organizations**](https://app.pinecone.io/organizations/-/settings/account/organizations).
       2. Click **+ Create organization**.
       3. Enter the name of the new organization and click **Create**.

    2. Upgrade the new organization:

       1. Go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
       2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
       3. Click **Credit / Debit card**.
       4. Enter your credit card information.
       5. Click **Upgrade**.

       The new organization is now set up with credit card billing. You'll use this organization after completing the rest of this process.

    3. Migrate your projects to the new Pinecone organization:

       1. Go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage) and copy your new organization ID.
       2. Go to [**Settings > Support > Tickets**](https://app.pinecone.io/organizations/-/settings/support/ticket/create).
       3. For **Ticket category**, select **Project or Organization Management**.
       4. For **Subject**, enter "Migrate projects to a new organization".
       5. For **Description**, enter the following:

          ```
          I am changing my payment method from Microsoft Marketplace to credit card. 
          Please migrate my projects to my new organization: `<NEW_ORG_ID>`
          ```
       6. Click **Submit**.

    4. Add your team members to the new organization:

       1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
       2. [Add your team members to the new organization](/guides/organizations/manage-organization-members#add-a-member-to-an-organization).

    5. Downgrade your original Pinecone organization:

       <Note>
         Do not downgrade your original organization until you receive a confirmation that Pinecone has finished the migration to your new organization.
       </Note>

       1. In the Pinecone console, go to your original organization.
       2. Go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
       3. In the **Starter** section, click **Downgrade**.
       4. Click **Confirm downgrade**.
       5. On the **Continue your downgrade on Azure marketplace** modal, click **Continue to marketplace**.
       6. On the **SaaS** page, click your subscription to Pinecone.
       7. Click **Cancel subscription**.
       8. Confirm the cancellation.

    Going forward, you'll use your new organization and your usage will be billed through the credit card you provided.

    <Warning>
      You can [delete your original organization](/troubleshooting/delete-your-organization). However, before deleting, make sure to [download your past invoices](/guides/organizations/manage-billing/access-your-invoices) since you will lose access to them once the organization is deleted.
    </Warning>
  </Tab>
</Tabs>

## Marketplace → marketplace

To change from one marketplace to another, you'll need to:

1. Subscribe to Pinecone in the new marketplace
2. Connect your existing org to the new marketplace
3. Cancel your subscription in the old marketplace

<Tabs>
  <Tab title="Any marketplace → Google Cloud">
    To change to a Google Cloud Marketplace billing account, do the following:

    1. Subscribe to Pinecone in the Google Cloud Marketplace:

       1. In the Google Cloud Marketplace, go to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone).
       2. Click **Subscribe**.
       3. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
       5. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your Google account:

       1. On the **Connect GCP to Pinecone** page, select the Pinecone organization that you want to use Google Cloud Marketplace.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm GCP marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the Google Cloud Marketplace.

    3. Cancel your subscription in your previous marketplace:

       * For AWS:
         1. In the AWS Marketplace, go to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
         2. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

       * For Microsoft:
         1. Go to [Azure SaaS Resource Management](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources).
         2. Select your subscription to Pinecone.
         3. Click **Cancel subscription**.
         4. Confirm the cancellation.
  </Tab>

  <Tab title="Any marketplace → AWS">
    To change to an AWS Marketplace billing account, do the following:

    1. Subscribe to Pinecone in the AWS Marketplace:

       1. In the AWS Marketplace, go to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
       2. Click **View purchase options**.
       3. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       4. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.
       5. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your AWS account:

       1. On the **Connect AWS to Pinecone** page, select the Pinecone organization that you want to change to AWS Marketplace.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm AWS marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the AWS Marketplace.

    3. Cancel your subscription in your previous marketplace:

       * For Google Cloud Marketplace:
         1. Go to the [Orders](https://console.cloud.google.com/marketplace/orders) page.
         2. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for Pinecone.

       * For Microsoft Marketplace:
         1. Go to [Azure SaaS Resource Management](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources).
         2. Select your subscription to Pinecone.
         3. Click **Cancel subscription**.
         4. Confirm the cancellation.
  </Tab>

  <Tab title="Any marketplace → Microsoft">
    To change to a Microsoft Marketplace billing account, do the following:

    1. Subscribe to Pinecone in the Microsoft Marketplace:

       1. In the Microsoft Marketplace, go to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas).
       2. Click **Get it now**.
       3. Select the **Pinecone - Pay As You Go** plan.
       4. Click **Subscribe**.
       5. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

          <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
       6. Click **Subscribe**.
       7. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
       8. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.

    2. Connect your existing org to your Microsoft account:

       1. On the **Connect Azure to Pinecone** page, select the Pinecone organization that you want to change to Microsoft Marketplace.

          <Note>If you see a message saying that the subscription is still in process, wait a few minutes, refresh the page, and proceed only when the message has disappeared.</Note>
       2. On the **Confirm Azure marketplace connection** modal, click **Connect**. This takes you to your organization in the Pinecone console.

          Going forward, your usage of Pinecone will be billed through the Microsoft Marketplace.

    3. Cancel your subscription in your previous marketplace:

       * For Google Cloud Marketplace:
         1. Go to the [Orders](https://console.cloud.google.com/marketplace/orders) page.
         2. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for Pinecone.

       * For AWS Marketplace:
         1. Go to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
         2. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.
  </Tab>
</Tabs>

## Credit card → credit card

To update your credit card information in the Pinecone console, do the following:

1. Go to [**Settings > Billing > Overview**](https://app.pinecone.io/organizations/-/settings/billing).
2. In the **Billing Contact** section, click **Edit**.
3. Enter your new credit card information.
4. Click **Update**.
