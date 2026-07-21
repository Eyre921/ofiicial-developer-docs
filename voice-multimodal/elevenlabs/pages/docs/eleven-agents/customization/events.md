---
title: "Events"
source: https://elevenlabs.io/docs/eleven-agents/customization/events.md
path: docs/eleven-agents/customization/events
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Events

## Overview

Events are the foundation of real-time communication in ElevenLabs Agents applications using WebSockets.
They facilitate the exchange of information like audio streams, transcriptions, agent responses, and contextual updates between the client application and the server infrastructure.

Understanding these events is crucial for building responsive and interactive conversational experiences.

Events are broken down into two categories:

#### [Client Events (Server-to-Client)](/docs/eleven-agents/customization/events/client-events)

Events sent from the server to the client, delivering audio, transcripts, agent messages, and
system signals.

#### [Client-to-Server Events](/docs/eleven-agents/customization/events/client-to-server-events)

Events sent from the client to the server, providing contextual updates or responding to server
requests.
