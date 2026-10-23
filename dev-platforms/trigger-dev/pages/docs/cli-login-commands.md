---
title: "CLI login command"
source: https://trigger.dev/docs/cli-login-commands
path: docs/cli-login-commands
---

Use these options when logging in to Trigger.dev using the CLI.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest login
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest login
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest login
```

## Options

**No browser** `--no-browser`

Do not open the browser. Print the URL only.

**Email** `--email \<email\>`

Prefill the email on the login page.

**Name** `--name \<name\>`

Set your name after authorization. Only applies to a new account that has not set its details yet.

**Cancel pending** `--cancel-pending`

Cancel a pending login and keep the current account.

**No wait** `--no-wait`

Save the authorization and exit so login can be resumed later.

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
