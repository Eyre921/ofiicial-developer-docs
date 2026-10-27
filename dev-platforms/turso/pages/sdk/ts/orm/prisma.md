---
title: "Prisma + Turso"
source: https://docs.turso.tech/sdk/ts/orm/prisma
path: sdk/ts/orm/prisma
---

Configure Prisma to work with your Turso database

![Prisma banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/prisma-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=ce5d303037fe9f45a7918d238def83f4)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Prisma versions 5.4.2 and later

**1. Install the libSQL SDK and its Prisma driver**

```bash npm theme={null}
npm install @libsql/client @prisma/adapter-libsql
```

```bash pnpm theme={null}
pnpm add @libsql/client @prisma/adapter-libsql
```

```bash yarn theme={null}
yarn add @libsql/client @prisma/adapter-libsql
```

**2. Retrieve database credentials**

<Snippet />

**3. Enable the `driverAdapters` preview feature flag:**

```js prisma/schema.prisma theme={null}
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["driverAdapters"]
}

datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}
```

**4. Generate Prisma client**

```sh npm theme={null}
npx prisma generate
```

```sh pnpm theme={null}
pnpm dlx prisma generate
```

**5. Update your Prisma Client Instance**

```ts Node.js / Serverless theme={null}
import { PrismaClient } from "@prisma/client";
import { PrismaLibSQL } from "@prisma/adapter-libsql";

const adapter = new PrismaLibSQL({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
})
const prisma = new PrismaClient({ adapter })
```

```ts Edge Runtimes theme={null}
import { PrismaClient } from "@prisma/client";
import { PrismaLibSQL } from "@prisma/adapter-libsql";

const adapter = new PrismaLibSQL({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
})
const prisma = new PrismaClient({ adapter })
```

**6. Database Migrations**

Prisma Migrate and Introspection workflows are currently not supported when working with Turso — [learn more](https://www.prisma.io/docs/orm/overview/databases/turso#how-to-manage-schema-changes).

First, generate a migration file using prisma migrate dev against a local SQLite database

```sh npm theme={null}
npx prisma migrate dev --name init
```

```sh pnpm theme={null}
pnpm dlx prisma migrate dev --name init
```

Then, apply the migration to your Turso database using the Turso's CLI

```bash theme={null}
turso db shell turso-prisma-db < ./prisma/migrations/20230922132717_init/migration.sql
```

> [!NOTE]
>
> Replace `20230922132717_init` with the name of your migration created from the `npx prisma migrate dev` command.

**7. Query**

```ts theme={null}
const response = await prisma.table_name.findMany();
```
