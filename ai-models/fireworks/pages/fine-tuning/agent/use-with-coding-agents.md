---
title: "Agent Skills"
source: https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents
path: fine-tuning/agent/use-with-coding-agents
---

Set up your agent to train with Fireworks.

Paste this into your agent:

```text wrap theme={null}
Set up Fireworks training for me. Fetch https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents.md and follow it.
```

| Skill | Use it for |
| - | - |
| **research** | Choose the method, data, evaluation, and cookbook example. Read-only. |
| **configure** | Plan and run training. Shows the parameters and cost, then waits for approval. |
| **debug** | Diagnose a stuck, failed, or low-quality run. Read-only until you approve a retry. |

**fireworks-training** holds the shared references that **configure** and **debug** load. Keep it installed with the other three.

Works with Cursor, Codex, OpenCode, Claude Code, and other Agent Skills agents.

## Install

To install them yourself, use the commands below.

### Claude Code

The `fireworks-training` plugin includes all four skills and updates with the plugin:

```bash theme={null}
claude plugin marketplace add fw-ai/cookbook
claude plugin install fireworks-training@fw-ai-cookbook
```

### Cursor

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training research configure debug -a cursor -y
```

### Codex

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training research configure debug -a codex -y
```

### OpenCode

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training research configure debug -a opencode -y
```

### Other agents

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training research configure debug -a <agent-id> -y
```

OpenCode's id is `opencode`.

These commands install the skills globally with `-g`. They do not update on their own. Refresh them with `npx --yes skills update -g -y`. Claude Code uses the plugin update flow.

## For a coding agent

Run the install command that matches the agent you are running in. If `fireworks-training`, `research`, `configure`, and `debug` are already installed, update them instead.

Tell the user which skills installed. They use the skills by describing a goal in a new chat.

Training uses the Python SDK with `FIREWORKS_API_KEY`. If it is missing, walk the user through [app.fireworks.ai/settings/users/api-keys](https://app.fireworks.ai/settings/users/api-keys). Prefer a scoped service-account key. Have them set it with hidden terminal input or a gitignored `.env`:

```bash theme={null}
read -s FIREWORKS_API_KEY
echo
export FIREWORKS_API_KEY
```

Do not ask them to paste the key in chat.

Python 3.11 or newer is needed when a run uses a cookbook example. [`firectl`](/tools-sdks/firectl/firectl) is optional and for the user. If it is already installed, the skills may record aggregate journey events with `firectl skill-journey record`.

## How to use the skills

Describe the goal. You do not need to name a skill. For example:

```text theme={null}
What can I try first with a preloaded dataset?
```

```text theme={null}
Plan an SFT run for my labeled JSONL dataset.
```

```text theme={null}
My training job is running but has made no progress for 15 minutes.
```

## Prerequisites

* A Fireworks API key in `FIREWORKS_API_KEY`, exported in the agent's terminal or set in a gitignored `.env`. The skills create and manage training through the Python SDK with this key. Prefer a **scoped** service-account key over a personal admin key for agent use.
* Python 3.11 or newer for running cookbook examples. The agent installs the cookbook when a run needs it.
* [Fireworks CLI (`firectl`)](/tools-sdks/firectl/firectl) is optional. Use it yourself for read-only checks. The agent does not need it to train. If it is already installed, the skills may use it for aggregate journey events, and they can give you the `firectl` command when you ask to inspect or run a managed step yourself.

## Usage data and privacy

Authenticated API calls include `fireworks-training-skill/<version>` and a random session ID for aggregate product analytics. Prompts and datasets are not collected.

Before the first structured question, the skills show a one-line privacy notice. With `FIREWORKS_API_KEY` set, aggregate journey events may be recorded through supported `firectl` commands. Say `do not track this session` to keep interaction telemetry local. Training still works.

## See also

<CardGroup>
  <Card title="Case studies" icon="book-open" href="https://github.com/fw-ai/cookbook/tree/main/training/case-studies">
    Runnable notebooks research routes to.
  </Card>

  <Card title="Training Overview" icon="compass" href="/fine-tuning/finetuning-intro#choose-a-surface">
    Compare managed training and the Training API.
  </Card>

  <Card title="Managed Training" icon="sliders" href="/fine-tuning/managed-finetuning-intro">
    Drive the same training infra directly when you know your config.
  </Card>

  <Card title="Training API" icon="code" href="/fine-tuning/training-api/introduction">
    Write your own Python training loop on Fireworks GPUs.
  </Card>

  <Card title="CLI reference" icon="terminal" href="/tools-sdks/firectl/firectl">
    Inspect managed training yourself with `firectl`.
  </Card>
</CardGroup>
