---
title: "How can I keep the WebSocket open?"
source: https://elevenlabs.io/docs/help-center/technical/how-can-i-keep-the-websocket-open.md
path: docs/help-center/technical/how-can-i-keep-the-websocket-open
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How can I keep the WebSocket open?

If you're working with the text-to-speech WebSockets endpoint via our API, the connection will automatically close after 20 seconds of inactivity.

To keep the connection open, you can send a single space character " ". Please note that this string must include a space, as sending a fully empty string, "", will send an End of Sequence (EOS) message, closing the socket.

This will keep the connection open for another 20 seconds.  To keep the connection open for longer, you will need to send additional single space characters " " every 20 seconds.  

You can also specify how long the connection can be inactive before it's automatically closed.  The default value is 20 seconds, but you can change this by adding `inactivity_timeout` as a query parameter in the WebSockets endpoint.  The maximum allowed value is 180 seconds.

For more information, please see the [WebSockets API Reference.](/docs/api-reference/websockets)
