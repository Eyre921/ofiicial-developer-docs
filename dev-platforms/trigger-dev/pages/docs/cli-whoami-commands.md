---
title: "CLI whoami command"
source: https://trigger.dev/docs/cli-whoami-commands
path: docs/cli-whoami-commands
---

Use these options to display the current logged in user and project details.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest whoami
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest whoami
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest whoami
```

## Options

**Config file** `-c, --config \<config file\>`

The name of the config file.

**Project ref** `-p, --project-ref \<project ref\>`

The project ref. Overrides the project in the config file.

**Env file** `--env-file \<env file\>`

Path to a `.env` file to read `TRIGGER_PROJECT_REF` from. Defaults to `.env`, `.env.development`, `.env.local`, `.env.development.local` and `dev.vars` in the current directory.

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
