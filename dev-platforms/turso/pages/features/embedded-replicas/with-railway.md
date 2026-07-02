---
title: "Turso + Railway"
source: https://docs.turso.tech/features/embedded-replicas/with-railway
path: features/embedded-replicas/with-railway
---

Deploy a JavaScript/Rust app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Railway](https://railway.app/).

<img alt="Koyeb banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* [Install the Railway CLI](https://docs.railway.app/guides/cli#installing-the-cli)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Get application code">
    Fork and clone the following embedded replica project from GitHub locally:

    <CardGroup>
      <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
        See the full source code
      </Card>

      <Card title="Web Traffic API - (Rust)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-rust">
        See the full source code
      </Card>
    </CardGroup>
  </Step>

  <Step title="Create a new Railway project">
    Run the following command to create a new Railway project. Provide the project's name when prompted.

    ```sh theme={null}
    railway init
    ```
  </Step>

  <Step title="Add a service to the Railway project">
    [Create a new empty service](https://docs.railway.app/guides/services#creating-a-service) on your Railway project to act as your app's deployment target.
  </Step>

  <Step title="Link application to service">
    Run the following command to list and select the service to link to your application:

    ```sh theme={null}
    railway service
    ```
  </Step>

  <Step title="Add database credentials">
    Open the service on your Railway dashboard and add your Turso Cloud database credentials.

    ```sh theme={null}
    TURSO_DATABASE_URL=libsql://[db-name]-[github-username].turso.io
    TURSO_AUTH_TOKEN=...
    LOCAL_DB=file:local-db-name.db
    ```
  </Step>

  <Step title="Deploy">
    Run the following command to deploy your application:

    ```sh theme={null}
    railway up
    ```

    <Info>
      Make sure you [expose your application to the internet](https://docs.railway.app/guides/public-networking) to make it accessible from the public network.
    </Info>

    <Warning>
      If you are on a free plan, you'll need to connect your Railway account to GitHub to have access to code deployments.
    </Warning>
  </Step>
</Steps>
