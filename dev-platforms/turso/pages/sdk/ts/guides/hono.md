---
title: "Hono + Turso"
source: https://docs.turso.tech/sdk/ts/guides/hono
path: sdk/ts/guides/hono
---

Set up Turso in your Hono project in minutes.

![Hono banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=1c88c1bf0425b350d511be756e47f83f)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Hono app — [learn more](https://hono.dev/top#quick-start)

**1. Install the libSQL SDK**

<Snippet />

**2. Retrieve database credentials**

<Snippet />

**3. Configure libSQL client**

<Snippet />

**4. Execute SQL**

```ts theme={null}
import { Hono } from "hono";
import { turso } from "./lib/turso";

const app = new Hono();

app.get("/items", async (c) => {
  const { rows } = await turso.execute("SELECT * FROM items");

  return c.json({ rows });
});
```

## Examples

> **[Expenses tracker app with Hono & Turso](https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-hono)**
>
> See the full source code
