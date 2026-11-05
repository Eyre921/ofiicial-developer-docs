---
title: "auth token"
source: https://docs.turso.tech/cli/auth/token
path: cli/auth/token
---

You can obtain your current API token that is used to authenticate with the Turso Platform API by running the following command:

```bash theme={null}
turso auth token
```

> [!NOTE]
>
> This login token also comes from `turso auth login --headless`.
> It is not a named API token, so [`api-tokens list`](/cli/auth/api-tokens/list) does not list it.
> The [`api-tokens revoke`](/cli/auth/api-tokens/revoke) command does not revoke it.
