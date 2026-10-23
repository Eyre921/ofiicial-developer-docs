---
title: "CLI update command"
source: https://trigger.dev/docs/cli-update-commands
path: docs/cli-update-commands
---

Use these options when using the `update` CLI command.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest update [path]
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest update [path]
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest update [path]
```

## Arguments

**Project path** `[path]`

The directory that contains the `package.json` file. Defaults to `.`.

## Options

### Common options

These options are available on most commands.

**Log level** `--log-level | -l`

The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.

**Skip telemetry** `--skip-telemetry`

Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.

**Help** `--help | -h`

Shows the help information for the command.

**Version** `--version | -v`

Displays the version number of the CLI.
