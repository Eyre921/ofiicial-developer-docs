---
title: "Build a real-time image generator with Flux"
source: https://docs.together.ai/docs/how-to-build-a-real-time-image-generator
path: docs/how-to-build-a-real-time-image-generator
---

Build a real-time text-to-image app with Juggernaut Lightning Flux, Next.js, and Together AI.

In this guide, we're going to go over how we built [BlinkShot](https://www.blinkshot.io/), an open source app that generates images from text in real time, as you type. It's built with [Juggernaut Lightning Flux](https://www.together.ai/models/juggernaut-lightning-flux) on Together AI, a Flux-based model that returns an image in under two seconds.

<img alt="BlinkShot generating an image as the user types a prompt" />

In this post, you'll learn how to build the core parts of BlinkShot. The app is [open source](https://github.com/Nutlope/blinkshot) and built with Next.js and React Query, but the concepts apply to any language or framework.

## Building the prompt input

The core interaction of BlinkShot is a single textarea where the user describes an image. There's no submit button. Because the model is fast enough to generate images in real time, the app fires a request as the user types:

```tsx theme={null}
function Home() {
  const [prompt, setPrompt] = useState("");

  return (
    <textarea
      rows={4}
      placeholder="Describe your image..."
      value={prompt}
      onChange={(e) => setPrompt(e.target.value)}
    />
  );
}
```

To turn keystrokes into API calls, we use `useQuery` from React Query with the prompt in the `queryKey`. Whenever the prompt changes, React Query runs the query function again:

```tsx theme={null}
const { data: image, isFetching } = useQuery({
  placeholderData: (previousData) => previousData,
  queryKey: [prompt],
  queryFn: async () => {
    const res = await fetch("/api/generateImage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    if (!res.ok) {
      throw new Error(await res.text());
    }

    return (await res.json()) as { b64_json: string };
  },
  enabled: !!prompt.trim(),
  staleTime: Infinity,
  retry: false,
});
```

The `placeholderData` option keeps the previous image on screen while the next one loads, so the UI never flashes empty between generations.

## Generating images in an API route

The query function above calls a Next.js API route. Generating from a server route keeps your Together API key out of the browser. Install the SDK:

```bash theme={null}
npm install together-ai
```

The SDK reads your API key from the `TOGETHER_API_KEY` environment variable, so add it to your `.env.local`:

```bash .env.local theme={null}
TOGETHER_API_KEY=your_api_key
```

Then create the route at `app/api/generateImage/route.ts`. It reads the prompt from the request body and generates an image with Juggernaut Lightning Flux:

```typescript app/api/generateImage/route.ts theme={null}
import Together from "together-ai";

const client = new Together();

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const response = await client.images.generate({
    prompt,
    model: "Rundiffusion/Juggernaut-Lightning-Flux",
    width: 1024,
    height: 768,
    steps: 4,
    response_format: "base64",
  });

  return Response.json(response.data[0]);
}
```

Setting `response_format` to `"base64"` returns the image data inline as `b64_json`, so the frontend can render it immediately with a data URL instead of waiting on a second request to fetch a hosted file:

```tsx theme={null}
{image && (
  <img
    src={`data:image/png;base64,${image.b64_json}`}
    alt={prompt}
    width={1024}
    height={768}
  />
)}
```

At this point the app works end to end: enter a prompt and an image appears.

## Debouncing requests

Firing a request on every keystroke wastes generations on half-typed prompts. To fix this, we debounce the prompt with the `useDebounce` hook from `@uidotdev/usehooks`:

```bash theme={null}
npm install @uidotdev/usehooks
```

```tsx theme={null}
const debouncedPrompt = useDebounce(prompt, 350);
```

Using `debouncedPrompt` in the `queryKey` means the app waits for a 350 millisecond pause in typing before generating:

```tsx theme={null}
const { data: image, isFetching } = useQuery({
  placeholderData: (previousData) => previousData,
  queryKey: [debouncedPrompt],
  // ...
});
```

BlinkShot goes one step further and scales the delay with prompt length, waiting 900 milliseconds after one or two words but only 350 milliseconds once the prompt is longer. Short fragments rarely describe the final image, so there's less value in generating them.

## Tuning quality with `steps`

The `steps` parameter controls how many diffusion steps the model runs. More steps produce more detailed images but take longer, which matters when every keystroke can trigger a generation. Juggernaut Lightning Flux is distilled to produce good images in very few steps, and BlinkShot uses 4 as its balance of quality and speed.

Pricing for Flux models is based on the size of the generated image in megapixels, and generations above the model's default step count cost proportionally more. See [image model pricing](/docs/serverless/models#image-models) for the formula.

## Keeping images consistent with `seed`

By default, every generation starts from random noise, so the same prompt produces a different image each time. Passing a fixed `seed` pins that starting point, so the same prompt and seed reproduce the same image. Repeated runs can differ by a few pixels, but the subject, composition, and details stay the same.

```typescript theme={null}
const response = await client.images.generate({
  prompt,
  model: "Rundiffusion/Juggernaut-Lightning-Flux",
  width: 1024,
  height: 768,
  steps: 4,
  seed: 123,
  response_format: "base64",
});
```

BlinkShot uses this for its consistency mode. With a fixed seed, extending the prompt evolves the previous image instead of replacing it with something unrelated, so "a cat" and then "a cat wearing a hat" look like the same cat.

## Going beyond real-time generation

BlinkShot is open source, so check out the [full code](https://github.com/Nutlope/blinkshot) to see the production details this guide skips, like rate limiting and prompt moderation. When you're ready to generate images in your own apps, [sign up for Together AI](https://togetherai.link) and make your first API call in minutes.

## Next steps

<CardGroup>
  <Card title="FLUX.2 quickstart" icon="bolt" href="/docs/quickstart-flux">
    Generate higher-fidelity images with the latest FLUX.2 model family.
  </Card>

  <Card title="Image generation overview" icon="photo" href="/docs/inference/images/overview">
    Explore every image model and parameter available on Together AI.
  </Card>
</CardGroup>
