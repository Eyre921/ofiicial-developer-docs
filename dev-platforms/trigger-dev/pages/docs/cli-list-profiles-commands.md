---
title: "CLI list-profiles command"
source: https://trigger.dev/docs/cli-list-profiles-commands
path: docs/cli-list-profiles-commands
---

Use these options when using the `list-profiles` CLI command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest list-profiles
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest list-profiles
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest list-profiles
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

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
