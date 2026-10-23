---
title: "CLI projects commands"
source: https://trigger.dev/docs/cli-projects-commands
path: docs/cli-projects-commands
---

List, create, inspect, and rename Trigger.dev projects from the terminal.

These commands act on the organizations and projects your account can access, so run
[`login`](/docs/cli-login-commands) first.

## projects create

Creates a project. You are prompted for the organization and name when the options are omitted.

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest projects create
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest projects create
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest projects create
```

**Organization** `--org | -o`

The organization slug or ID to create the project in.

**Name** `--name | -n`

The name of the new project.

## projects list

Lists your projects with the runtime and version of their current Production deployment.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest projects list
```

**Needs update** `--needs-update`

Only show projects using Node.js 21 in Production.

## projects get

Prints the name, ref, slug, organization, default runtime and region of a project.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest projects get proj_abc123
```

## projects rename

Renames a project. The project ref does not change.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest projects rename proj_abc123 "My new name"
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
