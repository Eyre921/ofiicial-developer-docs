---
title: "React UI Components"
source: https://developers.deepgram.com/docs/browser-agent-react-ui.md
path: docs/browser-agent-react-ui
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# React UI Components

> API reference for @deepgram/ui — composable components for building voice agent UIs with Deepgram. Includes orb visualizer, waveforms, frequency bars, conversation display, and CSS custom property theming.

These components require an `AgentProvider` ancestor. See [React Hooks](/docs/browser-agent-react) for provider setup. For the core JavaScript SDK, see [JavaScript](/docs/browser-agent-javascript).

## Installation

```shell
npm install @deepgram/ui
```

Import the stylesheet in your app's entry point:

```tsx
import "@deepgram/ui/styles.css";
```

`@deepgram/ui` re-exports all hooks from `@deepgram/react` and all types from `@deepgram/agents`. You can import everything from a single package.

## Live Preview

The embedded widget below uses the components documented on this page — conversation panel, start button, microphone toggle, speaker toggle, text input, and the orb visualizer.

## Usage

A complete voice agent interface in under 30 lines:

```tsx
import {
  AgentProvider,
  AgentConversation,
  AgentTextInput,
  AgentStartButton,
  AgentMicrophoneButton,
  AgentSpeakerButton,
  Orb,
} from "@deepgram/ui";
import "@deepgram/ui/styles.css";

function App() {
  return (
    <AgentProvider
      config={{
        auth: { tokenFactory: () => fetch("/api/token").then((r) => r.text()) },
        agent: "YOUR_AGENT_ID",
      }}
    >
      <div data-dg-agent>
        <Orb size={120} />
        <AgentConversation />
        <AgentTextInput />
        <div>
          <AgentStartButton />
          <AgentMicrophoneButton />
          <AgentSpeakerButton />
        </div>
      </div>
    </AgentProvider>
  );
}
```

Replace `YOUR_AGENT_ID` with a [Reusable Agent Configuration](/docs/reusable-agent-configurations) UUID, or pass an inline agent config object instead. See [Agent Configuration](/docs/browser-agent-overview#agent-configuration) for both patterns.

Every component is optional. Use one or all, and mix them with your own components inside the provider.

## Display Components

### AgentStatus

Renders the current connection state as a text label. Updates automatically as the session connects, disconnects, or reconnects.

Connected

```tsx
<AgentStatus />
```

**Props:**

| Prop        | Type                              | Default   | Description                               |
| ----------- | --------------------------------- | --------- | ----------------------------------------- |
| `className` | `string`                          | —         | Additional CSS class.                     |
| `labels`    | `Partial<Record<string, string>>` | See below | Override the display text for each state. |

Default labels: `"Not started"`, `"Connecting..."`, `"Connected"`, `"Reconnecting..."`, `"Disconnected"`.

```tsx
<AgentStatus
  labels={{
    idle: "Ready",
    connecting: "Connecting...",
    connected: "Live",
    disconnected: "Offline",
  }}
/>
```

**Data attributes:** `data-agent-status`, `data-state` (current state value).

### AgentConversation

Scrollable conversation history showing user and agent messages.

What time is my next meeting?

You have a 1:1 with Sarah at 3:30 PM.

```tsx
<AgentConversation />
```

**Props:**

| Prop            | Type                                      | Default | Description                               |
| --------------- | ----------------------------------------- | ------- | ----------------------------------------- |
| `className`     | `string`                                  | —       | CSS class for the container.              |
| `itemClassName` | `string`                                  | —       | CSS class applied to each message.        |
| `renderMessage` | `(entry: ConversationEntry) => ReactNode` | —       | Custom render function for messages.      |
| `emptyState`    | `ReactNode`                               | —       | Content shown when conversation is empty. |
| `autoScroll`    | `boolean`                                 | `true`  | Scroll to latest message automatically.   |

```tsx
<AgentConversation
  emptyState={<p>Say something to start the conversation.</p>}
  renderMessage={(entry) => (
    <div className={entry.role === "user" ? "user-msg" : "agent-msg"}>
      {entry.content}
    </div>
  )}
/>
```

**Data attributes:** `data-agent-conversation` on the container, `data-role="user"` or `data-role="assistant"` on each message.

### Response

Lightweight markdown renderer for agent text. Handles bold, italic, inline code, code blocks, lists, headings, links, and horizontal rules. Supports streaming — update the `children` string as tokens arrive.

<p>
  Voice agents combine 

  <strong>speech-to-text</strong>

  , an LLM, and 

  <em>text-to-speech</em>

   in a single connection.
</p>

<ul>
  <li>
    Low-latency conversation
  </li>

  <li>
    Natural prosody
  </li>
</ul>

```tsx
<Response>{markdownString}</Response>
```

**Props:**

| Prop        | Type     | Default | Description                |
| ----------- | -------- | ------- | -------------------------- |
| `children`  | `string` | —       | Markdown string to render. |
| `className` | `string` | —       | Additional CSS class.      |

**Data attributes:** `data-agent-response`.

## Input Components

### AgentTextInput

Text input field for sending messages to the agent. Submits on Enter (Shift+Enter for newline).

<input type="text" placeholder="Type a message…" disabled />

<button disabled>
  Send
</button>

```tsx
<AgentTextInput />
```

**Props:**

| Prop           | Type                     | Default               | Description                      |
| -------------- | ------------------------ | --------------------- | -------------------------------- |
| `className`    | `string`                 | —                     | Additional CSS class.            |
| `placeholder`  | `string`                 | `"Type a message..."` | Input placeholder text.          |
| `disabled`     | `boolean`                | `false`               | Disable the input.               |
| `onSend`       | `(text: string) => void` | —                     | Callback when a message is sent. |
| `submitButton` | `ReactNode`              | —                     | Custom send button element.      |

**Data attributes:** `data-agent-text-input`.

## Control Components

### AgentStartButton

Connect/disconnect toggle button. Reflects the current session state automatically.

<button disabled>
  Start
</button>

```tsx
<AgentStartButton />
```

**Props:**

| Prop                | Type         | Default             | Description                      |
| ------------------- | ------------ | ------------------- | -------------------------------- |
| `className`         | `string`     | —                   | Additional CSS class.            |
| `startLabel`        | `ReactNode`  | `"Start"`           | Label when idle.                 |
| `connectingLabel`   | `ReactNode`  | `"Connecting..."`   | Label while connecting.          |
| `stopLabel`         | `ReactNode`  | `"Stop"`            | Label when connected.            |
| `reconnectingLabel` | `ReactNode`  | `"Reconnecting..."` | Label while reconnecting.        |
| `onClick`           | `() => void` | —                   | Optional click handler override. |

**Data attributes:** `data-agent-start-button`, `data-state` (current state value).

### AgentMicrophoneButton

Microphone mute/unmute toggle. Renders SVG mic icons by default.

```tsx
<AgentMicrophoneButton />
```

**Props:**

| Prop            | Type         | Default      | Description                                                        |
| --------------- | ------------ | ------------ | ------------------------------------------------------------------ |
| `className`     | `string`     | —            | Additional CSS class.                                              |
| `activeLabel`   | `ReactNode`  | Mic icon     | Content when microphone is active.                                 |
| `mutedLabel`    | `ReactNode`  | Mic-off icon | Content when muted.                                                |
| `disabledLabel` | `ReactNode`  | —            | Content when microphone is unavailable. Returns `null` if omitted. |
| `onClick`       | `() => void` | —            | Optional click handler override.                                   |

**Data attributes:** `data-agent-mic-button`, `data-state` (`"active"`, `"muted"`, `"inactive"`, or `"disabled"`).

### AgentSpeakerButton

Speaker mute/unmute toggle. Renders SVG speaker icons by default.

```tsx
<AgentSpeakerButton />
```

**Props:**

| Prop          | Type         | Default          | Description                      |
| ------------- | ------------ | ---------------- | -------------------------------- |
| `className`   | `string`     | —                | Additional CSS class.            |
| `activeLabel` | `ReactNode`  | Speaker icon     | Content when speaker is active.  |
| `mutedLabel`  | `ReactNode`  | Speaker-off icon | Content when muted.              |
| `onClick`     | `() => void` | —                | Optional click handler override. |

**Data attributes:** `data-agent-speaker-button`, `data-state` (`"active"` or `"muted"`).

### VoiceButton

All-in-one button that combines connection and mode state into a single control. The appearance changes across five lifecycle states: idle, connecting, listening, speaking, and error.

```tsx
<VoiceButton />
```

**Props:**

| Prop        | Type                                           | Default   | Description                      |
| ----------- | ---------------------------------------------- | --------- | -------------------------------- |
| `className` | `string`                                       | —         | Additional CSS class.            |
| `labels`    | `Partial<Record<VoiceButtonState, ReactNode>>` | See below | Text for each state.             |
| `onClick`   | `() => void`                                   | —         | Optional click handler override. |

Default labels: `"Start conversation"`, `"Connecting..."`, `"Listening..."`, `"Agent speaking"`, `"Error"`.

Style each state with the `data-voice-state` attribute:

```css
[data-voice-state="listening"] {
  border-color: var(--dg-va-primary);
}
[data-voice-state="speaking"] {
  background: var(--dg-va-primary);
  animation: pulse 1.5s infinite;
}
```

**Data attributes:** `data-agent-voice-button`, `data-voice-state` (`"idle"`, `"connecting"`, `"listening"`, `"speaking"`, `"error"`).

## Visualization Components

### Orb

Deepgram's animated hoop visualization. Canvas 2D rendering of four crescent arcs with gradient colors — lightweight and works everywhere without WebGL. Audio-reactive: the orb responds to actual microphone input and agent playback volume in real time.

Three visual states:

* **idle** — deflated crescent, slow rocking, minimal animation
* **listening** — full circle, gentle pulse, mic-reactive radius flutter
* **talking** — crescent mouth, fast rotation, volume-modulated mouth movement

```tsx
<Orb size={200} />
```

**Props:**

| Prop              | Type                                 | Default         | Description                                           |
| ----------------- | ------------------------------------ | --------------- | ----------------------------------------------------- |
| `size`            | `number`                             | `200`           | Diameter in pixels.                                   |
| `colors`          | `[string, string]`                   | Deepgram greens | Two gradient colors.                                  |
| `state`           | `"idle" \| "listening" \| "talking"` | `"idle"`        | Visual state.                                         |
| `getInputVolume`  | `() => number`                       | —               | Getter sampled per frame for mic volume (0--1).       |
| `getOutputVolume` | `() => number`                       | —               | Getter sampled per frame for output volume (0--1).    |
| `inputVolume`     | `number`                             | —               | Direct mic volume value (0--1) for manual control.    |
| `outputVolume`    | `number`                             | —               | Direct output volume value (0--1) for manual control. |
| `className`       | `string`                             | —               | Additional CSS class.                                 |

**Automatic mode** (default inside `AgentProvider`):

```tsx
<Orb />
```

The orb reads `getInputVolume()` and `getOutputVolume()` every animation frame with zero re-renders.

**Manual mode** — push volume values directly:

```tsx
<Orb inputVolume={0.5} outputVolume={0.3} state="talking" />
```

**Custom volume sources:**

```tsx
<Orb
  getInputVolume={myMicAnalyser}
  getOutputVolume={myPlayerAnalyser}
/>
```

**Custom colors:**

```tsx
<Orb colors={["#6366f1", "#ec4899"]} />
```

**Data attributes:** `data-agent-orb`, `data-orb-state` (`"idle"`, `"listening"`, `"talking"`).

### BarVisualizer

Real-time frequency bar visualization. Renders vertical bars on a canvas that react to audio input or output.

{[40, 70, 30, 90, 60, 80, 45, 65, 55, 75, 35, 70, 50, 60, 40, 25].map((h, i) => (
    <div key={i} style={{ width: '6px', height: `${h}%`, background: '#13ef93', borderRadius: '2px', opacity: 0.85 }}></div>
  ))}

```tsx
<BarVisualizer source="output" barCount={16} />
```

**Props:**

| Prop        | Type                  | Default    | Description                |
| ----------- | --------------------- | ---------- | -------------------------- |
| `source`    | `"input" \| "output"` | `"output"` | Microphone or agent audio. |
| `barCount`  | `number`              | `16`       | Number of frequency bars.  |
| `className` | `string`              | —          | Additional CSS class.      |

**Data attributes:** `data-agent-bar-visualizer`.

### LiveWaveform

Smooth oscillating waveform driven by a volume source. Blends two sine waves for an organic feel.

```tsx
import { useAgentMicrophone } from "@deepgram/ui";

function MyWaveform() {
  const { getInputVolume } = useAgentMicrophone();
  return <LiveWaveform getVolume={getInputVolume} />;
}
```

**Props:**

| Prop        | Type                                 | Default           | Description                                                                                   |
| ----------- | ------------------------------------ | ----------------- | --------------------------------------------------------------------------------------------- |
| `getVolume` | `(() => number) \| (() => number)[]` | —                 | Volume source(s) returning 0--1. When multiple are provided, the max value is used per frame. |
| `active`    | `boolean`                            | `true`            | Whether the waveform animates. Renders a flat line when false.                                |
| `color`     | `string`                             | `--dg-va-primary` | Line color.                                                                                   |
| `lineWidth` | `number`                             | `2`               | Stroke width in pixels.                                                                       |
| `className` | `string`                             | —                 | Additional CSS class.                                                                         |

**Data attributes:** `data-agent-live-waveform`.

## Utility Components

### MicSelector

Dropdown for selecting the audio input device. Enumerates available microphones, requests permission on first open, and updates automatically when devices are plugged in or removed.

<select disabled>
  <option>
    Built-in microphone
  </option>
</select>

```tsx
const [deviceId, setDeviceId] = useState("");
<MicSelector value={deviceId} onValueChange={setDeviceId} />
```

**Props:**

| Prop            | Type                         | Default | Description                                |
| --------------- | ---------------------------- | ------- | ------------------------------------------ |
| `value`         | `string`                     | —       | Currently selected device ID (controlled). |
| `onValueChange` | `(deviceId: string) => void` | —       | Callback when the user selects a device.   |
| `className`     | `string`                     | —       | Additional CSS class.                      |
| `disabled`      | `boolean`                    | `false` | Disable the selector.                      |

**Data attributes:** `data-agent-mic-selector`.

## Theming

All components use CSS custom properties scoped to `[data-dg-agent]`. Add this attribute to your container element to apply the theme. Because these are standard CSS custom properties, they work with any CSS framework — Tailwind, CSS Modules, or plain stylesheets.

```tsx
<div data-dg-agent>
  <AgentConversation />
  <AgentTextInput />
</div>
```

### Design tokens

Tokens follow the shadcn `--color-*` naming convention generated by Tailwind v4's `@theme`. The package ships sensible light defaults; dark values are applied automatically when `[data-dg-scheme="dark"]` is set or when the user's system prefers dark mode. Override any token on a `[data-dg-agent]` ancestor to retheme.

```css
[data-dg-agent] {
  /* Brand */
  --color-primary:            #13ef93;
  --color-primary-foreground: #000000;

  /* Surfaces */
  --color-background:            #ffffff;
  --color-foreground:            #111827;
  --color-card:                  #f3f4f6;
  --color-card-foreground:       #111827;
  --color-popover:               #ffffff;
  --color-popover-foreground:    #111827;
  --color-muted:                 #f3f4f6;
  --color-muted-foreground:      #6b7280;
  --color-accent:                #f9fafb;
  --color-accent-foreground:     #111827;
  --color-input:                 #f3f4f6;
  --color-border:                rgba(0, 0, 0, 0.1);
  --color-ring:                  #13ef93;
  --color-secondary:             #f3f4f6;
  --color-secondary-foreground:  #111827;
  --color-destructive:           #dc2626;
  --color-destructive-foreground:#ffffff;

  /* Typography & shape */
  --font-sans: system-ui, -apple-system, sans-serif;
  --radius:    1rem;

  /* Widget layout (panel + FAB sizing) */
  --dg-va-panel-w:  min(440px, 100vw);
  --dg-va-fab-size: 56px;
  --dg-va-padding:  16px;

  /* Derived from --color-primary by default — override only if you need a different relationship */
  --primary-hover:   color-mix(in srgb, var(--color-primary) 85%, #000);
  --primary-active:  color-mix(in srgb, var(--color-primary) 70%, #000);
  --msg-user-bg:     color-mix(in srgb, var(--color-primary) 12%, transparent);
  --msg-user-border: color-mix(in srgb, var(--color-primary) 30%, transparent);
}
```

### Color scheme

Light/dark switching is driven by the `data-dg-scheme` attribute on the same element that has `data-dg-agent`. Without an explicit value, the components follow the user's `prefers-color-scheme`.

```tsx
<div data-dg-agent data-dg-scheme="dark">
  {/* Always renders in dark mode */}
</div>
```

| Behaviour               | Selector                                                 |
| ----------------------- | -------------------------------------------------------- |
| Force dark              | `[data-dg-agent][data-dg-scheme="dark"]`                 |
| Force light             | `[data-dg-agent][data-dg-scheme="light"]`                |
| Follow system (default) | no attribute, `prefers-color-scheme: dark` triggers dark |

If your app uses Tailwind's `dark:` variant or `next-themes`, write a small effect that mirrors that state onto `data-dg-scheme`. The package does not infer it from a `.dark` ancestor class.

### Custom theme example

A teal-on-midnight palette called **Aurora**, applied entirely through CSS custom properties on the host element. Same components, completely different feel.

```css
[data-dg-agent].aurora-theme {
  /* Brand */
  --color-primary:              #5eead4;
  --color-primary-foreground:   #042f2e;
  --color-ring:                 #5eead4;

  /* Surfaces */
  --color-background:           #0a0e1a;
  --color-foreground:           #e6edf6;
  --color-card:                 #121829;
  --color-card-foreground:      #e6edf6;
  --color-popover:              #121829;
  --color-popover-foreground:   #e6edf6;
  --color-muted:                #1a2236;
  --color-muted-foreground:     #94a3b8;
  --color-accent:               #182238;
  --color-accent-foreground:    #5eead4;
  --color-input:                #0d1322;
  --color-border:               rgba(94, 234, 212, 0.14);
  --color-secondary:            #1a2236;
  --color-secondary-foreground: #5eead4;

  /* Derived (override the color-mix defaults for a softer glow) */
  --primary-hover:              #2dd4bf;
  --primary-active:             #14b8a6;
  --msg-user-bg:                rgba(94, 234, 212, 0.10);
  --msg-user-border:            rgba(94, 234, 212, 0.28);

  /* Slightly tighter corners than the default 1rem */
  --radius:                     14px;
}
```

Apply the class to your `[data-dg-agent]` container (or extend the override to the element itself) and every component inside picks up the new palette. The same pattern works for any palette — swap the values, keep the keys.

### Styling with Data Attributes

Components use `data-agent-*` attribute selectors instead of class names. This prevents collisions with your application's CSS framework — no specificity battles with Tailwind utilities or CSS Modules hashes.

```css
/* Target the conversation container */
[data-agent-conversation] {
  max-height: 400px;
}

/* Target user messages */
[data-agent-conversation] [data-role="user"] {
  text-align: right;
}

/* Target agent messages */
[data-agent-conversation] [data-role="assistant"] {
  font-style: italic;
}

/* Target the text input */
[data-agent-text-input] {
  font-size: 16px;
}

/* Target the orb by state */
[data-agent-orb][data-orb-state="talking"] {
  filter: brightness(1.2);
}
```

### Data Attribute Reference

| Component             | Attribute                                     | Values                                                                      |
| --------------------- | --------------------------------------------- | --------------------------------------------------------------------------- |
| Container             | `data-dg-agent`                               | —                                                                           |
| Color scheme          | `data-dg-scheme`                              | `"light"`, `"dark"`                                                         |
| AgentStatus           | `data-agent-status`, `data-state`             | `"idle"`, `"connecting"`, `"connected"`, `"reconnecting"`, `"disconnected"` |
| AgentConversation     | `data-agent-conversation`                     | —                                                                           |
| Messages              | `data-role`                                   | `"user"`, `"assistant"`                                                     |
| AgentTextInput        | `data-agent-text-input`                       | —                                                                           |
| AgentStartButton      | `data-agent-start-button`, `data-state`       | `"idle"`, `"connecting"`, `"connected"`, `"reconnecting"`, `"disconnected"` |
| AgentMicrophoneButton | `data-agent-mic-button`, `data-state`         | `"active"`, `"muted"`, `"inactive"`, `"disabled"`                           |
| AgentSpeakerButton    | `data-agent-speaker-button`, `data-state`     | `"active"`, `"muted"`                                                       |
| VoiceButton           | `data-agent-voice-button`, `data-voice-state` | `"idle"`, `"connecting"`, `"listening"`, `"speaking"`, `"error"`            |
| Orb                   | `data-agent-orb`, `data-orb-state`            | `"idle"`, `"listening"`, `"talking"`                                        |
| BarVisualizer         | `data-agent-bar-visualizer`                   | —                                                                           |
| LiveWaveform          | `data-agent-live-waveform`                    | —                                                                           |
| MicSelector           | `data-agent-mic-selector`                     | —                                                                           |
| Response              | `data-agent-response`                         | —                                                                           |
