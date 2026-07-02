---
title: "Build a website with vinext"
source: https://replicate.com/docs/guides/run/vinext.md
path: docs/guides/run/vinext
---

[vinext](https://github.com/cloudflare/vinext) is a drop-in replacement for Next.js, built on [Vite](https://vite.dev/), that deploys to Cloudflare Workers with a single command. Read the [Cloudflare blog post](https://blog.cloudflare.com/vinext) for the full story.

In this guide, you’ll build a vinext web app that uses Replicate to generate images with [FLUX.2 \[klein\]](https://replicate.com/black-forest-labs/flux-2-klein-9b), then deploy it to Cloudflare Workers.

Tip

The completed project is on GitHub at [replicate/getting-started-vinext](https://github.com/replicate/getting-started-vinext).

[](#prerequisites)Prerequisites
-------------------------------

*   **Node.js**: Download and install it from [nodejs.org](https://nodejs.org/).
*   **[A Replicate account](https://replicate.com/signin)**: Free to get started. After your initial credit, you pay per second. See [how billing works](/docs/billing).
*   **[A GitHub account](https://github.com)**: For hosting your source code.
*   **[A Cloudflare account](https://dash.cloudflare.com/sign-up)**: For deploying your app to Cloudflare Workers.

[](#step-1-clone-the-starter-app)Step 1: Clone the starter app
--------------------------------------------------------------

Clone the getting-started repo and install dependencies:

```shell
git clone https://github.com/replicate/getting-started-vinext
cd getting-started-vinext
npm install
```

[](#step-2-configure-your-environment)Step 2: Configure your environment
------------------------------------------------------------------------

You need a Replicate API token to run models. Generate one at [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens) and copy it.

vinext runs on Cloudflare’s [workerd](https://github.com/cloudflare/workerd) runtime, which reads secrets from a `.dev.vars` file during local development (instead of `.env.local` like Next.js):

```shell
echo "REPLICATE_API_TOKEN=r8_..." > .dev.vars
```

Replace `r8_...` with your actual token. The `.dev.vars` file is git-ignored, so your token stays out of source control.

[](#step-3-run-the-app-locally)Step 3: Run the app locally
----------------------------------------------------------

Start the development server:

```shell
npm run dev
```

Open [localhost:5173](http://localhost:5173) in your browser. You should see the starter app with a text prompt form.

[](#step-4-explore-the-backend)Step 4: Explore the backend
----------------------------------------------------------

vinext uses the same file-based routing as Next.js. Files named `route.ts` in the `app/` directory are server-side API endpoints, and files named `page.tsx` are frontend components.

The starter app has two API routes that talk to Replicate.

### [](#creating-predictions)Creating predictions

`app/api/predictions/route.ts` handles POST requests to create a new prediction. It calls Replicate to run FLUX.2 \[klein\] with the user’s prompt:

```typescript
import { NextResponse } from "next/server";
import Replicate from "replicate";
const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});
// In production, WORKER_URL should be set to the Worker's public URL.
// In development, use NGROK_HOST for webhook tunneling.
const WEBHOOK_HOST = process.env.WORKER_URL ?? process.env.NGROK_HOST;
export async function POST(request: Request) {
  if (!process.env.REPLICATE_API_TOKEN) {
    throw new Error(
      "The REPLICATE_API_TOKEN environment variable is not set. See README.md for instructions on how to set it."
    );
  }
  const { prompt } = await request.json();
  const options: {
    model: string;
    input: { prompt: string };
    webhook?: string;
    webhook_events_filter?: string[];
  } = {
    model: "black-forest-labs/flux-2-klein-9b",
    input: { prompt },
  };
  if (WEBHOOK_HOST) {
    options.webhook = `${WEBHOOK_HOST}/api/webhooks`;
    options.webhook_events_filter = ["start", "completed"];
  }
  const prediction = await replicate.predictions.create(options);
  if (prediction?.error) {
    return NextResponse.json({ detail: prediction.error }, { status: 500 });
  }
  return NextResponse.json(prediction, { status: 201 });
}
```

Note how the `import` paths still use `next/server` — vinext reimplements these modules so your existing Next.js code works without changes.

### [](#polling-for-results)Polling for results

`app/api/predictions/[id]/route.ts` handles GET requests to check on a prediction’s status. The `[id]` in the path is a [dynamic route segment](https://nextjs.org/docs/routing/dynamic-routes), just like in Next.js:

```typescript
import { NextResponse } from "next/server";
import Replicate from "replicate";
const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});
export async function GET(
  _request: Request,
  context: { params: Promise<{ id: string }> }
) {
  const { id } = await context.params;
  const prediction = await replicate.predictions.get(id);
  if (prediction?.error) {
    return NextResponse.json({ detail: prediction.error }, { status: 500 });
  }
  return NextResponse.json(prediction);
}
```

[](#step-5-explore-the-frontend)Step 5: Explore the frontend
------------------------------------------------------------

The app uses [@tanstack/react-query](https://tanstack.com/query) for data fetching and polling. The root layout wraps the app in a `QueryClientProvider` via `app/providers.tsx`:

```tsx
"use client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
const queryClient = new QueryClient();
export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
```

`app/page.tsx` is the main page component. It uses `useMutation` to create a prediction and `useQuery` to poll until the image is ready:

```tsx
"use client";
import { useEffect, useRef, useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import Image from "next/image";
interface Prediction {
  id: string;
  status: string;
  output?: string[];
  detail?: string;
  error?: string;
}
async function createPrediction(prompt: string): Promise<Prediction> {
  const response = await fetch("/api/predictions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  const prediction = await response.json();
  if (response.status !== 201) {
    throw new Error(prediction.detail ?? "Something went wrong");
  }
  return prediction;
}
async function fetchPrediction(id: string): Promise<Prediction> {
  const response = await fetch(`/api/predictions/${id}`);
  const prediction = await response.json();
  if (response.status !== 200) {
    throw new Error(prediction.detail ?? "Something went wrong");
  }
  return prediction;
}
export default function Home() {
  const [predictionId, setPredictionId] = useState<string | null>(null);
  const promptInputRef = useRef<HTMLInputElement>(null);
  useEffect(() => {
    promptInputRef.current?.focus();
  }, []);
  const mutation = useMutation({
    mutationFn: createPrediction,
    onSuccess: (data) => setPredictionId(data.id),
  });
  const { data: prediction } = useQuery({
    queryKey: ["prediction", predictionId],
    queryFn: () => fetchPrediction(predictionId!),
    enabled: !!predictionId,
    refetchInterval: (query) => {
      const status = query.state.data?.status;
      return status === "succeeded" || status === "failed" ? false : 250;
    },
  });
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const prompt = formData.get("prompt") as string;
    mutation.mutate(prompt);
  };
  const error = mutation.error?.message ?? (prediction?.status === "failed" ? prediction.error : null);
  return (
    <div className="container max-w-2xl mx-auto p-5">
      <h1 className="py-6 text-center font-bold text-2xl">
        Dream something with{" "}
        <a href="https://replicate.com/black-forest-labs/flux-2-klein-9b?utm_source=project&utm_project=getting-started">
          FLUX.2 [klein]
        </a>
      </h1>
      <form className="w-full flex" onSubmit={handleSubmit}>
        <input
          type="text"
          className="flex-grow"
          name="prompt"
          placeholder="Enter a prompt to display an image"
          ref={promptInputRef}
        />
        <button className="button" type="submit">
          Go!
        </button>
      </form>
      {error && <div>{error}</div>}
      {prediction && (
        <>
          {prediction.output && (
            <div className="image-wrapper mt-5">
              <Image
                fill
                src={prediction.output[prediction.output.length - 1]}
                alt="output"
                sizes="100vw"
              />
            </div>
          )}
          <p className="py-3 text-sm opacity-50">
            status: {prediction.status}
          </p>
        </>
      )}
    </div>
  );
}
```

This is standard React — the same component would work in a regular Next.js app. The only thing talking to Replicate is the server-side route handler; the frontend just calls your own API routes.

[](#step-6-explore-the-vinext-specific-config)Step 6: Explore the vinext-specific config
----------------------------------------------------------------------------------------

A few files in the project are specific to vinext and Cloudflare Workers. You don’t need to modify these to get started, but it helps to know what they do.

`vite.config.ts` is the Vite configuration. It loads the vinext plugin and the Cloudflare plugin:

```typescript
import { defineConfig } from "vite";
import vinext from "vinext";
import { cloudflare } from "@cloudflare/vite-plugin";
export default defineConfig({
  plugins: [
    vinext(),
    cloudflare({
      viteEnvironment: {
        name: "rsc",
        childEnvironments: ["ssr"],
      },
    }),
  ],
});
```

`wrangler.jsonc` configures the Cloudflare Worker, including an [Images binding](https://developers.cloudflare.com/images/) for image optimization:

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "getting-started-vinext",
  "compatibility_date": "2026-02-12",
  "compatibility_flags": ["nodejs_compat"],
  "main": "./worker/index.ts",
  "preview_urls": true,
  "assets": {
    "not_found_handling": "none",
    "binding": "ASSETS"
  },
  "images": {
    "binding": "IMAGES"
  }
}
```

`worker/index.ts` is the Worker entry point. It handles image optimization requests via Cloudflare Images and delegates everything else to vinext:

```typescript
import { handleImageOptimization } from "vinext/server/image-optimization";
import handler from "vinext/server/app-router-entry";
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/_vinext/image") {
      return handleImageOptimization(request, {
        fetchAsset: (path) =>
          env.ASSETS.fetch(new Request(new URL(path, request.url))),
        transformImage: async (body, { width, format, quality }) => {
          const result = await env.IMAGES.input(body)
            .transform(width > 0 ? { width } : {})
            .output({ format, quality });
          return result.response();
        },
      });
    }
    return handler.fetch(request);
  },
};
```

`next.config.ts` configures image remote patterns, just like a regular Next.js app:

```typescript
const nextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "replicate.com",
      },
      {
        protocol: "https",
        hostname: "replicate.delivery",
      },
      {
        protocol: "https",
        hostname: "*.replicate.delivery",
      },
    ],
  },
};
export default nextConfig;
```

[](#step-7-create-a-prediction)Step 7: Create a prediction
----------------------------------------------------------

Your app should be running at [localhost:5173](http://localhost:5173). Enter a prompt and hit “Go!” to generate an image.

![screenshot of the app generating an iguana](https://github.com/replicate/getting-started-vinext/raw/main/public/screenshot.png)

[](#step-8-publish-to-github)Step 8: Publish to GitHub
------------------------------------------------------

Commit your changes and push to a new GitHub repository. You can use GitHub’s [`gh` CLI](https://cli.github.com/):

```shell
git add .
git commit -m "First working version"
gh repo create my-replicate-app --public --push --source=.
```

[](#step-9-deploy-to-cloudflare-workers)Step 9: Deploy to Cloudflare Workers
----------------------------------------------------------------------------

First, log in to Cloudflare:

```shell
npx wrangler login
```

Then build and deploy:

```shell
npm run deploy
```

This runs `vinext deploy`, which builds the app and deploys it to Cloudflare Workers in a single step.

After deploying, set your Replicate API token as a secret so the production app can use it:

```shell
npx wrangler secret put REPLICATE_API_TOKEN
```

Paste your token when prompted. Your app is now live on Cloudflare Workers.

[](#next-steps)Next steps
-------------------------

You now have a working web app powered by machine learning, deployed to the edge on Cloudflare Workers.

Here are some ideas for what to do next:

*   Update your app to [request and receive webhooks](/docs/webhooks) so you can do things like store prediction metadata in a database. See the [webhooks docs in the getting-started-vinext repo](https://github.com/replicate/getting-started-vinext?tab=readme-ov-file#webhooks).
*   Fine-tune and deploy [your own custom Flux model](/docs/get-started/fine-tune-with-flux) and use your new website to show it off.
*   Integrate a [super resolution model](https://replicate.com/collections/super-resolution) to upscale generated images.
*   [Explore other models on Replicate](https://replicate.com/explore) and integrate them into your app.
*   Add a [custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) to your Cloudflare Worker.
