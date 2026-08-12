---
title: "Netlify Database: Migrations"
source: https://docs.netlify.com/build/data-and-storage/netlify-database/migrations.md
path: build/data-and-storage/netlify-database/migrations
---

---
title: "Migrations"
description: "How Netlify Database tracks and applies schema migrations across production deploys and deploy previews, including manual migration workflows."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Migrations are a way to manage and version changes to your database schema. To ensure that the state of the database matches the exact shape that your application expects, you can define that shape in code and co-locate it with the rest of the application.

This is a crucial but often dreaded aspect of operating a database, because a defective migration has the potential to take down your entire application and even cause permanent data loss.

To help with this, Netlify Database offers a built-in database migration system that automatically tracks and applies migrations for you at the right point in your development cycle.

## Writing migrations

Migrations are defined in a `netlify/database/migrations` directory in your project. There are two supported formats:

- **SQL files**: each migration is a single SQL file in the migrations directory

    ```text
    netlify/database/migrations/
    ├── 20260301143000_create_users.sql
    ├── 20260318091500_add_posts.sql
    └── 20260425103000_create_comments.sql
    ```

- **Subdirectories**: each migration lives in its own subdirectory containing a `migration.sql` file

    ```text
    netlify/database/migrations/
    ├── 20260301143000_create_users/
    │   └── migration.sql
    ├── 20260318091500_add_posts/
    │   └── migration.sql
    └── 20260425103000_create_comments/
        └── migration.sql
    ```

In both cases, the naming pattern must match `<number>_<slug>`, where:

- `number` is any sequence of digits that defines the relative order of migrations; this is typically a sequential number (e.g. `0001`, `0002`, etc.) or a Unix timestamp
- `slug` is a string containing only lowercase letters, numbers, hyphens, and underscores, typically used to describe the purpose of the migration

Note that migrations are sorted lexicographically and applied in order, which means using Unix timestamps ensures they run in the order they were created.

## Applying migrations

Netlify will automatically apply your migrations at the right point in the deploy lifecycle:

- On **[production deploys](/deploy/deploy-types/production-deploy/)**, migrations are applied immediately before the deploy is [published](/deploy/deploy-overview/); a failure when applying the migration will block the deploy from being published
- On **[deploy previews](/deploy/deploy-types/deploy-previews/)**, migrations are applied on every new deploy, immediately before it becomes available; a failure when applying the migration will fail the deploy

### Example

Imagine your application has a `users` and `posts` table, which you had previously defined in the `20260301143000_create_users` and `20260318091500_add_posts` migrations, respectively. 

Now you want to create a table for comments, so you add `20260425103000_create_comments.sql`.

```text ins={4}
netlify/database/migrations/
├── 20260301143000_create_users.sql
├── 20260318091500_add_posts.sql
└── 20260425103000_create_comments.sql
```

The new migration file describes the full schema of the new table.

```sql title="netlify/database/migrations/20260425103000_create_comments.sql"
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  post_id INTEGER NOT NULL REFERENCES posts(id),
  author_id INTEGER NOT NULL REFERENCES users(id),
  body TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

When you open a pull request with this change, Netlify creates a deploy preview and immediately applies the migration to the preview's database branch. You can verify that the new table works with your application code, test queries against it, and confirm that nothing is broken - all on an isolated copy of your production data.

Once you merge the pull request and a new production deploy is created, one of two things will happen:

- If [auto publishing](/deploy/deploy-overview/#definitions) is enabled, the migration is applied and, if successful, the new deploy is published
- If not, we'll wait for you to manually publish the new deploy before we apply the migration

## Manual migrations

Netlify Database's native migration system has been designed to offer a seamless integration with the Netlify platform, handling all the complexity of applying migrations at the right time so you can focus on building.

While it is the recommended solution for handling migrations, it is completely optional. You have full access to the [database connection details](/build/data-and-storage/netlify-database/tooling/#database-drivers), so you can choose to use your own system for managing and applying migrations.

If you do that, there are some things you should keep in mind:

- If you want to test a migration on a deploy preview, you are responsible for applying it to the deploy preview's [database branch](/build/data-and-storage/netlify-database/#database-branches); you can do this as part of your build command
- You are responsible for applying migrations to the production database; there is currently no platform hook that lets you run arbitrary logic when a deploy is published, so we recommend an out-of-band process that applies a backwards-compatible migration before you publish the deploy

### Caution - Automatic migration detection

Migrations are applied automatically if placed in the `netlify/database/migrations` directory. If you want to use your own migrations system, choose a different directory to avoid conflicts.

## Best practices

Because Netlify Database applies migrations at the right point in the deploy lifecycle - just before the new version of your code goes live - the risk of drift between your application code and your database schema is heavily reduced. The window during which the old code is running against the new schema is minimized as much as possible.

Still, as a good practice, we recommend that you always write backwards-compatible migrations. A migration that introduces a breaking change, such as renaming or dropping a column, can cause errors during the brief transition between the old and new versions of your application.

For breaking changes, we recommend the [expand and contract pattern](https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html). Instead of modifying a structure in place, you:

1. **Expand**: Add the new structure (e.g. a new column) alongside the old one, writing to both
2. **Migrate**: Move existing data to the new structure
3. **Contract**: Once all application code has been updated to use the new structure, remove the old one in a subsequent migration

Non-breaking changes, such as adding a new table or a new nullable column, can safely be applied in a single migration.

