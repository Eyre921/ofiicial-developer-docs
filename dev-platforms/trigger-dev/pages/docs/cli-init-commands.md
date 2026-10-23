---
title: "CLI init command"
source: https://trigger.dev/docs/cli-init-commands
path: docs/cli-init-commands
---

Use these options when running the CLI `init` command.

Run the command like this:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest init
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest init
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest init
```

## Arguments

**Project path** `[path]`

The path to the project. Defaults to `.`.

## Options

**Javascript** `--javascript`

By default, the init command assumes you are using TypeScript. Use this flag to initialize a
project that uses JavaScript.

**Project ref** `--project-ref | -p`

The project ref to use when initializing the project.

**Package tag** `--tag | -t`

The version of the `@trigger.dev/sdk` package to install. Defaults to the CLI version.

**Skip package install** `--skip-package-install`

Skip installing the `@trigger.dev/sdk` package.

**Override config** `--override-config`

Override the existing config file if it exists.

**Project name** `--project-name \<name\>`

The name of the project to create when your account has no projects yet.

**Organization name** `--org-name \<name\>`

The organization to create the first project in. Matches an existing organization by name, or creates it if you have none.

**Runtime** `-r, --runtime \<runtime\>`

The runtime to use: `node`, `node-22`, `node-24`, `node-26` or `bun`. Defaults to `node-24`.

**Yes** `-y, --yes`

Skip all prompts. Requires `--project-ref`, or `--project-name` with `--org-name` for a new account.

**No browser** `--no-browser`

Do not open the browser during login. Print the URL only.

**Package arguments** `--pkg-args`

Additional arguments to pass to the package manager. Accepts CSV for multiple args.

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
