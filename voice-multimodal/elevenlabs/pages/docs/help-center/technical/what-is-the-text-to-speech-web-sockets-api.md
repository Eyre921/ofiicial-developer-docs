---
title: "What is the Text-to-Speech WebSockets API?"
source: https://elevenlabs.io/docs/help-center/technical/what-is-the-text-to-speech-web-sockets-api.md
path: docs/help-center/technical/what-is-the-text-to-speech-web-sockets-api
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is the Text-to-Speech WebSockets API?

The WebSocket streaming endpoint, also sometimes referred to as input streaming, provides real-time [text-to-speech](https://elevenlabs.io/text-to-speech) conversion using WebSockets. This allows you to send a text message and receive audio data back in real-time.

It is designed to start generating audio chunks from just partial text chunks as input. It can help minimize latency by starting to generate the output before the whole context is delivered and is supposed to be used in conjunction with other tools such as Large Language Models (LLMs). The generated audio will still sound like a string of continuous speech.

Although highly flexible, the WebSockets API isn’t a one-size-fits-all solution.

It’s well-suited for scenarios where:

* The input text is being streamed or generated in chunks.
* The lowest possible latency is needed.
* Word-to-audio alignment information is required.

It may not be the best choice when:

* The entire input text is delivered at once. Given that the generations are partial, some buffering is involved, which could potentially result in slightly higher latency compared to a standard HTTP request. Instead, using only the output streaming endpoint is most likely the better option in cases like this.
* You want to quickly experiment or prototype. Working with WebSockets can be harder and more complex than using a standard HTTP API, which might slow down rapid development and testing.
* Where the highest possible consistency is of utmost importance, you need to consider the AI's context understanding. Since the AI is not given the full context at the beginning of the request, it will only have a partial understanding of the text, which in certain instances can cause issues. However, you can experiment with some of the settings available when using WebSocket streaming, such as the "chunk\_length\_schedule". This parameter will determine how big the chunks need to be before the AI starts generating text.

In these cases, use the [Text to Speech API](/docs/api-reference/text-to-speech) instead.

To find out more, please see the [WebSockets API Reference.](/docs/api-reference/websockets)
