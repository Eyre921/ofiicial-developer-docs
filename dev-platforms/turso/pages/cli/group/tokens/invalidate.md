---
title: "group tokens invalidate"
source: https://docs.turso.tech/cli/group/tokens/invalidate
path: cli/group/tokens/invalidate
---

You can invalidate all group tokens for a group by running the command:

```bash theme={null}
turso group tokens invalidate <group-name> [flags]
```

## Flags

| Flag | Description |
| - | - |
| `-y`, `--yes` | Confirms the invalidation of all existing group tokens. |

> [!NOTE]
>
> This rotates the group's credentials and invalidates group tokens. On AWS, database-scoped tokens (created with `turso db tokens create`) are not invalidated and keep working; to invalidate them, run [`turso db tokens invalidate`](/cli/db/tokens/invalidate) for each database.
