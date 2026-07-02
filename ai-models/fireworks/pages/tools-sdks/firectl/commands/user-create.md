---
title: "firectl user create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-create
path: tools-sdks/firectl/commands/user-create
---

Creates a new user.

```
firectl user create [flags]
```

### Examples

```
firectl user create --email="alice.cullen@gmail.com"
firectl user create --service-account --user-id="my-bot"
firectl user create --service-account --user-id="my-agent" --permission-preset=agent
```

### Flags

```
      --display-name string        The display name of the user.
      --dry-run                    Print the request proto without running it.
      --email string               The email address of the user (not required for service accounts).
  -h, --help                       help for create
  -o, --output Output              Set the output format to "text", "json", or "flag". (default text)
      --permission-preset string   Permission preset for the service account. Automatically sets role to "custom".
      --role string                The user's role, must be one of "user", "admin", "contributor", "inference-user", or "custom". (default "user")
      --service-account            Admin only: Create as a service account (email will be auto-generated)
      --user-id string             The ID of the user (required for service accounts).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
