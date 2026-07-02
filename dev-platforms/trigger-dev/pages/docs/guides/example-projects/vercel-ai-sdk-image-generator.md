---
title: "Vercel AI SDK image generator"
source: https://trigger.dev/docs/guides/example-projects/vercel-ai-sdk-image-generator
path: docs/guides/example-projects/vercel-ai-sdk-image-generator
---

This example Next.js project uses the Vercel AI SDK to generate images from a prompt.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app using [shadcn](https://ui.shadcn.com/) for the UI
* Our 'useRealtimeRun' [React hook](/docs/realtime/react-hooks/subscribe#userealtimerun) to subscribe to the run and show updates on the frontend
* The [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction) to [generate images](https://sdk.vercel.ai/docs/ai-sdk-core/image-generation) using OpenAI's DALL-E models

## GitHub repo

<Card title="View the Vercel AI SDK image generator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* View the Trigger.dev task code which generates the image using the Vercel AI SDK in [src/trigger/realtime-generate-image.ts](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator/src/trigger/realtime-generate-image.ts).
* We use a [useRealtimeRun](/docs/realtime/react-hooks/subscribe#userealtimerun) hook to subscribe to the run in [src/app/processing/\[id\]/ProcessingContent.tsx](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator/src/app/processing/\[id]/ProcessingContent.tsx).

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/docs/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/docs/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/docs/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/docs/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API
