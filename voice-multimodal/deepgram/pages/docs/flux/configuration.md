---
title: "End-of-Turn Detection Parameters"
source: https://developers.deepgram.com/docs/flux/configuration.md
path: docs/flux/configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# End-of-Turn Detection Parameters

Flux provides configurable parameters that control end-of-turn detection and language biasing, allowing you to optimize your voice agent's conversational flow for your specific use case.

## Overview

Flux's behavior is controlled by the following key parameters:

| Parameter             | Range                    | Default | Required       | Description                                                                                                   |
| --------------------- | ------------------------ | ------- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| `eot_threshold`       | `0.5` - `0.9`            | `0.7`   | No             | Confidence threshold for triggering `EndOfTurn` events                                                        |
| `eager_eot_threshold` | `0.3` - `0.9`            | *None*  | For eager mode | Confidence threshold for triggering `EagerEndOfTurn` events                                                   |
| `eot_timeout_ms`      | `500` - `60000`          | `5000`  | No             | Maximum silence duration (ms) before forcing `EndOfTurn`                                                      |
| `language_hint`       | Supported language codes | *None*  | No             | Bias `flux-general-multi` toward specific languages. See [Language Prompting](/docs/flux/language-prompting). |

## Parameter Details

### `eot_threshold`

Confidence threshold required to trigger an `EndOfTurn` event, signaling that the user has finished speaking.

**Valid Values:** `0.5` to `0.9`
**Default:** `0.7`
**Type:** Float (passed as string in URL or SDK)

**Behavior:**

* **Higher values** (e.g., `0.8` - `0.9`) = Higher certainty required before ending a turn, fewer false positives, slightly increased latency
* **Lower values** (e.g., `0.5` - `0.7`) = Lower certainty required before ending a turn, faster responses, more false positives

**Example:**

```bash
wss://api.deepgram.com/v2/listen?model=flux-general-en&eot_threshold=0.8
```

---

### `eager_eot_threshold`

Confidence threshold for triggering `EagerEndOfTurn` events, enabling early LLM response generation.

**Valid Values:** `0.3` to `0.9`
**Default:** *Not set* (eager mode disabled)
**Type:** Float (passed as string in URL or SDK)

**Behavior:**

* **When set**: Enables `EagerEndOfTurn` and `TurnResumed` events
* **Lower values** (e.g., `0.3` - `0.5`) = Earlier triggers, lower latency, more false starts
* **Higher values** (e.g., `0.6` - `0.8`) = More conservative, fewer cancellations, less latency benefit

**Trade-offs:**

* ✅ Reduces E2E agent latency
* ❌ Increases LLM calls
* ❌ Requires handling `EagerEndOfTurn` speculative generation and `TurnResumed` cancellations

**Example:**

```bash
wss://api.deepgram.com/v2/listen?model=flux-general-en&eager_eot_threshold=0.6&eot_threshold=0.8
```

**Important**: The transcript in `EagerEndOfTurn` will **exactly match** the transcript in the subsequent `EndOfTurn` event (if no `TurnResumed` occurs). This guarantees consistency for caching strategies.

---

### `eot_timeout_ms`

Maximum silence duration before forcing an `EndOfTurn`, regardless of confidence.

**Valid Values:** `500` to `60000` (milliseconds)
**Default:** `5000` (5 seconds)
**Type:** Integer (passed as string in URL or SDK)

**Behavior:**

* Forces `EndOfTurn` after specified silence duration, even if confidence is below `eot_threshold`
* Timer resets when new speech is detected
* **Increase** (e.g., `7000` - `10000`) for users with frequent pauses
* **Decrease** (e.g., `3000` - `4000`) for rapid-response environments

**Example:**

```bash
wss://api.deepgram.com/v2/listen?model=flux-general-en&encoding=linear16&sample_rate=16000&eot_timeout_ms=7000
```

## Parameter Interactions

### Validation Rules

* `eager_eot_threshold` must be **less than or equal to** `eot_threshold` (if both are set)
* Setting `eager_eot_threshold > eot_threshold` will result in an error
* All parameters are optional, but their values must be within valid ranges if specified

## Common Configurations

### Simple Mode (Default)

```python Python
async with client.listen.v2.connect(
    model="flux-general-en",
    eot_threshold="0.7"  # Default value
) as connection:
    pass
```

```java Java
import com.deepgram.api.DeepgramClient;
import com.deepgram.api.resources.listen.resources.v2.resources.v2websocket.V2WebSocketClient;

DeepgramClient client = DeepgramClient.builder().build();
V2WebSocketClient wsClient = client.listen().v2().v2WebSocket();
wsClient.connect(V2WebSocketOptions.builder()
    .model("flux-general-en")
    .eotThreshold("0.7") // Default value
    .build())
    .get(10, TimeUnit.SECONDS);
```

**Best for:** Basic conversational agents, demos, getting started

---

### Low-Latency Mode

```python Python
async with client.listen.v2.connect(
    model="flux-general-en",
    eager_eot_threshold="0.4",
    eot_threshold="0.7",
    eot_timeout_ms="6000"
) as connection:
    pass
```

```java Java
V2WebSocketClient wsClient = client.listen().v2().v2WebSocket();
wsClient.connect(V2WebSocketOptions.builder()
    .model("flux-general-en")
    .eagerEotThreshold("0.4")
    .eotThreshold("0.7")
    .eotTimeoutMs("6000")
    .build())
    .get(10, TimeUnit.SECONDS);
```

**Best for:** High-volume customer service, fast-paced Q\&A, responsiveness over accuracy

---

### High-Reliability Mode

```python Python
async with client.listen.v2.connect(
    model="flux-general-en",
    eot_threshold="0.85",
    eot_timeout_ms="8000"
) as connection:
    pass
```

```java Java
V2WebSocketClient wsClient = client.listen().v2().v2WebSocket();
wsClient.connect(V2WebSocketOptions.builder()
    .model("flux-general-en")
    .eotThreshold("0.85")
    .eotTimeoutMs("8000")
    .build())
    .get(10, TimeUnit.SECONDS);
```

**Best for:** Medical/legal transcription, critical documentation, formal settings

---

### Complex Pipeline Mode

```python Python
async with client.listen.v2.connect(
    model="flux-general-en",
    eager_eot_threshold="0.4",
    eot_threshold="0.85",
    eot_timeout_ms="7000"
) as connection:
    pass
```

```java Java
V2WebSocketClient wsClient = client.listen().v2().v2WebSocket();
wsClient.connect(V2WebSocketOptions.builder()
    .model("flux-general-en")
    .eagerEotThreshold("0.4")
    .eotThreshold("0.85")
    .eotTimeoutMs("7000")
    .build())
    .get(10, TimeUnit.SECONDS);
```

**Best for:** RAG systems, tool-calling agents, multi-step reasoning workflows

---

### Multilingual Mode

```python Python
async with client.listen.v2.connect(
    model="flux-general-multi",
    encoding="linear16",
    sample_rate=16000,
    eot_threshold="0.7",
    request_options={
        "additional_query_parameters": {
            "language_hint": ["en", "es"],
        }
    },
) as connection:
    pass
```

```typescript JavaScript
const connection = await client.listen.v2.connect({
  model: "flux-general-multi",
  encoding: "linear16",
  sample_rate: 16000,
  eot_threshold: "0.7",
  Authorization: `Token ${process.env.DEEPGRAM_API_KEY}`,
  queryParams: { language_hint: ["en", "es"] },
});

connection.connect();
await connection.waitForOpen();
```

```java Java
import com.deepgram.DeepgramClient;
import com.deepgram.resources.listen.v2.types.ListenV2Configure;
import com.deepgram.resources.listen.v2.websocket.V2ConnectOptions;
import com.deepgram.resources.listen.v2.websocket.V2WebSocketClient;
import com.deepgram.types.ListenV2Encoding;
import com.deepgram.types.ListenV2EotThreshold;
import com.deepgram.types.ListenV2Model;
import com.deepgram.types.ListenV2SampleRate;
import java.util.List;
import java.util.concurrent.TimeUnit;

DeepgramClient client = DeepgramClient.builder().build();

V2ConnectOptions options = V2ConnectOptions.builder()
    .model(ListenV2Model.FLUX_GENERAL_MULTI)
    .encoding(ListenV2Encoding.LINEAR16)
    .sampleRate(ListenV2SampleRate.of(16000))
    .eotThreshold(ListenV2EotThreshold.of("0.7"))
    .build();

V2WebSocketClient wsClient = client.listen().v2().v2WebSocket();
wsClient.connect(options).get(10, TimeUnit.SECONDS);

// Set language hints for the session.
wsClient.sendConfigure(
    ListenV2Configure.builder()
        .languageHints(List.of("en", "es"))
        .build()
).get(5, TimeUnit.SECONDS);
```

```text Direct WebSocket
wss://api.deepgram.com/v2/listen?model=flux-general-multi&language_hint=en&language_hint=es&eot_threshold=0.7&encoding=linear16&sample_rate=16000
```

**Best for:** Multilingual call centers, global voice agents, code-switching scenarios

See the [Language Prompting guide](/docs/flux/language-prompting) for full details on language hint usage.

## Related Resources

* [Getting Started with Flux](/docs/flux/quickstart) - Quickstart guide with basic configuration
* [Configure Control Message](/docs/flux/configure) - Update configuration mid-stream without reconnecting
* [Flux State Machine](/docs/flux/state) - Understanding turn events and state transitions
* [Eager End-of-Turn Optimization](/docs/flux/voice-agent-eager-eot) - Deep dive on eager mode implementation
* [Build a Voice Agent](/docs/flux/agent) - Complete voice agent implementation guide
* [Migrating from Nova-3](/docs/flux/nova-3-migration) - Migration guide with configuration examples
