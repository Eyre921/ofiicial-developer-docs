---
title: "Netlify Database: Getting started"
source: https://docs.netlify.com/build/data-and-storage/netlify-database/getting-started.md
path: build/data-and-storage/netlify-database/getting-started
---

---
title: "Getting started"
description: "How to start a new project with Netlify Database, or add Netlify Database to an existing project."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Start using Netlify Database in just a few steps, no matter how far along you are in your building journey.

## Create a project with a database

If you don't have a project yet, start one of the following ways and Netlify Database will be set up as part of the project from day one.

### Start with Agent Runners

Go to [app.netlify.com/start](https://app.netlify.com/start) and describe the application you want to build. Include the type of data you want to store and how you want to access it.

For example:

> _An app for managing my music collection. For each record, I want to store the title, artist name, year and medium (CD or vinyl). I want to be able to filter entries and search by any of these fields._

[Agent Runners](/build/build-with-ai/agent-runners/overview/) will scaffold the project, install `@netlify/database`, write the necessary [migrations](/build/data-and-storage/netlify-database/migrations/), and deploy your project to production.

Whenever you want to make any changes, you can describe them in a new agent run:

> _For each record, I also want to store the recording studio._

The AI agent will change the application code, create new migrations, apply them, and deploy the project to a preview URL for you to review. Once you're happy with the result, click _Publish to production_ and your production site is updated.

### Start locally

If you'd rather work from your terminal, the Netlify CLI's [`netlify create`](/api-and-cli-guides/cli-guides/get-started-with-cli/) command kicks off the same agent-driven setup, but in your local machine:

```bash
netlify create "An app for managing my music collection. For each record, I want to store the title, artist name, year and medium (CD or vinyl). I want to be able to filter entries and search by any of these fields"
```

Alternatively, you can let any AI agent you already use locally (Claude Code, Cursor, Codex, and others) build the project for you.

Netlify ships [context for agents, including skills](/build/build-with-ai/agent-setup-guides/agent-setup-overview/) that give those agents the right context for working with the platform - including for setting up Netlify Database - so a prompt like the one above gets turned into a working project with the database wired up correctly.

## Add a database to an existing project

If you already have an existing project, you can add a database to it with just a few steps.

### With the CLI

The `netlify database init` CLI command offers an interactive setup guide for adding Netlify Database to your project.

```bash
netlify database init
```

The command walks you through an interactive setup that:

- Installs `@netlify/database` and any other packages you need for your chosen workflow
- Lets you pick your preferred query style - [Drizzle ORM](/build/data-and-storage/netlify-database/tooling/#drizzle-orm) for a type-safe query builder and schema-first migrations, or direct SQL with the `@netlify/database` package
- Scaffolds a starter [migration](/build/data-and-storage/netlify-database/migrations/) so you have a working schema to build on
- Optionally seeds the database with sample data, so you can run a query end-to-end and see real results before writing any code yourself

When the command finishes, you have a project that's wired up, populated with data, and ready for a first deploy.

From there, `netlify dev` starts a fully-featured local Postgres database on your machine, so you can iterate without touching the production database. Refer to [Local development](/build/data-and-storage/netlify-database/local-development/) for more details.

### Manually

If you prefer, you can set things up manually:

1. Install the [`@netlify/database`](/build/data-and-storage/netlify-database/api/) package:

    ```bash
    npm install @netlify/database
    ```

2. Optionally, install [Drizzle ORM](/build/data-and-storage/netlify-database/tooling/#drizzle-orm) for a type-safe query builder and schema-first migration workflow.
3. Write your first [migration](/build/data-and-storage/netlify-database/migrations/) under `netlify/database/migrations/`.
4. Write a [function](/build/functions/overview) or [edge function](/build/edge-functions/overview) that interacts with the database.
5. Run `netlify dev` or your Vite-based framework's development server (refer to [Local development](/build/data-and-storage/netlify-database/local-development/) for more information).
6. Deploy. Netlify automatically provisions the database and applies your migration as part of the deploy lifecycle.

If you'd rather provision the database first and wire up your code afterward, you can also do that from the Netlify UI: navigate to the **Database** page in your project and select **Create a database manually**. Once the database is provisioned, follow the same steps above to install the package and write your first migration.

