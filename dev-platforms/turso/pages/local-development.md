---
title: "Local Development"
source: https://docs.turso.tech/local-development
path: local-development
---

Build locally with a local Turso database, or a local libSQL server.

Developers can build locally with Turso using either of the following methods:

* [Local Turso database](#local-turso-database) — local database file, no server needed (recommended)
* [Turso CLI](#turso-cli) — managed libSQL server

## Using a dump locally

You can always dump your production database and use it locally for development:

**1. Create a dump using the Turso CLI**

```bash theme={null}
turso db shell your-database .dump > dump.sql
```

**2. Create SQLite file from dump**

```bash theme={null}
cat dump.sql | sqlite3 local.db
```

**3. Connect to the file**

You can use either of the methods below with the `local.db` file, or you can use a new file name if you prefer to create a database from scratch.

## Local Turso database

Whenever your application runs against a local database, we recommend the [Turso packages](/sdk). They are fully SQLite-compatible — they open existing SQLite files — and run entirely in your process, no server needed:

```ts JavaScript theme={null}
import { connect } from "@tursodatabase/database";

const db = await connect("local.db");
```

```rust Rust theme={null}
use turso::Builder;

let db = Builder::new_local("local.db").build().await?;
let conn = db.connect()?;
```

```go Go theme={null}
package main

import (
  "database/sql"

  _ "turso.tech/database/tursogo"
)

func main() {
  db, _ := sql.Open("turso", "local.db")
  defer db.Close()
}
```

```python Python theme={null}
import turso

db = turso.connect("local.db")
```

> [!NOTE]
>
> You don't need to provide an `authToken` in development.

> [!NOTE]
>
> It's recommended to use environment variables for both `url` and `authToken` for a seamless developer experience.

## Turso CLI

If you're developing against a [libSQL](/libsql) database and use libSQL-specific features like [extensions](/libsql#extensions), you should use the Turso CLI:

```bash theme={null}
turso dev
```

This will start a local libSQL server and create a database for you. You can then connect to it with your libSQL client using the `url` option:

```ts JavaScript theme={null}
import { createClient } from "@libsql/client";

const client = createClient({
  url: "http://127.0.0.1:8080",
});
```

The same URL works with the libSQL clients for [other languages](/sdk).

> [!WARNING]
>
> Changes will be lost when you stop the server.

If you want to persist changes, or use a production dump, you can pass the `--db-file` flag with the name of the SQLite file:

```bash theme={null}
turso dev --db-file local.db
```

## Turso Cloud database

If you already have a database created on Turso Cloud, you can use that same one in development by passing the `url` option to your SDK.

> [!WARNING]
>
> Keep in mind that using the Turso Cloud hosted database will incur platform costs and count towards your quota. Consider one of the local methods above to avoid platform costs.

## Connecting a GUI

During development you can easily connect to a SQLite, libSQL, or Turso database using one of the tools below:

* [Beekeeper Studio](https://www.beekeeperstudio.io/db/libsql-client/) — macOS, Linux, and Windows
* [Outerbase](https://www.outerbase.com) — Runs in the browser
* [TablePlus](https://tableplus.com) — macOS, Windows, and Linux
* [Dataflare](https://dataflare.app) — Paid (with limited free version) macOS, Windows, and Linux
* [Outerbase Studio](https://libsqlstudio.com) - Runs in the browser
* [DBeaver](https://dbeaver.io) - macOS, Windows, and Linux
