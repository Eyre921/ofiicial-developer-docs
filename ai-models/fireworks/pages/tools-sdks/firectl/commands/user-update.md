---
title: "firectl user update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-update
path: tools-sdks/firectl/commands/user-update
---

Updates a user.

```
firectl user update [flags]
```

### Examples

```
firectl user update my-user --display-name="Alice Cullen"
firectl user update accounts/my-account/users/my-user --display-name="Alice Cullen"
firectl user update my-agent --permission-preset=agent
```

### Flags

```
      --display-name string        The display name of the user.
      --dry-run                    Print the request proto without running it.
  -h, --help                       help for update
  -o, --output Output              Set the output format to "text", "json", or "flag". (default text)
      --permission-preset string   Permission preset for the service account. Automatically sets role to "custom".
      --role string                The role of the user. Must be one of {user, admin, contributor, inference-user, custom}.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
