---
title: "Widget Embedding Guide"
source: https://developers.deepgram.com/docs/browser-agent-widget.md
path: docs/browser-agent-widget
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Widget Embedding Guide

> How to embed the Deepgram voice agent widget on any web page. Covers CDN and ES module installation, six layout modes, theming with design tokens, VAD, callbacks, and programmatic teardown.

Add a voice agent to any website. No framework required, no build step needed. The widget ships as a self-contained bundle with its own Preact runtime (\~160KB gzipped), six layout modes, full design-token theming, and built-in voice activity detection. It works from a CDN or as an ES module, and tears down cleanly for single-page apps.

The widget bundles everything internally. No React or build tooling required. For React-native integration, see [React UI Components](/docs/browser-agent-react-ui).

## Quick Start

### Install

```bash
npm install @deepgram/agents-widget
```

### ES Module

```javascript
import { init } from "@deepgram/agents-widget";

const teardown = init({
  tokenFactory: () => fetch("/api/deepgram-token").then((r) => r.text()),
  agent: "YOUR_AGENT_ID",
  layout: "sidebar",
});

// Call teardown() to unmount the widget and clean up
```

Replace `YOUR_AGENT_ID` with a [Reusable Agent Configuration](/docs/reusable-agent-configurations) UUID, or pass an inline agent config object instead. See [Agent Configuration](/docs/browser-agent-overview#agent-configuration) for both patterns.

### CDN

Load the widget from `cdn.deepgram.com` for a no-build path:

```html
<script src="https://cdn.deepgram.com/widgets/latest/widget.umd.js"></script>
<script>
  const teardown = DeepgramAgent.init({
    tokenFactory: () => fetch("/api/deepgram-token").then((r) => r.text()),
    agent: "YOUR_AGENT_ID",
  });
</script>
```

The `latest` segment in the URL above is replaced with the current pinned version when this page loads, so the snippet you copy targets a specific build, not a moving release pointer.

### Self-hosted UMD

The package ships a UMD bundle at `dist/widget.umd.js` for `<script>`-tag usage. Copy or symlink it from `node_modules/@deepgram/agents-widget/dist/widget.umd.js` into your static assets, then load it like any other script:

```html
<script src="/assets/widget.umd.js"></script>
<script>
  const teardown = DeepgramAgent.init({
    tokenFactory: () => fetch("/api/deepgram-token").then((r) => r.text()),
    agent: "YOUR_AGENT_ID",
  });
</script>
```

Never include your API key in client-side code. Use `tokenFactory` to fetch short-lived tokens from your server. The `apiKey` option exists only for local development.

## Layouts

The widget ships with six layout modes. Set the `layout` option to choose one.

### sidebar (default)

A panel that slides in from the edge of the screen. Toggled by a floating action button (FAB).

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "sidebar",
  placement: "bottom-right",
  defaultOpen: false,
  dismissible: true,
});
```

### floating

A FAB button that reveals a floating overlay panel.

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "floating",
  placement: "bottom-right",
});
```

### inline

Mounts directly into an existing DOM element. No FAB, no overlay.

```html
<div id="agent-container"></div>
```

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "inline",
  containerId: "agent-container",
});
```

### embedded

Full-width card with configurable aspect ratio. Includes the conversation transcript. Ideal for landing pages and product demos.

```html
<div id="agent-embed"></div>
```

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "embedded",
  containerId: "agent-embed",
  theme: {
    aspect: "16 / 9",
    minHeight: "400px",
  },
});
```

### button

A single talk button -- press to start, press again to stop. Minimal footprint.

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "button",
  placement: "bottom-right",
});
```

### orb

The Deepgram animated hoop visualization with start/stop controls. Audio-reactive -- the orb responds to input and output volume in real time.

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "orb",
  placement: "bottom-right",
});
```

## Placement

For layouts with a FAB (`sidebar`, `floating`, `button`, `orb`), set where the button appears:

```javascript
placement: "bottom-right" // default
// Options: "bottom-right", "bottom-left", "bottom",
//          "top-right", "top-left", "top"
```

## External Trigger Button

To use your own button instead of the built-in FAB, pass its element ID:

```html
<button id="my-agent-btn">Talk to AI</button>
```

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "sidebar",
  buttonId: "my-agent-btn",
});
```

To toggle the widget programmatically from anywhere:

```javascript
document.dispatchEvent(new Event("dg-agent-toggle"));
```

## Features

Toggle UI features on or off:

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  showTranscript: true,    // conversation history (default: true)
  showMicToggle: true,     // microphone mute button (default: true)
  showSpeakerToggle: true, // speaker mute button (default: true)
  showTextInput: true,     // text input field (default: true)
  vad: true,               // voice activity detection (default: false)
});
```

## VAD Configuration

Enable Silero VAD to gate audio so only speech frames reach the agent. Pass `true` for defaults, or fine-tune the thresholds:

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  vad: {
    speechThreshold: 0.5,
    silenceThreshold: 0.35,
  },
});
```

When VAD is enabled, the microphone captures continuously but transmits only when speech is detected. This reduces bandwidth and improves turn-taking accuracy.

## Text Customization

Override labels and placeholder text:

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  text: {
    name: "Aria",
    startLabel: "Talk to Aria",
    stopLabel: "End conversation",
    connectingLabel: "Connecting...",
    inputPlaceholder: "Type a message...",
    emptyStateHint: "Press start to begin talking.",
  },
});
```

## Agent Overrides

Override the agent's system prompt or greeting for this session without changing the agent configuration in the Deepgram console:

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  overrides: {
    systemPrompt: "You are a customer support agent for Acme Corp.",
    greeting: "Hi! How can I help you with your Acme account?",
  },
});
```

## Callbacks

Listen to agent lifecycle events for analytics, logging, or UI integration:

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  on: {
    onConnect: () => console.log("Connected"),
    onDisconnect: (reason) => console.log("Disconnected:", reason),
    onError: (err) => console.error("Error:", err),
    onMessage: (msg) => console.log(`${msg.role}: ${msg.content}`),
    onAgentStartedSpeaking: (msg) => console.log("Agent speaking"),
    onFunctionCallRequest: (msg) => console.log("Function call:", msg),
    onAgentError: (msg) => console.error("Agent error:", msg),
    onReconnecting: (attempt, delayMs) =>
      console.log(`Reconnecting (attempt ${attempt}, ${delayMs}ms)`),
  },
});
```

| Callback                 | Fires when                                                  |
| ------------------------ | ----------------------------------------------------------- |
| `onConnect`              | WebSocket connection opens                                  |
| `onDisconnect`           | Session ends (user or server side)                          |
| `onError`                | SDK-level error occurs                                      |
| `onMessage`              | Any conversation turn (user or assistant text)              |
| `onAgentStartedSpeaking` | Agent begins speaking; includes latency metrics             |
| `onFunctionCallRequest`  | Agent requests a client-side function call                  |
| `onAgentError`           | Agent-reported error (distinct from SDK errors)             |
| `onReconnecting`         | Reconnect attempt starts; receives attempt number and delay |

## Color Scheme

Control how the widget adapts to light and dark mode:

```javascript
// Automatic -- follows prefers-color-scheme (default)
colorScheme: "auto"

// Force light or dark
colorScheme: "light"
colorScheme: "dark"

// Class-based -- for CSS framework integration (e.g., Tailwind dark mode)
colorScheme: {
  mode: "class",
  darkSelector: ".dark",   // default
  lightSelector: ".light", // default
}
```

The class-based option watches for a CSS selector on any ancestor element. Use it when the host app controls theme via a class on `<html>` rather than OS preference.

## Theming

Customize the widget's appearance by overriding design tokens. Each property maps to a CSS custom property on the widget root element (`[data-dg-agent]`). Set a token here to override the built-in adaptive default in both light and dark modes.

```javascript
init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  theme: {
    // Accent
    primary: "#6366f1",
    primaryHover: "#4f46e5",
    primaryActive: "#4338ca",
    onPrimary: "#ffffff",

    // Surface
    background: "#ffffff",
    backgroundRaised: "#f9fafb",
    backgroundInput: "#ffffff",
    backgroundHover: "#f3f4f6",
    backgroundActive: "#e5e7eb",

    // Text
    text: "#111827",
    textMuted: "#6b7280",

    // Chrome
    border: "#e5e7eb",
    error: "#ef4444",
    overlay: "rgba(0, 0, 0, 0.25)",

    // Messages
    userMessageBackground: "#f3f4f6",
    userMessageBorder: "#e5e7eb",

    // Radius
    panelRadius: "16px",
    buttonRadius: "9999px",
    inputRadius: "8px",
    messageRadius: "12px",

    // Structural
    fabSize: 56,
    padding: "16px",
    font: "Inter, system-ui, sans-serif",
  },
});
```

To override only one color scheme, skip the `theme` option and write CSS directly:

```css
@media (prefers-color-scheme: dark) {
  [data-dg-agent] {
    --dg-va-bg: #0d1117;
  }
}
```

### Embedded Layout Tokens

The `embedded` layout supports additional sizing tokens:

```javascript
theme: {
  aspect: "4 / 3",       // CSS aspect-ratio (default: "4 / 3")
  minHeight: "320px",     // default: "320px"
  maxHeight: "80vh",      // default: "80vh"
}
```

## Full Configuration Reference

```javascript
init({
  // -- Auth (one required) --
  apiKey: "...",                              // Development only
  tokenFactory: () => Promise<string>,        // Production

  // -- Agent --
  agent: "AGENT_ID" | AgentSettingsObject,    // Required
  overrides: { systemPrompt, greeting },

  // -- Layout --
  layout: "sidebar",                          // sidebar | inline | floating
                                              // button | embedded | orb
  placement: "bottom-right",                  // FAB position
  containerId: "my-element",                  // Required for inline / embedded
  buttonId: "my-button",                      // External trigger element
  defaultOpen: false,                         // Start panel open (sidebar/floating)
  dismissible: true,                          // Allow close/dismiss

  // -- Features --
  vad: false | { speechThreshold, silenceThreshold },
  showTranscript: true,
  showMicToggle: true,
  showSpeakerToggle: true,
  showTextInput: true,

  // -- Text --
  text: {
    name, startLabel, stopLabel,
    connectingLabel, inputPlaceholder, emptyStateHint,
  },

  // -- Theming --
  colorScheme: "auto" | "light" | "dark"
             | { mode: "class", darkSelector, lightSelector },
  theme: { /* design tokens listed above */ },

  // -- Callbacks --
  on: {
    onConnect, onDisconnect, onError, onMessage,
    onAgentStartedSpeaking, onFunctionCallRequest,
    onAgentError, onReconnecting,
  },

  // -- Audio --
  playerSampleRate: 24_000,                   // Agent audio sample rate

  // -- Network --
  url: "wss://...",                           // Custom WebSocket URL (proxy)
});
```

## Cleanup

The `init()` function returns a teardown function. Call it to unmount the widget, remove all injected styles, and release audio resources. This is essential for single-page apps where the widget mounts and unmounts as the user navigates.

```javascript
const teardown = init({
  tokenFactory,
  agent: "YOUR_AGENT_ID",
  layout: "sidebar",
});

// When the user navigates away or you no longer need the widget:
teardown();
```

For frameworks with lifecycle hooks, call teardown in the cleanup phase:

```javascript
// React useEffect
useEffect(() => {
  const teardown = init({ tokenFactory, agent: "YOUR_AGENT_ID" });
  return teardown;
}, []);

// Vue onUnmounted
onMounted(() => {
  const teardown = init({ tokenFactory, agent: "YOUR_AGENT_ID" });
  onUnmounted(teardown);
});
```
