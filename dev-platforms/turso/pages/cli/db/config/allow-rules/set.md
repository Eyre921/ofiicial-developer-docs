---
title: "db config allow-rules set"
source: https://docs.turso.tech/cli/db/config/allow-rules/set
path: cli/db/config/allow-rules/set
---

Set the access allow rules for a database. Each flag replaces the corresponding list; a list whose flag is not provided is left unchanged.

```bash theme={null}
turso db config allow-rules set <database-name> [--ip <address-or-cidr>]... [--aws-vpc <vpce-id>]...
```

At least one of `--ip` or `--aws-vpc` must be provided. To remove restrictions use [`turso db config allow-rules clear`](/cli/db/config/allow-rules/clear).

## Flags

| Flag        | Description                                                                           |
| ----------- | ------------------------------------------------------------------------------------- |
| `--ip`      | IP address or CIDR block to allow. Repeatable. Replaces the current IP list.          |
| `--aws-vpc` | AWS VPC endpoint ID (`vpce-...`) to allow. Repeatable. Replaces the current VPC list. |

## Examples

### Allow a single IP

```bash theme={null}
turso db config allow-rules set my-db --ip 203.0.113.7
```

### Allow a CIDR range

```bash theme={null}
turso db config allow-rules set my-db --ip 10.0.0.0/8
```

### Allow multiple IPs

```bash theme={null}
turso db config allow-rules set my-db --ip 203.0.113.7 --ip 10.0.0.0/8
```

### Restrict to an AWS VPC endpoint

```bash theme={null}
turso db config allow-rules set my-db --aws-vpc vpce-0fe6c8807461bba49
```

### Combine IP and VPC rules

When both lists are set, connections must satisfy both constraints.

```bash theme={null}
turso db config allow-rules set my-db \
  --ip 10.0.0.0/8 \
  --aws-vpc vpce-0fe6c8807461bba49
```
