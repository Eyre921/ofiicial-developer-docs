---
title: "Send emails using Metabase with SMTP"
source: https://resend.com/docs/send-with-metabase-smtp
path: docs/send-with-metabase-smtp
---

Learn how to integrate Metabase with Resend SMTP.

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

  <Step title="Integrate with Metabase SMTP">
    After logging into your [Metabase Cloud](https://www.metabase.com/cloud/login) account, you’ll need to enable the SMTP integration.

    1. From your Metabase Cloud Admin Panel, go to **Settings > Email** in the left menu. You'll see the form below.

    <img alt="Metabase Cloud SMTP" />

    2. Copy-and-paste the SMTP credentials from Resend to Metabase Cloud. Finally, click the **Save** button and all of your emails will be sent through Resend.

    <img alt="Metabase Cloud SMTP" />
  </Step>
</Steps>
