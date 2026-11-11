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

When the CLI opens your browser, approving the login sends you back to the CLI automatically. If the browser is on another machine, for example when you're connected over SSH, use `--no-browser`: after you approve, the page shows a code to paste into the terminal.

## Login expiry

A login stops working after 7 days without use. The 7 days count from the last command that used it, or from when you logged in if you never used it. Running a command that uses your login, such as `dev` or `deploy`, at least once a week keeps you logged in.

When a login has expired, commands that log you in, such as `login`, `dev` and `deploy`, start a new login. You don't need to log out first. The [MCP server](/docs/mcp-introduction#authentication) does the same on its next tool call.

* **In CI**, the CLI can't complete a login, so it fails and tells you to run `npx trigger.dev@latest login`. To deploy from CI, use an environment API key in `TRIGGER_ACCESS_TOKEN` instead of a copied CLI login. See [CI / GitHub Actions](/docs/github-actions).
* **CLI versions before 4.8.4** show the server's error but can't start a new login over an expired one. Run `trigger.dev logout`, then `trigger.dev login`.
* **Logins made before login expiry was introduced** (in 4.8.4 for self-hosted instances) don't expire.

If you self-host, `CLI_LOGIN_IDLE_TIMEOUT_DAYS` sets the window (default `7`), and `0` turns idle expiry off for new logins. Each login keeps the setting it was created with. See the [webapp environment variables](/docs/self-hosting/env/webapp).

## Options

**No browser** `--no-browser`

Do not open the browser. Print the URL only, and finish the login by pasting the code shown after you approve.

**Code** `--code \<code\>`

Finish a pending login with the code shown in your browser. Use this after `--no-wait`, or when the terminal can't prompt for the code.

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
