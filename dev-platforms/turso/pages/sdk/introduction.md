---
title: "Turso SDKs"
source: https://docs.turso.tech/sdk/introduction
path: sdk/introduction
---

## Which package should I use?

Two rules cover almost every case:

1. **If a local database is involved, use the Turso packages.** That means fully local databases (embedded, on-device, offline) and local databases that sync with the cloud — even when the database on the other side is libSQL.
2. **If your application only talks to a cloud database over the network, match the driver to the database engine.** [Turso databases](/tursodb/quickstart) use the serverless drivers; [libSQL](/libsql) databases use the libSQL clients.

| Use case | TypeScript | Python | Go | Rust |
| - | - | - | - | - |
| **Local database** (embedded, on-device, offline) | `@tursodatabase/database` | `pyturso` | `tursogo` | `turso` |
| **Local database + cloud sync** (push/pull) | `@tursodatabase/sync` | `pyturso` (with sync) | `tursogo` (with sync) | `turso` (with `sync` feature) |
| **Remote Turso database** (over-the-wire) | `@tursodatabase/serverless` | `turso_serverless` | `tursogo-serverless` | `turso_serverless` |
| **Remote libSQL database** (over-the-wire) | `@libsql/client` | `libsql` | `libsql-client-go` | `libsql` (with `remote` feature) |

**Starting a new project?** Use `@tursodatabase/database` (TypeScript), `pyturso` (Python), `tursogo` (Go), or `turso` (Rust). These are built on the Turso engine — the ground-up rewrite of SQLite with concurrent writes, async I/O, and local-first sync.

**Need sync?** Use [Turso Sync](/sync/usage) for local reads and writes with explicit `push()` / `pull()` to Turso Cloud.

**Using an ORM?**

* **TypeScript** — Drizzle and Prisma run on `@libsql/client` with production-ready support from all major ORMs in the ecosystem.
* **Rust** — [Toasty](/sdk/rust/orm/toasty), the async ORM from the Tokio project, has a native Turso driver built on the `turso` crate.
* **Python** — see the [SQLAlchemy guide](/sdk/python/orm/sqlalchemy).

**Migrating from SQLite?** Turso is a drop-in replacement. Your existing SQL, schema, and queries work unchanged.

**Already using `@libsql/client`, `libsql`, or `go-libsql`?** These packages are built on [libSQL](https://github.com/tursodatabase/libsql), the open-source fork of SQLite that has powered Turso Cloud for years. They are production-ready and battle-tested, and remain the recommended way to access libSQL databases remotely. If your workload needs concurrent writes, push/pull sync, or local-first writes (offline / multi-writer / bidirectional), consider a Turso database and its packages instead.

### The serverless drivers

The serverless drivers speak SQL over HTTP — no persistent connections, no native libraries. They work anywhere your language runs: servers, Docker containers, serverless functions, and edge runtimes. Each mirrors the API of its embedded counterpart, so code moves between local and remote with minimal changes.

> [!NOTE]
>
> **Need sync?** For new projects, use [Turso Sync](/sync/usage) — it gives you local reads and writes with explicit `push()` / `pull()` to the cloud. The libSQL-based SDKs below also support Embedded Replicas, where reads are local and writes are sent to the cloud primary.

## Official SDKs

<Snippet />

## Community SDKs

These SDKs are community-driven and don't come with official Turso support.

> **[Flutter / Dart](/sdk/flutter/quickstart)**

> **[Capacitor](https://capawesome.io/plugins/libsql)**

> **[React Native / OP-SQLite](https://op-engineering.github.io/op-sqlite/)**

> **[Laravel](https://github.com/richan-fongdasen/turso-laravel)**

> **[.NET](https://github.com/tvandinther/libsql-client-dotnet)**

> **[Java](https://github.com/dbeaver/dbeaver-jdbc-libsql)**

> **[Stateless libSQL](https://github.com/DaBigBlob/libsql-stateless-easy)**

## SQL over HTTP

<Snippet />
