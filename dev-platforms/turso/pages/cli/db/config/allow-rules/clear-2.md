---
title: "db config allow-rules clear"
source: https://docs.turso.tech/cli/db/config/allow-rules/clear
path: cli/db/config/allow-rules/clear
---

Clear the access allow rules for a database, allowing connections from any source.

```bash theme={null}
turso db config allow-rules clear <database-name> [flags]
```

Without any flags, both the IP list and the AWS VPC endpoint list are cleared. Use `--ips` or `--aws-vpcs` to clear only one list.

## Flags

| Flag         | Description                                          |
| ------------ | ---------------------------------------------------- |
| `--ips`      | Clear only the list of allowed IPs.                  |
| `--aws-vpcs` | Clear only the list of allowed AWS VPC endpoint IDs. |

## Examples

### Clear all rules

```bash theme={null}
turso db config allow-rules clear my-db
```

### Clear only the IP list

```bash theme={null}
turso db config allow-rules clear my-db --ips
```

### Clear only the VPC list

```bash theme={null}
turso db config allow-rules clear my-db --aws-vpcs
```
