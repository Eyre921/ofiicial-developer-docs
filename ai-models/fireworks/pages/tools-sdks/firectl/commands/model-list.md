---
title: "firectl model list"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-list
path: tools-sdks/firectl/commands/model-list
---

Prints all models in an account.

```
firectl model list [flags]
```

### Examples

```
# List all models
firectl model list

# Search by name (partial match)
firectl model list --search deepseek

# Filter by kind
firectl model list --kind HF_PEFT_ADDON

# Filter by state
firectl model list --state READY

# Combine filters
firectl model list --search deepseek --kind HF_PEFT_ADDON

# Use raw filter for advanced queries
firectl model list --filter 'create_time > timestamp("2025-01-01T00:00:00Z")'
```

### Flags

```
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
  -h, --help                help for list
      --kind string         Filter by model kind (e.g., HF_PEFT_ADDON, HF_BASE_MODEL, DRAFT_ADDON)
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
  -o, --output string       Set the output format to "text" or "json". (default "text")
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
      --search string       Filter models by name (searches both model_id and display_name)
      --state string        Filter by state (e.g., READY, UPLOADING)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
