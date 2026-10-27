---
title: "Turso Quickstart (Flutter / Dart)"
source: https://docs.turso.tech/sdk/flutter/quickstart
path: sdk/flutter/quickstart
---

Get started with Flutter and Dart using the libSQL client in a few simple steps

> [!NOTE]
>
> This SDK is community maintained and may not be officially supported by Turso, or up to date with the latest features. Join the `#libsql-dart` channel [on Discord](https://tur.so/discord) for help and feedback.

In this Flutter/Dart quickstart we will learn how to:

* Retrieve database credentials
* Install the Flutter/Dart libSQL client
* Connect to a local or remote Turso database
* Execute a query using SQL
* Sync changes to local database (optional)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**2. Install libsql\_dart**

```bash theme={null}
flutter pub add libsql_dart
```

**3. Initialize**

Now connect to your local or remote database using the `LibsqlClient` constructor:

> **Embedded Replicas**
>
> ```dart theme={null}
> final dir = await getApplicationCacheDirectory();
> final path = '${dir.path}/local.db';
>
> final client = LibsqlClient(path)
>   ..authToken = '<TOKEN>'
>   ..syncUrl = '<TURSO_OR_LIBSQL_URL>'
>   ..syncIntervalSeconds = 5
>   ..readYourWrites = true;
> ```

> **Local only**
>
> ```dart File theme={null}
> final dir = await getApplicationCacheDirectory();
> final path = '${dir.path}/local.db';
>
> final client = LibsqlClient(path);
> ```
>
> ```dart In-Memory theme={null}
> final client = LibsqlClient(":memory:");
> ```

> **Remote only**
>
> ```dart theme={null}
> final client = LibsqlClient('<TURSO_OR_LIBSQL_URL>')
>   ..authToken = '<TOKEN>';
> ```

**4. Connect**

```dart theme={null}
await client.connect();
```

**5. Execute**

```dart Execute theme={null}
await client.execute("create table if not exists customers (id integer primary key, name text);");
```

```dart Insert theme={null}
await client.query("insert into customers(name) values ('John Doe')");
```

```dart Select theme={null}
print(await client.query("select * from customers"));
```

```dart Batch theme={null}
await client.batch("""insert into customers (name) values ('Jane Doe'); insert into customers (name) values ('Jake Doe');""");
```

```dart Prepared statement theme={null}
final statement = await client
	.prepare("select * from customers where id = ?");

await statement.query(positional: [1])
```

```dart Interactive transaction theme={null}
final tx = await client.transaction();

await tx
	.execute("update customers set name = 'John Noe' where id = 1");
await tx
	.execute("update customers set name = 'Jane Noe' where id = 2");
print(await tx
	.query("select * from customers where id = ?", positional: [1]));

await tx.commit();
```

If you need to use placeholders for values, you can do that:

```dart Positional theme={null}
final statement = await client
  .prepare("select * from customers where id = ?");

await statement.query(positional: [1])
```

```dart Named theme={null}
final statement = await client
	.prepare("select * from customers where id = :id");

await statement.query(named: {"id": 1})
```

**6. Sync (Embedded Replicas only)**

When using embedded replicas you should call `sync()` on the connector to sync your local database with the primary database.

```dart theme={null}
await client.sync();
```
