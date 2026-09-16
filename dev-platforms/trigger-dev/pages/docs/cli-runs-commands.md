---
title: "CLI runs commands"
source: https://trigger.dev/docs/cli-runs-commands
path: docs/cli-runs-commands
---

Use these commands to list, inspect, replay and cancel runs from your terminal.

## runs list

Lists runs, newest first, in a table of ID, task, status, version, created time and duration.

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest runs list
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest runs list
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest runs list
  ```
</CodeGroup>

<ParamField type="--limit">
  The number of runs to list, up to 100. Defaults to 20.
</ParamField>

<ParamField type="--status">
  Only show runs with this status, e.g. `FAILED`.
</ParamField>

<ParamField type="--task">
  Only show runs for this task identifier.
</ParamField>

<ParamField type="--tag">
  Only show runs with this tag.
</ParamField>

<ParamField type="--cursor">
  The pagination cursor printed at the end of the previous page.
</ParamField>

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

<ParamField type="--yes | -y">
  Cancel without the confirmation prompt. Required in non-interactive environments such as CI.
</ParamField>

## Options

<ParamField type="--env | -e">
  The environment to use: `dev`, `prod`, `staging` or `preview`. Defaults to `prod`.
</ParamField>

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--branch | -b">
  When using `--env preview` the branch is automatically detected from git. But you can manually
  specify it by using this option, e.g. `--branch my-branch` or `-b my-branch`.
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
