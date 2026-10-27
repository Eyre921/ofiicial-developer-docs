---
title: "pg_pinecone quickstart"
source: https://docs.pinecone.io/guides/pg-pinecone/quickstart
path: guides/pg-pinecone/quickstart
---

Install the pg_pinecone extension for Postgres and search a sample table with a native index, which runs the search engine Pinecone uses at scale.

This quickstart installs pg\_pinecone on a PostgreSQL server you manage. You create a sample table with vectors and search it with a `native` index, which runs the search engine Pinecone uses at scale inside Postgres. You can bring your own vectors, with no API key or network access, or have Pinecone generate embeddings. To compare `native` with the other engines, see [Storage engines](/guides/pg-pinecone/storage-engines).

If you already have a table with a pgvector index, complete steps 1 and 2 to install pg\_pinecone, then [switch from pgvector to native](/guides/pg-pinecone/switch-from-pgvector).

## Prerequisites

* A PostgreSQL 17 or 18 server and a superuser role on it.
* pgvector installed on that server, because pg\_pinecone uses its `vector` column type and distance operators. If you don't have it, run `sudo apt install postgresql-17-pgvector` on Debian or Ubuntu, or `brew install pgvector` with Homebrew on macOS. For other Linux distributions, see the [pgvector installation guide](https://github.com/pgvector/pgvector#installation). If you install with Docker, the image includes Postgres and pgvector, so you need only Docker.
* Optional: a [Pinecone API key](https://app.pinecone.io/organizations/-/projects/-/keys), if you want Pinecone to generate the embeddings. A key from the free [Starter plan](https://www.pinecone.io/pricing/) is enough.

> [!NOTE]
>
> The `native` engine never calls Pinecone. Steps 3 and 4 each have two tabs, so pick the same one in both. **Your own vectors** runs entirely in your database with no API key or network access, and **Pinecone embeddings** generates embeddings with a Pinecone-hosted model.

## 1. Install pg\_pinecone

**Release archive**

1. Download the release archive for your platform and Postgres version from the [releases page](https://github.com/pinecone-io/pg_pinecone/releases).

   Archives are published for PostgreSQL 17 and 18 on Linux x86\_64, Linux arm64, and macOS arm64. The Linux x86\_64 build needs a CPU that supports x86-64-v3 (Intel Haswell or newer, which covers current cloud instances), and the Linux builds need glibc 2.39 or later, such as Ubuntu 24.04 or Debian 13.

2. Extract the archive and copy its files into your Postgres installation.

   The commands use `PG=17`. If your server runs PostgreSQL 18, change it to `PG=18`. To check your version, run `pg_config --version`. `pg_config` also reports where your Postgres installation keeps extension files:

   ```bash Linux theme={null}
   PG=17
   tar xzf pg_pinecone-0.11.0-pg$PG-linux-x86_64.tar.gz
   sudo cp usr/lib/postgresql/$PG/lib/pg_pinecone.so "$(pg_config --pkglibdir)/"
   sudo cp usr/share/postgresql/$PG/extension/pg_pinecone* "$(pg_config --sharedir)/extension/"
   ```

   ```bash macOS theme={null}
   PG=17
   tar xzf pg_pinecone-0.11.0-pg$PG-darwin-arm64.tar.gz
   cp opt/homebrew/lib/postgresql@$PG/pg_pinecone.dylib "$(pg_config --pkglibdir)/"
   cp opt/homebrew/share/postgresql@$PG/extension/pg_pinecone* "$(pg_config --sharedir)/extension/"
   ```

On Linux arm64, use the `linux-arm64` archive. If more than one Postgres version is installed, use the `pg_config` that belongs to the server you're installing into. On other platforms, including Debian 12, Ubuntu 22.04, RHEL 9, and older x86\_64 CPUs, [build from source](https://github.com/pinecone-io/pg_pinecone#readme).

**Docker**

The [`pineconeteam/pg_pinecone`](https://hub.docker.com/r/pineconeteam/pg_pinecone) image is the [`pgvector/pgvector`](https://hub.docker.com/r/pgvector/pgvector) image with pg\_pinecone added, so it includes Postgres and pgvector. It runs on x86\_64 and arm64 hosts. On x86\_64, it needs a CPU that supports x86-64-v3, like the Linux x86\_64 release archive.

1. Pull the image. The image includes its own Postgres, so you don't need to match a server you already have. This command uses PostgreSQL 17, the more widely used of the two supported versions. For PostgreSQL 18, use the `0.11.0-pg18` tag here and in the next step instead:

   ```bash theme={null}
   docker pull pineconeteam/pg_pinecone:0.11.0-pg17
   ```

2. Start a container from the image:

   ```bash theme={null}
   docker run -d --name pg_pinecone \
     -e POSTGRES_PASSWORD=secret \
     pineconeteam/pg_pinecone:0.11.0-pg17 \
     -c shared_preload_libraries=pg_pinecone
   ```

   The `shared_preload_libraries` setting isn't needed for this quickstart, but the `remote` engine and full-text search need it, and setting it now saves a restart later.

## 2. Connect and create the extensions

1. Connect to your database as a superuser with `psql`:

   ```bash Linux theme={null}
   sudo -u postgres psql
   ```

   ```bash macOS theme={null}
   psql postgres
   ```

   ```bash Docker theme={null}
   docker exec -it pg_pinecone psql -U postgres
   ```

   On Linux, the `postgres` system user is the superuser that the package creates. With Homebrew on macOS, your own user is the superuser. In the Docker image, the superuser is `postgres`. To connect to a different database or a remote server, add `-d your_database`, `-h your_host`, and `-U your_superuser`.

2. Create the extensions. Create pgvector first, because pg\_pinecone builds on its `vector` type and operators:

   ```sql SQL theme={null}
   CREATE EXTENSION vector;
   CREATE EXTENSION pg_pinecone;
   ```

## 3. Add sample data

**Your own vectors**

1. Create the table. These vectors have three dimensions:

   ```sql SQL theme={null}
   CREATE TABLE docs (
       id        bigint PRIMARY KEY,
       body      text,
       embedding vector(3)
   );
   ```

2. Insert a few short documents with their vectors. In a real application, you'd generate the vectors with an embedding model of your choice. To skip that step here, each document gets a hand-made vector whose values stand for food, nature, and places:

   ```sql SQL theme={null}
   INSERT INTO docs (id, body, embedding) VALUES
       (1, 'The Eiffel Tower was completed in 1889 for the World''s Fair in Paris.', '[0.1, 0.1, 0.9]'),
       (2, 'Photosynthesis converts sunlight, water, and carbon dioxide into glucose.', '[0.05, 0.9, 0.1]'),
       (3, 'The Great Barrier Reef is the largest coral reef system in the world.', '[0.1, 0.8, 0.3]'),
       (4, 'Espresso is brewed by forcing hot water through finely ground coffee.', '[0.95, 0.05, 0.05]'),
       (5, 'Mount Everest sits on the border between Nepal and China.', '[0.05, 0.4, 0.8]'),
       (6, 'Honeybees communicate the location of flowers with a waggle dance.', '[0.2, 0.85, 0.05]'),
       (7, 'A croissant is a flaky pastry made from laminated, buttered dough.', '[0.95, 0.05, 0.1]'),
       (8, 'The Amazon rainforest produces a large share of the world''s oxygen.', '[0.05, 0.9, 0.3]');
   ```

**Pinecone embeddings**

1. Store your Pinecone API key so the extension can generate embeddings. The key is stored in the `pinecone.secret` table, which only superusers can read by default:

   ```sql SQL theme={null}
   SELECT pinecone.set_api_key('YOUR_API_KEY');
   ```

2. Create the table. The [`multilingual-e5-large`](/models/multilingual-e5-large) model that `pinecone.embed_batch()` uses by default produces 1024-dimensional vectors:

   ```sql SQL theme={null}
   CREATE TABLE docs (
       id        bigint PRIMARY KEY,
       body      text,
       embedding vector(1024)
   );
   ```

3. Insert a few short documents and generate their embeddings in the same statement:

   ```sql SQL theme={null}
   WITH input(body) AS (
       VALUES
           ('The Eiffel Tower was completed in 1889 for the World''s Fair in Paris.'),
           ('Photosynthesis converts sunlight, water, and carbon dioxide into glucose.'),
           ('The Great Barrier Reef is the largest coral reef system in the world.'),
           ('Espresso is brewed by forcing hot water through finely ground coffee.'),
           ('Mount Everest sits on the border between Nepal and China.'),
           ('Honeybees communicate the location of flowers with a waggle dance.'),
           ('A croissant is a flaky pastry made from laminated, buttered dough.'),
           ('The Amazon rainforest produces a large share of the world''s oxygen.')
   ),
   numbered AS (
       SELECT row_number() OVER () AS ordinal, body FROM input
   )
   INSERT INTO docs (id, body, embedding)
   SELECT n.ordinal, n.body, e.embedding::vector
   FROM numbered n
   JOIN pinecone.embed_batch((SELECT array_agg(body ORDER BY ordinal) FROM numbered)) e
     ON e.ordinal = n.ordinal;
   ```

## 4. Search inside Postgres

### 1. Create a native index

Create a `native` index on the vector column. `native` is the default engine, so `engine => 'native'` is optional:

```sql SQL theme={null}
SELECT pinecone.create_index('docs', 'embedding', engine => 'native');
```

With Pinecone embeddings, `pinecone.create_index()` prints an informational message, labeled `NOTICE`, that suggests `SET STORAGE PLAIN` on the vector column, which speeds up searches on large tables. You can ignore it for this sample.

### 2. Run a search

Search with an ordinary pgvector query, the same query you'd run without pg\_pinecone. `<=>` is pgvector's cosine distance operator:

**Your own vectors**

Query with `[1, 0, 0]`, a vector that points entirely toward food, with no nature or places:

```sql SQL theme={null}
SET enable_seqscan = off;

SELECT id, body
FROM docs
ORDER BY embedding <=> '[1, 0, 0]'
LIMIT 2;
```

The two closest documents are the two about food:

```text Output theme={null}
 id |                                 body
----+-----------------------------------------------------------------------
  4 | Espresso is brewed by forcing hot water through finely ground coffee.
  7 | A croissant is a flaky pastry made from laminated, buttered dough.
```

**Pinecone embeddings**

Query with a question, which `pinecone.embed()` turns into a vector:

```sql SQL theme={null}
SET enable_seqscan = off;

SELECT id, body
FROM docs
ORDER BY embedding <=> (SELECT pinecone.embed('What should I order for breakfast at a cafe?')::vector)
LIMIT 2;
```

`::vector` converts the embedding to pgvector's `vector` type. The subquery embeds the question once, before the search, so Postgres can use the index. If you call `pinecone.embed()` directly in `ORDER BY`, Postgres reads every row instead.

The two closest documents are about espresso and croissants, even though neither one mentions breakfast or a cafe:

```text Output theme={null}
 id |                                 body
----+-----------------------------------------------------------------------
  4 | Espresso is brewed by forcing hot water through finely ground coffee.
  7 | A croissant is a flaky pastry made from laminated, buttered dough.
```

> [!NOTE]
>
> `SET enable_seqscan = off` makes Postgres use the index on this eight-row table. On a table this small, the planner would otherwise read every row directly, because that's cheaper than using any index. Once a table is large enough that reading every row costs more, the planner chooses the index on its own, and you don't need this setting. It lasts until you disconnect.

### 3. Check which index served the query

`EXPLAIN` shows the plan Postgres uses to run a query, including which index it reads. To confirm the `native` index served the search, check the plan:

```sql SQL theme={null}
SET enable_seqscan = off;

EXPLAIN (COSTS OFF)
SELECT id
FROM docs
ORDER BY embedding <=> (SELECT embedding FROM docs WHERE id = 4)
LIMIT 2;
```

The plan includes `Index Scan using docs_embedding_pinecone_idx`, the `native` index you created in step 4.1. If Postgres read every row instead, the plan would show `Seq Scan`.

## 5. Clean up

If you don't need the sample table anymore, delete it. `DROP TABLE` permanently deletes the table, its rows, and its indexes, including the `native` index. To try [switching from native to remote](/guides/pg-pinecone/switch-to-remote) next, skip this step, because that guide uses the same table.

```sql SQL theme={null}
DROP TABLE docs;
```

## Next steps

* [Choose a storage engine](/guides/pg-pinecone/storage-engines) for your workload.
* [Switch from pgvector to native](/guides/pg-pinecone/switch-from-pgvector) on an existing table.
* [Switch from native to remote](/guides/pg-pinecone/switch-to-remote) when a table outgrows one server.
* [Search a table with full-text search](/guides/pg-pinecone/full-text-search).
