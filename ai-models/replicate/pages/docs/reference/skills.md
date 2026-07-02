---
title: "Agent skills"
source: https://replicate.com/docs/reference/skills.md
path: docs/reference/skills
---

[](#what-are-agent-skills)What are agent skills?
------------------------------------------------

Agent skills are markdown instruction files that give coding assistants domain-specific knowledge. They follow the open [Agent Skills](https://agentskills.io) spec and work with tools like [Claude Code](https://claude.ai/code), [OpenCode](https://opencode.ai), [OpenAI Codex](https://openai.com/index/codex/), and others.

Skills are different from [MCP](/docs/reference/mcp). MCP gives your coding assistant tools to call Replicate’s API. Skills give it knowledge about _how to use those tools well_: which models to pick, how to structure prompts, what tradeoffs to consider. They work best together.

[](#replicates-skills)Replicate’s skills
----------------------------------------

Replicate publishes a collection of agent skills covering model discovery, comparison, execution, and prompting:

Skill

What it covers

`find-models`

Searching models, browsing collections, reading schemas, picking the right model

`compare-models`

Evaluating models by cost, speed, quality, and capabilities

`run-models`

Creating predictions, polling, webhooks, streaming, file handling, multi-model workflows

`prompt-images`

Prompting techniques for image generation and editing: photographic language, text rendering, style transfer, character consistency, inpainting

`prompt-videos`

Prompting techniques for video generation: scene description, camera motion, audio and dialogue, time-coded multi-shot prompting, style control

Source code: [github.com/replicate/skills](https://github.com/replicate/skills)

[](#install)Install
-------------------

Install all of Replicate’s skills with one command:

```plaintext
npx skills add replicate/skills
```

This downloads the skill files into your project and registers them with your coding assistant. The `skills` CLI detects which tools you have installed (Claude Code, OpenCode, etc.) and configures them automatically.

[](#update-and-remove)Update and remove
---------------------------------------

To pull the latest versions of all installed skills:

```plaintext
npx skills update
```

To remove Replicate’s skills:

```plaintext
npx skills remove replicate
```

[](#skills-and-mcp)Skills and MCP
---------------------------------

Skills and [MCP](/docs/reference/mcp) are complementary:

*   **MCP** connects your coding assistant to Replicate’s HTTP API, giving it _tools_ to search for models, create predictions, and fetch results.
*   **Skills** give your coding assistant _knowledge_ about how to use those tools effectively: which models to choose, how to write prompts that get good results, and what parameters to tune.

You don’t need both, but they work well together. With MCP alone, your assistant can call the API but may not know which model to pick or how to prompt it. With skills alone, your assistant has the knowledge but would need you to make API calls manually.

Tip

For the best experience, install both the [MCP server](/docs/reference/mcp) and agent skills.
