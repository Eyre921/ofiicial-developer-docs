---
title: "Connect to Turso using JavaScript"
source: https://docs.turso.tech/connect/javascript
path: connect/javascript
---

## Quickstart

<Steps>
  <Step title="Install">
    Add the Turso database package to your JavaScript project:

    ```bash theme={null}
    npm i @tursodatabase/database
    ```
  </Step>

  <Step title="Connect">
    Here's how you can connect to a local SQLite database:

    ```javascript theme={null}
    import { connect } from "@tursodatabase/database";

    const db = await connect("sqlite.db");
    ```
  </Step>

  <Step title="Create table">
    Create a table for users:

    ```javascript theme={null}
    const createTable = db.prepare(`
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
      )
    `);
    createTable.run();
    ```
  </Step>

  <Step title="Insert data">
    Insert some data into the users table:

    ```javascript theme={null}
    const insertUser = db.prepare("INSERT INTO users (username) VALUES (?)");
    insertUser.run("alice");
    insertUser.run("bob");
    ```
  </Step>

  <Step title="Query data">
    Query all users from the table:

    ```javascript theme={null}
    const stmt = db.prepare("SELECT * FROM users");
    const users = stmt.all();
    console.log(users);
    ```
  </Step>
</Steps>

## Examples

Explore these JavaScript examples to learn more about using Turso Database:

* [Node](https://github.com/tursodatabase/turso/blob/main/examples/javascript/database-node) — Node.js, local file database (no sync)
* [Wasm + Vite](https://github.com/tursodatabase/turso/blob/main/examples/javascript/database-wasm-vite) — Browser (WASM), local database in the browser
