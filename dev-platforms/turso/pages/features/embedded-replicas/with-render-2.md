---
title: "Turso + Render"
source: https://docs.turso.tech/features/embedded-replicas/with-render
path: features/embedded-replicas/with-render
---

Deploy a JavaScript app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Render](https://render.com/).

<img alt="Render banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* Have a Render account - [create one](https://dashboard.render.com/)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Get application code">
    Fork the following embedded replica project from GitHub locally:

    <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
      See the full source code
    </Card>

    <Note>
      Or, you can:

      <Card title="Deploy to Render with a single-click" href="https://render.com/deploy?repo=https://github.com/tursodatabase/embedded-replicas-with-js" />
    </Note>
  </Step>

  <Step title="Create a web service">
    Create a new Render **Web Service** by clicking on the "New Web Service" button on the Web Services card inside you Render dashboard.
  </Step>

  <Step title="Connect to Git repository">
    1. Select "build and deploy from a Git repository" and proceed to the next page.

    2. Click on "Connect" for your target project repository
  </Step>

  <Step title="Set project's environment variables">
    On the web service configuration page, under "Advanced" add **a secret file** and fill it in with your database secret credentials:

    <img alt="Render secret credentials" />
  </Step>

  <Step title="Deploy project">
    Scroll to the bottom of the web service configuration page and click on "Create Web Service".
  </Step>
</Steps>
