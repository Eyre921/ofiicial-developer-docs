---
title: "Set up LangSmith"
source: https://docs.langchain.com/langsmith/platform-setup
path: langsmith/platform-setup
---

Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

<div>
  <div>
    <h1>Set up LangSmith</h1>

    This section covers how to host and manage LangSmith infrastructure for [observability](/langsmith/observability), [evaluation](/langsmith/evaluation), and [prompt engineering](/langsmith/prompt-engineering).

    <h2>Choose how to set up LangSmith</h2>

    Deploy LangSmith in one of two modes:

    <CardGroup>
      <Card title="Cloud" href="/langsmith/cloud" icon="cloud">
        Fully managed observability, evaluation, and prompt engineering.
      </Card>

      <Card title="Self-hosted" href="/langsmith/self-hosted" icon="server">
        **(Enterprise)** Full control with observability, evaluation, and prompt engineering in your infrastructure.
      </Card>
    </CardGroup>

    <Callout>
      Self-hosted is available on the [Enterprise plan](/langsmith/pricing-plans). [Get a demo](https://www.langchain.com/contact-sales) to learn more.
    </Callout>

    <h2>Compare Cloud and Self-hosted</h2>

    | Feature                                          | **Cloud**                           | **Self-hosted**                           |
    | ------------------------------------------------ | ----------------------------------- | ----------------------------------------- |
    | **Infrastructure location**                      | LangChain's cloud                   | Your infrastructure                       |
    | **Who manages updates**                          | LangChain                           | You                                       |
    | **Can deploy agents?**                           | ✅ Yes                               | ✅ Yes (with LangSmith Deployment enabled) |
    | **Observability data location**                  | LangChain cloud                     | Your infrastructure                       |
    | **[Pricing](https://www.langchain.com/pricing)** | Plus tier                           | Enterprise                                |
    | **Best for**                                     | Quick setup, managed infrastructure | Full control, data isolation              |

    <Note>
      To self-host Agent Servers for [LangSmith Deployment](/langsmith/deployment) (which deploys and runs agents in production), refer to the [Hybrid](/langsmith/hybrid) page—a platform setup option that runs Agent Servers in your infrastructure while sending traces to either [Cloud](/langsmith/cloud) or [Self-hosted](/langsmith/self-hosted) LangSmith.
    </Note>

    <h2>Related</h2>

    <CardGroup>
      <Card title="Account setup" href="/langsmith/admin" icon="user-cog">
        Create an account, manage API keys, and choose a pricing tier.
      </Card>

      <Card title="Plans and pricing" href="https://www.langchain.com/pricing" icon="credit-card">
        Compare LangSmith plans and tiers.
      </Card>

      <Card title="Observability" href="/langsmith/observability" icon="chart-line">
        Trace and monitor your LLM applications.
      </Card>
    </CardGroup>
  </div>
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
