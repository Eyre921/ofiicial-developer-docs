---
title: "Remix + Turso"
source: https://docs.turso.tech/sdk/ts/guides/remix
path: sdk/ts/guides/remix
---

Set up Turso in your Remix project in minutes

<img alt="Remix banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Remix app — [learn more](https://remix.run/docs/en/main/start/quickstart#quick-start)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Configure database credentials">
    <Snippet />
  </Step>

  <Step title="Configure libSQL Client.">
    <Snippet />
  </Step>

  <Step title="Execute SQL">
    ```ts app/routes/_index.ts theme={null}
    import type { LoaderFunction } from "@remix-run/node";

    import { turso } from "~/lib/turso";

    export const loader: LoaderFunction = async () => {
      const { rows } = await turso.execute("SELECT * from TABLE_NAME");

      return {
        items: rows,
      };
    };
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="E-commerce Store" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-the-mug-store">
    See the full source code
  </Card>

  <Card title="CRM App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-turso-crm">
    See the full source code
  </Card>
</CardGroup>
