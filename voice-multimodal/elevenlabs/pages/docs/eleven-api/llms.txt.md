---
title: "ElevenAPI"
source: https://elevenlabs.io/docs/eleven-api/llms.txt
path: docs/eleven-api/llms.txt
---

> This is a page from the ElevenLabs documentation. For an index of the documentation, fetch https://elevenlabs.io/docs/llms.txt.

# ElevenAPI

> ElevenLabs provides APIs and SDKs for text to speech, voice cloning, speech to text, sound effects, voice isolator, voice changer, and conversational AI agents. Build voice-enabled applications with lifelike audio generation.

## Docs

- [ElevenAPI quickstart](https://elevenlabs.io/docs/eleven-api/quickstart.md): Learn how to make your first ElevenLabs API request.
- [How to choose the right model](https://elevenlabs.io/docs/eleven-api/choosing-the-right-model.md): This guide shows you how to choose the right ElevenLabs model for your use case.
- [Speech to Text quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/speech-to-text.md): Learn how to convert spoken audio into text.
- [Speech Engine quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/speech-engine.md): Add voice to your chat agent using the ElevenLabs SDK.
- [Music quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/music.md): Learn how to generate music with the Music API.
- [Text to Dialogue quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue.md): Learn how to generate immersive dialogue from text.
- [Image & Video quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/image-and-video.md): Learn how to generate images and videos from text prompts and reference media.
- [Templates quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/templates.md): Run a template built in ElevenCreative Flows from your own code.
- [Voice Changer quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/voice-changer.md): Learn how to transform the voice of an audio file using the Voice Changer API.
- [Voice Isolator quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/voice-isolator.md): Learn how to remove background noise from an audio file using the Voice Isolator API.
- [Dubbing quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/dubbing.md): Learn how to dub audio and video files across languages using the Dubbing API.
- [Sound Effects quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/sound-effects.md): Learn how to generate sound effects using the Sound Effects API.
- [Forced Alignment quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/forced-alignment.md): Learn how to use the Forced Alignment API to align text to audio.
- [Understanding audio streaming](https://elevenlabs.io/docs/eleven-api/concepts/audio-streaming.md): Why streaming audio generation is different from streaming files, and what that means for your application.
- [Understanding latency](https://elevenlabs.io/docs/eleven-api/concepts/latency.md): What latency means in audio generation, what contributes to it, and how to reason about tradeoffs.
- [How ElevenLabs latency figures are measured](https://elevenlabs.io/docs/eleven-api/concepts/latency-methodology.md): What the published latency figures for Eleven v4 Turbo, Eleven v3 Conversational, Eleven Flash and Scribe v2 Realtime measure, and the conditions behind them.
- [Voice cloning: how it works](https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning.md): The technical differences between Instant and Professional Voice Cloning, and what they mean for quality.
- [Content Provenance API (Beta)](https://elevenlabs.io/docs/eleven-api/concepts/content-provenance.md): Check whether an audio file carries an ElevenLabs watermark, and what that tells you about where it came from.
- [Streaming text to speech](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming.md): This guide shows you how to stream text to speech and optionally upload audio to AWS S3.
- [Stitching multiple requests](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching.md): This guide shows you how to maintain voice prosody across multiple text chunks/generations.
- [Using pronunciation dictionaries](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries.md): This guide shows you how to manage pronunciation dictionaries programmatically.
- [Streaming and Caching with Supabase](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming-and-caching-with-supabase.md): Generate and stream speech through Supabase Edge Functions. Store speech in Supabase Storage and cache responses via built-in CDN.
- [Sending generated audio through Twilio](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/twilio.md): Learn how to integrate generated speech into phone calls with Twilio.
- [Multichannel speech-to-text](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/multichannel-transcription.md): This guide shows you how to use multichannel transcription mode with the Speech to Text API.
- [Asynchronous Speech to Text](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks.md): This guide shows you how to use webhooks to receive asynchronous notifications when transcription tasks complete.
- [Keyterm prompting](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting.md): This guide shows you how to use keyterm prompting with the Speech to Text API.
- [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection.md): This guide shows you how to use entity detection with the Speech to Text API.
- [Transcript editing](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing.md): This guide shows you how to edit transcripts with natural-language instructions using the Speech to Text API.
- [Number and language options](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options.md): This guide shows you how to control number formatting and declare secondary languages with Scribe v3.
- [Transcription Telegram Bot](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/telegram-bot.md): Build a Telegram bot that transcribes audio and video messages in 90+languages using TypeScript with Deno in Supabase Edge Functions.
- [Vercel AI SDK](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/vercel-ai-sdk.md): Use the ElevenLabs Provider in the Vercel AI SDK to transcribe speech from audio and video files.
- [Client-side streaming](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming.md): This guide shows you how to transcribe audio in real time on the client side using ElevenLabs.
- [Server-side streaming](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming.md): This guide shows you how to transcribe audio in real time on the server side using ElevenLabs.
- [Transcripts and commit strategies](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies.md): This guide shows you how to handle transcripts and commit strategies with the ElevenLabs Realtime Speech to Text API.
- [Language options](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/language-options.md): This guide shows you how to transcribe audio in more than one language with the Realtime Speech to Text API.
- [Transcript editing](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcript-editing.md): This guide shows you how to apply natural-language edit instructions to committed transcripts with the Realtime Speech to Text API.
- [Speaker diarization](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/diarization.md): This guide shows you how to label who is speaking in realtime transcripts with the Realtime Speech to Text API.
- [Realtime event reference](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/event-reference.md): Reference of the events received from the Realtime Speech to Text API
- [Music streaming](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/streaming.md): This guide shows you how to stream music with our Music API.
- [Composition plans](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans.md): Precise control over music generation with structured JSON
- [Music inpainting](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/inpainting.md): Edit and combine sections of existing songs
- [References and assets](https://elevenlabs.io/docs/eleven-api/guides/how-to/image-and-video/references.md): Guide a generation with a previous generation, an uploaded asset, or inline media.
- [Image & Video webhooks](https://elevenlabs.io/docs/eleven-api/guides/how-to/image-and-video/webhooks.md): Receive the result of a generation instead of polling for it.
- [Run your team's template](https://elevenlabs.io/docs/eleven-api/guides/how-to/templates/run-a-template.md): Call a template published in ElevenCreative Flows from your application.
- [Refine and regenerate a dub](https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate.md): Edit the source transcript and translations, then regenerate a language's audio.
- [Dub into multiple languages](https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/multiple-languages.md): Add several target languages to a single project and download each dub.
- [Manage dubbing projects](https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/manage-projects.md): List, retrieve, and delete dubbing projects and their language targets.
- [Bring your own transcript](https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/bring-your-own-transcript.md): Create a dubbing project from your own transcript and supply your own translations.
- [Instant Voice Cloning quickstart](https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/instant-voice-cloning.md): This guide shows you how to clone a voice using the Clone Voice API.
- [Professional Voice Cloning quickstart](https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/professional-voice-cloning.md): This guide shows you how to create a Professional Voice Clone using the PVC API.
- [Voice Design quickstart](https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/voice-design.md): This guide shows you how to design a voice via a text prompt using the Voice Design API.
- [Voice Remixing quickstart](https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/remix-a-voice.md): This guide shows you how to remix an existing voice to create a new one.
- [Generate audio in real-time](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts.md): This guide shows you how to generate audio in real-time via a WebSocket connection.
- [Stream dialogue in real-time](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd.md): This guide shows you how to stream Eleven v3 dialogue audio over the Text to Dialogue WebSocket.
- [Text to Speech vs Text to Dialogue WebSockets](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets.md): This guide shows you how to choose the right WebSocket for streaming speech and how the two protocols differ.
- [Multi-Context Websocket](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket.md): This guide shows you how to build real-time voice agents using the multi-context WebSocket API.
- [LiveKit integration](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-engine/livekit-integration.md): Bridge a LiveKit room into Speech Engine using a LiveKit Agents worker.
- [Pipecat integration](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-engine/pipecat-integration.md): Use a Pipecat pipeline as the LLM brain behind Speech Engine.
- [Latency optimization](https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/latency-optimization.md): This guide shows you how to reduce text-to-speech latency in your application.
- [Secure by design](https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/security.md): Learn how to safely integrate ElevenLabs APIs.
- [Libraries & SDKs](https://elevenlabs.io/docs/eleven-api/resources/libraries.md): Explore language-specific libraries for using the ElevenLabs API.
- [JavaScript SDK](https://elevenlabs.io/docs/eleven-api/resources/libraries/scribe-stt/javascript-scribe.md): Scribe: real-time speech-to-text transcription in JavaScript
- [React SDK](https://elevenlabs.io/docs/eleven-api/resources/libraries/scribe-stt/react-scribe.md): useScribe: real-time speech-to-text transcription in React
- [JavaScript SDK reference](https://elevenlabs.io/docs/eleven-api/resources/libraries/speech-engine/javascript-sdk-reference.md): Classes, methods, and events for the Speech Engine JavaScript SDK.
- [Python SDK reference](https://elevenlabs.io/docs/eleven-api/resources/libraries/speech-engine/python-sdk-reference.md): Classes, methods, and events for the Speech Engine Python SDK.
- [Errors](https://elevenlabs.io/docs/eleven-api/resources/errors.md): Explore error messages and solutions.
- [Agent Tooling](https://elevenlabs.io/docs/eleven-api/resources/agent-tooling.md): Tools for agents to build with ElevenLabs.
- [ElevenLabs MCP server](https://elevenlabs.io/docs/eleven-api/resources/mcp-server.md): Generate speech, images and video and build agents from Claude and other MCP clients.
- [Webhooks](https://elevenlabs.io/docs/eleven-api/resources/webhooks.md): Enable external integrations by receiving webhook events.
- [IP allowlisting](https://elevenlabs.io/docs/eleven-api/resources/ip-allowlisting.md): Static egress IP addresses for ElevenLabs services.
- [Zero Retention Mode (Enterprise)](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode.md): Learn how to use Zero Retention Mode to protect sensitive data.
- [Breaking changes policy](https://elevenlabs.io/docs/eleven-api/resources/breaking-changes-policy.md): Learn how ElevenLabs defines breaking changes in the APIs.

