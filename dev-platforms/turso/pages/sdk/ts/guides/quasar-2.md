---
title: "Quasar + Turso"
source: https://docs.turso.tech/sdk/ts/guides/quasar
path: sdk/ts/guides/quasar
---

Set up Turso in your Quasar project in minutes

<img alt="Quasar banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Quasar app — [learn more](https://quasar.dev/start/quick-start#step-1-create-a-project)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Configure database credentials">
    Get the database URL:

    ```bash theme={null}
    turso db show --url <database-name>
    ```

    Get the database authentication token:

    ```bash theme={null}
    turso db tokens create <database-name>
    ```

    Assign credentials to the environment variables inside `.env.local`.

    ```bash theme={null}
    VITE_TURSO_DATABASE_URL="..."
    VITE_TURSO_AUTH_TOKEN="..."
    ```
  </Step>

  <Step title="Configure libSQL Client">
    ```js theme={null}
    import { createClient } from "@libsql/client/web";

    const turso = createClient({
      url: import.meta.env.VITE_TURSO_DATABASE_URL,
      authToken: import.meta.env.VITE_TURSO_AUTH_TOKEN,
    });
    ```

    <Info>
      Avoid a [gotcha
      moment](https://github.com/quasarframework/quasar/discussions/16071) by
      modifying the app configuration using the settings below.
    </Info>

    ```javascript quasar.config.js theme={null}
    {
      build: {
        target: {
          browser: [
            'es2020', 'edge88', 'firefox78', 'chrome87', 'safari13.1'
          ],
          node: 'node16'
        },
        extendViteConf(config) {
          config.optimizeDeps = {
            esbuildOptions: {
              target: 'es2020',
            }
          }
        }
      }
    }
    ```
  </Step>

  <Step title="Fetch data from Turso.">
    ```js IndexPage.vue theme={null}
    import { ref } from "vue";

    const items = ref();

    const { rows } = await turso.execute("select * from my-table");

    items.value = rows;
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Todo App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/quasar-todo-list">
    See the full source code
  </Card>
</CardGroup>
