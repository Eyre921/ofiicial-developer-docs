---
title: "CLI runs commands"
source: https://trigger.dev/docs/cli-runs-commands
path: docs/cli-runs-commands
---

Use these commands to list, inspect, replay and cancel runs from your terminal.

## runs list

Lists runs, newest first, in a table of ID, task, status, version, created time and duration.

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest runs list
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest runs list
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest runs list
```

**Limit** `--limit`

The number of runs to list, up to 100. Defaults to 20.

**Status** `--status`

Only show runs with this status, e.g. `FAILED`.

**Task** `--task`

Only show runs for this task identifier.

**Tag** `--tag`

Only show runs with this tag.

**Cursor** `--cursor`

The pagination cursor printed at the end of the previous page.

## runs get

Prints the status, version, tags, timings, duration, cost and error of a single run.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest runs get run_abc123
```

## runs replay

Triggers a new run with the same payload as an existing one, using the latest version of the task.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest runs replay run_abc123
```

## runs cancel

Cancels a run that has not finished yet. You are asked to confirm first.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest runs cancel run_abc123
```

**Skip confirmation** `--yes | -y`

Cancel without the confirmation prompt. Required in non-interactive environments such as CI.

## Options

**Environment** `--env | -e`

The environment to use: `dev`, `prod`, `staging` or `preview`. Defaults to `prod`.

**Config file** `--config | -c`

The name of the config file found at the project path. Defaults to `trigger.config.ts`

**Project ref** `--project-ref | -p`

The project ref. Required if there is no config file.

**Branch** `--branch | -b`

Required when using `--env preview`. Specify the branch, e.g. `--branch my-branch` or `-b my-branch`. With `--env dev`, it defaults to the same [dev branch](/docs/deployment/dev-branches) as the dev command.

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
