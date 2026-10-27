---
title: "Turso Quickstart (Swift)"
source: https://docs.turso.tech/sdk/swift/quickstart
path: sdk/swift/quickstart
---

Get started with Turso and Swift using the libSQL client in a few simple steps.

<Snippet />

In this Swift quickstart we will learn how to:

* Retrieve database credentials
* Install the libSQL package
* Connect to a local or remote Turso database
* Execute a query using SQL
* Sync changes to local database (optional)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

<Snippet />

**2. Install**

First begin by adding `libsql` as a package dependency in XCode using this repo:

> **[libSQL Swift](https://github.com/tursodatabase/libsql-swift)**
>
> Build from source code

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

**3. Connect**

You must first create a `Database` object and then open a `Connection` to it:

> **Embedded Replicas**
>
> ```swift theme={null}
> import Libsql
>
> let db = try Database(
>     path: "./local.db",
>     url: "TURSO_DATABASE_URL",
>     authToken: "TURSO_AUTH_TOKEN",
>     syncInterval: 300
> )
>
> let conn = try db.connect()
> ```

> **Local only**
>
> ```swift theme={null}
> import Libsql
>
> let db = try Database(
>     path: "./local.db",
> )
>
> let conn = try db.connect()
> ```

> **Remote only**
>
> ```swift theme={null}
> import Libsql
>
> let db = try Database(
>     url: "TURSO_DATABASE_URL",
>     authToken: "TURSO_AUTH_TOKEN"
> )
>
> let conn = try db.connect()
> ```

**4. Execute**

You can execute a SQL query against your existing database by calling `query()`,
or `execute()` when you expect the query to not yield any rows:

```swift theme={null}
let rows = try conn.query("SELECT * FROM users")
```

If you need to use placeholders for values, you can do that:

```swift Positional Query theme={null}
try conn.query("SELECT * FROM users WHERE id = ?", 1)
```

```swift Positional Insert theme={null}
try conn.execute("INSERT INTO users (id) VALUES (?)", 1)
```

> [!NOTE]
>
> Named arguments are not supported yet.

**5. Sync (Embedded Replicas only)**

When using embedded replicas you should call `sync()` on the database type to
sync your local database with the primary database, unless you are using
`sync_interval` (though there is no issue with calling `sync` with
`sync_interval` enabled):

```swift theme={null}
try db.sync()
```
