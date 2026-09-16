---
title: "CLI env commands"
source: https://trigger.dev/docs/cli-env-commands
path: docs/cli-env-commands
---

List, get, set, and pull environment variables for a Trigger.dev project.

These commands manage environment variables on a project environment. They default to `prod`. Use `--env staging` or `--env preview` (with `--branch`) for the other environments. There is no `dev` target: local `trigger dev` reads your local `.env`.

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest env list
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest env list
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest env list
  ```
</CodeGroup>

## env list

Lists user-set environment variables. `TRIGGER_` system variables are omitted. Values are hidden unless you pass `--show-values`.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest env list
npx trigger.dev@latest env list --show-values
```

<ParamField type="--show-values">
  Print the actual values, including secrets.
</ParamField>

## env get

Prints one variable. `--raw` prints only the value, with no banner or extra text, so you can capture it in a script.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest env get MY_VAR
npx trigger.dev@latest env get MY_VAR --raw
```

<ParamField type="<name>">
  The name of the environment variable.
</ParamField>

<ParamField type="--raw">
  Print only the value.
</ParamField>

## env set

Creates the variable if it does not exist, and overwrites the value if it does. Empty or whitespace-only values are rejected.

Updating an existing secret without `--secret` changes the value and leaves it secret. Pass `--secret` when you first create a secret, or when you want a non-secret variable to become one.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest env set MY_VAR my-value
npx trigger.dev@latest env set STRIPE_KEY sk_live_abc --secret
```

<ParamField type="<name>">
  The name of the environment variable.
</ParamField>

<ParamField type="<value>">
  The value to set. Cannot be empty.
</ParamField>

<ParamField type="--secret">
  Store the value as a secret, so it cannot be read back.
</ParamField>

## env pull

Writes the project's environment variables to a local file. Defaults to `.env.local`. Fails if the file already exists unless you pass `--force`.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest env pull
npx trigger.dev@latest env pull --output .env.trigger --force
```

<ParamField type="-o, --output <file>">
  The file to write. Defaults to `.env.local`.
</ParamField>

<ParamField type="--force">
  Overwrite the output file if it exists.
</ParamField>

## Options

<ParamField type="--env | -e">
  The environment to use: `prod`, `staging` or `preview`. Defaults to `prod`.
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
