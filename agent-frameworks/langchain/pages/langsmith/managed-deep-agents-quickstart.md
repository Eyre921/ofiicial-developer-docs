---
title: "Managed Deep Agents quickstart"
source: https://docs.langchain.com/langsmith/managed-deep-agents-quickstart
path: langsmith/managed-deep-agents-quickstart
---

Create and deploy your first Managed Deep Agent with the mda CLI.

Deploy a hosted Deep Agent without setting up infrastructure. This quickstart scaffolds a code-first project, runs the agent locally, edits the managed system prompt, and deploys it with `mda`. To build a fuller agent step by step, follow the [tutorial](/langsmith/managed-deep-agents-tutorial).

For the full deploy workflow and all CLI flags, see [Deploy an agent](/langsmith/managed-deep-agents-deploy) and the [CLI reference](/langsmith/managed-deep-agents-cli).

<Note>
  Managed Deep Agents is in **private [beta](/langsmith/release-stages)**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

## Prerequisites

Before you start, make sure you have:

* An organization with Managed Deep Agents [private beta access](https://www.langchain.com/langsmith-managed-deep-agents-waitlist).
* A [LangSmith API key](/langsmith/create-account-api-key).
* Python and `uv` for Python projects, or Node.js and npm for TypeScript projects.
* An API key for your model provider of choice.

## Create and deploy an agent

<Steps>
  <Step title="Install the package">
    Install `managed-deepagents` for the language you want to author in. Both packages include the `mda` CLI.

    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install --pre managed-deepagents
      ```

      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install -g managed-deepagents@dev
      ```
    </CodeGroup>

    For Python, the `pip` command installs the `mda` CLI. After you scaffold a project, run `uv sync` inside that project to install the dependencies from its generated `pyproject.toml`.
  </Step>

  <Step title="Create a project">
    Create a Managed Deep Agents project:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mda init research-assistant
    cd research-assistant
    ```

    The CLI detects `pyproject.toml` or `package.json` in the current directory. If it cannot infer a language, it prompts you to choose Python or TypeScript.

    The scaffold creates:

    | File                               | Purpose                                                                     |
    | ---------------------------------- | --------------------------------------------------------------------------- |
    | `agent.py` or `agent.ts`           | The named `agent` definition compiled by `mda`.                             |
    | `instructions.md`                  | Managed system prompt embedded locally and synced to Context Hub on deploy. |
    | `pyproject.toml` or `package.json` | Minimal project manifest with `managed-deepagents`.                         |
    | `README.md`                        | Local project notes and deploy command.                                     |
    | `.env`                             | Deploy auth and runtime secrets. Do not commit real secrets.                |
    | `.gitignore`                       | Ignores `.env`, `.env.*`, `.mda/`, and dependency caches.                   |

    For the full project layout, see the [CLI project file reference](/langsmith/managed-deep-agents-cli#project-file-reference).
  </Step>

  <Step title="Add API keys to `.env`">
    Open the generated `.env` file and add your LangSmith API key plus the provider key for the model you plan to use:

    ```text .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
    OPENAI_API_KEY=<OPENAI_API_KEY>
    ```

    `LANGSMITH_API_KEY` authenticates `mda deploy`. Provider keys, MCP tokens, database URLs, and other non-reserved `.env` values are sent to the hosted deployment as secrets when you deploy. The `.env` file itself is not uploaded in the source archive.

    The CLI targets US LangSmith Cloud by default. To deploy with an organization-scoped key, set `LANGSMITH_TENANT_ID` in `.env` or pass `--tenant-id` to `mda deploy`.

    <Note>
      If a request returns 401 or 403, confirm the key belongs to a workspace with beta access.
    </Note>
  </Step>

  <Step title="Edit the agent">
    Open the generated `agent.py` or `agent.ts` and configure the model, tools, middleware, and interrupts in code.

    <CodeGroup>
      ```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from managed_deepagents import define_deep_agent

      agent = define_deep_agent(
          model="openai:gpt-5.5",
      )
      ```

      ```ts agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { defineDeepAgent } from "managed-deepagents";

      export const agent = defineDeepAgent({
        model: "openai:gpt-5.5",
      });
      ```
    </CodeGroup>

    The managed runtime owns `backend`, `store`, `checkpointer`, `memory`, `skills`, and the system prompt. Do not set those fields in the agent definition.

    | Concern                                         | Owner                                  | Where you configure it                                              |
    | ----------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------- |
    | `backend`, `store`, `checkpointer`              | Managed runtime                        | Not configurable.                                                   |
    | `memory`                                        | Managed runtime, backed by Context Hub | `disableMemory` / `disable_memory` to turn off agent-scoped memory. |
    | `skills`                                        | Managed runtime, backed by Context Hub | `skills/**` in the project.                                         |
    | System prompt                                   | Managed runtime, backed by Context Hub | `instructions.md` in the project.                                   |
    | Model, tools, middleware, subagents, interrupts | You                                    | The agent definition and imported modules.                          |

    For the full field list, see the [agent definition reference](/langsmith/managed-deep-agents-cli#agent-definition-reference).

    The generated model uses OpenAI. If you use another provider, change the model identifier and set the API key required by that provider in `.env`, your shell environment, or LangSmith workspace secrets.
  </Step>

  <Step title="Edit the instructions">
    Open `instructions.md` and replace the generated prompt with the behavior you want:

    ```markdown instructions.md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Research assistant

    You are a careful research assistant. Search for sources, keep notes, and return
    concise answers with citations.
    ```

    `mda dev` embeds this file into the generated local entry module. `mda deploy` syncs it to Context Hub and the deployed runtime reads it from there.
  </Step>

  <Step title="Run locally">
    Install the generated project dependencies, then start the local LangGraph dev server:

    <CodeGroup>
      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv sync
      mda dev .
      ```

      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install
      mda dev .
      ```
    </CodeGroup>

    For TypeScript projects, `mda dev` runs `npx --yes @langchain/langgraph-cli dev`. For Python projects, it uses `uv` to resolve and run the local LangGraph dev server automatically. You do not need to install `langgraph-cli[inmem]` yourself.

    `mda dev` loads the project `.env` file from the compiled local build so model provider keys and connector tokens are available during local development.
  </Step>

  <Step title="Deploy the agent">
    Deploy the local project:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mda deploy .
    ```

    On success, the CLI prints the LangSmith deployment dashboard URL:

    ```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    Deployment live
    Deployment dashboard
    https://smith.langchain.com/o/<tenant-id>/host/deployments/<deployment-id>
    Deployed 'research-assistant' to LangSmith.
    ```

    Open the printed URL in LangSmith to inspect build status, revisions, and traces.
  </Step>
</Steps>

## Next steps

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/langsmith/managed-deep-agents-quickstart">
    Deploy a first code-first agent with the `mda` CLI.
  </Card>

  <Card title="Tutorial" icon="book" href="/langsmith/managed-deep-agents-tutorial">
    Build a scheduled research agent from an empty directory.
  </Card>

  <Card title="How it works" icon="settings" href="/langsmith/managed-deep-agents-how-it-works">
    Understand compilation, the deploy lifecycle, and Context Hub.
  </Card>

  <Card title="Identity" icon="fingerprint" href="/langsmith/managed-deep-agents-identity">
    Scope threads and memory to the authenticated caller.
  </Card>

  <Card title="Custom tools" icon="tool" href="/langsmith/managed-deep-agents-tools">
    Add authored LangChain tools from your project source.
  </Card>

  <Card title="Custom middleware" icon="code" href="/langsmith/managed-deep-agents-middleware">
    Add built-in or custom middleware around model and tool calls.
  </Card>

  <Card title="Connectors" icon="plug" href="/langsmith/managed-deep-agents-connectors">
    Attach remote MCP servers or constrained LangSmith capabilities.
  </Card>

  <Card title="Schedules" icon="calendar" href="/langsmith/managed-deep-agents-schedules">
    Run agents on managed cron schedules.
  </Card>

  <Card title="Deploy an agent" icon="upload" href="/langsmith/managed-deep-agents-deploy">
    Test and deploy Managed Deep Agents with `mda`.
  </Card>

  <Card title="Examples" icon="apps" href="/langsmith/managed-deep-agents-examples">
    Explore a complete project that uses every primitive.
  </Card>

  <Card title="CLI reference" icon="terminal" href="/langsmith/managed-deep-agents-cli">
    Review `mda init`, `mda dev`, and `mda deploy`.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
