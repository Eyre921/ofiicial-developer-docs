---
title: "Build with AI overview"
source: https://docs.netlify.com/build/build-with-ai/overview.md
path: build/build-with-ai/overview
---

---
title: "Overview"
description: "Optimize your AI workflows using Agent Runners, AI Gateway, the Netlify MCP Server, or other AI tools and learn best practices for building with AI whether you are an experienced developer, new to development, or an AI tool builder."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Optimize your AI workflows using Agent Runners, AI Gateway, the Netlify MCP Server, or other AI tools and learn best practices for building with AI whether you are an experienced developer, new to development, or an AI tool builder.

## AI workflows support 

Explore the following AI workflows and resources:
- **[Agent Runners](/build/build-with-ai/agent-runners/overview)**: Create or update projects from the Netlify dashboard. No local setup needed. Netlify runs the AI agent for you.
- **[Agent setup guides](/build/build-with-ai/agent-setup-guides/agent-setup-overview/)**: Guides for connecting Claude Code, Codex, or another AI coding agent to Netlify from your own text editor, terminal, or AI platform.
- **[AI Gateway](/build/ai-gateway/overview)**: Use popular AI models within your project code and connect to them seamlessly without managing API keys.
- **[Troubleshoot and fix failed deploys](/resources/troubleshooting/fix-a-failed-deploy)**: Select the "Why did it fail?" button in the Netlify dashboard to diagnose failed deploys and then use Agent Runners to start your fixes.
- **[Publish an AI code generated project to the web](/start/quickstarts/deploy-from-ai-code-generation-tool)**: You can publish your projects built with an AI code generation tool to the web.

For more info on working with Netlify's AI features, check out these docs:
- [Manage AI features](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features)
- [Security and privacy for AI features](/build/build-with-ai/security-and-privacy-for-ai-features)
- [Pricing for AI features](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/pricing-for-ai-features)

## Building with context

Ensure your AI agents, tools, and workflows always have the right context with the following:
- **[Netlify MCP Server](/build/build-with-ai/agent-setup-guides/agent-setup-overview/#mcp-servers-plugins-and-more)**: Share Netlify context with your AI tools and agents.
- **[Agent setup best practices](/build/build-with-ai/agent-setup-guides/agent-setup-overview/)**: Learn some best practices for setting up agents for Netlify.

If you're building with AI tools, we recommend using context files (sometimes called rule files) based on your AI tool's requirements.

You can also give your AI tools and code agents context from our documentation with Netlify's `llms.txt` file at [https://docs.netlify.com/llms.txt](https://docs.netlify.com/llms.txt).

Learn more in our docs on [agent setup](/build/build-with-ai/agent-setup-guides/agent-setup-overview/).

If you're prototyping with AI tools, check out our [prototyping best practices](/build/build-with-ai/prototyping-best-practices).

## Building AI tools and code agents

Build AI tools and code agents that scale on Netlify with the following:
- **[Build an AI code agent](/extend/building-code-agents/overview)**: Use Netlify's APIs, primitives, and MCP Server to build AI coding agents and tools that work with Netlify projects.
- **[Build your own MCP Server on Netlify](https://developers.netlify.com/guides/write-mcps-on-netlify/)**: Empower AI agents and others to get quick context from your own MCP Server.

If you're building AI tools and code agents, check out our [APIs for code agents](/extend/building-code-agents/apis-for-code-agents) and [general guidelines](/extend/building-code-agents/overview) for building AI tools that work with Netlify.

## Keep your app content accessible to AI search bots and crawlers

If your project is a Single Page Application (SPA), you can set up the Prerender extension to ensure your content is readable by AI agents, AI crawlers, SEO crawlers, and preview services, such as for social media previews. Learn more about Netlify's [Prerender extension](/build/post-processing/prerendering/).

## Block AI crawlers

If you want to prevent AI crawlers and bots from accessing your site, you can use the User Agent Blocker extension and rate limiting to control unwanted traffic. Learn more about [blocking AI crawlers](/build/build-with-ai/block-ai-crawlers).
