---
title: "CLI promote command"
source: https://trigger.dev/docs/cli-promote-commands
path: docs/cli-promote-commands
---

Use the promote command to promote a previously deployed version to the current version.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest promote [version]
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest promote [version]
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest promote [version]
  ```
</CodeGroup>

## Arguments

```
npx trigger.dev@latest promote [version]
```

<ParamField type="[version]">
  The version to promote. This is the version that was previously deployed.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>
