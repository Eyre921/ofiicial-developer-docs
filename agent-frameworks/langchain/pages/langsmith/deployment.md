---
title: "LangSmith Deployment"
source: https://docs.langchain.com/langsmith/deployment
path: langsmith/deployment
---

Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.

LangSmith Deployment is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment.

## Deployable products

LangSmith Deployment is framework-agnostic which means you can deploy agents built with:

<CardGroup>
  <Card title="LangGraph (and LangChain)" href="/langsmith/deployment-quickstart" icon="chart-dots-3">
    Use the LangGraph CLI and app templates to deploy a LangGraph application to LangSmith.
  </Card>

  <Card title="Google ADK" href="/langsmith/deploy-google-adk" icon="google">
    Deploy Google Agent Development Kit (ADK) agent as a LangGraph with the `deployments-wrap-sdk` package.
  </Card>

  <Card title="Other frameworks" href="/langsmith/deploy-other-frameworks" icon="packages">
    Deploy Claude Agent SDK, Strands, CrewAI, AutoGen, and other agent frameworks with the Functional API or `deployments-wrap-sdk`.
  </Card>

  <Card title="Managed Deep Agents" href="/langsmith/managed-deep-agents-overview" icon="robot">
    Deploy code-first Deep Agents with the Managed Deep Agents CLI private beta.
  </Card>
</CardGroup>

## Deployment environments

You can run the same [Agent Server](/langsmith/agent-server) runtime in several hosting models. A **standalone server** is the lightest option: you run containers yourself without the LangSmith [control plane](/langsmith/control-plane). For managed deployments through the UI and APIs, use **Cloud** or **Self-hosted** (full platform in your infrastructure).

<CardGroup>
  <Card title="Cloud" href="/langsmith/deploy-to-cloud" icon="cloud">
    Fully managed by LangChain, running on AWS and GCP. Create deployments from GitHub in the LangSmith UI or with [`langgraph deploy`](/langsmith/cli#deploy). Requires a [Plus plan or above](https://www.langchain.com/pricing).
  </Card>

  <Card title="Standalone server" href="/langsmith/deploy-standalone-server" icon="server">
    Deploy Agent Server with Docker, Compose, or Kubernetes. Bring your own PostgreSQL, Redis, and LangSmith license; no control plane. Optional [LangSmith tracing](/langsmith/observability) to Cloud or a self-hosted instance.
  </Card>

  <Card title="Self-hosted" href="/langsmith/self-hosted" icon="buildings">
    Run the full LangSmith platform, including the control plane and data plane, in your cloud (for example on Kubernetes). Requires [Enterprise plan](https://www.langchain.com/pricing). Integrates observability, evaluation, and agent deployment in one private stack.
  </Card>
</CardGroup>

For a feature-level comparison and infrastructure setup, see [Platform setup](/langsmith/platform-setup).

## After deployment

Once deployed, agents work with [Agent Server](/langsmith/assistants)'s execution model: **assistants** for configuration, **threads** for state, and **runs** for workloads. For capabilities, tutorials, server customization, and operations, see [Develop agents](/langsmith/develop-agents-overview).

<CardGroup>
  <Card title="Find and fix failures with Engine" icon="https://mintcdn.com/langchain-5e9cc07a/oHF6ZolKSFmH17u5/images/brand/engine-icon-dark.png?fit=max&auto=format&n=oHF6ZolKSFmH17u5&q=85&s=739a487161804691a14c36c2768d278d" href="/langsmith/engine-overview">
    Once agents are in production, use LangSmith Engine to detect recurring failures in their traces, diagnose root causes, and resolve them.
  </Card>

  <Card title="Interact with your deployment using RemoteGraph" icon="link" href="/langsmith/use-remote-graph">
    Call your deployed graph from client code as if it were a local compiled graph.
  </Card>
</CardGroup>

## Full-stack web apps

Ship a LangChain.js agent and chat UI together as a single web app. The Vite example uses LangSmith Deployment as the agent backend behind a separate UI. Other examples embed the agent inside the web framework's route handlers and ship to the host platform.

<Card title="Full-stack web apps" href="/langsmith/deploy-frameworks-and-platforms" icon="code">
  Ship a LangChain.js chat app: embed the agent in Next.js, SvelteKit, Nuxt, Cloudflare Workers, or Deno Deploy (no Agent Server required), or pair LangSmith Deployment with a Vite + React UI.

  <div>
    <span>
      <img alt="LangSmith" />
    </span>

    <span>
      <img alt="Next.js" />
    </span>

    <span>
      <img alt="SvelteKit" />
    </span>

    <span>
      <img alt="Nuxt" />
    </span>

    <span>
      <img alt="Cloudflare Workers" />
    </span>

    <span>
      <img alt="Deno Deploy" />
    </span>
  </div>
</Card>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
