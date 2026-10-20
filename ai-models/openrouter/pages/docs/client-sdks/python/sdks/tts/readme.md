---
title: "TTS"
source: https://openrouter.ai/docs/client-sdks/python/sdks/tts/README.md
path: docs/client-sdks/python/sdks/tts/readme
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TTS

> Text-to-speech endpoints

## Overview

Text-to-speech endpoints

### Available Operations

* [create\_speech](#create_speech) - Create speech

## create\_speech

Synthesizes audio from the input text. Returns a raw audio bytestream in the requested format (e.g. mp3, pcm, wav).

### Example Usage

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.tts.create_speech(input="Hello world", model="mistralai/voxtral-mini-tts-2603", response_format="pcm", speed=1, voice="en_paul_neutral")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `input` | [components.SpeechInput](../../components/speechinput.mdx) | ✅ | Text to synthesize, or a list of turns for multi-speaker input. Each turn has its own text, voice, and instructions. Multi-speaker input is supported by Gemini TTS models and by Fish Audio models other than S1. | Hello world |
| `model` | *str* | ✅ | TTS model identifier | mistralai/voxtral-mini-tts-2603 |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `input_references` | List\[[components.SpeechInputReference](../../components/speechinputreference.mdx)] | ➖ | Reference content for stateless voice cloning or voice design. Audio mode: one to three `input_audio` parts, each optionally paired with a `text` part carrying its transcript (a single clip accepts its transcript before or after it; with multiple clips each transcript immediately follows its clip), plus at most one `image_url` part as a scene image on providers that condition the cloned voice on its setting; only routed to endpoints that support voice cloning (and multiple references or image references when those parts are sent). Image mode: exactly one `image_url` part; only routed to endpoints that support image references. An empty array is treated as no reference. | \[ \{ "input\_audio": \{ "data": "data:audio/wav;base64,UklGRuQXDABXQVZF..." }, "type": "input\_audio" }, \{ "text": "I used to rule the world.", "type": "text" } ] |
| `instructions` | *Optional\[str]* | ➖ | Delivery instructions for the whole request, such as tone, pacing, or emotion. Supported by OpenAI gpt-4o-mini-tts, Gemini TTS, and Fish Audio models. Ignored by other providers. | Speak in a warm and friendly tone. |
| `provider` | [Optional\[components.SpeechRequestProvider\]](../../components/speechrequestprovider.mdx) | ➖ | Provider configuration: data policy routing preferences (`zdr`, `data_collection`) and provider-specific passthrough options | |
| `response_format` | [Optional\[components.SpeechRequestResponseFormat\]](../../components/speechrequestresponseformat.mdx) | ➖ | Audio output format | pcm |
| `session_id` | *Optional\[str]* | ➖ | A unique identifier for grouping related requests (e.g., a conversation or agent workflow). Used for observability grouping in Broadcast and private logging; never sent to the provider. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters. | session-1234 |
| `speed` | *Optional\[float]* | ➖ | Playback speed multiplier. Honored by models that support it (e.g. OpenAI TTS). Other providers either ignore it or return a 400 for a non-default value when the model has no speed control. | 1 |
| `trace` | [Optional\[components.TraceConfig\]](../../components/traceconfig.mdx) | ➖ | Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations. | \{ "trace\_id": "trace-abc123", "trace\_name": "my-app-trace" } |
| `user` | *Optional\[str]* | ➖ | A unique identifier representing your end-user. Forwarded to Broadcast and private logging as the end-user id; never sent to the provider. | user-1234 |
| `voice` | *Optional\[str]* | ➖ | Voice identifier (provider-specific). | en\_paul\_neutral |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Response

**[httpx.Response](../../models/.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.PayloadTooLargeResponseError | 413 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.ServiceUnavailableResponseError | 503 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

