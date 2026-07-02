---
title: "Generate an image from a prompt using Fal.ai and Trigger.dev Realtime"
source: https://trigger.dev/docs/guides/examples/fal-ai-realtime
path: docs/guides/examples/fal-ai-realtime
---

This example task generates an image from a prompt using Fal.ai and shows the progress of the task on the frontend using Trigger.dev Realtime.

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Walkthrough

This video walks through the process of creating this task in a Next.js project.

<iframe title="Trigger.dev walkthrough" />

## Prerequisites

* An existing project
* A [Trigger.dev account](https://cloud.trigger.dev) with Trigger.dev [initialized in your project](/docs/quick-start)
* A [Fal.ai](https://fal.ai/) account

## Task code

This task generates an image from a prompt using Fal.ai.

```ts trigger/fal-ai-image-from-prompt-realtime.ts theme={"theme":"css-variables"}
import * as fal from "@fal-ai/serverless-client";
import { logger, schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const FalResult = z.object({
  images: z.tuple([z.object({ url: z.string() })]),
});

export const payloadSchema = z.object({
  imageUrl: z.string().url(),
  prompt: z.string(),
});

export const realtimeImageGeneration = schemaTask({
  id: "realtime-image-generation",
  schema: payloadSchema,
  run: async (payload) => {
    const result = await fal.subscribe("fal-ai/flux/dev/image-to-image", {
      input: {
        image_url: payload.imageUrl,
        prompt: payload.prompt,
      },
      onQueueUpdate: (update) => {
        logger.info("Fal.ai processing update", { update });
      },
    });

    const $result = FalResult.parse(result);
    const [{ url: cartoonUrl }] = $result.images;

    return {
      imageUrl: cartoonUrl,
    };
  },
});
```

### Testing your task

You can test your task by triggering it from the Trigger.dev dashboard. Here's an example payload:

```json theme={"theme":"css-variables"}
{
  "imageUrl": "https://static.vecteezy.com/system/resources/previews/005/857/332/non_2x/funny-portrait-of-cute-corgi-dog-outdoors-free-photo.jpg",
  "prompt": "Dress this dog for Christmas"
}
```
