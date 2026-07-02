---
title: "firectl user get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-get
path: tools-sdks/firectl/commands/user-get
---

Prints information about a user.

```
firectl user get [flags]
```

### Examples

```
firectl user get my-user
firectl user get accounts/my-account/users/my-user
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for get
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
