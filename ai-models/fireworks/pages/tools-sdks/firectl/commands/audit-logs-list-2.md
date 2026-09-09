---
title: "firectl audit-logs list"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/audit-logs-list
path: tools-sdks/firectl/commands/audit-logs-list
---

Lists audit logs for the signed in user.

### Usage

Lists audit logs for the signed in user with filtering support.

```
firectl audit-logs list [flags]
```

### Examples

```
# List all audit logs from the past 30 days
firectl audit-logs list

# Filter by resource (exact or substring match)
firectl audit-logs list --filter 'resource="accounts/my-account/deployments/abc123"'
firectl audit-logs list --filter 'resource="accounts/my-account/models/model123"'
firectl audit-logs list --filter 'resource:model123"'

# Filter by message (exact or substring match)
firectl audit-logs list --filter 'message="CreateDeployment"'
firectl audit-logs list --filter 'message:"Create"'

# Filter by user email
firectl audit-logs list --filter 'email="user@example.com"'

# List logs from a specific date range with filters
firectl audit-logs list --start 2025-01-01 --end 2025-01-02

# Combine multiple filters
firectl audit-logs list --start 2025-01-01 --filter 'resource:"deployment-id"'
```

### Flags

```
      --end string          The end date for audit logs in YYYY-MM-DD format
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
  -h, --help                help for list
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
  -o, --output string       Set the output format to "text" or "json". (default "text")
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
      --start string        The start date for audit logs in YYYY-MM-DD format. If unspecified, the default is 30 days before now.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
