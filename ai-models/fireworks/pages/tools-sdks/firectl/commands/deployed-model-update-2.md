---
title: "firectl deployed-model update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployed-model-update
path: tools-sdks/firectl/commands/deployed-model-update
---

Update a deployed model.

```
firectl deployed-model update [flags]
```

### Examples

```
firectl deployed-model update my-deployed-model
firectl deployed-model update accounts/my-account/deployedModels/my-deployed-model
```

### Flags

```
      --default #<deployment>   If true, this is the default deployment when querying this model without the #<deployment> suffix.
      --description string      Description of the deployed model. Must be fewer than 1000 characters long.
      --display-name string     Human-readable name of the deployed model. Must be fewer than 64 characters long.
      --dry-run                 Print the request proto without running it.
  -h, --help                    help for update
  -o, --output Output           Set the output format to "text", "json", or "flag". (default text)
      --public                  If true, the deployed model will be publicly reachable.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
