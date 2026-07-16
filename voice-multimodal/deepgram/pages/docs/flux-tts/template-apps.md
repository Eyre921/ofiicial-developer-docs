---
title: "Template Apps"
source: https://developers.deepgram.com/docs/flux-tts/template-apps.md
path: docs/flux-tts/template-apps
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Template Apps

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

Each template is a runnable demo that streams text to Deepgram Flux TTS over `/v2/speak` and plays the audio back. Unlike the Flux **transcription** starters, these use the official SDK's `speak.v2` client on the backend, so the SDK manages the Deepgram WebSocket, authentication, and binary-audio framing for you.

## SDKs

The Python, JavaScript, and Java SDKs ship a `speak.v2` client for `/v2/speak`:

* **Python** — `deepgram-sdk` ([GitHub](https://github.com/deepgram/deepgram-python-sdk))
* **JavaScript** — `@deepgram/sdk` ([GitHub](https://github.com/deepgram/deepgram-js-sdk))
* **Java** — `deepgram-java-sdk` ([GitHub](https://github.com/deepgram/deepgram-java-sdk))

See [Getting Started](/docs/flux-tts/quickstart) for the `speak.v2` code shape. Languages without SDK support yet can connect to the [WebSocket directly](/docs/flux-tts/quickstart).

## Starter apps

* [Node.js](https://github.com/deepgram-starters/node-flux-tts) — Flux streaming TTS demo app using Node.js (`@deepgram/sdk`)
* [Flask](https://github.com/deepgram-starters/flask-flux-tts) — Flux streaming TTS demo app using Flask (`deepgram-sdk`)
* [FastAPI](https://github.com/deepgram-starters/fastapi-flux-tts) — Flux streaming TTS demo app using FastAPI (`deepgram-sdk`)
* [Django](https://github.com/deepgram-starters/django-flux-tts) — Flux streaming TTS demo app using Django (`deepgram-sdk`)
* [Java](https://github.com/deepgram-starters/java-flux-tts) — Flux streaming TTS demo app using Java (`deepgram-java-sdk`)
