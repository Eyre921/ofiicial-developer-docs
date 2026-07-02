---
title: "Next.js Batch LLM Evaluator"
source: https://trigger.dev/docs/guides/example-projects/batch-llm-evaluator
path: docs/guides/example-projects/batch-llm-evaluator
---

This example Next.js project evaluates multiple LLM models using the Vercel AI SDK and streams updates to the frontend using Trigger.dev Realtime.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app with [Prisma](https://www.prisma.io/) for the database.
* Trigger.dev [Realtime](https://trigger.dev/launchweek/0/realtime) to stream updates to the frontend.
* Work with multiple LLM models using the Vercel [AI SDK](https://sdk.vercel.ai/docs/introduction). (OpenAI, Anthropic, XAI)
* Distribute tasks across multiple tasks using the new [`batch.triggerByTaskAndWait`](https://trigger.dev/docs/triggering#batch-triggerbytaskandwait) method.

## GitHub repo

<Card title="View the Batch LLM Evaluator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/batch-llm-evaluator">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* View the Trigger.dev task code in the [src/trigger/batch.ts](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/trigger/batch.ts) file.
* The `evaluateModels` task uses the `batch.triggerByTaskAndWait` method to distribute the task to the different LLM models.
* It then passes the results through to a `summarizeEvals` task that calculates some dummy "tags" for each LLM response.
* We use a [useRealtimeRunsWithTag](/docs/realtime/react-hooks/subscribe#userealtimerunswithtag) hook to subscribe to the different evaluation tasks runs in the [src/components/llm-evaluator.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/llm-evaluator.tsx) file.
* We then pass the relevant run down into three different components for the different models:
  * The `AnthropicEval` component: [src/components/evals/Anthropic.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/Anthropic.tsx)
  * The `XAIEval` component: [src/components/evals/XAI.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/XAI.tsx)
  * The `OpenAIEval` component: [src/components/evals/OpenAI.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/OpenAI.tsx)
* Each of these components then uses [useRealtimeRunWithStreams](/docs/realtime/react-hooks/streams#userealtimerunwithstreams) to subscribe to the different LLM responses.

<Note>
  This example uses the older `useRealtimeRunWithStreams` hook. For new projects, consider using the new [`useRealtimeStream`](/docs/realtime/react-hooks/streams#userealtimestream-recommended) hook (SDK 4.1.0+) for a simpler API and better type safety with defined streams.
</Note>

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/docs/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/docs/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/docs/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/docs/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API
