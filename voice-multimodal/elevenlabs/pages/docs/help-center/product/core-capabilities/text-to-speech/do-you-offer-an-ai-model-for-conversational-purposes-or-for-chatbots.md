---
title: "Do you offer an AI model for conversational purposes or for chatbots?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/do-you-offer-an-ai-model-for-conversational-purposes-or-for-chatbots.md
path: docs/help-center/product/core-capabilities/text-to-speech/do-you-offer-an-ai-model-for-conversational-purposes-or-for-chatbots
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Do you offer an AI model for conversational purposes or for chatbots?

Yes. For conversational applications, chatbots, and real-time voice agents, we offer several models optimized for low latency and interactive dialogue.

### Real-time and low-latency models

* **Eleven v4 Turbo** (`eleven_v4_turbo`): Our state-of-the-art model for real-time speech synthesis, purpose-built for conversational applications, customer support agents, and interactive assistants. It delivers high-quality, expressive speech with a median latency of \~100ms and supports 90+ languages.
* **Eleven v3 Conversational** (`eleven_v3_conversational`): Our previous-generation real-time model, offering expressive delivery and dramatic performance across 70+ languages with \~165ms latency.
* **Eleven Flash v2.5** (`eleven_flash_v2_5`): An ultra-low-latency model (\~100ms median latency) across 32 languages, offering a cost-effective option with a 50% discount per character for API generations.
* **Eleven Flash v2** (`eleven_flash_v2`): An ultra-low-latency model (\~135ms median latency) for English-only applications.

For a full list of languages supported across models, see [What languages do you support?](/docs/help-center/other/what-languages-do-you-support).

### Deprecated models

Our Turbo v2 (`eleven_turbo_v2`) and Turbo v2.5 (`eleven_turbo_v2_5`) models are low-latency models from an earlier generation. They are deprecated and functionally outclassed by the Flash and v4 Turbo models, which achieve lower latency and better vocal performance. We recommend using Eleven v4 Turbo or Eleven Flash v2.5 for all new projects.

### ElevenAgents

If you are looking to build full conversational voice agents rather than integrating raw speech synthesis models yourself, we offer [ElevenAgents](/docs/eleven-agents/overview). ElevenAgents combines speech recognition, an LLM, speech synthesis, and turn-taking into a complete orchestration platform for interactive voice applications. By default, new agents use Eleven v4 Turbo. For more information, visit our [ElevenAgents documentation](/docs/eleven-agents/overview).
