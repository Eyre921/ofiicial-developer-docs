---
title: "AI agents overview"
source: https://trigger.dev/docs/guides/ai-agents/overview
path: docs/guides/ai-agents/overview
---

Real world AI agent example tasks using Trigger.dev

## Example projects using AI agents

> **[Claude changelog generator](/docs/guides/example-projects/claude-changelog-generator)**
>
> Automatically generate professional changelogs from git commits using Claude.

> **[Claude GitHub wiki agent](/docs/guides/example-projects/claude-github-wiki)**
>
> Generate and maintain GitHub wiki documentation with Claude-powered analysis.

> **[ClickHouse chat agent](/docs/guides/example-projects/clickhouse-chat-agent)**
>
> Build a chat agent that answers questions about your ClickHouse data with charts, tables and maps
> using `chat.agent()` and generative UI.

> **[Human-in-the-loop workflow](/docs/guides/example-projects/human-in-the-loop-workflow)**
>
> Create audio summaries of newspaper articles using a human-in-the-loop workflow built with
> ReactFlow and Trigger.dev waitpoint tokens.

> **[Mastra agents with memory](/docs/guides/example-projects/mastra-agents-with-memory)**
>
> Use Mastra to create a weather agent that can collect live weather data and generate clothing
> recommendations.

> **[OpenAI Agent Python SDK guardrails](/docs/guides/example-projects/openai-agent-sdk-guardrails)**
>
> Use the OpenAI Agent SDK to create a guardrails system for your AI agents.

> **[OpenAI Agent TypeScript SDK playground](/docs/guides/example-projects/openai-agents-sdk-typescript-playground)**
>
> A playground containing 7 AI agents using the OpenAI Agent SDK for TypeScript with Trigger.dev.

> **[Vercel AI SDK deep research agent](/docs/guides/example-projects/vercel-ai-sdk-deep-research)**
>
> Use the Vercel AI SDK to generate comprehensive PDF reports using a deep research agent.

> **[Smart Spreadsheet](/docs/guides/example-projects/smart-spreadsheet)**
>
> Enrich company data using Exa search and Claude with real-time streaming results.

> **[Batch LLM Evaluator](/docs/guides/example-projects/batch-llm-evaluator)**
>
> Evaluate multiple LLM models in parallel with the Vercel AI SDK and stream the results to a
> Next.js frontend using Trigger.dev Realtime.

> **[Claude thinking chatbot](/docs/guides/example-projects/claude-thinking-chatbot)**
>
> Build a Next.js chatbot that streams Claude's extended thinking to the frontend with the Vercel
> AI SDK and Trigger.dev Realtime.

## Chat agents

Build a durable, multi-turn chat agent with [`chat.agent()`](/docs/ai-chat/overview). A durable session per conversation, with streaming and resumability handled for you.

> **[Chat agent](/docs/guides/ai-agents/chat-agent)**
>
> Create a durable, multi-turn chat agent with `chat.agent()`, then add tools to it.

> **[ElevenLabs Voice agent](/docs/guides/example-projects/elevenlabs-voice-agent)**
>
> Build a spoken-conversation voice assistant on `chat.agent()`, with streaming speech-to-text and
> text-to-speech from ElevenLabs and server-side voice activity detection.

> **[Ask Trigger chat agent](/docs/guides/example-projects/ask-trigger-chat-agent)**
>
> Build a chat agent that teaches Trigger.dev with interactive node-graphs, quizzes and cards,
> using `chat.agent()`, generative UI and live docs grounding through an MCP server.

## Agent fundamentals

These guides will show you how to set up different types of AI agent workflows with Trigger.dev. The examples take inspiration from Anthropic's blog post on [building effective agents](https://www.anthropic.com/research/building-effective-agents).

> **[Prompt chaining](/docs/guides/ai-agents/generate-translate-copy)**
>
> Chain prompts together to generate and translate marketing copy automatically

> **[Routing](/docs/guides/ai-agents/route-question)**
>
> Send questions to different AI models based on complexity analysis

> **[Parallelization](/docs/guides/ai-agents/respond-and-check-content)**
>
> Simultaneously check for inappropriate content while responding to customer inquiries

> **[Orchestrator](/docs/guides/ai-agents/verify-news-article)**
>
> Coordinate multiple AI workers to verify news article accuracy

> **[Evaluator-optimizer](/docs/guides/ai-agents/translate-and-refine)**
>
> Translate text and automatically improve quality through feedback loops
