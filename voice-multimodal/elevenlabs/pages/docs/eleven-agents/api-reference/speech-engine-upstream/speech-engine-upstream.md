---
title: "Speech Engine Upstream"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/speech-engine-upstream/speech-engine-upstream.md
path: docs/eleven-agents/api-reference/speech-engine-upstream/speech-engine-upstream
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Speech Engine Upstream

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

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/speech-engine-upstream/speech-engine-upstream

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: Speech Engine Upstream
  version: subpackage_speechEngineUpstream.speechEngineUpstream
  description: >-
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
    description: >-
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
      summary: Server message
      message:
        name: subscribe
        payload:
          $ref: >-
            #/components/schemas/type_speechEngineUpstream:receiveUpstreamMessage
    subscribe:
      operationId: subpackage_speechEngineUpstream.speechEngineUpstream-subscribe
      summary: Client message
      message:
        name: publish
        payload:
          $ref: '#/components/schemas/type_speechEngineUpstream:sendUpstreamMessage'
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
    type_:Init:
      type: object
      properties:
        type:
          type: string
          enum:
            - init
        conversation_id:
          type: string
      required:
        - type
        - conversation_id
      title: Init
    type_:UserTranscriptUserTranscriptItem:
      type: object
      properties:
        role:
          type: string
        content:
          type: string
      required:
        - role
        - content
      title: UserTranscriptUserTranscriptItem
    type_:UserTranscript:
      type: object
      properties:
        type:
          type: string
          enum:
            - user_transcript
        event_id:
          type: integer
        user_transcript:
          type: array
          items:
            $ref: '#/components/schemas/type_:UserTranscriptUserTranscriptItem'
      required:
        - type
        - event_id
        - user_transcript
      title: UserTranscript
    type_:Ping:
      type: object
      properties:
        type:
          type: string
          enum:
            - ping
      required:
        - type
      title: Ping
    type_:Close:
      type: object
      properties:
        type:
          type: string
          enum:
            - close
      required:
        - type
      title: Close
    type_:SpeechEngineError:
      type: object
      properties:
        type:
          type: string
          enum:
            - error
        message:
          type: string
          description: Human-readable description of the error.
      required:
        - type
        - message
      title: SpeechEngineError
    type_speechEngineUpstream:receiveUpstreamMessage:
      oneOf:
        - $ref: '#/components/schemas/type_:Init'
        - $ref: '#/components/schemas/type_:UserTranscript'
        - $ref: '#/components/schemas/type_:Ping'
        - $ref: '#/components/schemas/type_:Close'
        - $ref: '#/components/schemas/type_:SpeechEngineError'
      description: Defines the message types ElevenLabs sends to your speech engine server
      title: receiveUpstreamMessage
    type_:AgentResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - agent_response
        event_id:
          type: integer
        content:
          type: string
          default: ''
        is_final:
          type: boolean
          default: false
      required:
        - type
        - event_id
      title: AgentResponse
    type_:Pong:
      type: object
      properties:
        type:
          type: string
          enum:
            - pong
      required:
        - type
      title: Pong
    type_speechEngineUpstream:sendUpstreamMessage:
      oneOf:
        - $ref: '#/components/schemas/type_:AgentResponse'
        - $ref: '#/components/schemas/type_:Pong'
      description: Defines the message types your speech engine server sends to ElevenLabs
      title: sendUpstreamMessage

```
