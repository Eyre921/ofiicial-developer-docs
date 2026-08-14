---
title: "Why do female and male voices converge in the output audio file?"
source: https://elevenlabs.io/docs/help-center/troubleshooting/why-do-female-and-male-voices-converge-in-the-output-audio-file.md
path: docs/help-center/troubleshooting/why-do-female-and-male-voices-converge-in-the-output-audio-file
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why do female and male voices converge in the output audio file?

Multiple genders can appear for either of two reasons:

* If the input samples have both male and female voices in them. In order to solve the issue please upload the voices separately.
* The input sample has a long fragment of text with dialogue references, then unfortunately it can sometimes change throughout. In order to address this instance please try lowering the stability setting of the recording.
