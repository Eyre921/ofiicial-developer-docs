---
title: "Connect to Turso using Rust"
source: https://docs.turso.tech/connect/rust
path: connect/rust
---

**1. Install**

Add the Turso crate to your Rust project:

```bash theme={null}
cargo add turso
```

**2. Connect**

Here's how you can connect to a local SQLite database:

```rust theme={null}
use turso::Builder;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Builder::new_local("sqlite.db").build().await?;
    let conn = db.connect()?;

    Ok(())
}
```

**3. Create table**

Create a table for users:

```rust theme={null}
conn.execute(
    "CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
    )",
    ()
).await?;
```

**4. Insert data**

Insert some data into the users table:

```rust theme={null}
conn.execute("INSERT INTO users (username) VALUES (?)", ("alice",)).await?;
conn.execute("INSERT INTO users (username) VALUES (?)", ("bob",)).await?;
```

**5. Query data**

Query all users from the table:

```rust theme={null}
let res = conn.query("SELECT * FROM users", ()).await?;
println!("{:?}", res);
```
