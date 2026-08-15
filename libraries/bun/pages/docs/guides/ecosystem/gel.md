---
title: "Use Gel with Bun"
source: https://bun.com/docs/guides/ecosystem/gel
path: docs/guides/ecosystem/gel
---

Gel (formerly EdgeDB) is a graph-relational database built on Postgres. It provides a declarative schema language, migrations system, and object-oriented query language. It also supports raw SQL queries. It solves object-relational mapping at the database layer, so your application code doesn't need an ORM library.

***

First, [install Gel](https://docs.geldata.com/learn/installation) if you haven't already.

<CodeGroup>
  ```sh Linux/macOS terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  curl https://www.geldata.com/sh --proto "=https" -sSf1 | sh
  ```

  ```sh Windows terminal icon="windows" theme={"theme":{"light":"github-light","dark":"dracula"}}
  irm https://www.geldata.com/ps1 | iex
  ```

  ```sh Homebrew terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  brew install geldata/tap/gel-cli
  ```
</CodeGroup>

***

Use `bun init` to create a fresh project.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
mkdir my-gel-app
cd my-gel-app
bun init -y
```

***

Initialize a Gel instance for the project with the Gel CLI. The `gel project init` command creates a `gel.toml` file in the project root.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
gel project init
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
No `gel.toml` (or `edgedb.toml`) found in `/Users/colinmcd94/Documents/bun/fun/examples/my-gel-app` or above
Initializing new project...
Checking Gel versions...
┌─────────────────────┬──────────────────────────────────────────────────────────────────┐
│ Project directory   │ /Users/colinmcd94/Documents/bun/fun/examples/my-gel-app          │
│ Project config      │ /Users/colinmcd94/Documents/bun/fun/examples/my-gel-app/gel.toml │
│ Schema dir (empty)  │ /Users/colinmcd94/Documents/bun/fun/examples/my-gel-app/dbschema │
│ Installation method │ portable package                                                 │
│ Version             │ x.y+6d5921b                                                      │
│ Instance name       │ my_gel_app                                                       │
│ Branch              │ main                                                             │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘
Version x.y+6d5921b is already downloaded
Initializing Gel instance 'my_gel_app'...
Applying migrations...
Everything is up to date. Revision initial
Writing gel.local.toml for configuration
Project initialized.
To connect to my_gel_app, run `gel`
```

***

To check that the database is running, open a REPL and run a query.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
gel
my_gel_app:main> select 1 + 1;
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
{2}
```

Then run `\quit` to exit the REPL.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
my_gel_app:main> \quit
```

***

Next, define a schema. The `gel project init` command already created a `dbschema/default.gel` file to hold it.

```txt File Tree icon="folder-tree" theme={"theme":{"light":"github-light","dark":"dracula"}}
dbschema
├── default.gel
├── extensions.gel
├── futures.gel
└── migrations
```

***

Open that file and paste the following contents.

```ts default.gel icon="file-code" theme={"theme":{"light":"github-light","dark":"dracula"}}
module default {
  type Movie {
    required title: str;
    releaseYear: int64;
  }
};
```

***

Then generate and apply an initial migration.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
gel migration create
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
Created dbschema/migrations/00001-m1uwekr.edgeql, id: m1uwekrn4ni4qs7ul7hfar4xemm5kkxlpswolcoyqj3xdhweomwjrq
```

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
gel migrate
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
Applying m1uwekrn4ni4qs7ul7hfar4xemm5kkxlpswolcoyqj3xdhweomwjrq (00001-m1uwekr.edgeql)
... parsed
... applied
```

***

With the schema applied, query the database with Gel's JavaScript client library. Install the client library and Gel's codegen CLI, then create a `seed.ts` file.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun add gel
bun add -D @gel/generate
touch seed.ts
```

***

Paste the following code into `seed.ts`.

The client auto-connects to the database. The script inserts a few movies with the `.execute()` method, using EdgeQL's `for` expression to turn the bulk insert into a single query.

```ts seed.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
import { createClient } from "gel";

const client = createClient();

const INSERT_MOVIE = `
  with movies := <array<tuple<title: str, year: int64>>>$movies
  for movie in array_unpack(movies) union (
    insert Movie {
      title := movie.title,
      releaseYear := movie.year,
    }
  )
`;

const movies = [
  { title: "The Matrix", year: 1999 },
  { title: "The Matrix Reloaded", year: 2003 },
  { title: "The Matrix Revolutions", year: 2003 },
];

await client.execute(INSERT_MOVIE, { movies });

console.log(`Seeding complete.`);
process.exit();
```

***

Then run this file with Bun.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun run seed.ts
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
Seeding complete.
```

***

Gel implements several code generation tools for TypeScript. To write typesafe queries against the seeded database, generate the EdgeQL query builder with `@gel/generate`.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bunx @gel/generate edgeql-js
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
Generating query builder...
Detected tsconfig.json, generating TypeScript files.
   To override this, use the --target flag.
   Run `npx @gel/generate --help` for full options.
Introspecting database schema...
Writing files to ./dbschema/edgeql-js
Generation complete! 🤘
Checking the generated query builder into version control
is not recommended. Would you like to update .gitignore to ignore
the query builder directory? The following line will be added:

   dbschema/edgeql-js

[y/n] (leave blank for "y")
> y
```

***

In `index.ts`, import the generated query builder from `./dbschema/edgeql-js` and write a select query.

```ts index.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
import { createClient } from "gel";
import e from "./dbschema/edgeql-js";

const client = createClient();

const query = e.select(e.Movie, () => ({
  title: true,
  releaseYear: true,
}));

const results = await query.run(client);
console.log(results);

results; // { title: string, releaseYear: number | null }[]
```

***

Run the file with Bun to see the movies you inserted.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun run index.ts
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
[
  {
    title: "The Matrix",
    releaseYear: 1999,
  }, {
    title: "The Matrix Reloaded",
    releaseYear: 2003,
  }, {
    title: "The Matrix Revolutions",
    releaseYear: 2003,
  }
]
```

***

See the [Gel docs](https://docs.geldata.com/).
