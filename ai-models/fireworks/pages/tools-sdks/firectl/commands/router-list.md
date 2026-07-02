---
title: "firectl router list"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-list
path: tools-sdks/firectl/commands/router-list
---

Prints all routers in the account.

```
firectl router list [flags]
```

### Examples

```
firectl router list
```

### Flags

```
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
  -h, --help                help for list
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
  -o, --output string       Set the output format to "text" or "json". (default "text")
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
