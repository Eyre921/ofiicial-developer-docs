---
title: "Connect to Turso using Python"
source: https://docs.turso.tech/connect/python
path: connect/python
---

<Steps>
  <Step title="Install">
    Add the Turso package to your Python project:

    ```bash theme={null}
    uv pip install pyturso
    ```
  </Step>

  <Step title="Connect">
    Here's how you can connect to a local SQLite database:

    ```python theme={null}
    import turso

    con = turso.connect("sqlite.db")
    cur = con.cursor()
    ```
  </Step>

  <Step title="Create table">
    Create a table for users:

    ```python theme={null}
    cur.execute("""
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
      )
    """)
    con.commit()
    ```
  </Step>

  <Step title="Insert data">
    Insert some data into the users table:

    ```python theme={null}
    cur.execute("INSERT INTO users (username) VALUES (?)", ("alice",))
    cur.execute("INSERT INTO users (username) VALUES (?)", ("bob",))
    con.commit()
    ```
  </Step>

  <Step title="Query data">
    Query all users from the table:

    ```python theme={null}
    res = cur.execute("SELECT * FROM users")
    users = res.fetchall()
    print(users)
    ```
  </Step>
</Steps>
