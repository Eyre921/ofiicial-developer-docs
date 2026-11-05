---
title: "firectl api-key create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/api-key-create
path: tools-sdks/firectl/commands/api-key-create
---

Creates an API key for the signed in user or a specified service account user.

```
firectl api-key create [flags]
```

> [!NOTE]
>
> API keys have a maximum expiration of 1 year (365 days). If you omit `--expire-time`, the key expires 1 year after creation. An `--expire-time` more than 365 days in the future is rejected.

### Examples

```
firectl api-key create
firectl api-key create --service-account=my-service-account
firectl api-key create --key-name="Production Key" --service-account=ci-bot
firectl api-key create --key-name="Temporary Key" --expire-time="2027-06-30 23:59:59"
```

### Flags

```
      --dry-run                  Print the request proto without running it.
      --expire-time string       The time at which the API key will automatically expire, in YYYY-MM-DD[ HH:MM:SS] format. Must be within 1 year (365 days); later values are rejected. Defaults to 1 year from creation.
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
