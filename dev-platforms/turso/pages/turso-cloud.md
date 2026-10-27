---
title: "Turso Cloud Documentation"
source: https://docs.turso.tech/turso-cloud
path: turso-cloud
---

Fully managed platform for SQLite-compatible databases. Deploy Turso, a rewrite of SQLite with concurrent writes and multi-user access built in, or libSQL, the battle-tested SQLite fork. No need to switch to Postgres for concurrency.

Turso Cloud is a fully managed database platform, designed to scale from prototype to production. It hosts two database engines, both fully compatible with SQLite:

* **[Turso](/tursodb/quickstart)** — a ground-up rewrite of SQLite. Turso supports **concurrent writes** and **multi-user access by default**: many clients can read and write the same database at the same time, over the network. If SQLite's single-writer limitation is what would push you toward a client-server database like Postgres, Turso removes it — you keep SQLite's simplicity and compatibility and gain the concurrency. Concurrent writes are the headline, but not the whole story: see the [Turso documentation](/tursodb/quickstart) for change data capture, vector search, encryption, sync, and more.

* **[libSQL](/libsql)** — a fork of SQLite, battle-tested in production on Turso Cloud for years.

> [!NOTE]
>
> Turso databases on Turso Cloud are in early preview — a reflection of how
> recently the offering landed on the platform, not of the engine itself.
> Create one with `turso db create --tursodb`.

> **[Vector Search](/features/ai-and-embeddings)**
>
> Native similarity search for AI apps and RAG workflows, no extensions
> required.

> **[Replication & Sync](/features/embedded-replicas/introduction)**
>
> Keep devices in sync with each other on demand with Turso Cloud.

> **[Branching](/features/branching)**
>
> Create isolated Copy-on-Write branches super fast.

> **Analytics**
>
> Monitor performance and usage across databases.

> **[Bring-Your-Own-Key Encryption](/cloud/encryption)**
>
> Keep sensitive data private with keys only you control. Keys are per-database for full isolation.

> **[Scoped Access Tokens](/sdk/authorization)**
>
> Fine-grained tokens scoped by database, table, action, and expiration. Read-only, write, or custom permissions.

> **Team Access**
>
> Collaborate on databases with members, and manage access permissions.

> **Fully Managed**
>
> We handle infrastructure, scaling, and security.

> **[Backups and Recovery](/features/point-in-time-recovery)**
>
> Restore your database to any point in time, and recover deleted databases
> for up to five days.

## Start building

Learn how to manage, distribute and integrate your databases with the CLI, API and SDKs.

> **[Turso CLI](/cli)**
>
> Manage groups, databases, and API tokens with the Turso CLI.

> **[Turso Platform API](/api-reference)**
>
> Programmatically manage groups and databases using the Platform API.

> **[Client SDKs](/sdk)**
>
> Connect and integrate your application with one of our client SDKs, for
> Turso and libSQL databases alike.

> **[Tutorials](https://turso.tech/blog)**
>
> Learn how to work with Turso and your favorite language or framework.

## Community

Join the Turso community to ask questions, share what you're working on, discuss best practices, and share tips on [Discord](https://tur.so/discord), [Twitter](https://twitter.com/tursodatabase), and [LinkedIn](https://www.linkedin.com/company/turso).

> **[Discord](https://tur.so/discord)**

> **[GitHub](https://github.com/tursodatabase)**

> **[X (Twitter)](https://twitter.com/tursodatabase)**
