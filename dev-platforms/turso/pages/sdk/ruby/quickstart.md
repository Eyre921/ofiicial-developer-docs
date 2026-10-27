---
title: "Turso Quickstart (Ruby)"
source: https://docs.turso.tech/sdk/ruby/quickstart
path: sdk/ruby/quickstart
---

Get started with Turso and Ruby using the libSQL client in a few simple steps.

<Snippet />

In this Ruby quickstart we will learn how to:

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

Inside your Ruby project, install the following Rubygem:

```bash theme={null}
bundle add turso_libsql
```

**3. Connect**

> **Embedded Replicas**
>
> ```rb theme={null}
> require 'turso_libsql'
>
> db =Libsql::Database.new(
>   path: 'local.db',
>   url: ENV['TURSO_DATABASE_URL'],
>   auth_token: ENV['TURSO_AUTH_TOKEN'],
>   sync_interval: 100
> )
> ```

> **Local only**
>
> ```rb theme={null}
> require 'turso_libsql'
>
> db = Libsql::Database.new(path: 'local.db')
> ```

> **Remote only**
>
> ```rb theme={null}
> require 'turso_libsql'
>
> db = Libsql::Database.new(
>   url: ENV['TURSO_DATABASE_URL'],
>   auth_token: ENV['TURSO_AUTH_TOKEN']
> )
> ```

**4. Execute**

You can execute a SQL query against your existing database by preparing a statement and then executing it:

```c theme={null}
db.connect do |conn|
  rows = conn.query 'SELECT * FROM users'
  rows.close
end
```

If you need to use placeholders for values, you can do that:

```c Positional theme={null}
name = 'Iku'
rows = conn.execute 'INSERT INTO users (id) VALUES (?)', [name]
```

**5. Sync (Embedded Replicas only)**

When using embedded replicas, you should call `sync` on the database to sync your local database with the primary database, unless you are using `sync_interval` (though there is no issue with calling `sync` with `sync_interval` enabled):

```rb theme={null}
db.sync
```
