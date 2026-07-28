---
title: "Make changes with Agent Runners"
source: https://docs.netlify.com/build/build-with-ai/agent-runners/make-changes-with-agent-runners.md
path: build/build-with-ai/agent-runners/make-changes-with-agent-runners
---

---
title: "Make changes with Agent Runners"
description: "Learn how to use Agent Runners to build and iterate."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Learn how to make changes and iterate on an existing project with your preferred AI agent using Agent Runners.

## Prerequisites

Before you begin, you must have the following: 
- a Netlify team account with a Credit-based plan and some available credits
- a Team Owner, Developer, [Internal Builder](/manage/accounts-and-billing/team-management/roles-and-permissions#internal-builder), or Publisher role on your Netlify team
- [Netlify AI features enabled](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features)

## Agent run modes

When you start an agent run, you select a mode that determines what the agent does with your prompt. Both modes are available for all supported AI agents.

### Build mode

Build mode is the default. The agent makes changes to your project's files and code based on your prompt and creates a [Deploy Preview](/deploy/compare-preview-options) so you can review the results before you ship them. Use Build mode when you want the agent to fix, update, or add code, such as fixing a bug, updating content, or creating a new landing page.

### Ask mode

In Ask mode, the agent answers questions about your project without making any changes to your code or creating a Deploy Preview. Use Ask mode to explore or understand a project before you make changes, such as learning how a feature works or planning an approach before you switch to Build mode.

Ask mode is read-only: the agent can read your whole project but can't edit files, run commands, deploy, or configure settings for you. Get the most out of Ask mode with prompts that investigate, explain, diagnose, or produce a plan:

- **Scope the question**: choose a specific feature, file, or symptom instead of the whole project.
- **Name the output you want**:  a list of files, a root cause, or a step-by-step plan.
- **Ask for understanding or a plan**: To change code, switch to Build mode.

#### Example prompts

- **Understand how authentication works:**
  > Walk me through how authentication is implemented in this project. Which files handle it, and where is the token stored?
- **Inventory work before a migration:**
  > Plan out how we can migrate to the latest version of Astro.
- **Generate a spec to hand to a Build mode run:**
  > Describe in detail how our main site handles builds that require a build step, so I can instruct another agent run to implement the same flow on our marketing site.
- **Think through an architecture or design decision:**
  > How would you architect a system for configuring MCP servers that works across multiple AI agents?
- **Ask questions about your database:**
  > Which data fields are required to add a new entry to the users list?

## Overview

This guide will help you make changes to an existing project through Agent Runners in your Netlify project dashboard.

If you want to create a new project with an AI agent, check out our [Agent Runners quickstart for new projects](/start/quickstarts/create-new-project-with-ai-agent/).

### 1. Start an agent run

To start an agent run to make changes to your project, follow these steps:

1. Go to your Netlify project dashboard. Under **Build with an AI agent**, select your preferred AI agent, such as Claude Code, Google Gemini, or OpenAI Codex.
  ![Empty prompt field on Project overview page](/images/build-with-an-ai-agent-from-project-overview.png)
2. Add your prompt. For examples of prompts, check out our [prompt examples](/build/build-with-ai/agent-runners/prompt-examples-for-agent-runners). You can optionally add more context as a file or image. Or you can add project context that applies to all agent runs, such as project-specific prompt guidelines or a link to a publicly available design system or style guide. 
3. Select a mode from the mode dropdown. To make changes, use the default **Build** mode so your agent can make code or file changes. To get answers or make plans without changing your project, use  **Ask** mode. For details, see [Agent run modes](#agent-run-modes).
4. Choose **Run task**. 
5. Your chosen AI agent will complete the task asynchronously and notify you when it's done. At this point, you can wait or take care of other tasks.

### Note

Because Ask mode doesn't change your code, the steps below for previewing and shipping updates apply only to Build mode runs.

### 2. Check the status of your agent run

To check the status of your agent run, go to the **Agent Runs** tab in your Netlify project dashboard. Then choose your agent run and check the log for the current status.

You can expand an individual agent run to view its credit usage. Note that credit usage for a run may take a brief moment to appear after the run begins. Learn more in [how pricing works](/build/build-with-ai/agent-runners/overview/#how-pricing-works).

### 3. Preview Agent Runners updates 

To preview your agent run's proposed updates, check out the **Files changed** tab, which shows you the changes that the agent made. 

You can also preview your agent run's proposed updates in a preview environment by choosing **Open preview**, which opens a [Deploy Preview](/deploy/compare-preview-options) of your changes. The Deploy Preview URL for agent runs uses the format `https://agent-[run-id]--my-site.netlify.app`.

  ![Open preview button highlighted for agent run](/images/open-preview-button-for-agent-run.png)

If your project is connected to a GitHub repository, then you can optionally open up a pull request or update an existing pull request with your updates from your agent run.

### 4. Ship your agent run updates

To ship your agent run updates, you have two options: 
   - **For projects using Git & GitHub:** Open a pull request or update an existing pull request with your updates from your agent run. When you merge your pull request into your production branch, Netlify publishes your changes to your production site for you.
   - **For projects without Git:** If you have publishing permission, you'll find a **Publish** button on your Netlify project's Agent Runs dashboard. Select **Publish** to make your agent run updates go live in the latest production version of your project.

