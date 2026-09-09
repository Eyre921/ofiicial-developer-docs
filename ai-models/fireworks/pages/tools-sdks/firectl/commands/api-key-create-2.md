---
title: "firectl api-key create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/api-key-create
path: tools-sdks/firectl/commands/api-key-create
---

Creates an API key for the signed in user or a specified service account user.

```
firectl api-key create [flags]
```

### Examples

```
firectl api-key create
firectl api-key create --service-account=my-service-account
firectl api-key create --key-name="Production Key" --service-account=ci-bot
firectl api-key create --key-name="Temporary Key" --expire-time="2025-12-31 23:59:59"
```

### Flags

```
      --dry-run                  Print the request proto without running it.
      --expire-time string       If specified, the time at which the API key will automatically expire. Specified in YYYY-MM-DD[ HH:MM:SS] format.
  -h, --help                     help for create
      --key-name string          The name of the key to be created. Defaults to "default"
  -o, --output Output            Set the output format to "text", "json", or "flag". (default text)
      --service-account string   Admin only: Create API key for the specified service account user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
