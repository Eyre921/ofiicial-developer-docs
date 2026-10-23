---
title: "CLI dev command"
source: https://trigger.dev/docs/cli-dev-commands
path: docs/cli-dev-commands
---

The `trigger.dev dev` command is used to run your tasks locally.

This runs a server on your machine that can execute Trigger.dev tasks:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest dev
```

It will first perform an update check to prevent version mismatches, failed deploys, and other errors. You will always be prompted first.

You will see in the terminal that the server is running and listening for tasks. When you run a task, you will see it in the terminal along with a link to view it in the dashboard.

It is worth noting that each task runs in a separate Node process. This means that if you have a long-running task, it will not block other tasks from running.

When a build fails, the dev command keeps watching your files and rebuilds as soon as you fix the errors. Until then, new runs use the last version that built successfully.

## Running dev from a coding agent

The dev command detects when a coding agent such as Claude Code, Cursor, Codex or Gemini CLI is running it, and changes its output so the agent can act on it:

* It skips the prompts to install the MCP server and agent skills.
* If your `@trigger.dev/*` packages don't match the CLI version, it exits with instructions instead of asking whether to update them.
* When the local worker is ready, it lists the task ids it registered and prints plain dashboard URLs.
* Each run prints its dashboard URL, and successful runs print their output.

If your agent isn't detected, set the `AI_AGENT` environment variable to its name.

To test a task, an agent can trigger it with [`tasks trigger`](/docs/cli-tasks-commands) and `--wait`, which prints the run's output or error.

## Options

**Config file** `--config | -c`

The name of the config file found at the project path. Defaults to `trigger.config.ts`

**Project ref** `--project-ref | -p`

The project ref. Required if there is no config file.

**Env file** `--env-file`

Load environment variables from a file instead of the default `.env` files. They are available to your tasks in the local dev session.

**Skip update check** `--skip-update-check`

Skip checking for `@trigger.dev` package updates.

**Branch** `--branch | -b`

The dev branch to use. Defaults to the `TRIGGER_DEV_BRANCH` environment variable. See [dev branches](/docs/deployment/dev-branches).

**Max concurrent runs** `--max-concurrent-runs`

The maximum number of concurrent runs in the dev session. It can only lower your dev environment's concurrency limit, not raise it.

**Keep temporary files** `--keep-tmp-files`

Keep temporary files after the dev session ends.

**Analyze build output** `--analyze`

Analyzes the build output and displays detailed import timings. This is useful for debugging the
start times for your runs which can be caused by importing lots of code or heavy packages.

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

## Concurrently running the terminal

Install the concurrently package as a dev dependency:

```ts theme={"theme":"css-variables"}
concurrently --raw --kill-others npm:dev:remix npm:dev:trigger
```

Then add something like this in your package.json scripts:

```json theme={"theme":"css-variables"}
"scripts": {
  "dev": "concurrently --raw --kill-others npm:dev:*",
  "dev:trigger": "npx trigger.dev@latest dev",
  // Add your framework-specific dev script here, for example:
  // "dev:next": "next dev",
  // "dev:remix": "remix dev",
  //...
}
```
