---
title: "n8n with Upstash Redis"
source: https://upstash.com/docs/redis/integrations/n8n
path: docs/redis/integrations/n8n
---

## Quickstart

In this quickstart we're going to set up an Redis node in n8n using Upstash Redis, and go over an example use case step by step.

***

### Step 1: Get Your Upstash Redis Credentials

1. Go to Upstash Console and create a Redis database if you don't have any
2. Note down your credentials in the details page, we will be using those to connect Redis
   Node in n8n to our Upstash Redis instance.
   <img />

***

### Step 2: Set Up an n8n Project

1. Go to https://n8n.io and create a new project
2. Create a Trigger as Webhook with default settings, this will be our entry point. Our Redis instances gonna watch the visits to this url.
   <img />

***

### Step 3: Create a Redis Node

Now, Let's create a redis node and connect it to our Upstash Redis instance

1. Search for redis in nodes, and select increment action.
   <img />
2. In the opening window, click select credentials, and create new credentials.
   Later, for other redis nodes, this will be saved and used automatically.
   <img />
3. Fill the credentials.

   * Pass your Upstash Token to the password field.
   * Leave the user field blank
   * Pass your Upstash Redis endpoint to the host field. (Leave the https:// part out)
   * If your Upstash Database has a port other than the default 6379, change it here.

   <img />

4. Enable SSL (Upstash Redis requires SSL) and hit the save button.
   <img />

***

### Redis Example: Store the Visit Count per Visitor

1. Track the users with `x-real-ip`
   <img />
2. Add another redis node with get action to see the visit counts
   <img />
3. Read the set visit count with redis get
   <img />

***

### Test Redis Example

Run the workflow and visit the webhook URL, This will send a get request and trigger the workflow run.
Then from the headers your ip will be fetched and in the redis instance you will see `user:user-ip` set to `1`.
As you visit the page it will be incremented and at the end of the workflow you can track and confirm this setup with
the get request.

***
