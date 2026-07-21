---
title: "Voice customization"
source: https://elevenlabs.io/docs/eleven-agents/customization/voice.md
path: docs/eleven-agents/customization/voice
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice customization

## Overview

You can customize various aspects of your AI agent's voice to create a more natural and engaging conversation experience. This includes controlling pronunciation, speaking speed, and language-specific voice settings.

## Available customizations

#### [Multi-voice support](/docs/eleven-agents/customization/voice/multi-voice-support)

Enable your agent to switch between different voices for multi-character conversations,
storytelling, and language tutoring.

#### [Pronunciation dictionary](/docs/eleven-agents/customization/voice/pronunciation-dictionary)

Control how your agent pronounces specific words and phrases using
[IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) or
[CMU](https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary) notation.

#### [Speed control](/docs/eleven-agents/customization/voice/speed-control)

Adjust how quickly or slowly your agent speaks, with values ranging from 0.7x to 1.2x.

#### [Expressive mode](/docs/eleven-agents/customization/voice/expressive-mode)

Context-aware emotional delivery powered by Eleven v3 Conversational and an improved turn-taking
system.

#### [Language-specific voices](/docs/eleven-agents/customization/voice/customization/language)

Configure different voices for each supported language to ensure natural pronunciation.

## Best practices

#### Voice selection

Choose voices that match your target language and region for the most natural pronunciation.
Consider testing multiple voices to find the best fit for your use case.

#### Speed optimization

Start with the default speed (1.0) and adjust based on your specific needs. Test different
speeds with your content to find the optimal balance between clarity and natural flow.

#### Pronunciation dictionaries

Focus on terms specific to your business or use case that need consistent pronunciation and are
not widely used in everyday conversation. Test pronunciations with your chosen voice and model
combination.

Some voice customization features may be model-dependent. For example, phoneme-based pronunciation
control is only available with the Flash v2 model.
