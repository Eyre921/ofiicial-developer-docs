---
title: "React Hooks & Provider"
source: https://developers.deepgram.com/docs/browser-agent-react.md
path: docs/browser-agent-react
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# React Hooks & Provider

> API reference for @deepgram/react — AgentProvider, connection state hooks, playback-aware mode tracking, conversation hooks, component-scoped client tools, and standalone useDeepgramAgent for simpler apps.

Looking for pre-built UI components? See [React UI Components](/docs/browser-agent-react-ui). For the core JavaScript SDK, see [JavaScript](/docs/browser-agent-javascript).

## Installation

```shell
npm install @deepgram/react
```

`@deepgram/react` lists `@deepgram/agents` as a dependency and re-exports the SDK types you need (`AgentSessionConfig`, `AgentSettingsObject`, `MicrophoneOptions`, and the rest), so a single `npm install @deepgram/react` is all you need for the React layer. If you want direct access to the SDK classes (`AgentSession`, `AgentMicrophone`, `AgentPlayer`), import them from `@deepgram/agents`.

## Usage

Wrap your component tree in `AgentProvider`, then use hooks to subscribe to exactly the state slices you need. Each hook triggers re-renders only when its own values change.

```tsx
import {
  AgentProvider,
  useAgentState,
  useAgentConversation,
  useAgentMode,
} from "@deepgram/react";

function App() {
  return (
    <AgentProvider
      config={{
        auth: { tokenFactory: () => fetch("/api/token").then((r) => r.text()) },
        agent: "YOUR_AGENT_ID",
      }}
    >
      <VoiceAgent />
    </AgentProvider>
  );
}

function VoiceAgent() {
  const { state, start, stop } = useAgentState();
  const { conversation } = useAgentConversation();
  const { mode } = useAgentMode();

  return (
    <div>
      <p>Mode: {mode}</p>
      <button onClick={() => (state === "connected" ? stop() : start())}>
        {state === "connected" ? "Disconnect" : "Connect"}
      </button>
      <ul>
        {conversation.map((msg) => (
          <li key={msg.id}>
            <strong>{msg.role}:</strong> {msg.content}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

Replace `YOUR_AGENT_ID` with a [Reusable Agent Configuration](/docs/reusable-agent-configurations) UUID, or pass an inline agent config object instead. See [Agent Configuration](/docs/browser-agent-overview#agent-configuration) for both patterns.

## AgentProvider

The provider creates and manages `AgentSession`, `AgentMicrophone`, and `AgentPlayer` instances. All hooks below must be called within an `AgentProvider`.

```tsx
<AgentProvider
  config={agentSessionConfig}
  microphone={true}
  microphoneOptions={{ vad: true }}
  tts={true}
  playerSampleRate={24_000}
  autoStart={false}
  onFunctionCall={handleFunctionCall}
>
  {children}
</AgentProvider>
```

### Props

| Prop                | Type                                                  | Default     | Description                                                                                                                                      |
| ------------------- | ----------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `config`            | `AgentSessionConfig`                                  | required    | Session configuration. See [JavaScript SDK](/docs/browser-agent-javascript) for all options.                                                     |
| `microphone`        | `boolean`                                             | `true`      | Enable microphone capture.                                                                                                                       |
| `microphoneOptions` | `MicrophoneOptions`                                   | `undefined` | Options passed to `AgentMicrophone` (sample rate, VAD, noise suppression). See [JavaScript SDK](/docs/browser-agent-javascript#agentmicrophone). |
| `tts`               | `boolean`                                             | `true`      | Enable TTS audio playback.                                                                                                                       |
| `playerSampleRate`  | `number`                                              | `24000`     | Sample rate for the audio player.                                                                                                                |
| `autoStart`         | `boolean`                                             | `false`     | Connect to the agent immediately on mount.                                                                                                       |
| `onFunctionCall`    | `(fn: FunctionCallItem) => Promise<string> \| string` | `undefined` | Default handler for agent function call requests. Dynamic tools registered with `useAgentClientTool` take priority over this prop.               |

## Hooks

### useAgentState

Connection state and lifecycle controls. Re-renders only when connection state changes.

```tsx
const {
  state,           // "idle" | "connecting" | "connected" | "reconnecting" | "disconnected"
  isIdle,          // true when state === "idle"
  isConnecting,    // true when state === "connecting"
  isConnected,     // true when state === "connected"
  isReconnecting,  // true when state === "reconnecting"
  isDisconnected,  // true when state === "disconnected"
  isActive,        // true when connected, connecting, or reconnecting
  start,           // () => Promise<void> — connect session + open mic
  stop,            // () => void — disconnect + close mic
} = useAgentState();
```

### useAgentConversation

Conversation history and text input. Re-renders when a new message arrives.

```tsx
const {
  conversation,       // ConversationEntry[]
  clearConversation,  // () => void
  sendUserMessage,    // (text: string) => void — inject a text message as the user
} = useAgentConversation();
```

Each `ConversationEntry` contains:

| Field     | Type                    | Description                      |
| --------- | ----------------------- | -------------------------------- |
| `id`      | `string`                | Unique identifier for the entry. |
| `role`    | `"user" \| "assistant"` | Who said it.                     |
| `content` | `string`                | The message text.                |

### useAgentMode

Tracks the agent's speaking/listening mode with playback awareness. The mode transitions from `"speaking"` to `"listening"` only after all queued audio finishes playing in the browser, not when the server sends the `AgentAudioDone` event. This prevents the UI from showing "listening" while the agent's voice is still audible.

```tsx
const {
  mode,        // "idle" | "listening" | "speaking"
  isSpeaking,  // true when mode === "speaking"
  isListening, // true when mode === "listening"
} = useAgentMode();
```

The playback-aware transition is automatic. The provider measures `AgentPlayer.getRemainingPlaybackTime()` when the server signals audio-done, then delays the mode switch by that duration. No configuration needed.

### useAgentMicrophone

Microphone state, mute controls, and input volume.

```tsx
const {
  micActive,       // true when hardware is open
  micMuted,        // true when muted (stream still open, not sending audio)
  setMicMuted,     // (muted: boolean) => void
  toggle,          // () => void — toggle mute state
  enabled,         // false when microphone={false} on provider — mic is fully disabled
  getInputVolume,  // () => number — returns 0-1, call per animation frame
} = useAgentMicrophone();
```

`getInputVolume()` reads the current microphone level without triggering a re-render. Call it inside `requestAnimationFrame` or a canvas draw loop for smooth audio visualizations.

### useAgentPlayer

Audio playback state, mute controls, and output volume.

```tsx
const {
  outputMuted,      // true when muted
  setOutputMuted,   // (muted: boolean) => void
  toggle,           // () => void — toggle mute state
  enabled,          // false when tts={false} on provider — playback is fully disabled
  getOutputVolume,  // () => number — returns 0-1, call per animation frame
} = useAgentPlayer();
```

### useAgentControls

Action methods only, no state. All returned functions are `useCallback`-wrapped refs with stable identity -- they never change between renders. Components that use only this hook will never re-render due to agent state changes.

Use this for components that dispatch commands but do not display state, such as a toolbar or keyboard shortcut handler.

```tsx
const {
  start,              // () => Promise<void>
  stop,               // () => void
  sendUserMessage,    // (text: string) => void
  clearConversation,  // () => void
  setMicMuted,        // (muted: boolean) => void
  setOutputMuted,     // (muted: boolean) => void
} = useAgentControls();
```

```tsx
// Safe in effects — stable refs mean no re-runs
useEffect(() => {
  const handleKey = (e: KeyboardEvent) => {
    if (e.key === "m") setMicMuted((prev) => !prev);
  };
  window.addEventListener("keydown", handleKey);
  return () => window.removeEventListener("keydown", handleKey);
}, [setMicMuted]); // setMicMuted identity never changes
```

### useAgentClientTool

Register a client-side tool handler scoped to the component lifecycle. The handler is automatically unregistered when the component unmounts, so tools only exist while the component that provides them is mounted.

```tsx
useAgentClientTool(
  name: string,
  handler: (fn: FunctionCallItem) => Promise<string> | string
): void
```

Dynamic tools registered with this hook take priority over the `onFunctionCall` prop on `AgentProvider`. If no dynamic tool matches the requested function name, the provider falls back to `onFunctionCall`.

```tsx
function WeatherWidget() {
  const [weather, setWeather] = useState(null);

  useAgentClientTool("get_weather", async (fn) => {
    const { city } = JSON.parse(fn.input);
    const data = await fetchWeather(city);
    setWeather(data);
    return JSON.stringify(data);
  });

  return weather ? <WeatherCard data={weather} /> : null;
}
```

The handler always captures the latest closure, so referencing component state inside the handler works without stale-state issues.

```tsx
function MapComponent() {
  const [location, setLocation] = useState({ lat: 0, lng: 0 });

  // Always reads the current location value
  useAgentClientTool("getLocation", () => {
    return JSON.stringify(location);
  });

  useAgentClientTool("setLocation", (fn) => {
    const coords = JSON.parse(fn.input);
    setLocation(coords);
    return JSON.stringify({ ok: true });
  });

  return <Map center={location} />;
}
```

### useAgentSession

Raw escape hatch to the underlying `AgentSession` instance. Use for advanced operations not covered by other hooks, such as listening to custom events or calling lower-level session methods.

```tsx
const session = useAgentSession();

useEffect(() => {
  const handler = (msg) => console.log("Agent thinking:", msg);
  session.on("agent-thinking", handler);
  return () => session.off("agent-thinking", handler);
}, [session]);
```

### useAgentContext

Access the full context value. Prefer the focused hooks above for selective re-rendering. This hook is available when you need several unrelated values without importing multiple hooks.

```tsx
const ctx = useAgentContext();
// ctx.state, ctx.mode, ctx.conversation, ctx.micMuted, etc.
```

## Standalone Hook

For simpler apps that do not need shared state across multiple components, `useDeepgramAgent` manages the session, microphone, and player internally without requiring a provider.

```tsx
import { useDeepgramAgent } from "@deepgram/react";

function VoiceAgent() {
  const {
    state,
    conversation,
    micActive,
    outputMuted,
    start,
    stop,
    setMicMuted,
    setOutputMuted,
    sendUserMessage,
    interrupt,
  } = useDeepgramAgent({
    config: {
      auth: { tokenFactory: () => fetch("/api/token").then((r) => r.text()) },
      agent: "YOUR_AGENT_ID",
    },
    micOptions: { vad: true },
    playerSampleRate: 24_000,
    onFunctionCall: async (fn) => {
      return JSON.stringify({ result: "ok" });
    },
  });

  return (
    <div>
      <button onClick={() => (state === "connected" ? stop() : start())}>
        {state === "connected" ? "Disconnect" : "Start"}
      </button>
      <ul>
        {conversation.map((msg) => (
          <li key={msg.id}>
            <strong>{msg.role}:</strong> {msg.content}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### Options

| Option             | Type                                | Default     | Description                                               |
| ------------------ | ----------------------------------- | ----------- | --------------------------------------------------------- |
| `config`           | `AgentSessionConfig`                | required    | Session configuration (auth, agent ID, settings).         |
| `micOptions`       | `MicrophoneOptions`                 | `{}`        | Microphone options (sample rate, VAD, noise suppression). |
| `playerSampleRate` | `number`                            | `24000`     | Audio player sample rate.                                 |
| `onFunctionCall`   | `(fn) => Promise<string> \| string` | `undefined` | Handler for agent function call requests.                 |

### Return values

| Value             | Type                       | Description                              |
| ----------------- | -------------------------- | ---------------------------------------- |
| `state`           | `AgentState`               | Current connection state.                |
| `micActive`       | `boolean`                  | Whether the microphone hardware is open. |
| `outputMuted`     | `boolean`                  | Whether agent audio output is muted.     |
| `conversation`    | `ConversationEntry[]`      | Conversation history.                    |
| `start`           | `() => Promise<void>`      | Connect session and open microphone.     |
| `stop`            | `() => void`               | Disconnect session and close microphone. |
| `setMicMuted`     | `(muted: boolean) => void` | Mute or unmute the microphone.           |
| `setOutputMuted`  | `(muted: boolean) => void` | Mute or unmute agent audio.              |
| `sendUserMessage` | `(text: string) => void`   | Inject a text message as the user.       |
| `interrupt`       | `() => void`               | Interrupt agent speech immediately.      |

`useDeepgramAgent` does not support `useAgentClientTool`. Use the provider pattern if you need per-component tool registration.
