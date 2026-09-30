---
title: "Advanced settings"
source: https://elevenlabs.io/docs/reception-ai/receptionist/advanced-settings.md
path: docs/reception-ai/receptionist/advanced-settings
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Advanced settings

The **Advanced settings** card on the Receptionists page opens **Model & call behavior**. Most businesses never need to change these defaults.

## Model

Select the language model that powers your receptionist's conversations. Faster models reduce response time; larger models handle complex instructions better.

| Family | Models                                                                               |
| ------ | ------------------------------------------------------------------------------------ |
| Gemini | Gemini 3 Flash, 3.5 Flash, 3.6 Flash (default), 3.7 Flash, 3.8 Flash, 3.1 Flash Lite |
| GPT    | GPT-5.4 Mini, GPT-5.4 Nano                                                           |
| Claude | Claude Haiku 4.5, Claude Sonnet 5                                                    |
| Qwen   | Qwen3.5-397B-A17B, Qwen3.6-35B-A3B                                                   |

### Reasoning effort

Controls how much the model thinks before responding. The available options depend on the model, up to **Medium**. New receptionists use **Minimal**. Higher effort can improve accuracy on complex procedures but increases response time. Some models do not support this setting.

## Call behavior

| Setting                              | Default | Description                                                                                                                                                                                                                                   |
| ------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Filter background speech**         | On      | Filters out distant voices in the background so the receptionist only responds to the caller.                                                                                                                                                 |
| **Skip retrieval (RAG)**             | Off     | Puts your whole knowledge base in the prompt instead of searching it on each turn. This lowers response time. The knowledge base must be under 2,000,000 characters and 2,000 documents in total; if it's larger, the setting can't be saved. |
| **Allow playing touch tones (DTMF)** | Off     | Lets the receptionist press keypad tones, for example to navigate an automated phone menu. Also enables **Digits to dial after connecting** on [transfer rules](/docs/reception-ai/receptionist/call-handling#transfer-to-a-human).           |
| **Hold sound**                       | Typing  | What the caller hears while the receptionist looks something up: No sound, Typing, or Hold music 1–4.                                                                                                                                         |

> **Tip**
>
> After changing the model or reasoning effort, [test your receptionist](/docs/reception-ai/receptionist/testing) on a few typical calls to confirm response
> time and accuracy.
