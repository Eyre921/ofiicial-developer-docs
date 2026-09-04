---
title: "Qwik + Turso"
source: https://docs.turso.tech/sdk/ts/guides/qwik
path: sdk/ts/guides/qwik
---

Set up Turso in your Qwik project in minutes

<img alt="Qwik banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Qwik app — [learn more](https://qwik.builder.io/docs/getting-started/#create-an-app-using-the-cli)

<Steps>
  <Step title="Add Turso Integration">
    <CodeGroup>
      ```bash npm theme={null}
      npm run qwik add turso
      ```

      ```bash pnpm theme={null}
      pnpm qwik add turso
      ```

      ```bash yarn theme={null}
      yarn qwik add turso
      ```
    </CodeGroup>
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
    PRIVATE_TURSO_DATABASE_URL="..."
    PRIVATE_TURSO_AUTH_TOKEN="..."
    ```
  </Step>

  <Step title="Execute SQL">
    ```ts theme={null}
    import { tursoClient } from "~/utils/turso";

    export const useFrameworks = routeLoader$(
      async (requestEvent: RequestEventBase) => {
        const db = tursoClient(requestEvent["env"]);
        const { rows } = await db.execute("select * from table_name");

        return {
          items: rows,
        };
      },
    );
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Social Website" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-find-me-on">
    See the full source code
  </Card>

  <Card title="Shopping Cart" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-turqw-store">
    See the full source code
  </Card>
</CardGroup>
