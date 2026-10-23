---
title: "CLI logout command"
source: https://trigger.dev/docs/cli-logout-commands
path: docs/cli-logout-commands
---

Use these options when using the `logout` CLI command.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest logout
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest logout
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest logout
```

## Options

### Common options

These options are available on most commands.

**Login profile** `--profile`

The login profile to use. Defaults to the current profile, which is set by your last `login` or `switch` (initially "default").

**API URL** `--api-url | -a`

Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.

**Log level** `--log-level | -l`

The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.

**Skip telemetry** `--skip-telemetry`

Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.

**Help** `--help | -h`

Shows the help information for the command.

**Version** `--version | -v`

Displays the version number of the CLI.
