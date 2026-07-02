---
title: "Image generation with Fal.ai and Trigger.dev Realtime"
source: https://trigger.dev/docs/guides/example-projects/realtime-fal-ai
path: docs/guides/example-projects/realtime-fal-ai
---

This example Next.js project generates an image from a prompt using Fal.ai and shows the progress of the task on the frontend using Trigger.dev Realtime.

## Overview

This full stack Next.js project showcases the following:

* A Trigger.dev task which [generates an image from a prompt using Fal.ai](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/trigger/realtime-generate-image.ts)
* When a [form is submitted](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/page.tsx) in the UI, triggering the task using a [server action](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/actions/process-image.ts)
* Showing the [progress of the task](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/processing/%5Bid%5D/ProcessingContent.tsx) on the frontend using Trigger.dev Realtime. This also includes error handling and a fallback UI
* Once the task is completed, showing the generated image on the frontend next to the original image

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Walkthrough video

This video walks through the process of creating this task in a Next.js project.

<iframe title="Trigger.dev walkthrough" />

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/docs/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/docs/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/docs/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/docs/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API
