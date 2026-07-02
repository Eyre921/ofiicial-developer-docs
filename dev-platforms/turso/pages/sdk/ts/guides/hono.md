---
title: "Hono + Turso"
source: https://docs.turso.tech/sdk/ts/guides/hono
path: sdk/ts/guides/hono
---

Set up Turso in your Hono project in minutes.

<img alt="Hono banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Hono app — [learn more](https://hono.dev/top#quick-start)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet />
  </Step>

  <Step title="Configure libSQL client">
    <Snippet />
  </Step>

  <Step title="Execute SQL">
    ```ts theme={null}
    import { Hono } from "hono";
    import { turso } from "./lib/turso";

    const app = new Hono();

    app.get("/items", async (c) => {
      const { rows } = await turso.execute("SELECT * FROM items");

      return c.json({ rows });
    });
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Expenses tracker app with Hono & Turso" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-hono">
    See the full source code
  </Card>
</CardGroup>
