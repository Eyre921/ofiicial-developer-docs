---
title: "Managed Deep Agents"
source: https://docs.langchain.com/langsmith/managed-deep-agents-overview
path: langsmith/managed-deep-agents-overview
---

Overview of Managed Deep Agents private beta features, workflows, and limits.

Managed Deep Agents is a hosted runtime for deploying and operating code-first Deep Agents in LangSmith, pairing the [Deep Agents](/oss/python/deepagents/overview) harness with managed infrastructure. It lets you run a production agent without standing up your own agent server or infrastructure. You author an agent in Python or TypeScript, then use the `mda` CLI to test and deploy it to the managed runtime.

The managed runtime provides:

* Durable runs
* [LangSmith sandboxes](/langsmith/sandboxes)
* [Context Hub](/langsmith/use-the-context-hub)-backed instructions, skills, and memory
* Traces
* Hosted LangGraph deployment

To deploy your first agent, see the [quickstart](/langsmith/managed-deep-agents-quickstart).

<Note>
  Managed Deep Agents is in **private [beta](/langsmith/release-stages)**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.

  **Private beta access:** During private beta, Managed Deep Agents is CLI-first while LangChain finalizes the supported API. API-driven creation, update, and invocation examples have been removed. To use agents programmatically, contact your LangChain team at the address in your beta access email.
</Note>

## When to use Managed Deep Agents

Choose the path that matches your control and infrastructure needs:

| Path                                                         | Use when                                                                                                                       | You manage                                                                 | LangSmith manages                                                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Managed Deep Agents**                                      | You want a code-first Deep Agent deployed quickly on managed infrastructure.                                                   | Agent code, tools, middleware, instructions, schedules, optional identity. | Backend, store, checkpointer, memory, skills, sandbox, hosted deployment, identity auth when declared. |
| **[LangSmith Deployment](/langsmith/deployment-quickstart)** | You need custom application code, custom routes, advanced authentication, stronger isolation controls, or maximum scalability. | Application code, server, deployment configuration.                        | Hosted infrastructure and scaling.                                                                     |
| **[OSS Deep Agents](/oss/python/deepagents/overview)**       | You want to run the Deep Agents harness in your own environment.                                                               | Everything, including hosting and persistence.                             | Nothing (self-managed).                                                                                |

## Structure your agent project

A Managed Deep Agent is a local project directory. A file's location determines its role: the CLI reads the directory to find the agent entry, managed instructions, skills, connectors, channels, schedules, optional identity, and sandbox configuration, then packages everything into a hosted deployment.

For the full directory layout and packaging rules, see the [CLI project file reference](/langsmith/managed-deep-agents-cli#project-file-reference). For how the CLI compiles this directory and what a deploy creates, see [How Managed Deep Agents work](/langsmith/managed-deep-agents-how-it-works).

## Recommended workflow

1. Install `managed-deepagents` for Python or TypeScript.
2. Create a local code-first agent project with `mda init`.
3. Put the agent system prompt in `instructions.md`.
4. Add authored tools, middleware, schedules, skills, MCP connectors, messaging channels, optional identity, and an optional sandbox.
5. Use `mda dev` to test your agent locally in LangSmith Studio, then `mda deploy` to deploy to LangSmith.
6. Inspect the deployment, traces, and runtime state in LangSmith.

New to Managed Deep Agents? Start with the [quickstart](/langsmith/managed-deep-agents-quickstart), then build a complete agent step by step in the [tutorial](/langsmith/managed-deep-agents-tutorial).

## Beta notes and limits

Operational notes that apply during private beta. Behavior may change before general availability.

### Supported models

Pass model identifiers in the form `{provider}:{model_id}`. For example, `openai:gpt-5.5`. The runtime resolves models with `init_chat_model`, so any provider that `init_chat_model` supports is usable from Managed Deep Agents, as long as the runtime has credentials for that provider. See [Supported providers and models](/oss/python/langchain/models#supported-providers-and-models) for the current list.

Put local keys in `.env`, export them in your shell, or configure them as LangSmith workspace secrets before deploying.

### Context Hub memory

Managed memory lives in the same Context Hub repo as the deployed instructions and skills. The runtime remounts one Hub slice as `/memories/user/` (hot `/memories/user/AGENTS.md`, cold files under that mount) and optional org facts as `/memories/org/` (read-only). Deploy syncs `instructions.md` and `skills/**`, but preserves existing `memories/**` and does not overwrite runtime-created memory. Set `disableMemory: true` or `disable_memory=True` to disable managed memory. For more information about hot/cold tiers, identity remounts, and org memory, see [Memory](/langsmith/managed-deep-agents-memory). To partition memory per caller, see [Identity](/langsmith/managed-deep-agents-identity).

### Rate limits and quotas

During private beta, Managed Deep Agents does not publish per-key, per-workspace, or per-agent request rate limits. For workspace-specific limits, contact your LangChain team at the address in your beta access email.

### Support and feedback

Beta access includes direct support. The contact for bug reports and feature requests is included in the email you receive when access is granted.

### Private beta scope

Managed Deep Agents is available on LangSmith Cloud in the US region only during private beta. Self-hosted and Hybrid deployments are not supported.

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

  <Card title="Memory" icon="brain" href="/langsmith/managed-deep-agents-memory">
    Persist preferences across threads with Context Hub `/memories`.
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

  <Card title="Channels" icon="messages" href="/langsmith/managed-deep-agents-channels">
    Receive Slack Events and reply from messaging channels.
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
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
