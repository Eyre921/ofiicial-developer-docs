---
title: "Turso Quickstart (PHP)"
source: https://docs.turso.tech/sdk/php/quickstart
path: sdk/php/quickstart
---

Get started with Turso and PHP using the libSQL client in a few simple steps.

In this PHP quickstart we will learn how to:

* Install libSQL with Composer
* Retrieve database credentials
* Connect to a Turso database
* Execute a query using SQL
* Sync changes to local database (optional)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create
    one](/quickstart).

    <Snippet />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Install">
    Install the package to your project using composer:

    ```console theme={null}
    composer require turso/libsql
    ```
  </Step>

  <Step title="Connect">
    Now connect to your local or remote database using the libSQL connector:

    <AccordionGroup>
      <Accordion title="Embedded Replica">
        ```php theme={null}
        use Libsql\Database;

        $db = new Database(
            path: 'test.db',
            url: getenv('TURSO_URL'),
            authToken: getenv('TURSO_AUTH_TOKEN')
            syncInterval: 100 // Sync every second
        );
        $conn = $db->connect();
        ```
      </Accordion>

      <Accordion title="Local only">
        ```php theme={null}
        use Libsql\Database;

        $db = new Database(path: "database.db");
        ```

        Or just:

        ```php theme={null}
        use Libsql\Database;

        $db = new Database("database.db");
        ```
      </Accordion>

      <Accordion title="Local only">
        ```php theme={null}
        use Libsql\Database;

        $db = new Database(path: "database.db");
        ```

        Or just:

        ```php theme={null}
        use Libsql\Database;

        $db = new Database("database.db");
        ```
      </Accordion>

      <Accordion title="Remote only">
        ```php theme={null}
        use Libsql\Database;

        $db = new Database(
            url: getenv('TURSO_URL'),
            authToken: getenv('TURSO_AUTH_TOKEN'),
        )
        ```
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Execute">
    You can execute SQL queries against your existing database as follows:

    ```php theme={null}
    $createUsers = "
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          age INTEGER
      );
      INSERT INTO users (name, age) VALUES ('Prof. Ir. Onno Widodo Purbo, M.Eng., Ph.D', 61);
      INSERT INTO users (name, age) VALUES ('Jim Geovedi', 41);
      INSERT INTO users (name, age) VALUES ('Nasirun', 59);
    ";

    $db->executeBatch($createUsers);
    $db->query("SELECT * FROM users")->fetchArray();
    ```

    If you need to use placeholders for values, you can do that:

    <CodeGroup>
      ```php Positional theme={null}
      $db->query("SELECT * FROM users WHERE id = ?", [1])->fetchArray();
      ```

      ```php Named theme={null}
      $db->query("SELECT * FROM users WHERE id = :id", [":id" => 1])->fetchArray();
      ```
    </CodeGroup>
  </Step>

  <Step title="Sync (Embedded Replicas only)">
    When using embedded replicas you should call `sync()` on the database type
    to sync your local database with the primary database:

    ```php theme={null}
    <?php

    $db->sync();
    ```
  </Step>
</Steps>
