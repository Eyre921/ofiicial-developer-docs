---
title: "How to choose the right model"
source: https://elevenlabs.io/docs/eleven-api/choosing-the-right-model.md
path: docs/eleven-api/choosing-the-right-model
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How to choose the right model

ElevenLabs offers a range of models optimised for different requirements. The right choice depends on your use case, latency requirements, and quality expectations. Refer to the [models reference](/docs/overview/models) for full specifications.

## By requirement

#### Quality

Use `eleven_v3`

The flagship model with the highest fidelity, richest emotional expression, and broadest language support.

#### Low-latency

Use Flash models (`eleven_flash_v2_5` or `eleven_flash_v2`)

Optimised for real-time applications with \~75ms latency.

#### Expressive realtime

Use `eleven_v3_conversational`

Our most expressive model for realtime speech synthesis, with \~280ms latency and audio tags for fine-grained control.

#### Multilingual

Use `eleven_v3` or `eleven_v3_conversational`

Both support 70+ languages.

#### Balanced

Use `eleven_flash_v2_5` or `eleven_v3_conversational`

High-quality output with low latency — the best all-round choice.

## By use case

#### Content creation

Use `eleven_v3`

Ideal for professional content, audiobooks, and video narration.

#### Conversational agents

Use `eleven_v3_conversational` for the most expressive delivery, or `eleven_flash_v2_5` and `eleven_flash_v2` for the lowest latency.

Use the 2.5 model for language support outside of English.

Optimised for real-time conversational applications.

#### Transcription

Use `scribe_v2` for batch transcription or `scribe_v2_realtime` for real-time transcription.

State-of-the-art accuracy across 90+ languages with speaker diarisation and word-level timestamps.

#### Voice changer

Use `eleven_multilingual_sts_v2`

Specialised for Speech-to-Speech conversion.

## Next steps

#### [Models](/docs/overview/models)

View full model specifications, latency benchmarks, and feature comparisons.

#### [Latency optimization](/docs/eleven-api/guides/how-to/best-practices/latency-optimization)

Reduce time-to-first-audio with model selection, voice choice, and geographic routing.
