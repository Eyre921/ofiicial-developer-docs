---
title: "Why does my voice sound different in the API compared to the website?"
source: https://elevenlabs.io/docs/help-center/technical/why-does-my-voice-sound-different-in-the-api-compared-to-the-website.md
path: docs/help-center/technical/why-does-my-voice-sound-different-in-the-api-compared-to-the-website
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why does my voice sound different in the API compared to the website?

One possible reason is that different models were used to generate the audio.  If you didn't set a model to use in your API call, it will use the default model which is Multilingual v2 - `eleven_multilingual_v2`.  You can see a list with details of all our models and their ids in our Help Center article, [What models do you offer and what is the difference between them?](/docs/help-center/technical/what-models-do-you-offer-and-what-is-the-difference-between-them)

Another potential cause is voice settings.  Due to the nature of generative AI, there will always be slight differences between different generations, and the same input will generate different results each time, but some voice settings will have an impact on how varied your outputs will be. For example, low stability and low similarity can result in higher than usual variation between generations. You can find out more in our [guide to Voice Settings.](/docs/product-guides/playground/text-to-speech#settings)
