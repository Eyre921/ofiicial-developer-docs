---
title: "Elysia + Turso"
source: https://docs.turso.tech/sdk/ts/guides/elysia
path: sdk/ts/guides/elysia
---

Set up Turso in your Elysia project in minutes.

<img alt="Elysia banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Elysia app — [learn more](https://elysiajs.com/quick-start.html)

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
    import { Elysia } from "elysia";
    import { turso } from "./lib/turso";

    const app = new Elysia().get("/items", async () => {
      const { rows } = await turso.execute("SELECT * FROM items");
      return rows;
    });
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Expenses tracker app with Elysia & Turso" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-elysia">
    See the full source code
  </Card>
</CardGroup>
