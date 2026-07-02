---
title: "firectl billing notification-settings update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-notification-settings-update
path: tools-sdks/firectl/commands/billing-notification-settings-update
---

Update notification settings for an account.

```
firectl billing notification-settings update [flags]
```

### Examples

```
firectl billing notification-settings update --monthly-spend-usd-thresholds=500,800
firectl billing notification-settings update --monthly-spend-usd-thresholds=500 --monthly-spend-usd-thresholds=800
firectl billing notification-settings update --monthly-spend-usd-thresholds=""
```

### Flags

```
      --dry-run                                   Print the request proto without running it.
  -h, --help                                      help for update
      --monthly-spend-usd-thresholds int64Slice   Spend alert thresholds in whole USD (e.g., 500,800). Use "" to clear. (default [])
  -o, --output Output                             Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
