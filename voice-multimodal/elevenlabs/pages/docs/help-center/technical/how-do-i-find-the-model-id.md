---
title: "How do I find the model ID?"
source: https://elevenlabs.io/docs/help-center/technical/how-do-i-find-the-model-id.md
path: docs/help-center/technical/how-do-i-find-the-model-id
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I find the model ID?

The model IDs follow a fairly simple pattern, and they can be found using the [/v1/models](/docs/api-reference/get-models) endpoint via the API.

Here is a list of the current models, and you can also find more information about each in their article [here](/docs/help-center/technical/what-models-do-you-offer-and-what-is-the-difference-between-them).

**Flagship Models**

| Model Name                    | Model ID                   |
| ----------------------------- | -------------------------- |
| Multilingual v2               | eleven_multilingual_v2     |
| Flash v2.5                    | eleven_flash_v2_5          |
| Flash v2                      | eleven_flash_v2            |
| Turbo v2.5                    | eleven_turbo_v2_5          |
| Turbo v2                      | eleven_turbo_v2            |
| Multilingual Speech to Speech | eleven_multilingual_sts_v2 |
| English Speech to Speech      | eleven_english_sts_v2      |

---

**Older Models**

| Model Name | Model ID          |
| ---------- | ----------------- |
| Turbo v2.5 | eleven_turbo_v2_5 |
| Turbo v2   | eleven_turbo_v2   |

---

**Cost when generating via the website:**

All models cost 1 credit per character. This excludes any credit modifiers that might apply to the voice you're using.

**Cost when generating via API:**

API generations are discounted - for details, see our [API Pricing.](https://elevenlabs.io/pricing)
