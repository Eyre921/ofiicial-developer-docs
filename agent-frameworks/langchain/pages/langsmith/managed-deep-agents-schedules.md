---
title: "Add schedules to Managed Deep Agents"
source: https://docs.langchain.com/langsmith/managed-deep-agents-schedules
path: langsmith/managed-deep-agents-schedules
---

Declare managed cron schedules for Managed Deep Agents deployments.

Managed Deep Agents can run agents on a cron schedule. Add one schedule file under `schedules/`, export a named `schedule` declaration, and `mda deploy` provisions it as a LangSmith cron after the deployment is live.

<Note>
  Managed Deep Agents is in **private [beta](/langsmith/release-stages)**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

## Add a schedule

Create one file per schedule under `schedules/`. The file name becomes the managed schedule name. For the full project layout, see the [CLI project file reference](/langsmith/managed-deep-agents-cli#project-file-reference).

The schedule module must export a named `schedule` declaration.

<CodeGroup>
  ```python schedules/daily_digest.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import define_schedule

  schedule = define_schedule(
      cron="0 8 * * 1-5",
      timezone="America/Los_Angeles",
      prompt="Write the daily digest.",
  )
  ```

  ```ts schedules/daily-digest.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineSchedule } from "managed-deepagents";

  export const schedule = defineSchedule({
    cron: "0 8 * * 1-5",
    timezone: "America/Los_Angeles",
    prompt: "Write the daily digest.",
  });
  ```
</CodeGroup>

## Configure schedule input

Each schedule must define exactly one of:

* `prompt`: A natural-language prompt. MDA converts it to a user message when the cron fires.
* `input`: A structured LangGraph input object. Use this when you need to pass custom graph input instead of a single prompt.

<CodeGroup>
  ```python schedules/nightly_sweep.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import define_schedule

  schedule = define_schedule(
      cron="30 2 * * *",
      input={
          "messages": [
              {"role": "user", "content": "Sweep stale tickets and summarize changes."}
          ]
      },
  )
  ```

  ```ts schedules/nightly-sweep.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineSchedule } from "managed-deepagents";

  export const schedule = defineSchedule({
    cron: "30 2 * * *",
    input: {
      messages: [
        { role: "user", content: "Sweep stale tickets and summarize changes." },
      ],
    },
  });
  ```
</CodeGroup>

`cron` must be a standard five-field cron expression: minute, hour, day of month, month, and day of week. If `timezone` is omitted, LangSmith crons use UTC.

## Choose thread behavior

Schedules use ephemeral threads by default. MDA creates a fresh thread for each run and asks LangSmith to delete that temporary thread after the run completes.

Use a persistent thread only when scheduled runs should accumulate durable thread state across invocations.

<CodeGroup>
  ```python schedules/nightly_memory.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import define_schedule

  schedule = define_schedule(
      cron="0 3 * * *",
      prompt="Review the current project memory and list follow-up tasks.",
      thread={"mode": "persistent", "id": "nightly-memory"},
  )
  ```

  ```ts schedules/nightly-memory.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineSchedule } from "managed-deepagents";

  export const schedule = defineSchedule({
    cron: "0 3 * * *",
    prompt: "Review the current project memory and list follow-up tasks.",
    thread: { mode: "persistent", id: "nightly-memory" },
  });
  ```
</CodeGroup>

## Use static declarations

Schedule declarations are extracted at compile time. Keep schedule configuration statically serializable:

* Use literals, arrays, objects, and references to top-level literal constants.
* Do not read environment variables, call functions, spread objects, use `**kwargs`, or compute schedule values dynamically.
* Put dynamic behavior in the agent, tools, middleware, or runtime context instead.

## Deploy schedules

Test the project locally with [`mda dev`](/langsmith/managed-deep-agents-cli#develop-locally), then deploy it with [`mda deploy`](/langsmith/managed-deep-agents-deploy). Open deployment traces in LangSmith to inspect model calls, tool calls, errors, and latency.

When the deployment reaches `DEPLOYED`, `mda deploy` searches for existing MDA-owned cron jobs on the deployed Agent Server, deletes them, and creates cron jobs for the current `schedules/` declarations. Removing a local schedule file and redeploying removes the corresponding managed cron.

<Warning>
  If you deploy with `--no-wait`, the CLI triggers the remote build and exits before the deployment reaches `DEPLOYED`, so it does not reconcile schedules during that invocation. Run `mda deploy .` without `--no-wait` when adding, changing, or removing schedules.
</Warning>

## Troubleshoot schedules

* `must export a named schedule declaration`: Export a top-level `schedule` from each file in `schedules/`.
* `must define exactly one of prompt or input`: Add either `prompt` or `input`, but not both.
* `cron must be a standard 5-field expression`: Use five cron fields, not seconds-based cron syntax.
* `schedule is not static`: Replace computed values with literals or top-level literal constants.
* `failed to create cron for schedule`: Open the deployment URL in LangSmith and confirm the deployed Agent Server is healthy.

## Next steps

<CardGroup>
  <Card title="Deploy an agent" icon="upload" href="/langsmith/managed-deep-agents-deploy">
    Deploy and reconcile schedule changes.
  </Card>

  <Card title="CLI reference" icon="terminal" href="/langsmith/managed-deep-agents-cli">
    Look up `mda deploy` flags and troubleshooting.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-schedules.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
