---
title: "Conversational Flows"
source: https://docs.crewai.com/v1.15.30/en/guides/frontend/conversational-flows
path: v1.15.30/en/guides/frontend/conversational-flows
---

Serve native, session-aware CrewAI Flows over AG-UI with managed conversation state and full frontend parity.

## Three execution shapes, one bridge

Behind the AG-UI bridge, a CrewAI backend can take one of three shapes. Knowing which one you are serving decides how you author the backend, not how you build the frontend.

| Shape | What it is | How it is entered |
| - | - | - |
| **Regular Flows** | Author-controlled `@start`/`@listen`/`@router` graphs. The default used throughout these guides. | `kickoff` / `astream` |
| **Conversational Flows** | Native, session-aware, turn-based Flows with managed conversation state. | `stream_turn(message, session_id=...)` |
| **Crews** | Closed autonomous task/agent loops. Basic chat only, a separate compatibility path. | Not the focus here. |

Conversational Flows are a newer CrewAI capability, and an important thing to be clear about up front: **they are Flows, not Crews.** They now run at full regular-Flow feature parity. This page introduces them and shows how they fit the rest of the frontend guides.

> [!NOTE]
>
> Reach for a Conversational Flow when you want native multi-turn conversation with CrewAI managing session state and history for you, rather than wiring turn and state handling into a regular Flow yourself. If you are new here, start with the [Frontend Overview](/edge/en/guides/frontend/overview) for the base server, runtime, and provider setup.

## Register a Conversational Flow

You register a Conversational Flow through the same endpoint helper as any other Flow, with one extra argument: `conversational=True`.

```python theme={null}
# server.py
from ag_ui_crewai.endpoint import add_crewai_flow_fastapi_endpoint

add_crewai_flow_fastapi_endpoint(
    app,
    flow,
    "/conversation",
    conversational=True,
)
```

Two requirements must hold for this to work:

* The Flow instance declares `conversational = True`.
* The Flow exposes CrewAI's public, callable `stream_turn(message, session_id=...)`.

Detection is capability-based, not version-gated: the bridge checks that the Flow actually offers turn-based conversation, rather than keying off a version number.

> [!WARNING]
>
> If those requirements are not met, the request fails loudly with a `RUN_ERROR` (code `AGUI_CREWAI_CONVERSATIONAL_FLOW_UNSUPPORTED`). It never silently falls back to regular kickoff semantics, so you always know exactly which path you are on.

Authoring the Flow itself, including how you implement `stream_turn`, belongs to CrewAI's Conversational Flows documentation. This page stays at the registration and integration boundary.

## Session and state

Conversational Flows manage session state and history for you across turns. You do not re-thread history manually.

* The AG-UI `threadId` **is** the CrewAI conversation `session_id`. The same thread is the same conversation.
* Before each turn the bridge hydrates the Flow's state and conversation history, then calls `stream_turn`. CrewAI restores the stored session state, and a per-request overlay reapplies the incoming AG-UI state and history so the browser's latest edits win over stale storage.

The result: from the backend author's side, each turn arrives already carrying the conversation's state, and CrewAI persists what you write for the next turn.

## Frontend parity

This is the point to hold onto: **Conversational Flows run through the same event pipeline as regular Flows, so the frontend code is identical.**

There is no Conversational-Flow-specific frontend API. Every feature in these guides works exactly the same way with a Conversational Flow as it does with a regular Flow, using the same hooks and components:

> **[Tool-Based Generative UI](/edge/en/guides/frontend/tool-based-generative-ui)**
>
> Map agent tool calls to your React components.

> **[Agentic Generative UI](/edge/en/guides/frontend/agentic-generative-ui)**
>
> Render the Flow's live state as it works.

> **[Shared State](/edge/en/guides/frontend/shared-state)**
>
> Keep agent state and app UI in two-way sync.

> **[Human-in-the-Loop](/edge/en/guides/frontend/human-in-the-loop)**
>
> Pause the agent for user approval or input mid-turn.

> **[Predictive State](/edge/en/guides/frontend/predictive-state-updates)**
>
> Stream in-progress tool arguments into state.

> **[Reasoning](/edge/en/guides/frontend/reasoning)**
>
> Show the model's thinking in the chat.

> **[A2UI](/edge/en/guides/frontend/a2ui)**
>
> Render agent-authored UI from a component catalog.

The only difference is on the backend: how you author the Flow (turn-based `stream_turn` with managed session state) and the `conversational=True` registration. Once the endpoint is up, everything you already know about building the frontend applies unchanged.

## Related

> **[Frontend Overview](/edge/en/guides/frontend/overview)**
>
> Wire a Crew or Flow to a Next.js frontend end to end.

> **[Generative UI](/edge/en/guides/frontend/generative-ui)**
>
> Render tool calls and agent state as custom components.

> **[Human-in-the-Loop](/edge/en/guides/frontend/human-in-the-loop)**
>
> Gate agent actions behind user approval.
