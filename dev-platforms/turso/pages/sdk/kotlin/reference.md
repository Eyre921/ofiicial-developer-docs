---
title: "Android Reference"
source: https://docs.turso.tech/sdk/kotlin/reference
path: sdk/kotlin/reference
---

libSQL Android Reference

<Snippet />

<Note>
  This will only work with the Android Gradle Plugin for now. Fully Kotlin
  support is coming.
</Note>

## Installing

Add libsql as a implementation dependency in Gradle:

```kotlin theme={null}
dependencies {
    implementation("tech.turso.libsql:libsql:0.1.0")
}
```

## In-Memory Databases

libSQL supports connecting to [in-memory
databases](https://www.sqlite.org/inmemorydb.html) for cases where you don't
require persistence:

```kotlin theme={null}
import tech.turso.libsql.Libsql

val db = Libsql.open(":memory:")
val conn = db.connect()
```

## Local Development

You can work locally using an SQLite file:

```kotlin theme={null}
import tech.turso.libsql.Libsql

val db = Libsql.open(path = "./local.db")
val conn = db.connect()
```

## Embedded Replicas

You can work with embedded replicas that can sync from the remote URL and
delegate writes to the remote primary database:

```kotlin theme={null}
import tech.turso.libsql.Libsql

val db = Libsql.open(
    path = "./local.db",
    url = "TURSO_DATABASE_URL",
    authToken = "TURSO_AUTH_TOKEN",
)

val conn = db.connect()
```

### Manual Sync

The `sync` function allows you to sync manually the local database with the
remote counterpart:

```kotlin theme={null}
db.sync() // Call sync manually to update local database (only for EmbeddedReplicaDatabase)
```

## Simple query

You can pass a string to `query()` to invoke a SQL statement, as well as
optional arguments:

<CodeGroup>
  ```kotlin Execute theme={null}
  db.connect().use {
      it.execute("INSERT INTO users VALUES (?)", 1)
  }
  ```

  ```kotlin Query theme={null}
  db.connect().use {
      it.query("INSERT INTO users VALUES (?)", 1)
  }
  ```

  ```kotlin Arguments theme={null}
  db.connect().use {
      it.query("SELECT * FROM users WHERE id = ?", 1)
  }
  ```
</CodeGroup>

## Placeholders

libSQL supports the use of positional and named placeholders within SQL statements:

```kotlin Positional theme={null}
db.connect().use {
    it.query("SELECT * FROM users WHERE id = ?", 1)
}
```

```kotlin Named theme={null}
db.connect().use {
    it.query("SELECT * FROM users WHERE id = :id", mapOf(":id" to 1))
}
```

## Batch Transactions

A batch consists of multiple SQL statements executed sequentially within an
implicit transaction. The backend handles the transaction: success commits all
changes, while any failure results in a full rollback with no modifications.

```kotlin theme={null}
db.connect().use {
    it.execute_batch("
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
      );

      INSERT INTO users (name) VALUES ('Alice');
      INSERT INTO users (name) VALUES ('Bob');
    ")
}
```

## Transactions

Interactive transactions in SQLite ensure the consistency of a series of read
and write operations within a transaction's scope. These transactions give you
control over when to commit or roll back changes, isolating them from other
client activity.

```kotlin theme={null}
db.connect().use {
    val tx = it.transaction();

    tx.execute("INSERT INTO users (name) VALUES (?)", "Iku");
    tx.execute("INSERT INTO users (name) VALUES (?)", "Iku 2");

    tx.commit() // or tx.rollback()
}
```
