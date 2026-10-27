---
title: "Turso + Railway"
source: https://docs.turso.tech/features/embedded-replicas/with-railway
path: features/embedded-replicas/with-railway
---

Deploy a JavaScript/Rust app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Railway](https://railway.app/).

![Koyeb banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=c04df842dadd8d42cd24364580fbf7bf)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* [Install the Railway CLI](https://docs.railway.app/guides/cli#installing-the-cli)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**2. Get application code**

Fork and clone the following embedded replica project from GitHub locally:

> **[My Expenses Tracker - (Elysia + Bun)](https://github.com/tursodatabase/embedded-replicas-with-js)**
>
> See the full source code

> **[Web Traffic API - (Rust)](https://github.com/tursodatabase/embedded-replicas-with-rust)**
>
> See the full source code

**3. Create a new Railway project**

Run the following command to create a new Railway project. Provide the project's name when prompted.

```sh theme={null}
railway init
```

**4. Add a service to the Railway project**

[Create a new empty service](https://docs.railway.app/guides/services#creating-a-service) on your Railway project to act as your app's deployment target.

**5. Link application to service**

Run the following command to list and select the service to link to your application:

```sh theme={null}
railway service
```

**6. Add database credentials**

Open the service on your Railway dashboard and add your Turso Cloud database credentials.

```sh theme={null}
TURSO_DATABASE_URL=libsql://[db-name]-[github-username].turso.io
TURSO_AUTH_TOKEN=...
LOCAL_DB=file:local-db-name.db
```

**7. Deploy**

Run the following command to deploy your application:

```sh theme={null}
railway up
```

> [!NOTE]
>
> Make sure you [expose your application to the internet](https://docs.railway.app/guides/public-networking) to make it accessible from the public network.

> [!WARNING]
>
> If you are on a free plan, you'll need to connect your Railway account to GitHub to have access to code deployments.
