---
title: "firectl quota update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/quota-update
path: tools-sdks/firectl/commands/quota-update
---

Updates a quota.

```
firectl quota update [flags]
```

### Examples

```
firectl quota update serverless-inference-rpm --value 300
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for update
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
      --value int       The quota allowed to be used by this account. Must be less than max_value.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
