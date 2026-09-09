---
title: "Authentication"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/authentication
path: tools-sdks/firectl/commands/authentication
---

Authentication for access to your account

### Signing in

Users using Google SSO can run:

```
firectl signin
```

If you are using [custom SSO](/accounts/sso), also specify the account ID:

```
firectl signin my-enterprise-account
```

### Authenticate with API Key

To authenticate with an API key, append `--api-key` to any firectl command.

```
firectl --api-key API_KEY <command>
```

To persist the API key for all subsequent commands, run:

```
firectl set-api-key API_KEY
```
