---
title: "What are some issues I might encounter and how can I avoid them?"
source: https://elevenlabs.io/docs/help-center/troubleshooting/what-are-some-issues-i-might-encounter-and-how-can-i-avoid-them.md
path: docs/help-center/troubleshooting/what-are-some-issues-i-might-encounter-and-how-can-i-avoid-them
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What are some issues I might encounter and how can I avoid them?

AI is a highly advanced field of technology and can, at times, be unpredictable as the output is based on the input and then interpreted by the AI. We have tried to minimize the unpredictability as much as possible and keep adding features and improvements that make it more predictable and controllable. However, there are still a few things you need to be mindful of, and this applies to all generative AI.

You can read more in our [guide to troubleshooting.](/docs/creative-platform/troubleshooting)

**Multilingual v2 Model**: This model represents a significant improvement in
predictability and consistency compared to the experimental multilingual v1 model. It has resolved
many of the issues associated with the v1 model, although some minor issues still exist, such as
inconsistency and language switching.

* **Inconsistency**: Users have reported occasional inconsistencies between AI
  generations, where the output does not fit together perfectly. This issue is being worked on and
  is less prominent in the multilingual v2 model. Cloning the voice with consistent samples is
  recommended to address this.
* **Language Switching**: A common problem is the AI switching languages or accents
  within a single generation, especially in longer texts. This issue is being addressed, but using a
  [properly cloned voice](/docs/voices/voice-lab/instant-voice-cloning) with the Projects feature
  can help mitigate it.
* **Corrupt Speech**: A rare issue where the AI produces muffled and strange-sounding
  speech. There are no specific solutions, but regenerating the section usually resolves it.

**Studio (previously Projects)**: Studio is a workflow for creating long-form content
using AI. It generally works well with a proper voice choice and model.

* **Import Function**: The import function attempts to import files, but due to the
  number of formatting variables, users should double-check imported content for accuracy. Some
  issues may require manual adjustments.
* **Glitches between Paragraphs**: Occasionally, glitches or abrupt transitions between
  paragraphs may happen. This issue is rare and is being actively worked on. Regenerating the last
  paragraph can often resolve it.

**Factors Affecting Issues**: Several factors affect AI performance, including text
chunk length, voice type (pre-made, voice-designed, or cloned), and settings like stability and
similarity.

**Future Developments**: The team is actively working on improving AI performance and
developing new features.
