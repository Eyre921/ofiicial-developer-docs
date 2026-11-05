---
title: "auth api-tokens revoke"
source: https://docs.turso.tech/cli/auth/api-tokens/revoke
path: cli/auth/api-tokens/revoke
---

To revoke a named API token for the current organization, run the following command:

```bash theme={null}
turso auth api-tokens revoke <api-token-name>
```

> [!NOTE]
>
> This command does not revoke login tokens from `turso auth login --headless` or [`turso auth token`](/cli/auth/token).
> Login tokens do not appear in [`api-tokens list`](/cli/auth/api-tokens/list).
