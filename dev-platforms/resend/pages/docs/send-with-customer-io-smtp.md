---
title: "Send emails using Customer.io with SMTP"
source: https://resend.com/docs/send-with-customer-io-smtp
path: docs/send-with-customer-io-smtp
---

Learn how to integrate Customer.io with Resend SMTP.

### Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

## Guide

<Steps>
  <Step title="Get the Resend SMTP credentials">
    When configuring your SMTP integration, you'll need to use the following credentials:

    * **Host**: `smtp.resend.com`
    * **Port**: `465`
    * **Username**: `resend`
    * **Password**: `YOUR_API_KEY`
  </Step>

  <Step title="Integrate with Customer.io SMTP">
    After logging into your [Customer.io](https://customer.io) account, you'll need to enable the SMTP integration.

    1. Go to **Settings** > **Workspace Settings**.

    <img alt="Customer.io SMTP - Workspace Settings" />

    2. Go to the Messaging tab and select **Email**.

    <img alt="Customer.io SMTP - Email" />

    3. Select the **Custom SMTP** tab and click **Add Custom SMTP Server**.

    <img alt="Customer.io SMTP - Add Custom SMTP Server" />

    4. Select **Other SMTP** and click **Continue to set up**.

    <img alt="Customer.io SMTP - Other SMTP" />

    5. Copy-and-paste the SMTP credentials from Resend to Customer.io.

    <img alt="Customer.io SMTP integration" />
  </Step>
</Steps>
