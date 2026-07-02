---
title: "Telemetry"
source: https://docs.together.ai/reference/cli/telemetry
path: reference/cli/telemetry
---

Understand what the Together CLI tracks, how to opt out, and where the local config file lives.

The Together CLI sends anonymous usage events that help Together AI understand how the CLI is used and prioritize fixes and features.

Telemetry applies only when you use the **`tg`** command-line tool (also available as `together`). It is separate from the Python SDK's behavior unless you invoke the CLI.

## How to opt out

You can disable telemetry tracking by setting the `TOGETHER_TELEMETRY_DISABLED` environment variable, or by running `tg telemetry disable`, which saves the choice to a local configuration file on disk.

```bash theme={null}
TOGETHER_TELEMETRY_DISABLED=1 tg files upload ./data.jsonl
```

Use these commands to enable, disable, or check telemetry status:

| Command                    | What it does                                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **`tg telemetry status`**  | Prints whether telemetry is enabled or disabled, and notes when the environment variable is forcing it off. |
| **`tg telemetry disable`** | Disables telemetry by updating the config file.                                                             |
| **`tg telemetry enable`**  | Enables telemetry by updating the config file.                                                              |

**Config file location**:

* **macOS / Linux:** `$XDG_CONFIG_HOME/together/cli.json` if `XDG_CONFIG_HOME` is set, otherwise `~/.config/together/cli.json`.
* **Windows:** `%APPDATA%\Together\cli.json`.

The same file also stores a generated UUID as a stable, pseudonymous device identifier. An example config file:

```json theme={null}
{
  "telemetry_enabled": true,
  "device_id": "7ba688c9-7e39-460a-9c96-ac518ab65605"
}
```

## What is tracked

The CLI collects the following data for every event:

| Field                 | Description                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`timestamp`**       | Millisecond timestamp when the event was built.                                                                                                                                   |
| **`session_id`**      | Identifier for this CLI process, stable for the lifetime of the process.                                                                                                          |
| **`device_id`**       | Stable pseudonymous ID stored in `cli.json` when first needed. Together AI does not use any host-hardware fingerprinting.                                                         |
| **`metadata`**        | Runtime metadata such as the CLI version, operating system, and CPU architecture.                                                                                                 |
| **`is_ci`**           | `true` if the `CI` environment variable is set.                                                                                                                                   |
| **`agent_detection`** | From [`detect_agent`](https://github.com/togethercomputer/detect_agent). Records whether the command was invoked by an agent and which known agent.                               |
| **`command`**         | The name of the command invoked, for example `clusters create`.                                                                                                                   |
| **`arg_names`**       | The names of any CLI arguments passed in. Together AI does **not** collect their values. For example, if you pass `--secret FOOBAR`, only the argument name `secret` is recorded. |
