---
title: "group create"
source: https://docs.turso.tech/cli/group/create
path: cli/group/create
---

You can create a new group of databases. Groups belong to a primary region.

```bash theme={null}
turso group create <group-name> [flags]
```

> [!WARNING]
>
> Creating more than one group is limited to Scaler, Pro and Enterprise plans.

> [!NOTE]
>
> Turso will automatically detect the closest region and use that as the primary region. You can override this by specifying the `--location` flag.

## Flags

| Flag | Description |
| - | - |
| `--canary` | Use database canary build. |
| `--location` | Create the group in the specified primary location using a three-digit code. |
| `-w`, `--wait` | Wait for group to be ready before exiting. |
