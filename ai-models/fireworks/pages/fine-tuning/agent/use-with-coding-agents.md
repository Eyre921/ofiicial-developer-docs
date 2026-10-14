---
title: "Agent Skills"
source: https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents
path: fine-tuning/agent/use-with-coding-agents
---

Install Fireworks training skills for your coding agent — research, configure, and debug.

One installation gives you three entry points. Open a chat and describe your goal in plain language.

| Skill | Use it for |
| - | - |
| **research** | Choose method, data, evaluation, and the closest [cookbook](https://github.com/fw-ai/cookbook) entry. Read-only. |
| **configure** | Plan, run, monitor, deploy, or resume training. Shows parameters and cost, then waits for approval before spend. |
| **debug** | Diagnose a stuck, failed, or low-quality run. Read-only until you approve a retry. |

The **fireworks-training** compatibility skill carries shared detailed references that **configure** and **debug** load. Keep it installed with the three entry skills.

Works with Cursor, Codex, OpenCode, Claude Code, and other Agent Skills agents.

## Install

### Paste this into your agent

Copy this into the agent you already use. The agent installs the skills. You stay in the chat.

```text theme={null}
Install the Fireworks training skills in this agent: fireworks-training, research, configure, and debug. Do it yourself. Do not start a training run.

Claude Code:
claude plugin marketplace add fw-ai/cookbook
claude plugin install fireworks-training@fw-ai-cookbook

Cursor, Codex, or OpenCode. Set -a to cursor, codex, or opencode. Do not pass -a '*':
npx --yes skills add fw-ai/cookbook -g -s fireworks-training research configure debug -a cursor -y

If FIREWORKS_API_KEY is missing, walk me through https://app.fireworks.ai/settings/users/api-keys. Do not ask me to paste the key in chat. Then tell me which skills installed and how to invoke them.
```

<Note>
  Every training page has a card that copies this prompt. Paste it into your agent. Installing the skills does not need a Fireworks account. The agent asks you to create an account and an API key before any training run.
</Note>

### Claude Code

Install the auto-updating cookbook plugin. Here `fireworks-training` is the plugin name rather than a single skill, and the plugin ships all of the skills above:

```bash theme={null}
claude plugin marketplace add fw-ai/cookbook
claude plugin install fireworks-training@fw-ai-cookbook
```

### Cursor

`npx skills` installs by skill directory, so name each skill you want:

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

### Other compatible agents

Use the Cursor command and replace `cursor` with your agent's id. OpenCode's id is `opencode`.

<Note>
  `-a '*'` installs the skills into every agent the CLI supports, not only the agents on your machine. Pass one agent id unless you want that broader install.
</Note>

<Note>
  The commands above install skills globally with `-g`. They do not update automatically. Refresh the global copies with `npx --yes skills update -g -y`.
</Note>

Full post-install walkthrough: [cookbook `skills/GETTING-STARTED.md`](https://github.com/fw-ai/cookbook/blob/main/skills/GETTING-STARTED.md).

## Prerequisites

* A Fireworks API key in `FIREWORKS_API_KEY`, exported in the agent's terminal or set in a gitignored `.env`. The skills create and manage training through the Python SDK with this key. Prefer a **scoped** service-account key over a personal admin key for agent use.
* Python 3.11 or newer for running cookbook examples. The agent installs the cookbook when a run needs it.
* [Fireworks CLI (`firectl`)](/tools-sdks/firectl/firectl) installed. The agent uses it for some read-only status checks, and gives you the `firectl` command when you ask to run a managed step yourself.

Use [managed training](/fine-tuning/managed-finetuning-intro) for standard jobs, or the [Training API](/fine-tuning/training-api/introduction) for custom loops on [serverless or dedicated infrastructure](/fine-tuning/training-api/introduction#infrastructure).

## Usage data and privacy

Authenticated API calls include `fireworks-training-skill/<version>` and a random session ID for aggregate product analytics. Prompts and datasets are not collected.

Before the first structured question, the skills show a one-line privacy notice. With `FIREWORKS_API_KEY` set, aggregate journey events may be recorded through supported `firectl` commands. Say `do not track this session` to keep interaction telemetry local. Training still works.

## See also

<CardGroup>
  <Card title="Getting started (cookbook)" icon="rocket" href="https://github.com/fw-ai/cookbook/blob/main/skills/GETTING-STARTED.md">
    Post-install guide and first run.
  </Card>

  <Card title="Case studies" icon="book-open" href="https://github.com/fw-ai/cookbook/tree/main/training/case-studies">
    Runnable notebooks research routes to.
  </Card>

  <Card title="Training Overview" icon="compass" href="/fine-tuning/finetuning-intro#choose-a-surface">
    Pick managed training vs the Training API before you install.
  </Card>

  <Card title="Managed Training" icon="sliders" href="/fine-tuning/managed-finetuning-intro">
    Drive the same training infra directly when you know your config.
  </Card>

  <Card title="Training API" icon="code" href="/fine-tuning/training-api/introduction">
    Write your own Python training loop on Fireworks GPUs.
  </Card>

  <Card title="CLI reference" icon="terminal" href="/tools-sdks/firectl/firectl">
    Automate managed training with `firectl`.
  </Card>
</CardGroup>
