---
title: "CLI deploy command"
source: https://trigger.dev/docs/cli-deploy-commands
path: docs/cli-deploy-commands
---

Use the deploy command to deploy your tasks to Trigger.dev.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

<Warning>
  This will fail in CI if any version mismatches are detected. Ensure everything runs locally first
  using the [dev](/docs/cli-dev-commands) command and don't bypass the version checks!
</Warning>

It performs a few steps to deploy:

1. Optionally updates packages when running locally.
2. Compiles and bundles the code.
3. Deploys the code to the Trigger.dev instance.
4. Registers the tasks as a new version in the environment (prod by default).

## Deploying from CI

When deploying from CI/CD environments such as GitHub Actions, GitLab CI, or Jenkins, you need to authenticate non-interactively by setting the `TRIGGER_ACCESS_TOKEN` environment variable. Please see the [CI / GitHub Actions guide](/docs/github-actions) for more information.

## Arguments

```
npx trigger.dev@latest deploy [path]
```

<ParamField type="[path]">
  The path to the project. Defaults to the current directory.
</ParamField>

## Options

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

<ParamField type="--env | -e">
  Defaults to `prod` but you can specify `staging` or `preview`. If you specify `preview` we will
  try and automatically detect the branch name from git.
</ParamField>

<ParamField type="--branch | -b">
  When using `--env preview` the branch is automatically detected from git. But you can manually
  specify it by using this option, e.g. `--branch my-branch` or `-b my-branch`.
</ParamField>

<ParamField type="--dry-run">
  Create a deployable build but don't deploy it. Prints out the build path so you can inspect it.
</ParamField>

<ParamField type="--skip-promotion">
  Skips automatically promoting the newly deployed version to the "current" deploy.
</ParamField>

<ParamField type="--skip-sync-env-vars">
  Turn off syncing environment variables with the Trigger.dev instance.
</ParamField>

<ParamField type="--local-build">
  Force building the deployment image locally using your local Docker. This is automatic when self-hosting.
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

### Self-hosting

When [self-hosting](/docs/self-hosting/overview), builds are performed locally by default. Once you've logged in to your self-hosted instance using the CLI, you can deploy with:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

For CI/CD environments, set `TRIGGER_ACCESS_TOKEN` and `TRIGGER_API_URL` environment variables. See the [GitHub Actions guide](/docs/github-actions#self-hosting) for more details.
