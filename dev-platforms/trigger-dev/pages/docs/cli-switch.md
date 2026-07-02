---
title: "CLI switch command"
source: https://trigger.dev/docs/cli-switch
path: docs/cli-switch
---

The `trigger.dev switch` command can be used to switch between profiles.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest switch [profile]
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest switch [profile]
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest switch [profile]
  ```
</CodeGroup>

It will switch to the specified profile. If no profile is specified, it will list all available profiles and run interactively.

## Arguments

```
npx trigger.dev@latest switch [profile]
```

<ParamField type="[profile]">
  The profile to switch to. If not specified, it will list all available profiles and run interactively.
</ParamField>
