---
title: "Turso Quickstart (Android)"
source: https://docs.turso.tech/sdk/kotlin/quickstart
path: sdk/kotlin/quickstart
---

Get started with Turso and Android using the libSQL client in a few simple steps.

<Snippet />

> [!NOTE]
>
> This will only work with the Android Gradle Plugin for now. Fully Kotlin
> support is coming.

In this Kotlin quickstart we will learn how to:

* Retrieve database credentials
* Add libSQL as a dependency in your Android Gradle project
* Connect to a local or remote Turso database
* Execute a query using SQL
* Sync changes to local database (optional)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

<Snippet />

**2. Install**

Add libsql as a implementation dependency in Gradle:

> [!NOTE]
>
> This will only work with the Android Gradle Plugin for now.

```kotlin theme={null}
dependencies {
    implementation("tech.turso.libsql:libsql:0.1.0")
}
```

**3. Connect**

You must first create a `Database` object and then open a `Connection` to it:

> **Embedded Replicas**
>
> ```kotlin theme={null}
> import tech.turso.libsql.Libsql
>
> val db = Libsql.open(
>     path = "./local.db",
>     url = "TURSO_DATABASE_URL",
>     authToken = "TURSO_AUTH_TOKEN",
> )
>
> val conn = db.connect()
> ```

> **Local only**
>
> ```kotlin theme={null}
> import tech.turso.libsql.Libsql
>
> val db = Libsql.open(path = "./local.db")
> val conn = db.connect()
> ```

> **Remote only**
>
> ```kotlin theme={null}
> import tech.turso.libsql.Libsql
>
> val db = Libsql.open(
>     url = "TURSO_DATABASE_URL",
>     authToken = "TURSO_AUTH_TOKEN",
> )
>
> val conn = db.connect()
> ```

**4. Execute**

You can execute a SQL query against your existing database by calling `execute()`:

```kotlin theme={null}
db.connect().use {
    it.execute("INSERT INTO users (id) VALUES (1)")
}
```

If you need to use placeholders for values, you can do that:

```kotlin Positional theme={null}
db.connect().use {
    it.query("SELECT * FROM users WHERE id = ?", 1)
}
```

```kotlin Named theme={null}
db.connect().use {
    it.query("INSERT INTO users (name) VALUES (:name)", mapOf(":name" to "Iku"))
}
```

**5. Sync (Embedded Replicas only)**

When using embedded replicas you should call `sync()` on the database type to
sync your local database with the primary database, unless you are using
`syncInterval` (though there is no issue with calling `sync` with
`syncInterval` enabled):

```kotlin theme={null}
db.sync()
```
