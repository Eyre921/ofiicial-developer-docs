---
title: "db tokens invalidate"
source: https://docs.turso.tech/cli/db/tokens/invalidate
path: cli/db/tokens/invalidate
---

You can invalidate all tokens for a database by running the following command:

```bash theme={null}
turso db tokens invalidate <database-name> [flags]
```

## Flags

| Flag          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `-y`, `--yes` | Confirms the invalidation of all existing db tokens. |

<Warning>
  All tokens in the group that provided database belongs will also be invalidated. This means that all existing tokens will no longer be valid and will need to be regenerated.
</Warning>
