---
title: "group tokens create"
source: https://docs.turso.tech/cli/group/tokens/create
path: cli/group/tokens/create
---

You can create a new token that can be used to connect to any database in the group using the command:

```bash theme={null}
turso group tokens create <group-name> [flags]
```

## Flags

| Flag                 | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| `-e`, `--expiration` | The expiration time for a token, can be `never` or a value in days, e.g. `7d` . |
| `-r`, `--read-only`  | Restrict the token to read only access.                                         |

## Examples

The examples below outline the most common use cases for the `group tokens create` command.

### Create a token with read only access

You can create a token with read only access using the command:

```bash theme={null}
turso group tokens create <group-name> --read-only
```

### Create a token with a specific expiration time

You can create a token with a specific expiration time using the command:

```bash theme={null}
turso group tokens create <group-name> --expiration 7d
```
