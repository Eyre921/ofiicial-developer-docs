---
title: "Realtime overview"
source: https://trigger.dev/docs/realtime/overview
path: docs/realtime/overview
---

Get live run updates and stream data from background tasks to your frontend or backend. No polling.

**Realtime is the umbrella for everything live in Trigger.dev.** It covers two things: getting notified when a run's state changes, and streaming continuous data (like AI tokens) from a running task to your app.

Both use the same `@trigger.dev/react-hooks` package and the same authentication system. The difference is what they give you.

## Run updates vs Streaming

|                         | Run updates                                              | Streaming                                                     |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| **What you get**        | Run state: status, metadata, tags                        | Continuous data you define (AI tokens, file chunks, progress) |
| **When it fires**       | On state changes                                         | While the task runs, as data is produced                      |
| **Use case**            | Progress bars, status badges, dashboards                 | AI chat output, live logs, file processing                    |
| **React hook**          | [`useRealtimeRun`](/docs/realtime/react-hooks/subscribe)      | [`useRealtimeStream`](/docs/realtime/react-hooks/streams)          |
| **Setup in task code?** | No, automatic                                            | Yes, using `streams.define()`                                 |
| **Infrastructure**      | [Electric SQL](/docs/realtime/how-it-works) (PostgreSQL sync) | Streams transport                                             |

You can use both at the same time. Subscribe to a run's status (to show a progress bar) while also streaming AI output (to display tokens as they arrive).

## Run updates

Subscribe to a run and your code gets called whenever its status, [metadata](/docs/runs/metadata), or [tags](/docs/tags) change. No setup needed in your task code.

You can subscribe to:

* **Specific runs** by run ID
* **Runs with specific tags** (e.g., all runs tagged with `user:123`)
* **Batch runs** within a specific batch
* **Trigger + subscribe combos** that trigger a task and immediately subscribe (frontend only)

→ [React hooks](/docs/realtime/react-hooks/subscribe) | [Backend](/docs/realtime/backend/subscribe)

## Streaming

Define typed streams in your task, pipe data to them, and read that data from your frontend or backend as it's produced. You need to set up streams in your task code using `streams.define()`.

→ [How to emit streams from tasks](/docs/tasks/streams) | [React hooks](/docs/realtime/react-hooks/streams) | [Backend](/docs/realtime/backend/streams)

## Authentication

All Realtime hooks and functions require authentication. See the [authentication guide](/docs/realtime/auth) for setup.

## Frequently asked questions

### How do I show a progress bar for a background task?

Use [run metadata](/docs/runs/metadata) to store progress data (like a percentage), then subscribe to the run with [`useRealtimeRun`](/docs/realtime/react-hooks/subscribe). Your component re-renders on every metadata update.

### How do I stream AI/LLM responses from a background task?

Define a stream in your task with `streams.define()`, pipe your AI SDK response to it, then consume it in React with [`useRealtimeStream`](/docs/realtime/react-hooks/streams). See [Streaming data from tasks](/docs/tasks/streams) for the full guide.

### Do I need WebSockets or polling?

No. Run updates are powered by [Electric SQL](/docs/realtime/how-it-works) (HTTP-based PostgreSQL syncing). Streams use their own transport. The hooks handle connections automatically.

### Can I use both run updates and streaming together?

Yes. A common pattern: subscribe to run status with `useRealtimeRun` (progress indicator) while streaming AI output with `useRealtimeStream` (token-by-token display).
