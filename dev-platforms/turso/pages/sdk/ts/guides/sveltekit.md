---
title: "SvelteKit + Turso"
source: https://docs.turso.tech/sdk/ts/guides/sveltekit
path: sdk/ts/guides/sveltekit
---

Set up Turso in your SvelteKit project in minutes

![SvelteKit banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=c5f43db5d48bf2eb2657f687d1f60fa2)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a SvelteKit app — [learn more](https://kit.svelte.dev/docs/creating-a-project)

**1. Install the libSQL SDK**

<Snippet />

**2. Configure database credentials**

<Snippet />

**3. Configure libSQL Client.**

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

**4. Execute SQL**

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

## Examples

> **[Blog](https://github.com/tursodatabase/examples/tree/master/app-at-the-polls)**
>
> See the full source code
