---
title: "Elysia + Turso"
source: https://docs.turso.tech/sdk/ts/guides/elysia
path: sdk/ts/guides/elysia
---

Set up Turso in your Elysia project in minutes.

![Elysia banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=feb0570b5243f4be9c133fe35f0f8f42)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Elysia app — [learn more](https://elysiajs.com/quick-start.html)

**1. Install the libSQL SDK**

<Snippet />

**2. Retrieve database credentials**

<Snippet />

**3. Configure libSQL client**

<Snippet />

**4. Execute SQL**

```ts theme={null}
import { Elysia } from "elysia";
import { turso } from "./lib/turso";

const app = new Elysia().get("/items", async () => {
  const { rows } = await turso.execute("SELECT * FROM items");
  return rows;
});
```

## Examples

> **[Expenses tracker app with Elysia & Turso](https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-elysia)**
>
> See the full source code
