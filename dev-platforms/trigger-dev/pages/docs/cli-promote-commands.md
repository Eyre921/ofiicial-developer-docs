---
title: "CLI promote command"
source: https://trigger.dev/docs/cli-promote-commands
path: docs/cli-promote-commands
---

Use the promote command to promote a previously deployed version to the current version.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest promote <version>
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest promote <version>
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest promote <version>
```

## Arguments

```
npx trigger.dev@latest promote <version>
```

**Deployment version** `\<version\>`

The version to promote, e.g. `20250208.1`.

## Options

**Config file** `-c, --config \<config file\>`

The name of the config file.

**Environment** `-e, --env \<env\>`

The environment to promote in: `prod`, `staging` or `preview`. Defaults to the environment of the
API key in `TRIGGER_ACCESS_TOKEN`, otherwise `prod`.

**Prod** `--prod`

Promote in the `prod` environment. Shorthand for `--env prod`.

**Branch** `-b, --branch \<branch\>`

The preview branch when `--env` is `preview`. If omitted, it's read from `TRIGGER_PREVIEW_BRANCH`, then `VERCEL_GIT_COMMIT_REF`, then your git branch.

**Project ref** `-p, --project-ref \<project ref\>`

The project ref. Required if there is no config file. Overrides the project in the config file.

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
