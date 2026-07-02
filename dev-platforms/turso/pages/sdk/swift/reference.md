---
title: "Swift Reference"
source: https://docs.turso.tech/sdk/swift/reference
path: sdk/swift/reference
---

libSQL Swift Reference

<Snippet />

## Installing

First begin by adding `libsql` as a package dependency in XCode using this repo:

<Card title="libSQL Swift" href="https://github.com/tursodatabase/libsql-swift">
  Build from source code
</Card>

Or add it to your SwiftPM dependencies:

```swift theme={null}
import PackageDescription

let package = Package(
    // ...
    dependencies: [
        .package(url: "https://github.com/tursodatabase/libsql-swift", from: "0.1.1"),
    ],
    // ...
)
```

## In-Memory Databases

libSQL supports connecting to [in-memory
databases](https://www.sqlite.org/inmemorydb.html) for cases where you don't
require persistence:

```swift theme={null}
import Libsql

let db = Database(":memory:")
let conn = try db.connect()
```

## Local Development

You can work locally using an SQLite file:

```swift theme={null}
import Libsql

let db = Database("local.db")
let conn = try db.connect()
```

## Embedded Replicas

You can work with embedded replicas that can sync from the remote URL and
delegate writes to the remote primary database:

```swift theme={null}
import Libsql

let db = try Database(
    path: "./local.db",
    url: "TURSO_DATABASE_URL",
    authToken: "TURSO_AUTH_TOKEN"
)

let conn = try db.connect()
```

### Manual Sync

The `sync` function allows you to sync manually the local database with the remote counterpart:

```swift theme={null}
try db.sync() // Call sync manually to update local database
```

### Sync Interval

The `syncInterval` parameter allows you to set an interval for automatic
synchronization of the database in the background:

```swift theme={null}
import Libsql

let db = try Database(
    path: "./local.db",
    url: "TURSO_DATABASE_URL",
    authToken: "TURSO_AUTH_TOKEN"
    syncInterval: 300 // Sync every 3 seconds
)

let conn = try db.connect()
```

### Read Your Own Writes

The `readYourWrites` parameter configures the database connection to ensure
that writes are immediately visible to subsequent read operations initiated by
the same connection. This is **enabled by default**, and is particularly
important in distributed systems to ensure consistency from the perspective of
the writing process.

You can disable this behavior by passing `false` to the function:

```swift theme={null}
import Libsql

let db = try Database(
    path: "./local.db",
    url: <LIBSQL_URL>,
    authToken: <LIBSQL_AUTH_TOKEN>,
    readYourWrites: false
)

let conn = try db.connect()
```

## Simple query

You can pass a string to `query()` to invoke a SQL statement, as well as
optional arguments:

<CodeGroup>
  ```swift Execute theme={null}
  try conn.execute("INSERT INTO users VALUES (?)", [1])
  ```

  ```swift Query theme={null}
  try conn.query("SELECT * FROM users")
  ```

  ```swift Arguments theme={null}
  try conn.query("SELECT * FROM users WHERE id = ?", [1])
  ```
</CodeGroup>

## Prepared Statements

You can prepare a cached statement using `prepare()` and then execute it with
`query()`:

```swift theme={null}
let stmt = try conn.prepare("SELECT * FROM users WHERE id = ?")
stmt.bind([1])
stmt.query()
```

## Placeholders

libSQL supports the use of positional and named placeholders within SQL statements:

<CodeGroup>
  ```swift Positional theme={null}
  try conn.query("SELECT * FROM users WHERE id = ?", [1])
  ```

  ```swift Named theme={null}
  try conn.query("SELECT * FROM users WHERE id = :id", [ ":id": 1 ])
  ```
</CodeGroup>
