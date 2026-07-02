---
title: "SvelteKit + Turso"
source: https://docs.turso.tech/sdk/ts/guides/sveltekit
path: sdk/ts/guides/sveltekit
---

Set up Turso in your SvelteKit project in minutes

<img alt="SvelteKit banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a SvelteKit app — [learn more](https://kit.svelte.dev/docs/creating-a-project)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Configure database credentials">
    <Snippet />
  </Step>

  <Step title="Configure libSQL Client.">
    <CodeGroup>
      ```ts Node.js / Serverless theme={null}
      import { TURSO_DATABASE_URL, TURSO_AUTH_TOKEN } from "$env/static/private";
      import { createClient } from "@libsql/client";

      export const turso = createClient({
        url: TURSO_DATABASE_URL,
        authToken: TURSO_AUTH_TOKEN,
      });
      ```

      ```ts Edge Runtimes theme={null}
      import { TURSO_DATABASE_URL, TURSO_AUTH_TOKEN } from "$env/static/private";
      import { createClient } from "@libsql/client/web";

      export const turso = createClient({
        url: TURSO_DATABASE_URL,
        authToken: TURSO_AUTH_TOKEN,
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Execute SQL">
    <CodeGroup>
      ```ts src/routes/+page.server.ts theme={null}
      import { turso } from "$lib/turso.server";

      export async function load() {
        const { rows } = await turso.execute("SELECT * FROM table_name");

        return { rows };
      }
      ```

      ```svelte src/routes/+page.svelte theme={null}
      <script lang="ts">
        export let data
      </script>

      <ul>
        {#each data.rows as row}
          <li>{row.id}</li>
        {/each}
      </ul>
      ```
    </CodeGroup>
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Blog" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-at-the-polls">
    See the full source code
  </Card>
</CardGroup>
