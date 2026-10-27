---
title: "Turso + Render"
source: https://docs.turso.tech/features/embedded-replicas/with-render
path: features/embedded-replicas/with-render
---

Deploy a JavaScript app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Render](https://render.com/).

![Render banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=6e416c1d54d38e041de310997834574e)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* Have a Render account - [create one](https://dashboard.render.com/)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**2. Get application code**

Fork the following embedded replica project from GitHub locally:

> **[My Expenses Tracker - (Elysia + Bun)](https://github.com/tursodatabase/embedded-replicas-with-js)**
>
> See the full source code

> [!NOTE]
>
> Or, you can:
>
> > **[Deploy to Render with a single-click](https://render.com/deploy?repo=https://github.com/tursodatabase/embedded-replicas-with-js)**

**3. Create a web service**

Create a new Render **Web Service** by clicking on the "New Web Service" button on the Web Services card inside you Render dashboard.

**4. Connect to Git repository**

1. Select "build and deploy from a Git repository" and proceed to the next page.

2. Click on "Connect" for your target project repository

**5. Set project's environment variables**

On the web service configuration page, under "Advanced" add **a secret file** and fill it in with your database secret credentials:

![Render secret credentials](https://mintlify.s3.us-west-1.amazonaws.com/turso/features/embedded-replicas/images/platforms/render-env-vars.png)

**6. Deploy project**

Scroll to the bottom of the web service configuration page and click on "Create Web Service".
