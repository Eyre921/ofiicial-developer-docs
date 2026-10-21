---
title: "Frontend Overview"
source: https://docs.crewai.com/v1.15.28/en/guides/frontend/overview
path: v1.15.28/en/guides/frontend/overview
---

Build interactive user interfaces for your CrewAI agents with CopilotKit and the AG-UI protocol.

## Give your agents a user interface

CrewAI runs your agents. [CopilotKit](https://copilotkit.ai) gives them a frontend. Together they let you build applications where users chat with a Crew or Flow, watch it work in real time, approve its decisions, and see its output rendered as live UI instead of walls of text.

The two connect through the [AG-UI protocol](https://docs.ag-ui.com). The `ag-ui-crewai` package exposes any Crew or Flow as an AG-UI endpoint. CopilotKit's React hooks and components consume that endpoint. This unlocks experiences that go well beyond a chat box:

> **[Generative UI](/edge/en/guides/frontend/generative-ui)**
>
> Render agent tool calls and state as your own React components.

> **[Human-in-the-Loop](/edge/en/guides/frontend/human-in-the-loop)**
>
> Pause the agent to collect user approval or input mid-run.

> **[Shared State](/edge/en/guides/frontend/shared-state)**
>
> Keep agent state and your app UI in two-way sync.

> **[Channels](/edge/en/guides/frontend/channels)**
>
> Run the same agent as a Slack, Discord, or Teams bot.

This guide gets a Crew or Flow talking to a Next.js frontend end to end. The rest of the section builds on the app you set up here.

## Architecture

There are three pieces:

1. **CrewAI agent server** — a Python process that serves your Crew or Flow over AG-UI (FastAPI + `ag-ui-crewai`).
2. **CopilotKit runtime** — a Next.js route that registers your agent and proxies requests to it.
3. **React frontend** — the `<CopilotKit>` provider plus chat and generative-UI components.

```
React app  ──►  CopilotKit runtime (/api/copilotkit)  ──►  CrewAI server (AG-UI)  ──►  Crew / Flow
```

> [!NOTE]
>
> This guide covers the **self-hosted** path: you run the CrewAI agent server yourself with `ag-ui-crewai`, and it works locally with no managed service. CopilotKit also offers a **managed** path (CopilotKit Cloud / Enterprise Intelligence) with hosted threads and an inspector — see the [CopilotKit CrewAI quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart) if you want that instead. The frontend code in this section is the same either way; only how the agent is hosted and registered differs.

> [!NOTE]
>
> CrewAI runs behind AG-UI in three shapes: regular **Flows** (used throughout these guides), **[Conversational Flows](/edge/en/guides/frontend/conversational-flows)** (native, session-aware, turn-based, at full feature parity), and **Crews** (basic chat). The frontend in this section is identical across them — only the backend authoring and registration differ.

## Integration guide

**1. Serve your agent over AG-UI**

Install the integration package into your CrewAI project:

```bash theme={null}
pip install ag-ui-crewai
```

Expose your agent from a FastAPI app. Flows use `add_crewai_flow_fastapi_endpoint`; Crews use `add_crewai_crew_fastapi_endpoint`. You can register as many as you want, each on its own path.

```python Flow theme={null}
# server.py
from fastapi import FastAPI
from ag_ui_crewai.endpoint import add_crewai_flow_fastapi_endpoint
from my_agents.recipe_flow import RecipeFlow

app = FastAPI(title="CrewAI Agent Server")

add_crewai_flow_fastapi_endpoint(
    app=app,
    flow=RecipeFlow(),
    path="/recipe",
)
```

```python Crew theme={null}
# server.py
from fastapi import FastAPI
from ag_ui_crewai.endpoint import add_crewai_crew_fastapi_endpoint
from my_agents.research_crew import ResearchCrew

app = FastAPI(title="CrewAI Agent Server")

add_crewai_crew_fastapi_endpoint(
    app=app,
    crew=ResearchCrew().crew(),
    path="/research",
)
```

Run it:

```bash theme={null}
uvicorn server:app --port 8000
```

> [!NOTE]
>
> Set the environment variables for your LLM provider (for example `OPENAI_API_KEY`) before starting the server.

**2. Create a Next.js app**

If you do not have a frontend yet, scaffold one:

```bash theme={null}
npx create-next-app@latest my-app
cd my-app
```

Install CopilotKit and the CrewAI AG-UI client:

```bash theme={null}
npm install @copilotkit/react-core @copilotkit/react-ui @copilotkit/runtime @ag-ui/crewai
```

**3. Add the CopilotKit runtime**

Create a route that registers your CrewAI agent(s) with the CopilotKit runtime. Each agent points at a path on your Python server via `CrewAIAgent`.

```ts theme={null}
// app/api/copilotkit/route.ts
import {
  CopilotRuntime,
  InMemoryAgentRunner,
  createCopilotEndpoint,
} from "@copilotkit/runtime/v2";
import { CrewAIAgent } from "@ag-ui/crewai";
import { handle } from "hono/vercel";

const runtime = new CopilotRuntime({
  agents: {
    recipe: new CrewAIAgent({ url: "http://localhost:8000/recipe" }),
  },
  runner: new InMemoryAgentRunner(),
});

const app = createCopilotEndpoint({
  runtime,
  basePath: "/api/copilotkit",
});

const handler = handle(app);
export const GET = handler;
export const POST = handler;
```

**4. Wrap your app with the provider**

Point `<CopilotKit>` at the runtime route and name the agent you registered.

```tsx theme={null}
// app/page.tsx
"use client";
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotSidebar } from "@copilotkit/react-core/v2";
import "@copilotkit/react-core/v2/styles.css";

export default function Page() {
  return (
    <CopilotKit runtimeUrl="/api/copilotkit" agent="recipe">
      <YourApp />
      <CopilotSidebar agentId="recipe" labels={{ modalHeaderTitle: "Assistant" }} />
    </CopilotKit>
  );
}
```

**5. Run it**

Start both processes and open the app. Chatting in the sidebar now runs your Crew or Flow.

```bash theme={null}
uvicorn server:app --port 8000   # terminal 1
npm run dev                       # terminal 2
```

## Chat UI options

CopilotKit ships three interchangeable chat surfaces. Swap the component; the wiring is identical.

```tsx Sidebar theme={null}
import { CopilotSidebar } from "@copilotkit/react-core/v2";

<CopilotSidebar agentId="recipe" />
```

```tsx Popup theme={null}
import { CopilotPopup } from "@copilotkit/react-core/v2";

<CopilotPopup agentId="recipe" />
```

```tsx Inline theme={null}
import { CopilotChat } from "@copilotkit/react-core/v2";

<CopilotChat agentId="recipe" />
```

## Where to go next

> **[Generative UI](/edge/en/guides/frontend/generative-ui)**
>
> Render tool calls and agent state as custom components.

> **[Frontend Actions](/edge/en/guides/frontend/frontend-actions)**
>
> Let the agent call functions that run in the browser.

> **[Human-in-the-Loop](/edge/en/guides/frontend/human-in-the-loop)**
>
> Gate agent actions behind user approval.

> **[Predictive State](/edge/en/guides/frontend/predictive-state-updates)**
>
> Stream in-progress state to the UI as the agent works.
