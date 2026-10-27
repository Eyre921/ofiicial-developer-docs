---
title: "Turso + Actix"
source: https://docs.turso.tech/sdk/rust/guides/actix
path: sdk/rust/guides/actix
---

Set up Turso in your Actix project in minutes

![Actix banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/actix-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=4d06a48cc1186caa607491545546e600)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Actix app — [learn more](https://actix.rs/docs/getting-started)

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**2. Add the libsql crate to the project**

```sh theme={null}
cargo add libsql
```

> [!NOTE]
>
> Optionally, you can add a package such as [`dotenvy`](https://docs.rs/dotenvy/latest/dotenvy) to help you work with `.env` files:
>
> ```sh theme={null}
> cargo add dotenvy
> ```

**3. Execute SQL**

```rust theme={null}
#[tokio::main]
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/", web::get().to(index)).route("/items", web::get().to(get_items)))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}

async fn get_items() -> Result<HttpResponse, Error> {
    dotenv().expect(".env file not found");

    let db_url = env::var("TURSO_DATABASE_URL").unwrap();
    let auth_token = env::var("TURSO_AUTH_TOKEN").unwrap();
    let db_file = env::var("LOCAL_DB").unwrap();

    let db = Builder::new_remote_replica(db_file, url, auth_token)
    .read_your_writes(true)
    .build()
    .await
    .unwrap();

    let conn = db.connect().unwrap();

    let mut results = conn.query("SELECT * FROM items", ()).await.unwrap();

    let mut items: Vec<T> = Vec::new();

    while let Some(row) = results.next().await.unwrap() {
        let item: Item = Item {
            task: row.get(0).unwrap(),
        };
        items.push(item);
    }

    Ok(HttpResponse::Ok().json(items))
}
```

## Examples

> **[Turso + Actix Web Traffic Tracker](https://github.com/tursodatabase/examples/tree/master/app-web-traffic-tracker-actix)**
>
> See the full source code
