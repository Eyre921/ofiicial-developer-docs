---
title: "Turso + Rocket"
source: https://docs.turso.tech/sdk/rust/guides/rocket
path: sdk/rust/guides/rocket
---

Set up Turso in your Rocket project in minutes

![Rocket banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/rocket-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=74dabf48dfb2a2ec82d5750672eab0e9)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Rocket app — [learn more](https://rocket.rs/v0.5/guide/getting-started/)

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
#[get("/todos")]
async fn get_todos() -> Json<Vec<Todo>> {
    dotenv().expect(".env file not found");

    let url = env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL not found!");
    let token = env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN not found!");

    let db = Database::open_remote(url, token).unwrap();
    let conn = db.connect().unwrap();

    let mut response = conn.query("select * from todos", ()).await.unwrap();

    let mut todos: Vec<Todo> = Vec::new();
    while let Some(row) = response.next().unwrap() {
        let todo: Todo = Todo {
            task: row.get(0).unwrap(),
        };
        todos.push(todo);
    }

    Json(todos)
}

#[launch]
fn rocket() -> _ {
    dotenv().ok();
    rocket::build().mount("/", routes![get_todos])
}
```

## Examples

> **[Turso + Rocket Todo List](https://github.com/tursodatabase/examples/tree/master/app-todo-rocket)**
>
> See the full source code
