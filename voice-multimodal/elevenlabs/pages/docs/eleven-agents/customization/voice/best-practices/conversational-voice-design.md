---
title: "Conversational voice design"
source: https://elevenlabs.io/docs/eleven-agents/customization/voice/best-practices/conversational-voice-design.md
path: docs/eleven-agents/customization/voice/best-practices/conversational-voice-design
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Conversational voice design

## Overview

Selecting the right voice is crucial for creating an effective voice agent. The voice you choose should align with your agent's personality, tone, and purpose.

## Voice design

If you need a voice that doesn't exist in our library, [Voice Design](/docs/eleven-creative/voices/voice-design) lets you create custom voices from text descriptions. Define characteristics like age, accent, tone, and pacing to generate voices tailored to your agent's personality and use case.

## Library voices

These voices offer a range of styles and characteristics that work well for different agent types:

* `kdmDKE6EkgrWrrykO9Qt` - **Alexandra:** A super realistic, young female voice that likes to chat
* `L0Dsvb3SLTyegXwtm47J` - **Archer:** Grounded and friendly young British male with charm
* `g6xIsTj2HwM6VR4iXFCw` - **Jessica Anne Bogart:** Empathetic and expressive, great for wellness coaches
* `OYTbf65OHHFELVut7v2H` - **Hope:** Bright and uplifting, perfect for positive interactions
* `dj3G1R1ilKoFKhBnWOzG` - **Eryn:** Friendly and relatable, ideal for casual interactions
* `HDA9tsk27wYi3uq0fPcK` - **Stuart:** Professional & friendly Aussie, ideal for technical assistance
* `1SM7GgM6IMuvQlz2BwM3` - **Mark:** Relaxed and laid back, suitable for non chalant chats
* `PT4nqlKZfc06VW1BuClj` - **Angela:** Raw and relatable, great listener and down to earth
* `vBKc2FfBKJfcZNyEt1n6` - **Finn:** Tenor pitched, excellent for podcasts and light chats
* `56AoDkrOh6qfVPDXZ7Pt` - **Cassidy:** Engaging and energetic, good for entertainment contexts
* `NOpBlnGInO9m6vDvFkFC` - **Grandpa Spuds Oxley:** Distinctive character voice for unique agents

## Voice settings

![Voice settings](/docs/_fern-files/_img/007b0ec153f9210ce48a6e6ed3184c4d004476222a2be2b5bf6ab6afdecf4804.webp)

Voice settings dramatically affect how your agent is perceived:

* **Stability:** Lower values (0.30-0.50) create more emotional, dynamic delivery but may occasionally sound unstable. Higher values (0.60-0.85) produce more consistent but potentially monotonous output.

* **Similarity:** Higher values will boost the overall clarity and consistency of the voice. Very high values may lead to sound distortions. Adjusting this value to find the right balance is recommended.

* **Speed:** Most natural conversations occur at 0.9-1.1x speed. Depending on the voice, adjust slower for complex topics or faster for routine information. Speed is not available for Eleven v3 and Eleven v4 models.

* **Clone Strength:** When you select Eleven v4 or Eleven v4 Turbo and a [Professional Voice Clone](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning) trained for Eleven v4, Voice settings include an additional **Clone Strength** slider. Clone Strength controls how closely the generated speech follows the clone's training recordings. At lower values, the voice is smoothed slightly and the delivery gains more performance flexibility, which often sounds better overall while still sounding like the original voice. At higher values, the output stays closer to the training recordings with less smoothing, mimicking the original voice's delivery and performance more closely. Higher values can be especially useful for voices with distinctive traits or unique accents. For most voices, start at 0%.

> **Tip**
>
> Test your agent with different voice settings using the same prompt to find the optimal
> combination. Small adjustments can dramatically change the perceived personality of your agent.
