---
title: "Quickstart"
source: https://docs.turso.tech/quickstart
path: quickstart
---

Welcome to Turso Cloud! Get started in minutes.

**In this quickstart you will learn how to:**

1. Install the Turso CLI
2. Signup to Turso Cloud
3. Create your first Turso Cloud database
4. Connect to Database Shell

**1. Install the Turso CLI**

We'll be using the Turso CLI throughout this quickstart to manage databases and connect to the database shell.

```bash macOS theme={null}
brew install tursodatabase/tap/turso
```

```bash Linux theme={null}
curl -sSfL https://get.tur.so/install.sh | bash
```

```bash Windows (WSL) theme={null}
curl -sSfL https://get.tur.so/install.sh | bash
```

**2. Signup to Turso Cloud**

The next command will open your browser to sign up:

```bash Signup theme={null}
turso auth signup
```

```bash Login theme={null}
turso auth login
```

**3. Create a Database**

Turso Cloud hosts two SQLite-compatible engines: [Turso](/tursodb/quickstart), with concurrent writes and multi-user access built in, and [libSQL](/libsql). Create your first Turso database with the name `my-db`:

```bash theme={null}
turso db create my-db --tursodb
```

To create a libSQL database instead, omit the `--tursodb` flag:

```bash theme={null}
turso db create my-db
```

You can inspect your new database using the following command:

```bash theme={null}
turso db show my-db
```

**4. Connect to Database Shell**

Congratulations, you created a database! Now connect to it with the `shell` command:

```bash theme={null}
turso db shell my-db
```

> [!NOTE]
>
> Replace `my-db` with the name of your database if you named it differently.

> **Create table**
>
> Now create a table for `users` using SQL:
>
> ```sql theme={null}
> CREATE TABLE users (
>   ID INTEGER PRIMARY KEY AUTOINCREMENT,
>   name TEXT
> );
> ```

> **Insert into new table**
>
> Then insert a row into the `users` table:
>
> ```sql theme={null}
> INSERT INTO users (name) VALUES ('Iku');
> ```

> **Select all rows from table**
>
> Finally, query for all `users`:
>
> ```sql theme={null}
> SELECT * FROM users;
> ```

When you're ready to move onto the next step, you'll want to to quit the shell:

```sql theme={null}
.quit
```

**5. Connect your application to your database**

You're now ready to connect your application to your database. Pick from one of the SDKs below to continue:

<Snippet />
