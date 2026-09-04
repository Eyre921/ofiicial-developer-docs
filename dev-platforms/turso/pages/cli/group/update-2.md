---
title: "group update"
source: https://docs.turso.tech/cli/group/update
path: cli/group/update
---

You can update the group, including all databases the following command:

```bash theme={null}
turso group update <group-name> [flags]
```

## Flags

| Flag                  | Description                                                                         |
| --------------------- | ----------------------------------------------------------------------------------- |
| `--extensions string` | Enable extensions by passing `all` or `none`.                                       |
| `--version string`    | Specify the version of the group to update to. Values include `latest` or `canary`. |
| `-y`, `--yes`         | Skip confirmation prompt and confirm.                                               |

## Examples

### Update a group to enable all extensions

You can update a group and all its databases to enable `all` extensions:

```bash theme={null}
turso group update <group-name> --extensions all
```
