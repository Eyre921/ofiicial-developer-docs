---
title: "Agent Runners overview"
source: https://docs.netlify.com/build/build-with-ai/agent-runners/overview.md
path: build/build-with-ai/agent-runners/overview
---

---
title: "Agent Runners overview"
description: "Learn about Agent Runners and how to use them to optimize your AI workflows."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Prompt AI agents to [create a new project](/start/quickstarts/create-new-project-with-ai-agent/), fix, update, ship code and ask questions about your project using your unique project context directly from your Netlify dashboard.

Without any extra setup or additional accounts, Agent Runners offer advantages over running AI agents in other environments by giving secure access to your Netlify project context, deployment pipeline, build settings, and more. This enables you and your team to optimize AI workflows for your Netlify projects.

> **Pricing Information:** This feature is available on Credit-based plans only, including the [Free, Personal, and Pro](https://www.netlify.com/pricing) plans. If you are on an Enterprise plan and you're interested, reach out to your Account Manager.

Agent Runners offer agents unique advantages on Netlify's platform with the following: 
   - [create a new project](/start/quickstarts/create-new-project-with-ai-agent/) with an AI agent from your own prompt or a starter prompt 
   - no technical background needed to run the most powerful agents for building
   - access to your Netlify project's context, environment variables, build settings, and deployment pipeline
   - no additional setup or extra accounts needed
   - quick access from your mobile phone
   - staging environments to preview changes
   - staging environments with and without Git version control
   - rollback capabilities
   - consistent production and staging environments
   - log tracking with role-based access control

> **Video**: [Watch video](https://www.youtube.com/embed/u3mR7Me3lPw?si)

## Use cases 

Agent Runners are optimized for the following use cases:
   - Async-friendly or background tasks, such as maintenance tasks, including fixing broken links, redirects, and updating feature flag code
   - Quick fixes, such as bugs, typos, and well-defined backlog items
   - Well-defined content updates from your entire team, including Marketing, Design, and Content teams
   - On-the-go changes from your mobile phone
   - Jumpstart platform primitives with automated setup
   - Jumpstart customizable features with code, such as Netlify forms
   - Quick new pages, such as landing pages, maintenance pages, 404 pages, etc.

Get more ideas for use cases and practical guidance from our [prompt examples](/build/build-with-ai/agent-runners/prompt-examples-for-agent-runners).

You can use Agent Runners to make changes to projects you published using the Netlify drag and drop publisher. Learn more about [iterating on projects published with Netlify Drop](/start/quickstarts/netlify-drop-quickstart/).

> **Video**: [Watch video](https://www.youtube.com/embed/v774j5xLPtA?si)

## Supported AI agents

Agent Runners support the following AI agents:
   - Claude Code
   - OpenAI Codex 
   - Google Gemini

## Agent run modes

When you start an agent run, you can select a mode from the dropdown:

   - **Build** (default): The agent makes changes to your code and creates a Deploy Preview so you can review and ship the results.
   - **Ask**: The agent answers questions about your project without making any changes to your code or creating a Deploy Preview. Use Ask mode to explore or understand a project before you make changes.

Both modes are available for all supported AI agents.

Learn more about starting a run in each mode in [Make changes with Agent Runners](/build/build-with-ai/agent-runners/make-changes-with-agent-runners/#1-start-an-agent-run).

## Requirements

To use Agent Runners, you must meet the following requirements: 
   - Your Netlify team must have a Credit-based plan.
   - You must have one of the following roles on a Netlify team with a Credit-based plan: 
      - Team Owner
      - Developer
      - [Internal Builder](/manage/accounts-and-billing/team-management/roles-and-permissions#internal-builder)
      - Publisher
   - Your Netlify Team Owner must keep AI features turned on. AI features are on by default for all Credit-based Free, Personal, and Pro plans.
   - Your Netlify team must have credits available to use an Agent Runner.

Learn more about [enabling or disabling Netlify AI features](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features).

## How pricing works

Agent runs use your pricing plan credits and these usage meters:
- AI inference
- Compute

You can view the Netlify credits used for an individual agent run by expanding it in the agent run detail view.  This credit usage summary shows you the credits used by the AI inference usage meter.

Learn more in [Make changes with Agent Runners](/build/build-with-ai/agent-runners/make-changes-with-agent-runners/#2-check-the-status-of-your-agent-run).

To learn more about how pricing works for Agent Runners, check out [Pricing for AI features](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/pricing-for-ai-features).

For example, if you run an agent through Netlify to fix a failed deploy, your usage of [web requests](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/#credit-usage-for-web-requests), [bandwidth](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/#credit-usage-for-bandwidth), and [compute](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/#credit-usage-for-compute) will be calculated and applied to your credit balance.

If you publish a production deploy, then the production deploy credit costs will apply. Learn more about [production deploy costs](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/#credit-usage-for-production-deploys).

Note that failed deploys do not use credits.

## Use Agent Runners

1. Go to your Netlify project dashboard under **Build with an AI agent**, select your preferred AI agent, such as Claude Code, Google Gemini, or OpenAI Codex, enter your prompt and optionally add any additional context. Then choose **Run task**.
  ![Build with an AI agent from project overview](/images/build-with-an-ai-agent-from-project-overview.png)

To check out the fuller process of prompting and reviewing agent run results, check out [Make changes with Agent Runners](/build/build-with-ai/agent-runners/make-changes-with-agent-runners).

You can also check out example prompts in our [prompt examples](/build/build-with-ai/agent-runners/prompt-examples-for-agent-runners).

### Agent runs for different branches

By default, Agent Runners work on a new automated custom branch created off your [production branch](/deploy/deploy-types/production-deploy/).

To use Agent Runners for a [branch deploy](/deploy/deploy-types/branch-deploys/), you can choose a branch deploy branch from the Netlify UI or specify the branch deploy branch with `--branch` when using the [Netlify CLI](https://cli.netlify.com/commands/agents/#agentscreate).

You can also start an agent run from any deploy details page. From your project's **Deploys** tab, open a deploy and select **Run AI agent**. If your project is connected to a Git remote repository, the agent run will use that deploy's branch as the base branch.

![Run AI agent button on deploy details page](/images/run-agent-button.png)

To learn more about different types of deploys and branch types, check out our [deploy docs](/deploy/deploy-overview).

### Redeploy an agent run

After a successful agent run, you or a team member may update your site's environment variables or build settings. To see these changes reflected in your agent run's Deploy Preview, you can redeploy the agent run. This rebuilds the Deploy Preview with your updated configuration without re-running the AI agent and costing you more AI inference credits.

Redeploying a Deploy Preview from an agent run is useful when you or someone on your Netlify team changes your site configuration.

For example, when updates are made to the following:
   - changes to environment variables that your site needs at build time or runtime
   - updates to your build configuration or build commands

To redeploy an agent run:

1. From your Netlify project dashboard, go to your project's 
### NavigationPath Component:

Agent runs
 page.
2. Find the completed agent run you want to redeploy.
3. On the far right of the agent run, select the hamburger icon menu, then choose **Redeploy**.

The redeploy creates a new agent run session that applies the same code changes from your original agent run but builds with your updated site configuration. Because the AI agent does not re-run, redeployments are faster than the original agent run and don't use credits for AI inference like other agent runs.

### Note

You can only redeploy an agent run that has completed successfully and made file changes. You cannot redeploy while another agent run is actively in progress from the same starting Agent Runners task. An Agent Runners starting task can have several agent runs.

### Limitations

If your project is set up with continuous deployment through a connection to a Git provider, then Agent Runners will only work with your project if it is using GitHub as a Git provider. You cannot use Agent Runners with projects connected to Git repositories hosted on GitLab, Bitbucket, or Azure DevOps.

Agent Runners are not compatible with [Split Testing](/manage/monitoring/split-testing/). If your site has Split Testing enabled, you must disable it before using Agent Runners.

### Troubleshoot with Agent Runners

When a deploy fails, you can use Agent Runners to start fixing the issue directly from your failed deploy details page.

![Fix with Agent Runners](/images/fix-with-agent.png)

### Prompt examples 

For practical prompt examples, check out our [Agent Runners prompt examples](/build/build-with-ai/agent-runners/prompt-examples-for-agent-runners).

