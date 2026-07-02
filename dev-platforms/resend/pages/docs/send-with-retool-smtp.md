---
title: "Send emails using Retool with SMTP"
source: https://resend.com/docs/send-with-retool-smtp
path: docs/send-with-retool-smtp
---

Learn how to integrate Retool with Resend SMTP.

### Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Retool SMTP

Log into your [Retool](https://retool.com) account and create a new SMTP Resource.

1. Go to **Resources** and click **Create New**

<img alt="Retool SMTP - Create new Resources" />

2. Search for **SMTP** and select it

<img alt="Retool SMTP - Search for SMTP" />

3. Add name and SMTP credentials

<img alt="Retool SMTP - Add SMTP credentials" />
