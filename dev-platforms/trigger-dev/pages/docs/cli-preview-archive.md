---
title: "CLI preview archive command"
source: https://trigger.dev/docs/cli-preview-archive
path: docs/cli-preview-archive
---

The `trigger.dev preview archive` command can be used to archive a preview branch.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest preview archive
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest preview archive
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest preview archive
  ```
</CodeGroup>

It will archive the preview branch, automatically detecting the branch name from git. You can manually specify the branch using the `--branch` option.

## Arguments

```
npx trigger.dev@latest preview archive [path]
```

<ParamField type="[path]">
  The path to the project. Defaults to the current directory.
</ParamField>

## Options

<ParamField type="--branch | -b">
  When using `--env preview` the branch is automatically detected from git. But you can manually
  specify it by using this option, e.g. `--branch my-branch` or `-b my-branch`.
</ParamField>

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--env-file">
  Load environment variables from a file. This will only hydrate the `process.env` of the CLI
  process, not the tasks.
</ParamField>

<ParamField type="--skip-update-check">
  Skip checking for `@trigger.dev` package updates.
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
