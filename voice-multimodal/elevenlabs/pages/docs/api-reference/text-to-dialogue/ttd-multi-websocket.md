---
title: "Multi-Context WebSocket"
source: https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-multi-websocket.md
path: docs/api-reference/text-to-dialogue/ttd-multi-websocket
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Multi-Context WebSocket

GET /v1/text-to-dialogue/multi-stream-input

Stream expressive dialogue audio for multiple independent streams (contexts) multiplexed over a single WebSocket connection.

Each context, identified by a client-chosen `context_id`, behaves like an independent [Text to Dialogue WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket) session: it registers its own voices and settings, buffers its own text, and produces its own audio stream. This is useful for scenarios requiring concurrent or interleaved dialogue generations, such as conversational AI applications that need to handle interruptions.

The connection uses Eleven v3 dialogue models only (`model_id` must start with `eleven_v3`). The default model is `eleven_v3_conversational`.

## Context setup
- Every message **must** include a `context_id`. A message containing only `close_socket` is the exception.
- The first message for a new `context_id` creates that context and **must** include `voices` (voice IDs to register for the context). Optional `voice_settings` and `pronunciation_dictionary_locators` are only accepted on this first message.
- For `eleven_v3_conversational`, only **one** voice ID may be registered per context. For `eleven_v3`, you may register up to **10** voices per context.
- A connection can hold at most **5** simultaneous contexts; close a context to free a slot.

## Streaming text
- Send `inputs`: an array of `{ "text", "voice_id", "new_turn"? }`. Each `voice_id` must be registered for that context. Text for the same turn is buffered per context until the server has enough context, then partial audio chunks tagged with the `context_id` are emitted.
- Set `new_turn` to `true` (or switch `voice_id`) to finalize the current prosody segment and start a new speaker turn.

## Control messages
- `flush`: force generation of the context's buffered text.
- `close_context`: flush the context's remaining audio, emit its `is_final` message, and close it. Other contexts stay open.
- `close_socket`: flush and close **all** contexts, then close the connection.
- `keep_alive`: reset the context's **20 second** inactivity timeout (no generation). A context idle for longer is automatically flushed and closed (its `is_final` message is sent); other contexts are unaffected.

Protocol errors — a missing `context_id`, an unregistered voice, messaging a context that is closing, or exceeding the context limit — send an error payload and close the whole connection.

## Authentication
Authentication is connection-level, not per context: use the `xi-api-key` or `Authorization` header, `single_use_token` query parameter, or include `xi_api_key`, `authorization`, or `single_use_token` in the first message of the connection. Anonymous sessions are rejected.

For a single dialogue stream per connection, see the [Text to Dialogue WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket). For non-streaming dialogue over HTTP, see [Create dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream dialogue](/docs/api-reference/text-to-dialogue/stream).


Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-multi-websocket

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Dialogue Multi Stream Input
  version: subpackage_v1TextToDialogueMultiStreamInput.v1TextToDialogueMultiStreamInput
  description: >
    Stream expressive dialogue audio for multiple independent streams (contexts)
    multiplexed over a single WebSocket connection.


    Each context, identified by a client-chosen `context_id`, behaves like an
    independent [Text to Dialogue
    WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket) session: it
    registers its own voices and settings, buffers its own text, and produces
    its own audio stream. This is useful for scenarios requiring concurrent or
    interleaved dialogue generations, such as conversational AI applications
    that need to handle interruptions.


    The connection uses Eleven v3 dialogue models only (`model_id` must start
    with `eleven_v3`). The default model is `eleven_v3_conversational`.


    ## Context setup

    - Every message **must** include a `context_id`. A message containing only
    `close_socket` is the exception.

    - The first message for a new `context_id` creates that context and **must**
    include `voices` (voice IDs to register for the context). Optional
    `voice_settings` and `pronunciation_dictionary_locators` are only accepted
    on this first message.

    - For `eleven_v3_conversational`, only **one** voice ID may be registered
    per context. For `eleven_v3`, you may register up to **10** voices per
    context.

    - A connection can hold at most **5** simultaneous contexts; close a context
    to free a slot.


    ## Streaming text

    - Send `inputs`: an array of `{ "text", "voice_id", "new_turn"? }`. Each
    `voice_id` must be registered for that context. Text for the same turn is
    buffered per context until the server has enough context, then partial audio
    chunks tagged with the `context_id` are emitted.

    - Set `new_turn` to `true` (or switch `voice_id`) to finalize the current
    prosody segment and start a new speaker turn.


    ## Control messages

    - `flush`: force generation of the context's buffered text.

    - `close_context`: flush the context's remaining audio, emit its `is_final`
    message, and close it. Other contexts stay open.

    - `close_socket`: flush and close **all** contexts, then close the
    connection.

    - `keep_alive`: reset the context's **20 second** inactivity timeout (no
    generation). A context idle for longer is automatically flushed and closed
    (its `is_final` message is sent); other contexts are unaffected.


    Protocol errors — a missing `context_id`, an unregistered voice, messaging a
    context that is closing, or exceeding the context limit — send an error
    payload and close the whole connection.


    ## Authentication

    Authentication is connection-level, not per context: use the `xi-api-key` or
    `Authorization` header, `single_use_token` query parameter, or include
    `xi_api_key`, `authorization`, or `single_use_token` in the first message of
    the connection. Anonymous sessions are rejected.


    For a single dialogue stream per connection, see the [Text to Dialogue
    WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket). For
    non-streaming dialogue over HTTP, see [Create
    dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream
    dialogue](/docs/api-reference/text-to-dialogue/stream).
channels:
  /v1/text-to-dialogue/multi-stream-input:
    description: >
      Stream expressive dialogue audio for multiple independent streams
      (contexts) multiplexed over a single WebSocket connection.


      Each context, identified by a client-chosen `context_id`, behaves like an
      independent [Text to Dialogue
      WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket) session: it
      registers its own voices and settings, buffers its own text, and produces
      its own audio stream. This is useful for scenarios requiring concurrent or
      interleaved dialogue generations, such as conversational AI applications
      that need to handle interruptions.


      The connection uses Eleven v3 dialogue models only (`model_id` must start
      with `eleven_v3`). The default model is `eleven_v3_conversational`.


      ## Context setup

      - Every message **must** include a `context_id`. A message containing only
      `close_socket` is the exception.

      - The first message for a new `context_id` creates that context and
      **must** include `voices` (voice IDs to register for the context).
      Optional `voice_settings` and `pronunciation_dictionary_locators` are only
      accepted on this first message.

      - For `eleven_v3_conversational`, only **one** voice ID may be registered
      per context. For `eleven_v3`, you may register up to **10** voices per
      context.

      - A connection can hold at most **5** simultaneous contexts; close a
      context to free a slot.


      ## Streaming text

      - Send `inputs`: an array of `{ "text", "voice_id", "new_turn"? }`. Each
      `voice_id` must be registered for that context. Text for the same turn is
      buffered per context until the server has enough context, then partial
      audio chunks tagged with the `context_id` are emitted.

      - Set `new_turn` to `true` (or switch `voice_id`) to finalize the current
      prosody segment and start a new speaker turn.


      ## Control messages

      - `flush`: force generation of the context's buffered text.

      - `close_context`: flush the context's remaining audio, emit its
      `is_final` message, and close it. Other contexts stay open.

      - `close_socket`: flush and close **all** contexts, then close the
      connection.

      - `keep_alive`: reset the context's **20 second** inactivity timeout (no
      generation). A context idle for longer is automatically flushed and closed
      (its `is_final` message is sent); other contexts are unaffected.


      Protocol errors — a missing `context_id`, an unregistered voice, messaging
      a context that is closing, or exceeding the context limit — send an error
      payload and close the whole connection.


      ## Authentication

      Authentication is connection-level, not per context: use the `xi-api-key`
      or `Authorization` header, `single_use_token` query parameter, or include
      `xi_api_key`, `authorization`, or `single_use_token` in the first message
      of the connection. Anonymous sessions are rejected.


      For a single dialogue stream per connection, see the [Text to Dialogue
      WebSocket](/docs/api-reference/text-to-dialogue/ttd-websocket). For
      non-streaming dialogue over HTTP, see [Create
      dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream
      dialogue](/docs/api-reference/text-to-dialogue/stream).
    bindings:
      ws:
        query:
          type: object
          properties:
            model_id:
              description: Any type
            output_format:
              description: Any type
            language_code:
              description: Any type
            sync_alignment:
              description: Any type
            apply_text_normalization:
              description: Any type
            seed:
              description: Any type
            enable_logging:
              description: Any type
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: >-
        subpackage_v1TextToDialogueMultiStreamInput.v1TextToDialogueMultiStreamInput-publish
      summary: subscribe
      description: >-
        Defines the message types that can be received by the client from the
        server
      message:
        name: subscribe
        title: subscribe
        description: >-
          Defines the message types that can be received by the client from the
          server
        payload:
          $ref: '#/components/schemas/V1TextToDialogueMultiStreamInputSubscribe'
    subscribe:
      operationId: >-
        subpackage_v1TextToDialogueMultiStreamInput.v1TextToDialogueMultiStreamInput-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1TextToDialogueMultiStreamInputPublish'
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
    DialogueTextAlignment:
      type: object
      properties:
        chars:
          type: array
          items:
            type: string
        char_start_times_ms:
          type: array
          items:
            type: integer
        char_durations_ms:
          type: array
          items:
            type: integer
      description: Character-level alignment data (field names use snake_case in JSON).
      title: DialogueTextAlignment
    TextToDialogueWebsocketAudioChunkMulti:
      type: object
      properties:
        audio:
          type: string
          description: Base64-encoded audio bytes for the selected `output_format`.
        alignment:
          oneOf:
            - $ref: '#/components/schemas/DialogueTextAlignment'
            - type: 'null'
          description: >-
            Present when `sync_alignment` query parameter is `true` and the
            model returned timing data for the chunk.
        normalized_alignment:
          oneOf:
            - $ref: '#/components/schemas/DialogueTextAlignment'
            - type: 'null'
          description: Reserved for future use; currently unused by the server.
        context_id:
          type: string
          description: The context this audio chunk belongs to.
      description: >-
        Server chunk containing encoded audio for a specific context and
        optional alignment metadata.
      title: TextToDialogueWebsocketAudioChunkMulti
    TextToDialogueWebsocketFinalAudioForTurnMulti:
      type: object
      properties:
        is_final_audio_for_turn:
          type: boolean
          description: >-
            Indicates that the final audio for a given turn of this context has
            been sent.
        context_id:
          type: string
          description: The context whose turn has finished.
      title: TextToDialogueWebsocketFinalAudioForTurnMulti
    TextToDialogueWebsocketFinalMulti:
      type: object
      properties:
        is_final:
          type: boolean
          description: Marks the end of this context's closing flush sequence.
        context_id:
          type: string
          description: The context that has been finalized.
      required:
        - is_final
      title: TextToDialogueWebsocketFinalMulti
    TextToDialogueWebsocketError:
      type: object
      properties:
        message:
          type: string
          description: Human-readable error description.
        error:
          type: string
          description: >-
            Machine-readable error identifier (for example
            `authentication_required`).
        code:
          type: integer
          description: WebSocket close code that will follow this payload.
        param:
          type:
            - string
            - 'null'
          description: Field name related to the error, when applicable.
      required:
        - message
        - error
        - code
      title: TextToDialogueWebsocketError
    V1TextToDialogueMultiStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/TextToDialogueWebsocketAudioChunkMulti'
        - $ref: '#/components/schemas/TextToDialogueWebsocketFinalAudioForTurnMulti'
        - $ref: '#/components/schemas/TextToDialogueWebsocketFinalMulti'
        - $ref: '#/components/schemas/TextToDialogueWebsocketError'
      title: V1TextToDialogueMultiStreamInputSubscribe
    TextToDialogueWebsocketVoiceInput:
      type: object
      properties:
        text:
          type: string
          description: >-
            Text appended for this voice. Buffered with prior text until the
            server triggers generation.
        voice_id:
          type: string
          description: Must be one of the IDs from the initial `voices` array.
        new_turn:
          type: boolean
          default: false
          description: >-
            When `true`, the server finalizes the current pending segment (as if
            the speaker finished their turn) before applying this input.
      required:
        - text
        - voice_id
      title: TextToDialogueWebsocketVoiceInput
    TextToDialogueWebsocketVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
          default: 0.5
          description: >-
            Determines how stable the voice is and the randomness between each
            generation. Lower values introduce broader emotional range for the
            voice. Higher values can result in a monotonous voice with limited
            emotion.
      description: >-
        Voice settings for dialogue generation. Only `stability` is supported
        for `eleven_v3` dialogue models.
      title: TextToDialogueWebsocketVoiceSettings
    PronunciationDictionaryLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
          description: The unique identifier of the pronunciation dictionary
        version_id:
          type: string
          description: The version identifier of the pronunciation dictionary
      required:
        - pronunciation_dictionary_id
        - version_id
      description: Identifies a specific pronunciation dictionary to use
      title: PronunciationDictionaryLocator
    TextToDialogueWebsocketClientMessageMulti:
      type: object
      properties:
        context_id:
          type: string
          description: >-
            Identifier for an independent dialogue stream within the socket. The
            first message with a new `context_id` creates that context. Required
            on every message except one containing only `close_socket`.
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/TextToDialogueWebsocketVoiceInput'
          description: >-
            Dialogue lines to append to this context for synthesis. Each
            `voice_id` must be registered for this context.
        flush:
          type: boolean
          default: false
          description: Force generation of this context's buffered text without closing it.
        close_context:
          type: boolean
          default: false
          description: >-
            Flush this context's remaining audio, emit its `is_final` message,
            and close it. Other contexts stay open.
        close_socket:
          type: boolean
          default: false
          description: >-
            Flush all contexts, emit their remaining audio and `is_final`
            messages, and close the WebSocket.
        keep_alive:
          type: boolean
          default: false
          description: Resets this context's 20s inactivity timer; performs no synthesis.
        xi_api_key:
          type: string
          description: >-
            API key for the first message of the connection if not provided via
            the `xi-api-key` header.
        authorization:
          type: string
          description: >-
            Bearer token for the first message of the connection if not provided
            via the `Authorization` header.
        single_use_token:
          type: string
          description: >-
            Single-use token for the first message of the connection if not
            provided via the `single_use_token` query parameter.
        voices:
          type: array
          items:
            type: string
          description: >-
            Voice IDs to load for this context (first message for the context
            only, required on that message).
        voice_settings:
          $ref: '#/components/schemas/TextToDialogueWebsocketVoiceSettings'
          description: >-
            Optional voice settings for this context (first message for the
            context only).
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocator'
          description: >-
            Optional pronunciation dictionaries for this context (first message
            for the context only).
      description: >
        All fields are optional unless noted for a context's **first** message.


        **Every message**

        - `context_id` is required, except on a message containing only
        `close_socket`.


        **First message for a context**

        - `voices`: non-empty array of voice IDs (maximum 10 per context for
        `eleven_v3`; exactly 1 for `eleven_v3_conversational`).

        - Credentials if not supplied via `xi-api-key` / `Authorization` headers
        or `single_use_token` query parameter (accepted on the first message of
        the connection only).


        **Subsequent messages for a context**

        - Do not resend `voices`, `voice_settings`,
        `pronunciation_dictionary_locators`, or credential fields.
      title: TextToDialogueWebsocketClientMessageMulti
    V1TextToDialogueMultiStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/TextToDialogueWebsocketClientMessageMulti'
      title: V1TextToDialogueMultiStreamInputPublish

```
