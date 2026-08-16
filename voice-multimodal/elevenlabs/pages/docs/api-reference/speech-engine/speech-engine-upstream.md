---
title: "WebSocket"
source: https://elevenlabs.io/docs/api-reference/speech-engine/speech-engine-upstream.md
path: docs/api-reference/speech-engine/speech-engine-upstream
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WebSocket

GET /speech-engine/upstream

The Speech Engine upstream WebSocket protocol defines the interface your server must
implement so that ElevenLabs can connect to it during a Speech Engine conversation.
Unlike other ElevenLabs WebSocket channels where your client connects to ElevenLabs,
the Speech Engine reverses this relationship: **ElevenLabs is the WebSocket client and
your server is the WebSocket server**.

This page shows the WebSocket API shape, however we recommend using the provided server side SDKs
instead of implementing this yourself. The SDKs include several helper methods and automatically
handle auth for you. You can find SDK installation instructions and
guides in the [Speech Engine quickstart](/docs/eleven-api/guides/cookbooks/speech-engine).

Configure your server's publicly reachable WebSocket URL in the `wsUrl` field when
creating or updating a Speech Engine via the REST API. When a user starts a conversation
with that agent, ElevenLabs will open a WebSocket connection to your server and begin
the message exchange described below.

## Connection flow

1. A user starts a conversation with a Speech Engine agent (via the ElevenLabs client SDK or API).
2. ElevenLabs opens a WebSocket connection to your `wsUrl`.
3. ElevenLabs sends an `init` message containing the conversation ID.
4. As the user speaks, ElevenLabs transcribes the audio and sends `user_transcript` messages with the full conversation history.
5. Your server calls an LLM and streams the response back as one or more `agent_response` messages.
6. ElevenLabs synthesizes the text to speech and streams the audio back to the user.
7. Periodic `ping` messages keep the connection alive; reply with `pong`.
8. When the conversation ends, ElevenLabs sends a `close` message.

## Authentication

Every connection from ElevenLabs includes an `X-Elevenlabs-Speech-Engine-Authorization`
header containing a short-lived JWT. Verify this token before accepting the WebSocket
upgrade to ensure the connection originates from ElevenLabs.

The JWT is signed with **HS256** using the SHA-256 hash of your ElevenLabs API key as
the HMAC secret, and has:
- **Issuer** (`iss`): `https://api.elevenlabs.io/convai/speech-engine`
- **Subject** (`sub`): `convai_speech_engine_upstream`
- **Expiry** (`exp`): short-lived; a 60-second clock-skew leeway is applied

## Interruption handling

Each `user_transcript` message carries an `event_id`. If the user speaks again before
your server finishes responding, a new `user_transcript` arrives with a higher `event_id`.
Cancel your in-flight LLM call and begin responding to the new transcript. Any
`agent_response` messages sent with an outdated `event_id` are silently discarded by
ElevenLabs.

## Streaming responses

Send LLM output as a sequence of `agent_response` messages with `is_final: false` for
each text chunk, followed by a final `agent_response` with `is_final: true` and an empty
`content` string. ElevenLabs begins synthesizing audio as chunks arrive, minimising
latency.


Reference: https://elevenlabs.io/docs/api-reference/speech-engine/speech-engine-upstream

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: Speech Engine Upstream
  version: subpackage_speechEngineUpstream.speechEngineUpstream
  description: >
    The Speech Engine upstream WebSocket protocol defines the interface your
    server must

    implement so that ElevenLabs can connect to it during a Speech Engine
    conversation.

    Unlike other ElevenLabs WebSocket channels where your client connects to
    ElevenLabs,

    the Speech Engine reverses this relationship: **ElevenLabs is the WebSocket
    client and

    your server is the WebSocket server**.


    This page shows the WebSocket API shape, however we recommend using the
    provided server side SDKs

    instead of implementing this yourself. The SDKs include several helper
    methods and automatically

    handle auth for you. You can find SDK installation instructions and

    guides in the [Speech Engine
    quickstart](/docs/eleven-api/guides/cookbooks/speech-engine).


    Configure your server's publicly reachable WebSocket URL in the `wsUrl`
    field when

    creating or updating a Speech Engine via the REST API. When a user starts a
    conversation

    with that agent, ElevenLabs will open a WebSocket connection to your server
    and begin

    the message exchange described below.


    ## Connection flow


    1. A user starts a conversation with a Speech Engine agent (via the
    ElevenLabs client SDK or API).

    2. ElevenLabs opens a WebSocket connection to your `wsUrl`.

    3. ElevenLabs sends an `init` message containing the conversation ID.

    4. As the user speaks, ElevenLabs transcribes the audio and sends
    `user_transcript` messages with the full conversation history.

    5. Your server calls an LLM and streams the response back as one or more
    `agent_response` messages.

    6. ElevenLabs synthesizes the text to speech and streams the audio back to
    the user.

    7. Periodic `ping` messages keep the connection alive; reply with `pong`.

    8. When the conversation ends, ElevenLabs sends a `close` message.


    ## Authentication


    Every connection from ElevenLabs includes an
    `X-Elevenlabs-Speech-Engine-Authorization`

    header containing a short-lived JWT. Verify this token before accepting the
    WebSocket

    upgrade to ensure the connection originates from ElevenLabs.


    The JWT is signed with **HS256** using the SHA-256 hash of your ElevenLabs
    API key as

    the HMAC secret, and has:

    - **Issuer** (`iss`): `https://api.elevenlabs.io/convai/speech-engine`

    - **Subject** (`sub`): `convai_speech_engine_upstream`

    - **Expiry** (`exp`): short-lived; a 60-second clock-skew leeway is applied


    ## Interruption handling


    Each `user_transcript` message carries an `event_id`. If the user speaks
    again before

    your server finishes responding, a new `user_transcript` arrives with a
    higher `event_id`.

    Cancel your in-flight LLM call and begin responding to the new transcript.
    Any

    `agent_response` messages sent with an outdated `event_id` are silently
    discarded by

    ElevenLabs.


    ## Streaming responses


    Send LLM output as a sequence of `agent_response` messages with `is_final:
    false` for

    each text chunk, followed by a final `agent_response` with `is_final: true`
    and an empty

    `content` string. ElevenLabs begins synthesizing audio as chunks arrive,
    minimising

    latency.
channels:
  /speech-engine/upstream:
    description: >
      The Speech Engine upstream WebSocket protocol defines the interface your
      server must

      implement so that ElevenLabs can connect to it during a Speech Engine
      conversation.

      Unlike other ElevenLabs WebSocket channels where your client connects to
      ElevenLabs,

      the Speech Engine reverses this relationship: **ElevenLabs is the
      WebSocket client and

      your server is the WebSocket server**.


      This page shows the WebSocket API shape, however we recommend using the
      provided server side SDKs

      instead of implementing this yourself. The SDKs include several helper
      methods and automatically

      handle auth for you. You can find SDK installation instructions and

      guides in the [Speech Engine
      quickstart](/docs/eleven-api/guides/cookbooks/speech-engine).


      Configure your server's publicly reachable WebSocket URL in the `wsUrl`
      field when

      creating or updating a Speech Engine via the REST API. When a user starts
      a conversation

      with that agent, ElevenLabs will open a WebSocket connection to your
      server and begin

      the message exchange described below.


      ## Connection flow


      1. A user starts a conversation with a Speech Engine agent (via the
      ElevenLabs client SDK or API).

      2. ElevenLabs opens a WebSocket connection to your `wsUrl`.

      3. ElevenLabs sends an `init` message containing the conversation ID.

      4. As the user speaks, ElevenLabs transcribes the audio and sends
      `user_transcript` messages with the full conversation history.

      5. Your server calls an LLM and streams the response back as one or more
      `agent_response` messages.

      6. ElevenLabs synthesizes the text to speech and streams the audio back to
      the user.

      7. Periodic `ping` messages keep the connection alive; reply with `pong`.

      8. When the conversation ends, ElevenLabs sends a `close` message.


      ## Authentication


      Every connection from ElevenLabs includes an
      `X-Elevenlabs-Speech-Engine-Authorization`

      header containing a short-lived JWT. Verify this token before accepting
      the WebSocket

      upgrade to ensure the connection originates from ElevenLabs.


      The JWT is signed with **HS256** using the SHA-256 hash of your ElevenLabs
      API key as

      the HMAC secret, and has:

      - **Issuer** (`iss`): `https://api.elevenlabs.io/convai/speech-engine`

      - **Subject** (`sub`): `convai_speech_engine_upstream`

      - **Expiry** (`exp`): short-lived; a 60-second clock-skew leeway is
      applied


      ## Interruption handling


      Each `user_transcript` message carries an `event_id`. If the user speaks
      again before

      your server finishes responding, a new `user_transcript` arrives with a
      higher `event_id`.

      Cancel your in-flight LLM call and begin responding to the new transcript.
      Any

      `agent_response` messages sent with an outdated `event_id` are silently
      discarded by

      ElevenLabs.


      ## Streaming responses


      Send LLM output as a sequence of `agent_response` messages with `is_final:
      false` for

      each text chunk, followed by a final `agent_response` with `is_final:
      true` and an empty

      `content` string. ElevenLabs begins synthesizing audio as chunks arrive,
      minimising

      latency.
    bindings:
      ws:
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
            X-ElevenLabs-Speech-Engine-Authorization:
              type: string
    publish:
      operationId: subpackage_speechEngineUpstream.speechEngineUpstream-publish
      summary: subscribe
      description: Defines the message types ElevenLabs sends to your speech engine server
      message:
        name: subscribe
        title: subscribe
        description: >-
          Defines the message types ElevenLabs sends to your speech engine
          server
        payload:
          $ref: '#/components/schemas/SpeechEngineUpstreamSubscribe'
    subscribe:
      operationId: subpackage_speechEngineUpstream.speechEngineUpstream-subscribe
      summary: publish
      description: Defines the message types your speech engine server sends to ElevenLabs
      message:
        name: publish
        title: publish
        description: >-
          Defines the message types your speech engine server sends to
          ElevenLabs
        payload:
          $ref: '#/components/schemas/SpeechEngineUpstreamPublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
  Production Singapore:
    url: wss://api.sg.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    Init:
      type: object
      properties:
        type:
          type: string
          enum:
            - init
          description: The message type identifier.
        conversation_id:
          type: string
          description: Unique identifier for this conversation session.
      required:
        - type
        - conversation_id
      description: Payload for the session initialisation message sent by ElevenLabs.
      title: Init
    TranscriptMessageRole:
      type: string
      enum:
        - user
        - agent
      description: The speaker for this turn.
      title: TranscriptMessageRole
    TranscriptMessage:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/TranscriptMessageRole'
          description: The speaker for this turn.
        content:
          type: string
          description: The transcript text for this turn.
      required:
        - role
        - content
      description: A single turn in the conversation history.
      title: TranscriptMessage
    UserTranscript:
      type: object
      properties:
        type:
          type: string
          enum:
            - user_transcript
          description: The message type identifier.
        user_transcript:
          type: array
          items:
            $ref: '#/components/schemas/TranscriptMessage'
          description: >
            Full conversation history up to and including the latest user turn,
            ordered

            chronologically. Contains both `user` and `agent` turns.
        event_id:
          type: integer
          description: >
            Monotonically increasing identifier for this transcript event. Pass
            this value

            back in every `agent_response` message so ElevenLabs can correlate
            responses and

            discard any that belong to an interrupted turn.
      required:
        - type
        - user_transcript
      description: >
        Payload containing the full conversation history sent by ElevenLabs each
        time

        the user finishes speaking.
      title: UserTranscript
    Ping:
      type: object
      properties:
        type:
          type: string
          enum:
            - ping
          description: The message type identifier.
      required:
        - type
      description: Keep-alive ping sent periodically by ElevenLabs.
      title: Ping
    Close:
      type: object
      properties:
        type:
          type: string
          enum:
            - close
          description: The message type identifier.
      required:
        - type
      description: Payload indicating a clean end-of-conversation signal from ElevenLabs.
      title: Close
    Error:
      type: object
      properties:
        type:
          type: string
          enum:
            - error
          description: The message type identifier.
        message:
          type: string
          description: Human-readable description of the error.
      required:
        - type
        - message
      description: >-
        Payload for protocol-level errors sent by ElevenLabs before closing the
        connection.
      title: Error
    SpeechEngineUpstreamSubscribe:
      oneOf:
        - $ref: '#/components/schemas/Init'
        - $ref: '#/components/schemas/UserTranscript'
        - $ref: '#/components/schemas/Ping'
        - $ref: '#/components/schemas/Close'
        - $ref: '#/components/schemas/Error'
      title: SpeechEngineUpstreamSubscribe
    AgentResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - agent_response
          description: The message type identifier.
        content:
          type: string
          description: >
            The text to synthesize. For streaming responses, send incremental
            chunks here.

            The final message in a response must have an empty string (`""`).
        event_id:
          type: integer
          description: >
            The `event_id` from the `user_transcript` this response addresses.
            ElevenLabs

            uses this to discard responses that belong to an interrupted turn.
        is_final:
          type: boolean
          description: >
            Set to `true` on the last message of a response (with an empty
            `content`).

            Set to `false` on all preceding chunks.
      required:
        - type
        - content
        - is_final
      description: >
        Text chunk sent from your server to ElevenLabs for speech synthesis.

        Stream LLM output by sending multiple messages with `is_final: false`,
        then

        terminate the response with a message where `is_final: true` and
        `content` is

        an empty string.
      title: AgentResponse
    Pong:
      type: object
      properties:
        type:
          type: string
          enum:
            - pong
          description: The message type identifier.
      required:
        - type
      description: Reply to a `ping` message.
      title: Pong
    SpeechEngineUpstreamPublish:
      oneOf:
        - $ref: '#/components/schemas/AgentResponse'
        - $ref: '#/components/schemas/Pong'
      title: SpeechEngineUpstreamPublish

```
