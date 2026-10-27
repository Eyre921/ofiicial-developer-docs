---
title: "Turso + Koyeb"
source: https://docs.turso.tech/features/embedded-replicas/with-koyeb
path: features/embedded-replicas/with-koyeb
---

Deploy a JavaScript/Rust app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Koyeb](https://www.koyeb.com/).

![Koyeb banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=6f7f0ee22ae417bb3743cd771b4c8a4a)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* Have a Koyeb account - [create one](https://app.koyeb.com/)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**Step 2**

Fork one of the following embedded replica project from GitHub

> **[My Expenses Tracker - (Elysia + Bun)](https://github.com/tursodatabase/embedded-replicas-with-js)**
>
> See the full source code

> **[Web Traffic API - (Rust)](https://github.com/tursodatabase/embedded-replicas-with-rust)**
>
> See the full source code

> [!NOTE]
>
> Or, you can:
>
> > **[Deploy to Koyeb with a single-click](https://app.koyeb.com/deploy?name=er-with-js\&type=git\&repository=tursodatabase/embedded-replicas-with-js\&branch=main\&env\[PORT]=8000\&env\[TURSO_DATABASE_URL]=REPLACE_ME\&env\[TURSO_AUTH_TOKEN]=REPLACE_ME\&env\[LOCAL_DB]=file:expenses.db)**

**3. Add a new Koyeb app**

1. Create a new app in the Koyeb control panel.

2. Select GitHub as the deployment option.

3. Import the GitHub project to Koyeb.

**4. Fill in the environment variables on Koyeb's deploy page**

![Koyeb deploy page - environment variables](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=fbe69407ce481b6f89954813101965b4)

**5. Deploy**

Click the **Deploy** button at the bottom to deploy your web service.
