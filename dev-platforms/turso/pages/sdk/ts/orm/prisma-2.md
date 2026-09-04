---
title: "Prisma + Turso"
source: https://docs.turso.tech/sdk/ts/orm/prisma
path: sdk/ts/orm/prisma
---

Configure Prisma to work with your Turso database

<img alt="Prisma banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Prisma versions 5.4.2 and later

<Steps>
  <Step title="Install the libSQL SDK and its Prisma driver">
    <CodeGroup>
      ```bash npm theme={null}
      npm install @libsql/client @prisma/adapter-libsql
      ```

      ```bash pnpm theme={null}
      pnpm add @libsql/client @prisma/adapter-libsql
      ```

      ```bash yarn theme={null}
      yarn add @libsql/client @prisma/adapter-libsql
      ```
    </CodeGroup>
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet />
  </Step>

  <Step title="Enable the `driverAdapters` preview feature flag:">
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
  </Step>

  <Step title="Generate Prisma client">
    <CodeGroup>
      ```sh npm theme={null}
      npx prisma generate
      ```

      ```sh pnpm theme={null}
      pnpm dlx prisma generate
      ```
    </CodeGroup>
  </Step>

  <Step title="Update your Prisma Client Instance">
    <CodeGroup>
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
    </CodeGroup>
  </Step>

  <Step title="Database Migrations">
    Prisma Migrate and Introspection workflows are currently not supported when working with Turso — [learn more](https://www.prisma.io/docs/orm/overview/databases/turso#how-to-manage-schema-changes).

    First, generate a migration file using prisma migrate dev against a local SQLite database

    <CodeGroup>
      ```sh npm theme={null}
      npx prisma migrate dev --name init
      ```

      ```sh pnpm theme={null}
      pnpm dlx prisma migrate dev --name init
      ```
    </CodeGroup>

    Then, apply the migration to your Turso database using the Turso's CLI

    ```bash theme={null}
    turso db shell turso-prisma-db < ./prisma/migrations/20230922132717_init/migration.sql
    ```

    <Info>
      Replace `20230922132717_init` with the name of your migration created from the `npx prisma migrate dev` command.
    </Info>
  </Step>

  <Step title="Query">
    ```ts theme={null}
    const response = await prisma.table_name.findMany();
    ```
  </Step>
</Steps>
