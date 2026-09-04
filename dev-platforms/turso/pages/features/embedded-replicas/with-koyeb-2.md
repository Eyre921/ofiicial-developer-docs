---
title: "Turso + Koyeb"
source: https://docs.turso.tech/features/embedded-replicas/with-koyeb
path: features/embedded-replicas/with-koyeb
---

Deploy a JavaScript/Rust app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Koyeb](https://www.koyeb.com/).

<img alt="Koyeb banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* Have a Koyeb account - [create one](https://app.koyeb.com/)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step>
    Fork one of the following embedded replica project from GitHub

    <CardGroup>
      <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
        See the full source code
      </Card>

      <Card title="Web Traffic API - (Rust)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-rust">
        See the full source code
      </Card>
    </CardGroup>

    <Note>
      Or, you can:

      <Card title="Deploy to Koyeb with a single-click" href="https://app.koyeb.com/deploy?name=er-with-js&type=git&repository=tursodatabase/embedded-replicas-with-js&branch=main&env[PORT]=8000&env[TURSO_DATABASE_URL]=REPLACE_ME&env[TURSO_AUTH_TOKEN]=REPLACE_ME&env[LOCAL_DB]=file:expenses.db" />
    </Note>
  </Step>

  <Step title="Add a new Koyeb app">
    1. Create a new app in the Koyeb control panel.

    2. Select GitHub as the deployment option.

    3. Import the GitHub project to Koyeb.
  </Step>

  <Step title="Fill in the environment variables on Koyeb's deploy page">
    <img alt="Koyeb deploy page - environment variables" />
  </Step>

  <Step title="Deploy">
    Click the **Deploy** button at the bottom to deploy your web service.
  </Step>
</Steps>
