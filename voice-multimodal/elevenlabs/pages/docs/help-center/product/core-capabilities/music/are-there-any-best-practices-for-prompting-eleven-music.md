---
title: "Are there any best practices for prompting Eleven Music?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/music/are-there-any-best-practices-for-prompting-eleven-music.md
path: docs/help-center/product/core-capabilities/music/are-there-any-best-practices-for-prompting-eleven-music
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Are there any best practices for prompting Eleven Music?

The key to great results is a descriptive and detailed prompt. The model understands nuance, so the more information you provide, the closer the output will be to your vision. Here are some best practices:

* **Be Specific with Genre and Style:** Instead of `rock music`, try `energetic 1980s
  synth-pop with a driving drum machine beat and male vocals`.
* **Layer Multiple Descriptors:** Combine mood, instrumentation, tempo, and use case.
* Example: `A slow, melancholic piano melody over ambient synth textures, suitable for a tragic film scene`.
* **Define Instrumentation:** Call out the specific instruments you want to hear.
* Example: `Upbeat funk track with a prominent slap bass line, funky rhythm guitar, and a horn section`.
* **Use the "Include/Exclude Styles" Feature:** Refine your output by explicitly
  including or excluding certain tags like acoustic, repetitive structure, or four-on-the-floor
  kick.
* **Build Section by Section:** To have the most control when creating a full song,
  generate the Intro first. Once you're happy with that first section, you can click the "+" sign
  and specify the style for the next part. Then, use the "Continue the conversation..." prompt box
  to generate the Main Groove or Chorus, building your track piece by piece.
* **Iterate and Refine:** If the first generation isn't perfect, don't start over!
  Adjust your prompt and regenerate. Small changes can have a big impact.

For a complete list of tips and examples, please see our official [Prompting Guide](/docs/overview/capabilities/music/best-practices).
