---
title: "Build a chat API on Render"
source: https://docs.together.ai/docs/render-chat-api
path: docs/render-chat-api
---

Deploy an authenticated single-turn chat API backed by Together AI to a Render web service.

<Tip>Using a coding agent? Load the [together-chat-completions](https://github.com/togethercomputer/skills/tree/main/skills/together-chat-completions) skill to teach your agent to write correct chat completions code for Together AI. [Learn more](/docs/agent-skills).</Tip>

This guide walks through building and deploying a single-turn chat API. You will create a small web service that accepts an authenticated `POST /chat` request, forwards the message to Together AI's chat completions API, and returns the model's reply as JSON. You can follow the guide in TypeScript with Express or in Python with FastAPI.

Both versions call `https://api.together.ai/v1/chat/completions`, default to Qwen3.5 9B, expose an unauthenticated `GET /health` endpoint for Render health checks, protect `POST /chat` with a separate bearer token, and stop an inference request after 60 seconds.

## Architecture

<Frame>
  <img alt="A trusted client sends an authenticated POST /chat request to the Render web service, which calls Together AI and returns the reply, model ID, and token usage. CHAT_API_KEY authenticates the caller on the first hop, and TOGETHER_API_KEY stays inside the service." />
</Frame>

Each request follows four steps. The client sends a bearer token and a message to the Render service. The service validates both. The service sends one chat completion request to Together AI. The service returns the reply, model ID, and token usage to the client.

The service uses two separate secrets. `CHAT_API_KEY` authenticates the caller, and `TOGETHER_API_KEY` authenticates the server-to-server request to Together AI.

## Prerequisites

Before you start, make sure you have:

* A [Together AI account](https://api.together.ai/) with an [active credit balance](/docs/billing-credits).
* A [project-scoped Together API key](/docs/api-keys-authentication).
* A [Render account](https://dashboard.render.com/register).
* A GitHub, GitLab, or Bitbucket account.
* Node.js 22 through 24 for the TypeScript path, or Python 3.10 or later for the Python path.

You also need a secret that callers will use to authenticate with your chat API. Generate one and save it in a password manager:

```bash Shell theme={null}
openssl rand -hex 32
```

This value becomes `CHAT_API_KEY`. It is different from your `TOGETHER_API_KEY`.

<Warning>
  The shared `CHAT_API_KEY` is a minimal guard for a server-to-server demo. Do not embed it in browser or mobile application code. For a public application, add user authentication, per-user authorization, and rate limits.
</Warning>

## Step 1: Create the project

Create a new directory and initialize a Git repository:

```bash Shell theme={null}
mkdir together-render-chat
cd together-render-chat
git init
```

Create a subdirectory for the runtime you want to use. You only need the files for the path you select.

<CodeGroup>
  ```bash TypeScript theme={null}
  mkdir ts
  cd ts
  ```

  ```bash Python theme={null}
  mkdir python
  cd python
  ```
</CodeGroup>

For the TypeScript path, create `package.json`:

```json ts/package.json theme={null}
{
  "name": "together-render-chat",
  "private": true,
  "type": "module",
  "engines": {
    "node": ">=22 <25"
  },
  "scripts": {
    "build": "tsc",
    "start": "node dist/server.js"
  },
  "dependencies": {
    "express": "^5.2.1"
  },
  "devDependencies": {
    "@types/express": "^5.0.6",
    "@types/node": "^24.13.3",
    "typescript": "^7.0.2"
  }
}
```

Then create `tsconfig.json`:

```json ts/tsconfig.json theme={null}
{
  "compilerOptions": {
    "outDir": "dist",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "target": "ES2023",
    "strict": true,
    "skipLibCheck": true
  }
}
```

Install the dependencies and compile the project:

```bash Shell theme={null}
npm install
npm run build
cd ..
```

Commit the generated `ts/package-lock.json`. The Render build uses `npm ci`, which requires this file.

For the Python path, create `requirements.txt` instead:

```text python/requirements.txt theme={null}
fastapi==0.141.1
uvicorn[standard]==0.52.0
httpx==0.28.1
```

Verify the dependencies in an isolated environment:

```bash Shell theme={null}
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

## Step 2: Add the chat handler

The handler validates the caller before it makes a billable request to Together AI. It also limits the message to 8,000 characters and maps upstream failures to explicit HTTP responses.

<CodeGroup>
  ```typescript ts/server.ts theme={null}
  import { timingSafeEqual } from "node:crypto";
  import express, { type ErrorRequestHandler } from "express";

  const app = express();
  app.use(express.json({ limit: "16kb" }));

  const TOGETHER_URL = "https://api.together.ai/v1/chat/completions";
  const MODEL = process.env.TOGETHER_MODEL ?? "Qwen/Qwen3.5-9B";

  function requiredEnv(name: string): string {
    const value = process.env[name];
    if (!value) throw new Error(`${name} is required.`);
    return value;
  }

  const TOGETHER_API_KEY = requiredEnv("TOGETHER_API_KEY");
  const CHAT_API_KEY = requiredEnv("CHAT_API_KEY");

  type TogetherResponse = {
    model?: string;
    choices?: Array<{ message?: { content?: string | null } }>;
    usage?: unknown;
  };

  function isAuthorized(header: string | undefined): boolean {
    if (!header?.startsWith("Bearer ")) return false;

    const supplied = Buffer.from(header.slice(7));
    const expected = Buffer.from(CHAT_API_KEY);
    return (
      supplied.length === expected.length && timingSafeEqual(supplied, expected)
    );
  }

  app.get("/health", (_req, res) => {
    res.json({ ok: true, model: MODEL });
  });

  app.post("/chat", async (req, res) => {
    if (!isAuthorized(req.get("authorization"))) {
      return res.status(401).json({ error: "Unauthorized" });
    }

    const message = req.body?.message;
    if (typeof message !== "string" || !message.trim() || message.length > 8000) {
      return res.status(400).json({
        error:
          'Body must include a non-empty "message" string of at most 8000 characters.',
      });
    }

    try {
      const upstream = await fetch(TOGETHER_URL, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${TOGETHER_API_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: MODEL,
          messages: [{ role: "user", content: message.trim() }],
          reasoning: { enabled: false },
          max_tokens: 512,
        }),
        signal: AbortSignal.timeout(60_000),
      });

      if (!upstream.ok) {
        const detail = (await upstream.text()).slice(0, 500);
        console.error("Together error", upstream.status, detail);
        return res.status(502).json({
          error: "Upstream inference failed",
          upstreamStatus: upstream.status,
        });
      }

      const data = (await upstream.json()) as TogetherResponse;
      const reply = data.choices?.[0]?.message?.content;
      if (typeof reply !== "string" || !reply) {
        return res
          .status(502)
          .json({ error: "Together returned an invalid response." });
      }

      return res.json({
        model: data.model ?? MODEL,
        reply,
        usage: data.usage,
      });
    } catch (error) {
      if (error instanceof DOMException && error.name === "TimeoutError") {
        return res
          .status(504)
          .json({ error: "Together timed out after 60 seconds." });
      }

      console.error("Together request failed", error);
      return res.status(502).json({ error: "Could not reach Together." });
    }
  });

  const requestErrorHandler: ErrorRequestHandler = (error, _req, res, _next) => {
    const type =
      typeof error === "object" && error !== null && "type" in error
        ? String(error.type)
        : "";

    if (type === "entity.parse.failed") {
      return res.status(400).json({ error: "Request body must be valid JSON." });
    }
    if (type === "entity.too.large") {
      return res.status(413).json({ error: "Request body is too large." });
    }

    console.error("Unhandled request error", error);
    return res.status(500).json({ error: "Internal server error." });
  };
  app.use(requestErrorHandler);

  const port = Number(process.env.PORT) || 3000;
  app.listen(port, "0.0.0.0", () => console.log(`listening on ${port}`));
  ```

  ```python python/main.py theme={null}
  import os
  import secrets

  import httpx
  from fastapi import FastAPI, Header, HTTPException
  from pydantic import BaseModel

  TOGETHER_URL = "https://api.together.ai/v1/chat/completions"
  MODEL = os.environ.get("TOGETHER_MODEL", "Qwen/Qwen3.5-9B")
  TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]
  CHAT_API_KEY = os.environ["CHAT_API_KEY"]

  app = FastAPI()


  class ChatRequest(BaseModel):
      message: str


  @app.get("/health")
  def health():
      return {"ok": True, "model": MODEL}


  @app.post("/chat")
  async def chat(
      req: ChatRequest,
      authorization: str | None = Header(default=None),
  ):
      supplied_key = (
          authorization.removeprefix("Bearer ")
          if authorization and authorization.startswith("Bearer ")
          else ""
      )
      if not supplied_key or not secrets.compare_digest(
          supplied_key, CHAT_API_KEY
      ):
          raise HTTPException(
              status_code=401,
              detail="Unauthorized",
              headers={"WWW-Authenticate": "Bearer"},
          )

      message = req.message.strip()
      if not message or len(message) > 8000:
          raise HTTPException(
              status_code=400,
              detail='Field "message" must contain 1 to 8000 characters.',
          )

      try:
          async with httpx.AsyncClient(timeout=60.0) as client:
              upstream = await client.post(
                  TOGETHER_URL,
                  headers={"Authorization": f"Bearer {TOGETHER_API_KEY}"},
                  json={
                      "model": MODEL,
                      "messages": [{"role": "user", "content": message}],
                      "reasoning": {"enabled": False},
                      "max_tokens": 512,
                  },
              )
      except httpx.TimeoutException as exc:
          raise HTTPException(
              status_code=504,
              detail="Together timed out after 60 seconds.",
          ) from exc
      except httpx.RequestError as exc:
          raise HTTPException(
              status_code=502,
              detail="Could not reach Together.",
          ) from exc

      if not upstream.is_success:
          print("Together error", upstream.status_code, upstream.text)
          raise HTTPException(
              status_code=502,
              detail={
                  "message": "Upstream inference failed",
                  "upstream_status": upstream.status_code,
              },
          )

      try:
          data = upstream.json()
          reply = data["choices"][0]["message"]["content"]
      except (ValueError, KeyError, IndexError, TypeError) as exc:
          raise HTTPException(
              status_code=502,
              detail="Together returned an invalid response.",
          ) from exc

      if not isinstance(reply, str) or not reply:
          raise HTTPException(
              status_code=502,
              detail="Together returned an empty response.",
          )

      return {
          "model": data.get("model", MODEL),
          "reply": reply,
          "usage": data.get("usage"),
      }
  ```
</CodeGroup>

Check the finished code before you deploy it:

<CodeGroup>
  ```bash TypeScript theme={null}
  cd ts
  npm run build
  cd ..
  ```

  ```bash Python theme={null}
  python3 -m py_compile python/main.py
  ```
</CodeGroup>

## Step 3: Configure the Render service

Render can create the service from a Blueprint stored in `render.yaml`. Create that file in the repository root and use the version for your runtime.

<CodeGroup>
  ```yaml TypeScript theme={null}
  services:
    - type: web
      name: together-chat
      runtime: node
      plan: free
      rootDir: ts
      buildCommand: npm ci && npm run build
      startCommand: npm start
      healthCheckPath: /health
      envVars:
        - key: TOGETHER_API_KEY
          sync: false
        - key: CHAT_API_KEY
          sync: false
        - key: TOGETHER_MODEL
          value: Qwen/Qwen3.5-9B
  ```

  ```yaml Python theme={null}
  services:
    - type: web
      name: together-chat
      runtime: python
      plan: free
      rootDir: python
      buildCommand: pip install -r requirements.txt
      startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
      healthCheckPath: /health
      envVars:
        - key: TOGETHER_API_KEY
          sync: false
        - key: CHAT_API_KEY
          sync: false
        - key: TOGETHER_MODEL
          value: Qwen/Qwen3.5-9B
        - key: PYTHON_VERSION
          value: 3.14.3
  ```
</CodeGroup>

Two Render settings matter here. The server binds to `0.0.0.0` so Render can route traffic to it, and it reads the `PORT` environment variable that Render provides.

The `sync: false` setting tells Render to prompt for each secret during the initial Blueprint creation instead of storing it in Git. Render does not prompt for these values when it creates a Blueprint preview, so set preview secrets separately if you use preview environments.

## Step 4: Deploy the Blueprint

Commit the project and push it to your Git provider:

```bash Shell theme={null}
git add .
git commit -m "Add Together AI chat service"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Then create the service:

1. Open the [Render Dashboard](https://dashboard.render.com/).
2. Select **New**, then **Blueprint**.
3. Connect the repository.
4. Enter your Together project API key for `TOGETHER_API_KEY`.
5. Enter the secret you generated earlier for `CHAT_API_KEY`.
6. Select **Deploy Blueprint**.

Render builds the selected runtime and assigns the service an HTTPS URL such as `https://together-chat-xxxx.onrender.com`. The service is ready when the deploy is live and the `/health` check passes.

<Note>
  A free Render web service spins down after 15 minutes without inbound traffic. Its next request can take about a minute while the service starts again. Use a paid instance if your application needs consistent response latency.
</Note>

## Step 5: Verify the deployment

Save the service URL in your shell:

```bash Shell theme={null}
export SERVICE_URL="https://together-chat-xxxx.onrender.com"
```

Check the health endpoint:

```bash Shell theme={null}
curl "$SERVICE_URL/health"
```

The response includes the configured model:

```json theme={null}
{
  "ok": true,
  "model": "Qwen/Qwen3.5-9B"
}
```

Confirm that the chat route rejects an unauthenticated request:

```bash Shell theme={null}
curl -i -X POST "$SERVICE_URL/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
```

The response has HTTP status `401`.

Next, load your `CHAT_API_KEY` without placing it in your shell history:

```bash Shell theme={null}
read -s CHAT_API_KEY
export CHAT_API_KEY
```

Send one authenticated inference request:

```bash Shell theme={null}
curl -X POST "$SERVICE_URL/chat" \
  -H "Authorization: Bearer $CHAT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message":"In one sentence, what is a vector database?"}'
```

A successful response has this shape:

```json theme={null}
{
  "model": "Qwen/Qwen3.5-9B",
  "reply": "A vector database stores and searches data as numerical vectors...",
  "usage": {
    "prompt_tokens": 17,
    "completion_tokens": 24,
    "total_tokens": 41
  }
}
```

The exact reply and token counts vary.

<Check>
  A non-empty `reply` confirms that the client authentication, Render service, Together API key, model ID, and network path all work.
</Check>

Remove the shared secret from your shell when you finish:

```bash Shell theme={null}
unset CHAT_API_KEY
```

## Change the model

The example uses Qwen3.5 9B. To use a different chat model:

1. Choose a model from the [recommended models](/docs/inference/recommended-models) or the [serverless model catalog](/docs/serverless/models).
2. Open the service in the Render Dashboard.
3. Change `TOGETHER_MODEL` under **Environment**.
4. Save the change and deploy the service.
5. Repeat the authenticated verification request.

Model availability, capabilities, and pricing change over time. Check the live catalog before changing the model string.

## Extend the app

This guide sends one user message and waits for one complete response. These features require changes to the request schema and the handler:

* **Multi-turn chat:** Accept and validate a `messages` array instead of a single `message`. See [chat completions](/docs/inference/chat/overview).
* **Streaming:** Request `stream: true` and forward the returned stream to the client. The client must also parse streamed events.
* **Structured JSON:** Add a supported response format and schema. See [structured outputs](/docs/inference/chat/structured-outputs).
* **Public access:** Replace the shared bearer token with user authentication, and add rate limiting, usage monitoring, and abuse controls.

## Next steps

<CardGroup>
  <Card title="Chat completions" icon="message" href="/docs/inference/chat/overview">
    Add multi-turn conversations and streaming to the handler.
  </Card>

  <Card title="Structured outputs" icon="braces" href="/docs/inference/chat/structured-outputs">
    Enforce a JSON Schema on the model response.
  </Card>

  <Card title="Render web services" icon="server" href="https://render.com/docs/web-services">
    Review instance types, health checks, and scaling on Render.
  </Card>

  <Card title="Batch inference" icon="stack-2" href="/docs/inference/batch/overview">
    Process many independent requests offline at lower cost.
  </Card>
</CardGroup>
