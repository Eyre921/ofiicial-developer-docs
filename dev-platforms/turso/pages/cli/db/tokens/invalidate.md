---
title: "db tokens invalidate"
source: https://docs.turso.tech/cli/db/tokens/invalidate
path: cli/db/tokens/invalidate
---

You can invalidate all database-scoped tokens for a single database by running the following command:

```bash theme={null}
turso db tokens invalidate <database-name> [flags]
```

## Flags

| Flag | Description |
| - | - |
| `-y`, `--yes` | Confirms the invalidation of all existing db tokens. |

> [!WARNING]
>
> On AWS, this only invalidates tokens created for this database (for example with `turso db tokens create`). Group tokens, and tokens for other databases in the same group, are not invalidated and keep working. Clients using the invalidated tokens will need new ones.
>
> To invalidate group tokens, use [`turso group tokens invalidate`](/cli/group/tokens/invalidate).
