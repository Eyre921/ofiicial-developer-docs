---
title: "Netlify Database API reference"
source: https://docs.netlify.com/build/data-and-storage/netlify-database/api.md
path: build/data-and-storage/netlify-database/api
---

---
title: "API reference"
description: "Reference for the modules and methods you can use to interact with Netlify Database from your application code."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

This page documents the modules and methods you can use to interact with Netlify Database from your application code.

## `@netlify/database`

The recommended way to get started with Netlify Database is to install the `@netlify/database` module in your project:

```
npm install @netlify/database
```

This module offers a set of methods that let you seamlessly interact with your database, providing a database driver that is automatically configured and optimized for where your code is running.

### `getConnectionString`

Returns the database connection string for the current environment, automatically pointing to the correct [database branch](/build/data-and-storage/netlify-database/#database-branches) (e.g. the production database for production deploys, or an isolated branch for deploy previews).

This is useful if you want to use your own database driver or ORM.

```ts
import { getConnectionString } from "@netlify/database";

const connectionString = getConnectionString();
```

#### Return value

A `string` containing the Postgres connection URL for the current environment.

#### Example

This example shows how you might use `getConnectionString` to initialize a third-party Postgres client, such as [`pg`](https://www.npmjs.com/package/pg), with the connection string for the current environment.

```ts
import { getConnectionString } from "@netlify/database";
import pg from "pg";

const pool = new pg.Pool({ connectionString: getConnectionString() });
const { rows: users } = await pool.query("SELECT * FROM users");
```

### `getDatabase`

Returns a database client that you can use to run queries using the [`sql`](#sql) and [`pool`](#pool) methods. The client is intelligently configured to use the best connection type for your environment - for example, it uses a different underlying connector when running queries from builds or a long-running server compared to when running them in [Netlify Functions](/build/functions/overview) or [Edge Functions](/build/edge-functions/overview).

```ts
import { getDatabase } from "@netlify/database";

const db = getDatabase();
```

#### Parameters

- **`options`** _(optional)_: an object with the following properties:
  - `connectionString`: a Postgres connection string to use instead of the automatically-provisioned one
  - `debug`: a boolean to enable debug logging

#### Return value

A database driver object that you can use to query the database using the [`sql`](#sql) or [`pool`](#pool) methods.

### `sql`

A [tagged template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) function for executing SQL queries safely, based on the [Waddler](https://waddler.drizzle.team/docs/overview) open-source module.

Values interpolated into the template are automatically parameterized to prevent SQL injection.

```ts
const db = getDatabase();

const userId = 42;
const users = await db.sql`SELECT * FROM users WHERE id = ${userId}`;
```

#### Parameters

The `sql` function accepts a template literal string with interpolated values. Any JavaScript value interpolated into the template is treated as a parameterized value, not raw SQL.

You can optionally specify a generic type parameter to type the returned rows:

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

const users = await db.sql<User>`SELECT * FROM users`;
```

#### Return value

A thenable `SQLTemplate` object that resolves to an array of row objects.

This object also supports the following methods:

- **`execute()`**: executes the query and returns a `Promise<T[]>` of row objects
- **`stream()`**: returns an `AsyncGenerator<T>` that yields rows one at a time
- **`chunked(chunkSize?)`**: returns an `AsyncGenerator<T[]>` that yields rows in chunks of the specified size
- **`toSQL()`**: returns the raw SQL string and parameters without executing the query

#### Example

This example shows common CRUD operations using the `sql` tagged template, including selecting, inserting, updating, and deleting rows, as well as streaming results for large datasets.

```ts
import { getDatabase } from "@netlify/database";

const db = getDatabase();

// Select with a condition
const activeUsers = await db.sql`SELECT * FROM users WHERE active = ${true}`;

// Insert a row
await db.sql`INSERT INTO users (name, email) VALUES (${"Ada"}, ${"ada@example.com"})`;

// Update a row
await db.sql`UPDATE users SET name = ${"Ada Lovelace"} WHERE id = ${1}`;

// Delete a row
await db.sql`DELETE FROM users WHERE id = ${1}`;

// Stream rows one at a time
for await (const row of db.sql`SELECT * FROM users`.stream()) {
  console.log(row);
}

// Stream rows in chunks
for await (const chunk of db.sql`SELECT * FROM users`.chunked(100)) {
  console.log(`Processing ${chunk.length} rows`);
}
```

The `sql` function also exposes the following helpers:

- **`sql.identifier(value)`**: creates a safe SQL identifier for dynamically referencing table or column names. Accepts a string, an array of strings, or an object with `schema`, `table`, `column`, and `as` properties.

  ```ts
  const table = db.sql.identifier({ table: "users" });
  const rows = await db.sql`SELECT * FROM ${table}`;
  ```

- **`sql.values(value)`**: creates a values list for bulk inserts. Accepts a two-dimensional array where each inner array represents a row.

  ```ts
  const data = db.sql.values([
    ["Ada", "ada@example.com"],
    ["Bob", "bob@example.com"],
  ]);
  await db.sql`INSERT INTO users (name, email) VALUES ${data}`;
  ```

- **`sql.raw(value)`**: injects a raw, unparameterized value into a query. Accepts a string, number, boolean, or bigint. Use with caution - this bypasses SQL injection protection.

  ```ts
  const order = db.sql.raw("DESC");
  const users = await db.sql`SELECT * FROM users ORDER BY name ${order}`;
  ```

- **`sql.unsafe(query, params?, options?)`**: executes a raw SQL query string. Accepts a query string, an optional array of parameter values, and an optional options object with a `rowMode` property (`"array"` or `"object"`).

  ```ts
  const results = await db.sql.unsafe("SELECT * FROM users WHERE id = $1", [42]);
  ```

- **`sql.default`**: a constant representing the SQL `DEFAULT` keyword, for use when inserting rows that should use the column's default value.

  ```ts
  await db.sql`INSERT INTO users (name, created_at) VALUES (${"Ada"}, ${db.sql.default})`;
  ```

### `pool`

A [`pg.Pool`](https://node-postgres.com/apis/pool) connection pool instance. Use this when you need direct control over the connection lifecycle - most commonly for transactions, where `BEGIN`, your queries, and `COMMIT`/`ROLLBACK` must all run on the same connection.

#### Example

This example shows how you might use the connection pool to run a transaction that inserts a user and their first post atomically - if either insert fails, both are rolled back.

```ts
import { getDatabase } from "@netlify/database";

const db = getDatabase();

const client = await db.pool.connect();
try {
  await client.query("BEGIN");
  await client.query(
    "INSERT INTO users (name, email) VALUES ($1, $2)",
    ["Ada", "ada@example.com"]
  );
  await client.query(
    "INSERT INTO posts (author_id, title) VALUES ($1, $2)",
    [1, "First post"]
  );
  await client.query("COMMIT");
} catch (e) {
  await client.query("ROLLBACK");
  throw e;
} finally {
  client.release();
}
```

## REST API

The Netlify REST API exposes endpoints for managing databases, branches, and snapshots programmatically. All endpoints are scoped to a site, are rooted at `https://api.netlify.com/api/v1`, and authenticate via OAuth 2 - see the full [Netlify API reference](https://open-api.netlify.com) for authentication details and shared response shapes.

### `POST /sites/{site_id}/database`

Creates a new database for the specified site. If a database already exists, returns the existing connection string. The database region defaults to the site's functions region if not specified.

**Request body**

- `region` _(string, optional)_: the region where the database should be created

**Response** - `201 Created`, or `200 OK` if a database already exists

- `connection_string` _(string)_: the connection string for the database

### `GET /sites/{site_id}/database`

Returns the database connection string for the specified site.

**Response** - `200 OK`

- `connection_string` _(string)_: the connection string for the database

### `POST /sites/{site_id}/database/branch`

Creates a new database branch for a deploy. If a branch already exists for the specified deploy ID, returns the existing connection string.

**Request body**

- `deploy_id` _(string, required)_: the deploy ID to associate with this branch
- `parent_branch_id` _(string, optional)_: the ID of the parent branch to fork from; defaults to the production branch

**Response** - `201 Created`, or `200 OK` if a branch already exists for this deploy

- `connection_string` _(string)_: the connection string for the database branch

### `GET /sites/{site_id}/database/branch/{deploy_id}`

Returns the database branch connection string for a specific deploy. Returns `404` if no branch exists for the deploy.

**Response** - `200 OK`

- `connection_string` _(string)_: the connection string for the database branch

### `DELETE /sites/{site_id}/database/branch/{deploy_id}`

Deletes the database branch associated with a deploy.

**Response** - `204 No Content`

### `POST /sites/{site_id}/database/snapshot`

Creates a point-in-time snapshot of a database branch. Defaults to the production branch if no branch name is specified.

**Request body**

- `branch_name` _(string, optional)_: the name of the branch to snapshot; defaults to `production`
- `name` _(string, optional)_: an optional name for the snapshot

**Response** - `201 Created`

- `id` _(string)_: the unique identifier of the snapshot
- `timestamp` _(string, ISO 8601)_: the timestamp when the snapshot was created
- `source_branch_id` _(string)_: the ID of the branch that was snapshotted

### `GET /sites/{site_id}/database/snapshots`

Returns all snapshots for the site's database.

**Response** - `200 OK`

- `snapshots` _(array)_: list of snapshot objects with `id`, `timestamp`, and `source_branch_id` fields

### `DELETE /sites/{site_id}/database/snapshot/{snapshot_id}`

Deletes a database snapshot.

**Response** - `204 No Content`

### `POST /sites/{site_id}/database/snapshot/{snapshot_id}/restore`

Restores a snapshot to a database branch. Defaults to the production branch if no branch name is specified.

**Request body**

- `branch_name` _(string, optional)_: the name of the branch to restore the snapshot to; defaults to `production`

**Response** - `200 OK`

