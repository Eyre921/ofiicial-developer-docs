---
title: "Browser Agent SDK"
source: https://developers.deepgram.com/docs/browser-agent-overview.md
path: docs/browser-agent-overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Browser Agent SDK

> Four composable packages that connect your web app to Deepgram's Voice Agent API. Works with any JavaScript framework. Ship in minutes, customize for months.

The demo above requires a Deepgram account. [Sign up free](https://console.deepgram.com/signup) to try it, or keep reading to understand the architecture first.

## Choose Your Approach

Start from how much control you need, not which package to install.

**"I want a voice agent on my site in five minutes."**
Use the [Widget](/docs/browser-agent-widget). One install, one function call. Pick from six layouts — sidebar, floating, inline, button, embedded, or orb. No framework required.

```bash
npm install @deepgram/agents-widget
```

```javascript
import { init } from "@deepgram/agents-widget";

init({
  tokenFactory: () => fetch("/api/deepgram-token").then((r) => r.text()),
  agent: "YOUR_AGENT_ID",
  layout: "floating",
});
```

**"I'm building a React app and want pre-built components."**
Use [React UI Components](/docs/browser-agent-react-ui). Conversation view, animated orb, mic/speaker buttons, text input, and a waveform visualizer — all styled through CSS custom properties that work alongside your existing design system.

**"I'm building a React app but want full control over the UI."**
Use [React Hooks](/docs/browser-agent-react). Provider context and focused hooks for state, conversation history, microphone control, audio playback, and client-side function calling. You build every pixel; the hooks manage every connection.

**"I'm using Vue, Svelte, Angular, or vanilla JS."**
Use the [JavaScript SDK](/docs/browser-agent-javascript). The core `AgentSession` class is framework-agnostic. Pair it with `AgentMicrophone` for capture and `AgentPlayer` for playback. Wire the events into whatever UI layer you prefer.

## Architecture

Four packages, each building on the one below it. Install only the layer you need — everything above comes with it.

```
@deepgram/agents-widget    Drop-in widget (UMD + ESM, bundles Preact)
       ↓
@deepgram/ui               Pre-built React components + CSS
       ↓
@deepgram/react            React provider + hooks
       ↓
@deepgram/agents           Core WebSocket client, microphone, player
```

Every layer shares the same connection logic, audio pipeline, and event model. The difference is how much UI you want handled for you.

Each layer pulls in the layer below as a dependency, and re-exports the parts you need from above. Installing `@deepgram/ui` brings in `@deepgram/react` and `@deepgram/agents` automatically and re-exports the hooks, provider, and SDK types — you import everything you need from `@deepgram/ui` alone. The same pattern applies one layer down: `@deepgram/react` brings in `@deepgram/agents` and re-exports its types.

### What You Get at Every Layer

* **Reconnection with exponential backoff and jitter.** Configurable max attempts, base delay, and ceiling. Connections recover without user intervention.
* **Playback-aware mode tracking.** The SDK knows when audio has actually finished playing in the browser — not just when the server finished sending it. Mode transitions from "speaking" to "listening" wait for the audio queue to drain.
* **Audio buffering before settings are applied.** Microphone frames captured before the server acknowledges your configuration are queued and flushed automatically.
* **Voice Activity Detection.** Optional Silero VAD runs client-side for precise speech endpoint detection.
* **KeepAlive pings.** Automatic heartbeat prevents idle WebSocket disconnects. Interval is configurable.
* **Typed event emitter.** Every server message — `Welcome`, `ConversationText`, `AgentAudioDone`, `FunctionCallRequest`, and more — has a typed event. Subscribe to exactly what you need.
* **Custom WebSocket URL support.** Connect to proxied or self-hosted endpoints by overriding the default Deepgram URL.

### What the React Layer Adds

* **Client-side function calling** scoped to React component lifecycle. Register tool handlers with `useAgentClientTool` — they mount and unmount with the component. Dynamic tools are checked first, then the provider falls back to `onFunctionCall`.
* **Conversation state management.** The `useAgentConversation` hook accumulates transcript events into a structured message array with roles, content, and IDs.
* **Mode awareness.** The `useAgentMode` hook tracks whether the agent is idle, listening, or speaking — with the playback-aware delay described above.

### What the UI Layer Adds

* **26 CSS custom properties** with `light-dark()` adaptive defaults. Works with Tailwind, CSS Modules, plain CSS — anything that can set a custom property.
* **Canvas 2D visualizations.** The orb and waveform components use Canvas 2D, not WebGL. They render well on low-power devices and do not require GPU acceleration.
* **`data-dg-*` attribute selectors** instead of class names. Your existing CSS framework cannot collide with component styles.

### What the Widget Adds

* **Six layouts:** `sidebar`, `floating`, `inline`, `button`, `embedded`, `orb`. Each adapts to its container and responds to the host page's color scheme.
* **Preact runtime bundled internally.** The UMD build is self-contained — no React dependency, no build tooling, no framework assumptions. The ESM build is also available for projects with a bundler.
* **Single `init()` call** returns a teardown function. Mount and unmount cleanly in single-page applications without leaking event listeners or audio contexts.
* **Full theming support.** Pass a theme object to `init()` or use CSS custom properties from the host page. The widget inherits `light-dark()` behavior automatically.

## Authentication

Browser applications must never expose API keys to the client. Use a **token factory** — a function that returns a short-lived token from your server.

```javascript title="Client"
const config = {
  auth: {
    tokenFactory: async () => {
      const res = await fetch("/api/deepgram-token");
      return res.text();
    },
  },
  agent: "YOUR_AGENT_ID",
};
```

```javascript title="Server (Node.js)"
app.get("/api/deepgram-token", async (req, res) => {
  const response = await fetch("https://api.deepgram.com/v1/auth/grant", {
    method: "POST",
    headers: {
      Authorization: `Token ${process.env.DEEPGRAM_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ttl: 30 }),
  });
  const { access_token } = await response.json();
  res.send(access_token);
});
```

The browser `WebSocket` constructor does not support custom headers. The SDK works around this by passing the token as a `Sec-WebSocket-Protocol` value — the only header browsers allow on a WebSocket handshake. This is handled internally; you just return a token string from your factory function.

The token factory is called before every connection and reconnection attempt. Tokens stay fresh even across network interruptions.

The `apiKey` option exists for local development only. Never ship it in client-side code.

## Agent Configuration

Configure the agent by referencing one you created in the [Deepgram Console](https://console.deepgram.com), or define the full configuration inline:

```javascript title="By Agent ID"
const config = {
  agent: "YOUR_AGENT_ID",
};
```

```javascript title="Inline Configuration"
const config = {
  agent: {
    listen: {
      provider: { type: "deepgram", model: "nova-3" },
    },
    think: {
      provider: { type: "open_ai", model: "gpt-4o-mini" },
      prompt: "You are a helpful voice assistant.",
    },
    speak: {
      provider: { type: "deepgram", version: "v2", model: "flux-kit-en" },
    },
  },
};
```

Agent IDs let you change behavior from the console without redeploying your application. Inline configuration gives you version control and the ability to construct prompts dynamically at runtime.

You can combine both approaches — reference an agent ID for base configuration and override specific settings inline. See the individual package guides for details.

## Next Steps

| Guide                                               | What you will learn                                                                            |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [JavaScript SDK](/docs/browser-agent-javascript)    | `AgentSession`, `AgentMicrophone`, and `AgentPlayer` — the core primitives for any framework.  |
| [React Hooks](/docs/browser-agent-react)            | `AgentProvider`, state hooks, conversation hooks, and client-side function calling.            |
| [React UI Components](/docs/browser-agent-react-ui) | Pre-built conversation view, orb visualizer, mic/speaker buttons, and CSS theming.             |
| [Widget](/docs/browser-agent-widget)                | Embed a complete voice agent with one function call. Six layouts, full theming, no build step. |
