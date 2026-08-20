---
title: "Get started"
source: https://docs.together.ai/reference/cli/getting-started
path: reference/cli/getting-started
---

Install the Together CLI to deploy endpoints, fine-tune models, and manage GPU clusters from your terminal.

You can use the Together CLI to manage your Together AI resources from your terminal, or using automated systems. Use the Together CLI to deploy endpoints, fine-tune models, manage your GPU clusters, and more.

## Install the Together CLI

<Note>
  Requires [Python 3.10+](https://www.python.org/).
</Note>

Run the following command to install the CLI:

```bash theme={null}
# Install
uv tool install "together[cli]"

# Upgrade
uv tool upgrade "together[cli]"

# List commands
tg --help
```

<Note>
  The `[cli]` extra target includes additional dependencies used by the CLI. The extra target prevents the Python SDK from being bloated with dependencies it does not use.
</Note>

The CLI is also installed as `together`, an alias of `tg` that's identical in behavior. Examples throughout these docs use `tg`.

<Warning>
  **Migrating from a `pip`-installed CLI?** An earlier `pip install together` can pin the CLI to an older Python interpreter and leave a stale `tg` binary earlier on your `PATH`, which shadows the `uv`-managed install. Commands that need a newer CLI (such as OIDC SSH into clusters, which requires 2.20+) then fail even after you upgrade. To switch to the `uv`-managed install:

  1. Uninstall the pip package: `pip uninstall together`.
  2. Reload your shell (or run `hash -r`) so `PATH` resolves to the `uv`-managed binary.
  3. Reinstall: `uv tool install "together[cli]"`.
  4. Confirm the version: `tg --version`.
</Warning>

## Upgrade notices

The CLI checks [PyPI](https://pypi.org/project/together/) in the background for a newer release and caches the result for 24 hours. When one is available, it prints an upgrade notice at most once per day. In an interactive terminal it also offers to run the upgrade for you, using the command that matches your install (`uv`, `pipx`, or `pip`). With `--json` or `--non-interactive`, it prints the upgrade command instead.

To disable the check entirely (for example, in CI), set:

```bash Shell theme={null}
export TOGETHER_DISABLE_VERSION_CHECK=1
```

## Authenticate

The CLI relies on the `TOGETHER_API_KEY` environment variable being set to your account's API token to authenticate requests. You can find your API token in your [account settings](https://api.together.ai/settings/projects/~first/api-keys).

To create an environment variable in the current shell, run:

```bash Shell theme={null}
export TOGETHER_API_KEY=<your_key>
```

You can also add it to your shell's global configuration so all new sessions can access it. Different shells have different semantics for setting global environment variables, so see your preferred shell's documentation to learn more.

## Use the CLI in a CI/CD environment

`uvx` is a helper utility from `uv` that downloads and runs a Python binary without a separate install step. In a CI/CD environment, invoke the CLI directly with `uvx`:

```bash theme={null}
uvx "together[cli]" COMMAND [ARGS]...
```

In CI/CD, set `TOGETHER_API_KEY` instead of passing `--api-key` so the token does not appear in process lists or logs. If both are provided, `--api-key` takes precedence over the environment variable.

## Available commands

### `models`

View Together models and upload your own.

```bash theme={null}
tg models list
tg models upload
```

[Learn more about the models command](/reference/cli/models).

### `endpoints`

Manage your models on your own custom endpoints for improved reliability at scale.

```bash theme={null}
tg endpoints create
tg endpoints start endpoint-id
tg endpoints stop endpoint-id
tg endpoints hardware --available --model my-uploaded-model
```

[Learn more about the endpoints command](/reference/cli/endpoints).

### `files`

Upload and manage datasets for use in fine-tuning, evals, and batch inference.

```bash theme={null}
tg files check ./dataset.jsonl
tg files upload ./eval-data.jsonl --purpose eval
tg files list
```

[Learn more about the files command](/reference/cli/files).

### `fine-tuning`

Fine tune custom models.

```bash theme={null}
tg fine-tuning create
tg fine-tuning model-limits
tg fine-tuning list-checkpoints
tg fine-tuning download

# Shorthand alias
tg ft create
```

[Learn more about the fine-tuning command](/reference/cli/finetune).

### `evals`

Manage model evaluation jobs.

```bash theme={null}
tg evals create 
tg evals status [EVAL_ID]
```

[Learn more about the evals command](/reference/cli/evals).

### `clusters` (beta)

Reserve, manage, and interact with GPU clusters.

```bash theme={null}
tg beta clusters create
tg beta clusters get-credentials [CLUSTER_ID]
tg beta clusters list-regions
```

[Learn more about the clusters command](/reference/cli/clusters).

### `jig` (beta)

Build, deploy, and manage dedicated containers.

```bash theme={null}
tg beta jig init
tg beta jig deploy
tg beta jig secrets set HF_TOKEN $HF_TOKEN
```

[Learn more about the jig command](/reference/cli/jig).

### `whoami`

Show the project and organization your current API key is authenticated against.

```bash theme={null}
tg whoami
```

[Learn more about the whoami command](/reference/cli/whoami).

## Beta commands

The `beta` namespace provides access to experimental features and new capabilities before they become part of the standard API.

Features in the beta namespace are largely considered stable. However, these features are subject to change and may be modified or removed in future releases.

## Command aliases

Several commands and subcommands have shorthand aliases for faster typing:

| Alias | Full command  | Available on                                                                                                                                                                                                     |
| :---- | :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ft`  | `fine-tuning` | `tg ft …` (e.g. `tg ft create`, `tg ft ls`)                                                                                                                                                                      |
| `ls`  | `list`        | `tg files ls`, `tg fine-tuning ls`, `tg models ls`, `tg endpoints ls`, `tg evals ls`, `tg beta clusters ls`, `tg beta clusters storage ls`, `tg beta jig ls`, `tg beta jig secrets ls`, `tg beta jig volumes ls` |
| `-c`  | `create`      | `tg fine-tuning -c`, `tg endpoints -c`, `tg evals -c`, `tg beta clusters -c`, `tg beta clusters storage -c`                                                                                                      |
| `-d`  | `delete`      | `tg files -d`, `tg fine-tuning -d`, `tg endpoints -d`, `tg beta clusters -d`, `tg beta clusters storage -d`, `tg beta jig secrets -d`, `tg beta jig volumes -d`                                                  |

## Global parameters

The following parameters are available on every command:

| Flag                     | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--help`                 | Print help for the prefixed command.                                                                                                                                                                                                                                                                                |
| `--json`                 | Return the response as JSON. Useful for scripting.                                                                                                                                                                                                                                                                  |
| `--non-interactive`      | Disable interactive prompts and manual input.                                                                                                                                                                                                                                                                       |
| `--api-key [string]`     | Your Together API key. Falls back to the `TOGETHER_API_KEY` environment variable.                                                                                                                                                                                                                                   |
| `--project [string]`     | Together project ID for project-scoped commands. Falls back to the `TOGETHER_PROJECT_ID` environment variable. When omitted, read-only commands use the project associated with your API key. Mutating commands may prompt for confirmation or require an explicit project in `--json` or `--non-interactive` mode. |
| `--timeout [number]`     | Request timeout, in seconds.                                                                                                                                                                                                                                                                                        |
| `--max-retries [number]` | Maximum number of HTTP retries.                                                                                                                                                                                                                                                                                     |
| `--version`              | Print the CLI version.                                                                                                                                                                                                                                                                                              |
| `--debug`                | Enable debug logging.                                                                                                                                                                                                                                                                                               |
