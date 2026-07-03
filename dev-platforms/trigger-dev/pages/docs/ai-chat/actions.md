---
title: "Actions"
source: https://trigger.dev/docs/ai-chat/actions
path: docs/ai-chat/actions
---

Custom commands sent from the frontend that mutate chat state without consuming a turn — undo, rollback, edit, regenerate.

## Overview

Custom actions let the frontend send structured commands (undo, rollback, edit, regenerate) that modify the conversation state. **Actions are not turns**: they fire `hydrateMessages` (if set) and `onAction` only. No turn lifecycle hooks (`onTurnStart` / `prepareMessages` / `onBeforeTurnComplete` / `onTurnComplete`), no `run()`, no turn-counter increment. The trace span is named `chat action`.

Actions wake the agent from suspension the same way a new message does, run their handler against the latest accumulator state, and emit a `trigger:turn-complete` chunk so the frontend's `useChat` knows the action has been applied.

## Defining an action handler

Define an `actionSchema` for validation and an `onAction` handler that uses [`chat.history`](/docs/ai-chat/backend#chat-history) to modify state:

```ts theme={"theme":"css-variables"}
import { z } from "zod";

export const myChat = chat.agent({
  id: "my-chat",
  actionSchema: z.discriminatedUnion("type", [
    z.object({ type: z.literal("undo") }),
    z.object({ type: z.literal("rollback"), targetMessageId: z.string() }),
    z.object({ type: z.literal("edit"), messageId: z.string(), text: z.string() }),
  ]),

  onAction: async ({ action }) => {
    switch (action.type) {
      case "undo":
        chat.history.slice(0, -2); // Remove last user + assistant exchange
        break;
      case "rollback":
        chat.history.rollbackTo(action.targetMessageId);
        break;
      case "edit":
        chat.history.replace(action.messageId, {
          id: action.messageId,
          role: "user",
          parts: [{ type: "text", text: action.text }],
        });
        break;
    }
    // returning void → side-effect-only, no model call
  },

  run: async ({ messages, signal }) => {
    return streamText({ model: anthropic("claude-sonnet-4-5"), messages, abortSignal: signal });
  },
});
```

**Lifecycle flow:** Wake → parse action against `actionSchema` → `hydrateMessages` (if set) → **`onAction`** → apply `chat.history` mutations → emit `trigger:turn-complete` → wait for next message.

## Returning a model response from an action

`onAction` can return a `StreamTextResult`, `string`, or `UIMessage` to produce a response. The returned stream is auto-piped to the frontend just like a normal turn, but the rest of the turn machinery (`onTurnStart`, `onTurnComplete`, etc.) still does not fire.

```ts theme={"theme":"css-variables"}
onAction: async ({ action, messages }) => {
  if (action.type === "regenerate") {
    chat.history.slice(0, -1); // drop the last assistant
    return streamText({
      model: anthropic("claude-sonnet-4-5"),
      messages,
      stopWhen: stepCountIs(15),
    });
  }
  // other actions return void → side-effect only
}
```

This is useful for actions that both mutate state and want a fresh model response (regenerate-from-here, retry-with-different-style). Persistence is your responsibility inside `onAction` itself; you have access to the streamed response object.

## Gating actions on HITL state

If you have a [human-in-the-loop](/docs/ai-chat/patterns/human-in-the-loop) tool waiting on `addToolOutput`, you usually want to refuse competing actions like `regenerate` until the answer arrives. [`chat.history.getPendingToolCalls()`](/docs/ai-chat/backend#chat-history) gives you exactly that signal:

```ts theme={"theme":"css-variables"}
onAction: async ({ action, messages, signal }) => {
  if (action.type === "regenerate") {
    if (chat.history.getPendingToolCalls().length > 0) return; // gated
    chat.history.slice(0, -1);
    return streamText({ model: anthropic("claude-sonnet-4-5"), messages, abortSignal: signal });
  }
},
```

## Sending actions from the frontend

```ts theme={"theme":"css-variables"}
// Browser — TriggerChatTransport
const stream = await transport.sendAction(chatId, { type: "undo" });

// Server — AgentChat
const stream = await agentChat.sendAction({ type: "rollback", targetMessageId: "msg-3" });
```

The action payload is validated against `actionSchema` on the backend; invalid actions throw and surface as a stream error. The `action` parameter in `onAction` is fully typed from the schema.

<Note>
  For silent state changes that should never appear as a turn (e.g. injecting background context), use [`chat.inject()`](/docs/ai-chat/background-injection) instead. Actions are explicit user-driven mutations; injections are agent-side context updates.
</Note>

## See also

* [`chat.history`](/docs/ai-chat/backend#chat-history) — the imperative API actions use to mutate state
* [Sending actions from the frontend](/docs/ai-chat/frontend#sending-actions) — `transport.sendAction` ergonomics
* [`hydrateMessages`](/docs/ai-chat/lifecycle-hooks#hydratemessages) — fires before `onAction` when set
* [Branching conversations](/docs/ai-chat/patterns/branching-conversations) — pairs action handlers with backend-controlled history
* [Human-in-the-loop](/docs/ai-chat/patterns/human-in-the-loop) — gating fresh actions while a tool is waiting
