---
title: "Partial sync"
source: https://docs.turso.tech/sync/partial
path: sync/partial
---

Sync only what you need. Faster cold starts and lower bandwidth by lazily fetching database pages on demand.

<Note>
  This particular usage uses the Turso Cloud to sync the local Turso databases and assumes that you have an account.
</Note>

Partial sync lets your app open and use a database without downloading the entire file.
The client lazily fetches pages of the database file from the Turso Cloud when a query touches data that is not present locally.
This reduces startup time and network usage for large databases, while remaining fully compatible with the push/pull methods used
by Turso's standard `sync` solution.

<Note>
  * Reads on not-yet-downloaded data transparently trigger on-demand page fetches.
  * Writes still apply locally first and are pushed as logical statements.
</Note>

## Modes

Two bootstrap strategies define what is present locally at connect time:

* **Prefix bootstrap**: download the first N bytes of the database file.
  * Good default when you want a minimal, predictable starting footprint.
* **Query bootstrap**: download pages touched by running a server-side SQL query.
  * Ideal to hydrate only a narrow working set (e.g., a single user's rows, small tables with metadata, references, etc).

Both modes continue to lazily fetch missing pages on demand.

### Prefix bootstrap

<CodeGroup>
  ```ts TypeScript theme={null}
  import { connect } from '@tursodatabase/sync';

  const db = await connect({
    path: './app.db',
    url: 'turso://...',
    authToken: process.env.TURSO_AUTH_TOKEN,
    partialSyncExperimental: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
    },
  });
  ```

  ```py Python theme={null}
  import os
  import turso.sync

  conn = turso.sync.connect(
      path="./app.db",
      remote_url="turso://...",
      auth_token=os.environ["TURSO_AUTH_TOKEN"],
      partial_sync_experimental=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
      ),
  )
  ```

  ```go Go theme={null}
  import (
  	turso "turso.tech/database/tursogo"
  )

  db, err := turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    Path:      "./app.db",
    RemoteUrl: "turso://...",
    AuthToken: os.Getenv("TURSO_AUTH_TOKEN"),
    PartialSyncExperimental: turso.TursoPartialSyncConfig{
      BootstrapStrategyPrefix: 128 * 1024, // 128 KiB
    },
  })
  ```
</CodeGroup>

### Query bootstrap

<CodeGroup>
  ```ts TypeScript theme={null}
  import { connect } from '@tursodatabase/sync';

  const db = await connect({
    path: './app.db',
    url: 'turso://...',
    authToken: process.env.TURSO_AUTH_TOKEN,
    partialSyncExperimental: {
      bootstrapStrategy: {
        kind: 'query',
        query: `SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100`,
      },
    },
  });
  ```

  ```py Python theme={null}
  import turso.sync

  conn = turso.sync.connect(
      path=":memory:",
      remote_url="turso://...",
      partial_sync_experimental=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncQueryBootstrap(
              query="SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100"
          ),
      ),
  )
  ```

  ```go Go theme={null}
  import (
  	turso "turso.tech/database/tursogo"
  )

  db, err := turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    Path:      "./app.db",
    RemoteUrl: "turso://...",
    AuthToken: os.Getenv("TURSO_AUTH_TOKEN"),
    PartialSyncExperimental: turso.TursoPartialSyncConfig{
      BootstrapStrategyQuery: "SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100",
    },
  })
  ```
</CodeGroup>

## Optimizations

### Segment size (batched lazy reads)

<Frame>
  <div>
    <svg>
      <defs>
        <marker>
          <polygon />
        </marker>
      </defs>

      <g>
        <text>select page</text>

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>
      </g>

      <g>
        <line />

        <text>read(7)</text>
      </g>

      <g>
        <text>fetching segment</text>

        <rect />

        <rect />

        <rect />

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>
        <text>segment 5-8</text>
      </g>

      <g>
        <line />
      </g>

      <g>
        <text>segment cached</text>

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>
      </g>
    </svg>

    <p>
      Read page 7 → fetch segment 5-8 (3 new pages)
    </p>
  </div>
</Frame>

When the client needs a page that isn’t present locally, partial sync performs an on-demand fetch from the remote database.

To reduce round-trips and speed up these fetches, you can configure the **segment size**: instead of requesting a single page, the client downloads a whole *segment* of pages in one request.

This lets the client amortize network overhead and hydrate nearby pages that are likely to be accessed soon.

**How it works**

Suppose your database has:

* `page_size = 4 KiB`
* `segment_size = 16 KiB`

If a local query touches page **6**, the client computes the segment that page belongs to:

* 16 KiB segment = 4 pages
* Segment covering page 6 = pages **5-8**

The client then fetches all four pages in a single request and stores them locally.
Future reads to those pages incur no additional network cost.

**Benefits**

* Fewer HTTP requests (one segment fetch vs. many single-page fetches)
* Faster hydration of hot ranges
* Better performance for workloads with spatial locality (e.g., range scans, index lookups)

**Default**

The default `segment_size` is **128 KiB** (typically 32 pages on a 4 KiB page size), which provides a good balance between request overhead and total bytes transferred.

<Tip>
  If your workload touches data in tight clusters (e.g., reading several adjacent rows), larger segment sizes can significantly improve performance.

  Conversely, very sparse/random-access workloads may benefit from smaller segment sizes.
</Tip>

<CodeGroup>
  ```ts TypeScript theme={null}
  await connect({
    ...
    partialSyncExperimental: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
      segmentSize: 16 * 1024,
    },
  });
  ```

  ```py Python theme={null}
  turso.sync.connect(
      ...
      partial_sync_experimental=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
          segment_size=16 * 1024,
      ),
  )
  ```

  ```go Go theme={null}
  turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    ...
    PartialSyncExperimental: turso.TursoPartialSyncConfig{
      BootstrapStrategyPrefix: 128 * 1024, // 128 KiB
      SegmentSize: 16 * 1024,
    },
  })
  ```
</CodeGroup>

### Prefetch

<Frame>
  <div>
    <svg>
      <defs>
        <marker>
          <polygon />
        </marker>

        <marker>
          <polygon />
        </marker>
      </defs>

      <g>
        <text>select page</text>

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>

        <g />
      </g>

      <g>
        <line />

        <text>read(4)</text>
      </g>

      <g>
        <text>fetching</text>

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>
      </g>

      <g>
        <line />
      </g>

      <g>
        <text>loaded</text>

        <g><rect /><text>1</text></g>
        <g><rect /><text>2</text></g>
        <g><rect /><text>3</text></g>
        <g><rect /><text>4</text></g>

        <g><rect /><text>5</text></g>
        <g><rect /><text>6</text></g>
        <g><rect /><text>7</text></g>
        <g><rect /><text>8</text></g>

        <g><rect /><text>9</text></g>
        <g><rect /><text>10</text></g>
        <g><rect /><text>11</text></g>
        <g><rect /><text>12</text></g>
      </g>
    </svg>

    <p>
      Read page 4 → prefetch 2 child pages (11, 12)
    </p>
  </div>
</Frame>

Prefetch is an optional optimization that builds on top of lazy page fetches.
When enabled, the client not only retrieves the pages required by the current query, but also **inspects the structure of the newly downloaded pages and recent access patterns** to predict which pages are likely to be needed next.

If the client detects a natural continuation of the access pattern — such as child pages referenced by an internal B-tree node — it proactively downloads those pages in advance.
This reduces the number of future on-demand fetches and helps avoid stalls during operations like range scans, index walks, or sequential lookups.

<CodeGroup>
  ```ts TypeScript theme={null}
  await connect({
    ...
    partialSyncExperimental: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
      prefetch: true,
    },
  });
  ```

  ```py Python theme={null}
  turso.sync.connect(
      ...
      partial_sync_experimental=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
          prefetch=True,
      ),
  )
  ```

  ```go Go theme={null}
  turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    ...
    PartialSyncExperimental: turso.TursoPartialSyncConfig{
      BootstrapStrategyPrefix: 128 * 1024, // 128 KiB
      Prefetch: true,
    },
  })
  ```
</CodeGroup>

<Note>
  `segment_size` and `prefetch` are complementary.

  Segment size batches nearby pages into a single on-demand fetch, while prefetch looks at the query's access pattern and proactively fetches additional pages likely to be needed next.

  Using both together can provide the best performance for real-world workloads.
</Note>
