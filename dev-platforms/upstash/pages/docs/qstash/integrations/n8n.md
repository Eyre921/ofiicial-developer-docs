---
title: "n8n with QStash"
source: https://upstash.com/docs/qstash/integrations/n8n
path: docs/qstash/integrations/n8n
---

Leverage your n8n workflow with Upstash Qstash, here is how you can make those requests using HTTP Request node.

### Step 1: Set Up an n8n Project

1. Go to https://n8n.io and create a new project
2. Create a Trigger as Webhook with default settings, this will be our entry point.
3. Create a HTTP Request Node
   <img alt="n8n with QStash: QStash http" />

***

### Step 2: Import QStash Configurations to HTTP Node

1. Go to Upstash Console and open QStash Request Builder Tab.
2. Fill out the fields to create an QStash Request. (Publish, Enqueue, Schedule)
   <img alt="n8n with QStash: QStash request builder" />
3. Copy the cURL snippet created for you, representing your request.
   <img alt="n8n with QStash: QStash curl" />
4. Back to the n8n, in HTTP Request Parameters tab, use import cURL.
   <img alt="n8n with QStash: QStash import button" />
5. Paste the cURL snippet that you copied in the console, and let n8n to fill out the form for you.
   <img alt="n8n with QStash: QStash import" />

***

### Step 3: Test the Workflow

1. Execute workflow.
2. Visit the Webhook URL.
3. That's it! You can check the logs in the Qstash Console to confirm your QStash Request is working.
   <img alt="n8n with QStash: QStash logs" />
