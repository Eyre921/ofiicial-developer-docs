---
title: "JavaScript SDK"
source: https://developers.deepgram.com/docs/browser-agent-javascript.md
path: docs/browser-agent-javascript
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# JavaScript SDK

> API reference for @deepgram/agents — the core WebSocket session, microphone capture with Silero VAD, and audio playback with volume and frequency analysis for browser-based voice agents.

This page covers the core JavaScript SDK, which works with vanilla JS, Vue, Svelte, Angular, and any other framework. If you are using React, see [React Hooks and Provider](/docs/browser-agent-react). For a drop-in embeddable solution, see [Widget](/docs/browser-agent-widget).

## Installation

```shell
npm install @deepgram/agents
```

## Usage

Connect to a Deepgram voice agent, capture microphone audio, and play back the agent's speech:

```javascript
import { AgentSession, AgentMicrophone, AgentPlayer } from "@deepgram/agents";

const session = new AgentSession({
  auth: {
    tokenFactory: () => fetch("/api/deepgram-token").then((r) => r.text()),
  },
  agent: "YOUR_AGENT_ID",
});

const player = new AgentPlayer();
const mic = new AgentMicrophone((data) => session.sendAudio(data));

// Play agent audio
session.on("audio", (chunk) => player.queue(chunk));

// Interrupt playback when the user speaks (barge-in)
session.on("user-started-speaking", () => player.interrupt());

// Log conversation turns
session.on("conversation-text", (msg) => {
  console.log(`${msg.role}: ${msg.content}`);
});

await session.connect();
await mic.start();
```

Replace `YOUR_AGENT_ID` with a [Reusable Agent Configuration](/docs/reusable-agent-configurations) UUID, or pass an inline agent config object instead. See [Agent Configuration](/docs/browser-agent-overview#agent-configuration) for both patterns.

## AgentSession

The core class that manages the WebSocket connection to the Voice Agent API. It handles authentication, automatic reconnection with exponential backoff, keep-alive pings, and audio buffering before the server acknowledges settings.

```javascript
import { AgentSession } from "@deepgram/agents";

const session = new AgentSession(config);
```

### Configuration

```javascript
const session = new AgentSession({
  // Required — authentication
  auth: {
    tokenFactory: () => fetch("/api/token").then((r) => r.text()),
  },

  // Required — agent ID or inline settings
  agent: "YOUR_AGENT_ID",

  // Optional — audio format
  audio: {
    input: { encoding: "linear16", sampleRate: 16_000 },
    output: { encoding: "linear16", sampleRate: 24_000 },
  },

  // Optional — reconnection behavior
  reconnect: {
    enabled: true,
    maxAttempts: 8,
    baseDelay: 500,
    maxDelay: 30_000,
    jitter: true,
  },

  // Optional — keep-alive ping interval (ms)
  keepAliveInterval: 10_000,

  // Optional — custom WebSocket URL (for proxies)
  url: undefined,
});
```

**Auth options:**

| Option         | Type                    | Description                                                                                                                                              |
| -------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tokenFactory` | `() => Promise<string>` | Returns a short-lived bearer token from your backend. Called at connect-time and before every reconnect. Tokens are cached internally until near expiry. |
| `apiKey`       | `string`                | Raw Deepgram API key. Server-side or local development only. Never expose in production browser bundles.                                                 |

**Agent options:**

The `agent` field accepts either a string agent ID from the Deepgram Console or an inline `AgentSettingsObject` with `listen`, `think`, and `speak` configuration.

**Audio options:**

| Option              | Default      | Description                                                                                                                                             |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input.encoding`    | `"linear16"` | Audio encoding sent to the server. Supported: `linear16`, `linear32`, `flac`, `alaw`, `mulaw`, `amr-nb`, `amr-wb`, `opus`, `ogg-opus`, `speex`, `g729`. |
| `input.sampleRate`  | `16000`      | Input sample rate in Hz.                                                                                                                                |
| `output.encoding`   | `"linear16"` | Audio encoding received from the server. Supported: `linear16`, `mulaw`, `alaw`.                                                                        |
| `output.sampleRate` | `24000`      | Output sample rate in Hz.                                                                                                                               |

**Reconnection options:**

| Option        | Default | Description                                                                   |
| ------------- | ------- | ----------------------------------------------------------------------------- |
| `enabled`     | `true`  | Automatically reconnect on unexpected disconnections.                         |
| `maxAttempts` | `8`     | Maximum number of reconnection attempts before giving up.                     |
| `baseDelay`   | `500`   | Initial delay in ms before the first retry.                                   |
| `maxDelay`    | `30000` | Maximum delay in ms between retries. Delays grow via exponential backoff.     |
| `jitter`      | `true`  | Add randomization (plus or minus 20%) to each delay to avoid thundering herd. |

### Connection States

The `state` property reflects the current connection lifecycle:

```javascript
session.state; // "idle" | "connecting" | "connected" | "reconnecting" | "disconnected"
```

* **`idle`** — session created but `connect()` has not been called.
* **`connecting`** — WebSocket connection attempt in progress.
* **`connected`** — WebSocket is open and the session is active.
* **`reconnecting`** — connection lost; attempting to reconnect with backoff.
* **`disconnected`** — connection closed and no further reconnection attempts will be made.

### Methods

**`connect(): Promise<void>`** — establish the WebSocket connection to the agent. Resolves when the socket is open. The SDK automatically sends a `Settings` message after receiving the `Welcome` event.

```javascript
await session.connect();
```

**`disconnect(): void`** — close the connection and cancel any pending reconnection attempts.

```javascript
session.disconnect();
```

**`sendAudio(data: ArrayBuffer): void`** — send a PCM audio frame to the agent. Frames sent before the server fires `settings-applied` are queued internally and flushed automatically once the agent is ready. This prevents dropped frames during connection setup.

```javascript
session.sendAudio(audioBuffer);
```

**`injectUserMessage(content: string): void`** — inject a text message into the conversation as the user.

```javascript
session.injectUserMessage("What's the weather like?");
```

**`injectAgentMessage(message: string): void`** — inject a text message into the conversation as the agent.

```javascript
session.injectAgentMessage("Let me look that up for you.");
```

**`updatePrompt(prompt: string): void`** — change the agent's system prompt mid-session.

```javascript
session.updatePrompt("You are now a customer support agent.");
```

**`updateSpeak(settings): void`** — change TTS settings mid-session. Accepts a `SpeakSettings` object or an array.

```javascript
session.updateSpeak({
  provider: { type: "deepgram", model: "aura-2-orion-en" },
});
```

**`updateThink(settings): void`** — change LLM settings mid-session. Accepts a `ThinkSettings` object or an array.

```javascript
session.updateThink({
  provider: { type: "open_ai", model: "gpt-4o" },
});
```

**`sendFunctionCallResponse(id, name, content): void`** — respond to a function call request from the agent. See [Function Calls](#function-calls) for a complete example.

```javascript
session.sendFunctionCallResponse(fn.id, fn.name, JSON.stringify(result));
```

**`getId(): string | null`** — returns the session ID assigned by the server. Available after the `welcome` event fires. Returns `null` before connection.

```javascript
const sessionId = session.getId();
```

### Events

Subscribe with `session.on(event, callback)` and unsubscribe with `session.off(event, callback)`.

**Connection lifecycle:**

| Event          | Callback signature                           | Description                                                                           |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- |
| `connecting`   | `() => void`                                 | WebSocket connection attempt started.                                                 |
| `connected`    | `() => void`                                 | WebSocket connection established.                                                     |
| `reconnecting` | `(attempt: number, delayMs: number) => void` | Attempting reconnection. Includes the attempt number and delay before the next retry. |
| `disconnected` | `(reason: string) => void`                   | Connection closed. The reason string describes why.                                   |

**Agent protocol:**

| Event                    | Callback signature | Description                                                                                       |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------- |
| `welcome`                | `(msg) => void`    | Session initialized by the server. Payload includes `session_id`.                                 |
| `settings-applied`       | `(msg) => void`    | Server acknowledged settings. The agent is ready to receive audio.                                |
| `conversation-text`      | `(msg) => void`    | A conversation turn was transcribed. Payload: `{ role: "user" \| "assistant", content: string }`. |
| `user-started-speaking`  | `(msg) => void`    | Server detected user speech.                                                                      |
| `agent-thinking`         | `(msg) => void`    | Agent is processing a response.                                                                   |
| `agent-started-speaking` | `(msg) => void`    | Agent began sending TTS audio.                                                                    |
| `agent-audio-done`       | `(msg) => void`    | Agent finished sending audio. Note: browser playback may still be in progress.                    |
| `function-call-request`  | `(msg) => void`    | Agent requests one or more client-side function calls. Payload includes a `functions` array.      |
| `function-call-response` | `(msg) => void`    | Server acknowledged a function call response.                                                     |
| `prompt-updated`         | `(msg) => void`    | System prompt was changed successfully.                                                           |
| `speak-updated`          | `(msg) => void`    | TTS settings were changed successfully.                                                           |
| `think-updated`          | `(msg) => void`    | LLM settings were changed successfully.                                                           |
| `injection-refused`      | `(msg) => void`    | A message injection was rejected by the server.                                                   |

**Audio:**

| Event   | Callback signature             | Description                                                         |
| ------- | ------------------------------ | ------------------------------------------------------------------- |
| `audio` | `(chunk: ArrayBuffer) => void` | Raw PCM audio buffer from the agent. Pass to `AgentPlayer.queue()`. |

**Errors:**

| Event       | Callback signature     | Description                                                  |
| ----------- | ---------------------- | ------------------------------------------------------------ |
| `error`     | `(msg) => void`        | Server-side agent error.                                     |
| `warning`   | `(msg) => void`        | Server-side warning.                                         |
| `sdk-error` | `(err: Error) => void` | Client-side SDK error (connection failures, timeouts, etc.). |

## AgentMicrophone

Captures PCM audio from the user's microphone using the Web Audio API. Optionally integrates Silero VAD for voice activity detection so audio is only transmitted during speech.

```javascript
import { AgentMicrophone } from "@deepgram/agents";

const mic = new AgentMicrophone(
  (data) => session.sendAudio(data),
  {
    sampleRate: 16_000,
    echoCancellation: true,
    noiseSuppression: true,
    autoGainControl: true,
  }
);

await mic.start();
```

The first argument is a callback invoked with each captured audio frame as an `ArrayBuffer`. Pass `session.sendAudio` to stream audio directly to the agent.

### Options

| Option             | Type                    | Default | Description                                                                             |
| ------------------ | ----------------------- | ------- | --------------------------------------------------------------------------------------- |
| `sampleRate`       | `number`                | `16000` | Target sample rate in Hz for PCM capture.                                               |
| `echoCancellation` | `boolean`               | `true`  | Enable browser echo cancellation via `getUserMedia`.                                    |
| `noiseSuppression` | `boolean`               | `true`  | Enable browser noise suppression via `getUserMedia`.                                    |
| `autoGainControl`  | `boolean`               | `true`  | Enable browser auto gain control via `getUserMedia`.                                    |
| `vad`              | `boolean \| VadOptions` | `false` | Enable Silero voice activity detection. Pass `true` for defaults, or an options object. |

**VAD options** (when `vad` is an object):

| Option             | Default | Description                                                              |
| ------------------ | ------- | ------------------------------------------------------------------------ |
| `speechThreshold`  | `0.5`   | Probability threshold (0--1) above which audio is classified as speech.  |
| `silenceThreshold` | `0.35`  | Probability threshold (0--1) below which audio is classified as silence. |

VAD requires the optional peer dependencies `@ricky0123/vad-web` and `onnxruntime-web`. Install them separately: `npm install @ricky0123/vad-web onnxruntime-web`.

### Methods

**`start(): Promise<void>`** — request microphone permission via `getUserMedia` and begin capturing audio frames.

```javascript
await mic.start();
```

**`stop(): void`** — stop capturing audio, disconnect the audio worklet, and release the microphone device.

```javascript
mic.stop();
```

**`mute(): void`** — pause audio transmission without releasing the microphone. The device remains active but frames are not forwarded.

```javascript
mic.mute();
```

**`unmute(): void`** — resume audio transmission after a `mute()` call.

```javascript
mic.unmute();
```

**`muted: boolean`** — read-only property indicating whether the microphone is currently muted.

**`getInputVolume(): number`** — returns the current RMS input volume level as a value between 0 and 1. Call per animation frame for real-time visualizations.

```javascript
function animate() {
  const volume = mic.getInputVolume();
  drawMeter(volume);
  requestAnimationFrame(animate);
}
```

**`getInputByteFrequencyData(): Uint8Array`** — returns frequency domain data as a `Uint8Array` with values 0--255. Use for spectrum or waveform visualizations.

### Events

Subscribe with `mic.on(event, callback)` and unsubscribe with `mic.off(event, callback)`.

| Event          | Callback signature            | Description                                                             |
| -------------- | ----------------------------- | ----------------------------------------------------------------------- |
| `speech-start` | `() => void`                  | VAD detected the user started speaking. Only fires when VAD is enabled. |
| `speech-end`   | `() => void`                  | VAD detected the user stopped speaking. Only fires when VAD is enabled. |
| `audio-frame`  | `(data: ArrayBuffer) => void` | A raw audio frame was captured.                                         |
| `error`        | `(err: Error) => void`        | Microphone error (permission denied, device lost, etc.).                |

## AgentPlayer

Decodes and plays PCM audio received from the agent. Maintains a playback queue with interrupt support for barge-in, and exposes volume and frequency analysis APIs for building custom visualizations.

```javascript
import { AgentPlayer } from "@deepgram/agents";

const player = new AgentPlayer({ sampleRate: 24_000 });

session.on("audio", (chunk) => player.queue(chunk));
session.on("user-started-speaking", () => player.interrupt());
```

### Options

| Option       | Type     | Default | Description                                                                                                               |
| ------------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| `sampleRate` | `number` | `24000` | Expected sample rate of audio received from the agent. Must match `audio.output.sampleRate` in the session configuration. |

### Methods

**`queue(data: ArrayBuffer): void`** — decode a PCM audio buffer and add it to the playback queue. Buffers are played in order with sample-accurate scheduling.

**`interrupt(): void`** — immediately stop playback and discard all queued audio. Use when the user starts speaking to enable barge-in.

**`getRemainingPlaybackTime(): number`** — returns the number of seconds of audio still queued for playback. Returns 0 when idle. Useful for delaying mode transitions until the agent finishes speaking.

**`mute(): void`** — stop playback and discard queued audio. Subsequent calls to `queue()` are silently dropped until `unmute()` is called.

**`unmute(): void`** — resume accepting and playing queued audio.

**`muted: boolean`** — read-only property indicating whether the player is currently muted.

**`setVolume(volume: number): void`** — set the playback volume as a value between 0 and 1. Default: `1`.

```javascript
player.setVolume(0.5);
```

**`volume: number`** — read-only property returning the current playback volume (0--1).

**`getOutputVolume(): number`** — returns the current RMS output volume level as a value between 0 and 1. Call per animation frame for real-time visualizations.

**`getOutputByteFrequencyData(): Uint8Array`** — returns frequency domain data as a `Uint8Array` with values 0--255. Use for spectrum visualizations of the agent's speech.

**`dispose(): void`** — close the underlying `AudioContext` and free resources. Call when the session is no longer needed.

## Function Calls

The agent can request client-side function calls during a conversation. Listen for the `function-call-request` event, execute the requested function, and respond with the result using `sendFunctionCallResponse`.

```javascript
session.on("function-call-request", async (msg) => {
  for (const fn of msg.functions) {
    let result;

    switch (fn.name) {
      case "get_weather":
        result = await fetchWeather(JSON.parse(fn.input));
        break;
      case "book_appointment":
        result = await bookAppointment(JSON.parse(fn.input));
        break;
      default:
        result = { error: `Unknown function: ${fn.name}` };
    }

    session.sendFunctionCallResponse(fn.id, fn.name, JSON.stringify(result));
  }
});
```

Each item in the `functions` array contains:

| Field   | Type     | Description                                                          |
| ------- | -------- | -------------------------------------------------------------------- |
| `id`    | `string` | Unique identifier for this function call. Pass back in the response. |
| `name`  | `string` | The function name the agent wants to invoke.                         |
| `input` | `string` | JSON-encoded arguments for the function.                             |

The agent pauses until it receives a response for each requested function call.

## Token Caching

The SDK caches authentication tokens internally. When you provide a `tokenFactory` in the auth configuration, the `AgentSession` wraps it in a caching layer that avoids requesting a new token on every reconnect. Tokens are cached for 4 minutes by default, which is safe for Deepgram's 5-minute short-lived keys. The cache is automatically invalidated before each reconnection attempt to ensure a fresh token is available.

```javascript
const session = new AgentSession({
  auth: {
    // This function is only called when the cache is empty or expired
    tokenFactory: async () => {
      const res = await fetch("/api/deepgram-token");
      return res.text();
    },
  },
  agent: "YOUR_AGENT_ID",
});
```

No additional setup is required. The caching behavior is automatic and transparent.
