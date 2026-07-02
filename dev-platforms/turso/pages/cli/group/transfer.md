---
title: "group transfer"
source: https://docs.turso.tech/cli/group/transfer
path: cli/group/transfer
---

You can transfer a group (including its databases) to an organization you're an admin or owner of using the following command:

```bash theme={null}
turso group transfer <group-name> <organization-name> [flags]
```

<Warning>
  Existing database URL and tokens will continue to work, but should update your application to use the new URL and token as soon as possible.
</Warning>

## Flags

| Flag          | Description                                  |
| ------------- | -------------------------------------------- |
| `-y`, `--yes` | Confirms the transfer to a new organization. |
