---
title: "db import"
source: https://docs.turso.tech/cli/db/import
path: cli/db/import
---

You can import an existing SQLite file to Turso Cloud using the following command:

```bash theme={null}
turso db import ~/path/to/database.db
```

> [!NOTE]
>
> Make sure the SQLite file has WAL journal mode enabled.

> [!NOTE]
>
> If you have more than one group, you will need to pass the `--group` flag.

## Flags

| Flag | Description |
| - | - |
| `--group` | Import the database in the specified group. |
| `-h`, `--help` | Get help for import. |
