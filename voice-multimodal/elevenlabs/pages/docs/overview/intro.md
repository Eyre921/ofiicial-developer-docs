---
title: "ElevenLabs Documentation"
source: https://elevenlabs.io/docs/overview/intro.md
path: docs/overview/intro
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenLabs Documentation

## How ElevenLabs works

ElevenLabs provides AI voice infrastructure: text-to-speech, speech-to-text, voice cloning, conversational agents, and generative audio. You can use it in four ways, suited to different audiences.

**[ElevenCreative](/docs/eleven-creative)** is a no-code web application where creators, producers, and editors generate voiceovers, music, dubs, and studio projects directly in the browser.

**[ElevenAgents](/docs/eleven-agents)** is the platform for designing and operating conversational voice agents, with a visual builder for non-technical users and full programmatic control for developers.

**[ElevenAPI](/docs/eleven-api)** exposes every capability as a REST interface with official Python and TypeScript SDKs, so developers can embed voice into their own applications and workflows.

**[Reception AI](/docs/reception-ai)** is a ready-to-deploy AI phone receptionist for small and medium businesses that answers calls, books appointments, and manages day-to-day operations from a single dashboard.

### Concepts

**Voices** are the speech persona used in audio generation. Each voice has a unique ID — for example, `JBFqnCBsd6RMkjVDRZzb` — that you select in the dashboard or pass in API requests. ElevenLabs maintains a [library of 10,000+ voices](https://elevenlabs.io/app/voice-library). You can also clone a voice from an audio recording or generate one from a text description.

**Models** control the quality, latency, and language coverage of generated audio. [`eleven_v3`](/docs/overview/models) produces the most expressive output across 70+ languages. [`eleven_flash_v2_5`](/docs/overview/models) targets real-time use at \~75ms latency. Each capability — speech-to-text, music, sound effects — has its own dedicated model.

**Credits** are the unit of consumption shared across every product. Text-to-speech costs one credit per character of input text. Other operations are charged per second of audio processed. Credits reset monthly and unused credits roll over for up to two months. See [pricing](https://elevenlabs.io/pricing/api) for a full breakdown.

## Choose your path

[![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/12097a437e55f60c199946cf59c9528eb8349d110142394833d67fe93b50e68d/assets/images/overview/voice-library-bg.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T233130Z&X-Amz-Expires=604800&X-Amz-Signature=9377afe39734f3f96718f6f7d35dbff01b38b6667d2368c09458a87d30e57c98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)](/docs/eleven-creative/overview)

### ElevenCreative

Learn how to use the ElevenCreative platform with step-by-step guides

[![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7375358c43ac5dd1a170937123f0874e01b3d8b6cf178c282805588a11d39593/assets/images/agents/agents-overview-integrate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T233130Z&X-Amz-Expires=604800&X-Amz-Signature=250d2c45d861edb1928a2c7b7ee82f9021a34b6b8ef5b504ee8f2195ecf2cd42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)](/docs/eleven-agents/overview)

### ElevenAgents

Learn how to build, launch, and scale agents with ElevenLabs

[![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/002b2432fa6ab18befc9f1a6e7fadf348f46506a5a5a72a2358ba1e7f92d8ded/assets/images/overview/scribe-code-bg.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T233130Z&X-Amz-Expires=604800&X-Amz-Signature=ac175fb3d599303e2679e084dbe00bc1abbb4a4fc4ea69b37d28048ce8289c5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)](/docs/eleven-api/quickstart)

### ElevenAPI

Learn how to integrate with the ElevenLabs API with examples and tutorials

## Meet the models

#### [Eleven v3](/docs/overview/models#eleven-v3)

Our most emotionally rich, expressive speech synthesis model

Dramatic delivery and performance

70+ languages supported

5,000 character limit

Support for natural multi-speaker dialogue

#### [Eleven v3 Conversational](/docs/overview/models#eleven-v3-conversational)

Our most expressive, realtime speech synthesis model

Low latency (\~280ms)

Dramatic delivery and performance

70+ languages supported

Audio tags for fine-grained control

#### [Eleven Multilingual v2](/docs/overview/models#multilingual-v2)

Lifelike, consistent quality speech synthesis model

Natural-sounding output

29 languages supported

10,000 character limit

Most stable on long-form generations

#### [Eleven Flash v2.5](/docs/overview/models#flash-v25)

Our fast, affordable speech synthesis model

Ultra-low latency (\~75ms†)

32 languages supported

40,000 character limit

Faster model, 50% lower price per character for API generations

#### [Scribe v2](/docs/overview/models#scribe-v2)

State-of-the-art speech recognition model

Accurate transcription in 90+ languages

Keyterm prompting, up to 1000 terms

Entity detection, 65 entity types

Precise word-level timestamps

Speaker diarization, up to 32 speakers

Dynamic audio tagging

Smart language detection

#### [Scribe v2 Realtime](/docs/overview/models#scribe-v2-realtime)

Real-time speech recognition model

Accurate transcription in 90+ languages

Real-time transcription

Low latency (\~150ms†)

Precise word-level timestamps

Entity detection, 65 entity types

[Explore all](/docs/overview/models)

† Excluding application & network latency

## Browse by capability

Text to Speech

Convert text into lifelike speech

Speech to Text

Transcribe spoken audio into text

Music

Generate music from text

Text to Dialogue

Create natural-sounding dialogue from text

Image & Video

Generate images and videos from text

Voice changer

Modify and transform voices

Voice isolator

Isolate voices from background noise

Dubbing

Dub audio and videos seamlessly

Sound effects

Create cinematic sound effects

Voices

Clone and design custom voices

Voice Remixing

Transform and enhance existing voices

Forced Alignment

Align text to audio

Speech Engine

Add voice to anything

ElevenAgents

Deploy intelligent voice agents

Private deployments

Run ElevenLabs in your own cloud
