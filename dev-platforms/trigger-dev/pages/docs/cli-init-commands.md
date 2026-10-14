---
title: "CLI init command"
source: https://trigger.dev/docs/cli-init-commands
path: docs/cli-init-commands
---

Use these options when running the CLI `init` command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest init
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest init
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest init
  ```
</CodeGroup>

## Arguments

<ParamField type="[path]">
  The path to the project. Defaults to `.`.
</ParamField>

## Options

<ParamField type="--javascript">
  By default, the init command assumes you are using TypeScript. Use this flag to initialize a
  project that uses JavaScript.
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref to use when initializing the project.
</ParamField>

<ParamField type="--tag | -t">
  The version of the `@trigger.dev/sdk` package to install. Defaults to the CLI version.
</ParamField>

<ParamField type="--skip-package-install">
  Skip installing the `@trigger.dev/sdk` package.
</ParamField>

<ParamField type="--override-config">
  Override the existing config file if it exists.
</ParamField>

<ParamField type="--project-name <name>">
  The name of the project to create when your account has no projects yet.
</ParamField>

<ParamField type="--org-name <name>">
  The organization to create the first project in. Matches an existing organization by name, or creates it if you have none.
</ParamField>

<ParamField type="-r, --runtime <runtime>">
  The runtime to use: `node`, `node-22`, `node-24`, `node-26` or `bun`. Defaults to `node-24`.
</ParamField>

<ParamField type="-y, --yes">
  Skip all prompts. Requires `--project-ref`, or `--project-name` with `--org-name` for a new account.
</ParamField>

<ParamField type="--no-browser">
  Do not open the browser during login. Print the URL only.
</ParamField>

<ParamField type="--pkg-args">
  Additional arguments to pass to the package manager. Accepts CSV for multiple args.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to the current profile, which is set by your last `login` or `switch` (initially "default").
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
