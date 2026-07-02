---
title: "Netlify Database"
source: https://docs.netlify.com/build/data-and-storage/netlify-database/index.md
path: build/data-and-storage/netlify-database/index
---

---
title: "Netlify Database"
description: "A zero-config, fully integrated Postgres database primitive for Netlify. Build full-stack apps with isolated database branches and platform-managed migrations."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Netlify Database is a fully managed Postgres database built into the Netlify platform. We automatically handle provisioning, [migrations](/build/data-and-storage/netlify-database/migrations/), and [branching](#database-branches) for you, so you can focus on building your application.

> **Pricing Information:** Netlify Database is available on [Credit-based plans](https://www.netlify.com/pricing/) only. When a database is active, it consumes credits for the compute and bandwidth used. However, database storage space (i.e., the size of data stored) is free until July 1, 2026. Learn more in our [billing and usage docs](https://docs.netlify.com/build/data-and-storage/netlify-database/billing-and-usage/).

## Use cases

- Build your full-stack app with a production-grade Postgres database that's ready instantly
- Store and query relational data from your [Functions](/build/functions/overview), [Edge Functions](/build/edge-functions/overview), [Builds](/build/configure-builds/overview), and [Agent Runners](/build/build-with-ai/agent-runners/overview/)
- Scale when you're ready: start prototyping immediately and grow into production without changing your setup

## How it works

When iterating on an application, it is a good practice to have an environment where you can freely update the schema and mutate data without that affecting the live site.

In traditional setups, there is a pre-production (or staging) database that is used during development, but that comes with its own challenges:

- A staging database can easily fall out of sync with the one it's supposed to mirror, creating a false sense of safety when validating changes
- A single staging database becomes a bottleneck when multiple changes are made at the same time, since changes during development may break other work in progress

### Database branching

Netlify Database takes a fundamentally different approach by offering dynamic database branches that are natively integrated into the Netlify development workflow. Here's how it works:

- **[Production deploys](/deploy/deploy-types/production-deploy/)** are the only ones allowed to access the main database, protecting it from unintended side effects of experimentation
- **[Deploy previews](/deploy/deploy-types/deploy-previews/)** get their own database branch, with a copy of the production data taken when the deploy preview is first created; any changes to the data or the schema made during the lifecycle of the deploy preview will _not_ affect the production database

Imagine that you're working on a new feature that allows users of your application to delete articles from the homepage.

Once you open a pull request (or start [an agent run](/build/build-with-ai/agent-runners/overview/)) with the changes, Netlify creates a deploy preview where you can validate the new flow.

This deploy preview is automatically connected to a new database branch, without requiring any code changes. This branch is a copy of the production database, so it contains all the articles that exist on your live site. But any changes are now contained in the deploy preview's database branch, so you can safely test your changes by deleting any homepage article without that causing any articles to disappear from your production site.

Also, consider the scenario in which the change contains a bad database query that accidentally deletes all articles and not just the one you've clicked on. By operating on a separate database branch, you can just reset the branch and start over, without your users ever noticing.

> **Video**: [Watch video](https://www.youtube.com/embed/YM4nwb-bHMs)

### Automatic migrations

Netlify Database includes a built-in migration system that tracks schema changes in your repository and applies them at the right point in the deploy lifecycle - automatically, on every production deploy and deploy preview - so your database schema never drifts from the version of the code that's running.

For details on how to write migrations, the directory layout, and best practices, see the [Migrations](/build/data-and-storage/netlify-database/migrations/) page.

## Built for AI

Netlify Database has been built from the ground up to integrate seamlessly with AI agents - especially [Agent Runners](/build/build-with-ai/agent-runners/overview/).

Every agent run gets its own [database branch](#database-branches) automatically, so agents can experiment, build features, and iterate on schema changes in fully isolated environments. There's no risk of an agent corrupting production data or breaking the live site, which makes it safe to let them ship work end-to-end.

Beyond branching, the rest of the surface area is also designed for agents:

- The **[Netlify Database skill](https://github.com/netlify/context-and-tools/blob/main/skills/netlify-database/SKILL.md)** gives agents the right context to make informed decisions about schema changes and queries. You can install skills by sharing [https://netlify.ai/](https://netlify.ai/) with your agent. Learn more about [using agent skills for Netlify](/build/build-with-ai/agent-setup-guides/agent-setup-overview/#agent-skills).
- The **[Netlify CLI](/build/data-and-storage/netlify-database/cli/)** commands have an agent-first design, with structured `--json` output and non-interactive flags so they're easy to invoke programmatically

> **Video**: [Watch video](https://www.youtube.com/embed/tpXp63Z8MHE)


