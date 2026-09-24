---
title: "db destroy"
source: https://docs.turso.tech/cli/db/destroy
path: cli/db/destroy
---

You can destroy a database by using the following command:

```bash theme={null}
turso db destroy <database-name> [flags]
```

<Note>
  On paid plans, a destroyed database can be restored for up to five days — see [Recover Deleted Databases](/features/recover-deleted-databases).
</Note>

## Flags

| Flag          | Description                            |
| ------------- | -------------------------------------- |
| `-y`, `--yes` | Confirms the destruction the database. |
