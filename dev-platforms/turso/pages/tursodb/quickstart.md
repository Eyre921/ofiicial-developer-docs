---
title: "Quickstart"
source: https://docs.turso.tech/tursodb/quickstart
path: tursodb/quickstart
---

<Steps>
  <Step title="Install">
    <Tabs>
      <Tab title="macOS / Linux">
        ```bash theme={null}
        curl --proto '=https' --tlsv1.2 -LsSf https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh | sh
        ```
      </Tab>

      <Tab title="Windows">
        Run the following command in PowerShell:

        ```powershell theme={null}
        irm https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.ps1 | iex
        ```

        Alternatively, you can [download the Windows executable](https://github.com/tursodatabase/turso/releases/latest) and add it to your PATH.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Launch">
    Then launch the interactive shell:

    ```bash theme={null}
    tursodb
    ```

    This will start the Turso interactive shell where you can execute SQL statements:

    ```
    Turso
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database
    turso>
    ```
  </Step>

  <Step title="Execute">
    Now you can execute SQL statements in the interactive shell:

    <AccordionGroup>
      <Accordion title="Create a table">
        Create a table for users:

        ```sql theme={null}
        CREATE TABLE users (id INT, username TEXT);
        ```
      </Accordion>

      <Accordion title="Insert data">
        Insert some data into the users table:

        ```sql theme={null}
        INSERT INTO users VALUES (1, 'alice');
        INSERT INTO users VALUES (2, 'bob');
        ```
      </Accordion>

      <Accordion title="Query data">
        Query all users from the table:

        ```sql theme={null}
        SELECT * FROM users;
        ```

        This will return:

        ```
        1|alice
        2|bob
        ```
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>

## Experimental Features

You can enable experimental features when launching `tursodb` using various flags such as `--experimental-encryption`, `--experimental-mvcc`, `--experimental-strict`, and `--experimental-views`.

**Note:** These features are not production ready, so do not use them for critical data right now.

For a complete list of available flags and options, see the [Turso manual](https://github.com/tursodatabase/turso).
