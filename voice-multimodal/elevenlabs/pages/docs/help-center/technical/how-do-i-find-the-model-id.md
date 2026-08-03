---
title: "How do I find the model ID?"
source: https://elevenlabs.io/docs/help-center/technical/how-do-i-find-the-model-id.md
path: docs/help-center/technical/how-do-i-find-the-model-id
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I find the model ID?

The model IDs follow a fairly simple pattern, and they can be found using the [/v1/models](/docs/api-reference/get-models) endpoint via the API.

Here is a list of the current models, and you can also find more information about each in their article [here](/docs/help-center/technical/what-models-do-you-offer-and-what-is-the-difference-between-them).

<strong>
  Flagship Models
</strong>

| Model Name                    | Model ID                      |
| ----------------------------- | ----------------------------- |
| Multilingual v2               | eleven\_multilingual\_v2      |
| Flash v2.5                    | eleven\_flash\_v2\_5          |
| Flash v2                      | eleven\_flash\_v2             |
| Turbo v2.5                    | eleven\_turbo\_v2\_5          |
| Turbo v2                      | eleven\_turbo\_v2             |
| Multilingual Speech to Speech | eleven\_multilingual\_sts\_v2 |
| English Speech to Speech      | eleven\_english\_sts\_v2      |

---

<strong>
  Older Models
</strong>

| Model Name | Model ID             |
| ---------- | -------------------- |
| Turbo v2.5 | eleven\_turbo\_v2\_5 |
| Turbo v2   | eleven\_turbo\_v2    |

---

<strong>
  Cost when generating via the website:
</strong>

All models cost 1 credit per character. This excludes any credit modifiers that might apply to the voice you're using.

<strong>
  Cost when generating via API:
</strong>

API generations are discounted - for details, see our <a href="https://elevenlabs.io/pricing">API Pricing.</a>
