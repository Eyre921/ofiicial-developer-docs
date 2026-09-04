---
title: "Astro + Turso"
source: https://docs.turso.tech/sdk/ts/guides/astro
path: sdk/ts/guides/astro
---

Set up Turso in your Astro project in minutes.

<img alt="Astro banner" />

## Prerequisites

To get the most out of this guide, you'll need to:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Astro project — [learn more](https://docs.astro.build/en/install/auto/#1-run-the-setup-wizard)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Configure database credentials">
    <Snippet />
  </Step>

  <Step title="Configure libSQL client">
    ```ts src/turso.ts theme={null}
    import { createClient } from "@libsql/client/web";

    export const turso = createClient({
      url: import.meta.env.TURSO_DATABASE_URL!,
      authToken: import.meta.env.TURSO_AUTH_TOKEN,
    });
    ```

    <Note>
      Astro will soon introduce a new ENV API. [Take a
      look](https://docs.astro.build/en/reference/configuration-reference/#experimentalenv).
    </Note>
  </Step>

  <Step title="Execute SQL">
    ```ts theme={null}
    ---
    import { turso } from './turso'

    const { rows } = await turso.execute('SELECT * FROM table_name')
    ---
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Blog" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-tustro-blog">
    See the full source code
  </Card>
</CardGroup>
