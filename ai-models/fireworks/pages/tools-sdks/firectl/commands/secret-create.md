---
title: "firectl secret create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/secret-create
path: tools-sdks/firectl/commands/secret-create
---

Creates a secret for the signed in user.

```
firectl secret create [flags]
```

### Examples

```
firectl secret create --name MY_SECRET --value mysecretvalue
firectl secret create --name AWS_CREDS --from-file aws-credentials.json
firectl secret create --name AWS_CREDS --aws-access-key-id AKIA... --aws-secret-access-key ...
```

### Flags

```
      --aws-access-key-id string       AWS access key ID (automatically formats as JSON with --aws-secret-access-key)
      --aws-secret-access-key string   AWS secret access key (automatically formats as JSON with --aws-access-key-id)
      --dry-run                        Print the request proto without running it.
      --from-file string               Path to a file containing the secret value
  -h, --help                           help for create
      --name string                    The name of the secret to be created
  -o, --output Output                  Set the output format to "text", "json", or "flag". (default text)
      --value string                   The value of the secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
