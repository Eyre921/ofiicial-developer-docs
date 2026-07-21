---
title: "Multi-Context WebSocket"
source: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input.md
path: docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Multi-Context WebSocket

GET /v1/text-to-speech/{voice_id}/multi-stream-input

The Multi-Context Text-to-Speech WebSockets API allows for generating audio from text input
while managing multiple independent audio generation streams (contexts) over a single WebSocket connection.
This is useful for scenarios requiring concurrent or interleaved audio generations, such as dynamic
conversational AI applications.

Each context, identified by a context id, maintains its own state. You can send text to specific
contexts, flush them, or close them independently. A `close_socket` message can be used to terminate
the entire connection gracefully.

For more information on best practices for how to use this API, please see the [multi context websocket guide](/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket).


Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Speech Voice Id Multi Stream Input
  version: >-
    subpackage_v1TextToSpeechVoiceIdMultiStreamInput.v1TextToSpeechVoiceIdMultiStreamInput
  description: >
    The Multi-Context Text-to-Speech WebSockets API allows for generating audio
    from text input

    while managing multiple independent audio generation streams (contexts) over
    a single WebSocket connection.

    This is useful for scenarios requiring concurrent or interleaved audio
    generations, such as dynamic

    conversational AI applications.


    Each context, identified by a context id, maintains its own state. You can
    send text to specific

    contexts, flush them, or close them independently. A `close_socket` message
    can be used to terminate

    the entire connection gracefully.


    For more information on best practices for how to use this API, please see
    the [multi context websocket
    guide](/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket).
channels:
  /v1/text-to-speech/{voice_id}/multi-stream-input:
    description: >
      The Multi-Context Text-to-Speech WebSockets API allows for generating
      audio from text input

      while managing multiple independent audio generation streams (contexts)
      over a single WebSocket connection.

      This is useful for scenarios requiring concurrent or interleaved audio
      generations, such as dynamic

      conversational AI applications.


      Each context, identified by a context id, maintains its own state. You can
      send text to specific

      contexts, flush them, or close them independently. A `close_socket`
      message can be used to terminate

      the entire connection gracefully.


      For more information on best practices for how to use this API, please see
      the [multi context websocket
      guide](/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket).
    parameters:
      voice_id:
        description: The unique identifier for the voice to use in the TTS process.
        schema:
          type: string
    bindings:
      ws:
        query:
          type: object
          properties:
            authorization:
              description: Any type
            single_use_token:
              description: Any type
            model_id:
              description: Any type
            language_code:
              description: Any type
            enable_logging:
              description: Any type
            output_format:
              description: Any type
            inactivity_timeout:
              description: Any type
            sync_alignment:
              description: Any type
            auto_mode:
              description: Any type
            apply_text_normalization:
              description: Any type
            seed:
              description: Any type
            enable_ssml_parsing:
              description: Any type
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: >-
        subpackage_v1TextToSpeechVoiceIdMultiStreamInput.v1TextToSpeechVoiceIdMultiStreamInput-publish
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
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdMultiStreamInputSubscribe'
    subscribe:
      operationId: >-
        subpackage_v1TextToSpeechVoiceIdMultiStreamInput.v1TextToSpeechVoiceIdMultiStreamInput-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdMultiStreamInputPublish'
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
    AudioOutputMultiNormalizedAlignment:
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
      required:
        - chars
        - char_start_times_ms
        - char_durations_ms
      title: AudioOutputMultiNormalizedAlignment
    AudioOutputMultiAlignment:
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
      required:
        - chars
        - char_start_times_ms
        - char_durations_ms
      title: AudioOutputMultiAlignment
    AudioOutputMulti:
      type: object
      properties:
        audio:
          type: string
        is_final:
          type: boolean
        normalized_alignment:
          $ref: '#/components/schemas/AudioOutputMultiNormalizedAlignment'
        alignment:
          $ref: '#/components/schemas/AudioOutputMultiAlignment'
        context_id:
          type: string
      required:
        - audio
      title: AudioOutputMulti
    FinalOutputMulti:
      type: object
      properties:
        is_final:
          type: boolean
          enum:
            - true
          description: Indicates the generation is complete. When true, audio is null.
        context_id:
          type: string
      title: FinalOutputMulti
    V1TextToSpeechVoiceIdMultiStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/AudioOutputMulti'
        - $ref: '#/components/schemas/FinalOutputMulti'
      title: V1TextToSpeechVoiceIdMultiStreamInputSubscribe
    InitializeConnectionMultiVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
          default: 0.5
        similarity_boost:
          type: number
          format: double
          default: 0.75
        style:
          type: number
          format: double
          default: 0
        use_speaker_boost:
          type: boolean
          default: true
        speed:
          type: number
          format: double
          default: 1
      title: InitializeConnectionMultiVoiceSettings
    InitializeConnectionMultiGenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: integer
      title: InitializeConnectionMultiGenerationConfig
    InitializeConnectionMultiPronunciationDictionaryLocatorsItems:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type: string
      required:
        - pronunciation_dictionary_id
        - version_id
      title: InitializeConnectionMultiPronunciationDictionaryLocatorsItems
    InitializeConnectionMulti:
      type: object
      properties:
        text:
          type: string
          enum:
            - ' '
          description: The initial text that must be sent is a blank space.
        voice_settings:
          $ref: '#/components/schemas/InitializeConnectionMultiVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/InitializeConnectionMultiGenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: >-
              #/components/schemas/InitializeConnectionMultiPronunciationDictionaryLocatorsItems
        xi_api_key:
          type: string
        authorization:
          type: string
        context_id:
          type: string
      required:
        - text
      title: InitializeConnectionMulti
    InitialiseContextVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
          default: 0.5
        similarity_boost:
          type: number
          format: double
          default: 0.75
        style:
          type: number
          format: double
          default: 0
        use_speaker_boost:
          type: boolean
          default: true
        speed:
          type: number
          format: double
          default: 1
      title: InitialiseContextVoiceSettings
    InitialiseContextGenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: integer
      title: InitialiseContextGenerationConfig
    InitialiseContextPronunciationDictionaryLocatorsItems:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type: string
      required:
        - pronunciation_dictionary_id
        - version_id
      title: InitialiseContextPronunciationDictionaryLocatorsItems
    InitialiseContext:
      type: object
      properties:
        text:
          type: string
        voice_settings:
          $ref: '#/components/schemas/InitialiseContextVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/InitialiseContextGenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: >-
              #/components/schemas/InitialiseContextPronunciationDictionaryLocatorsItems
        xi_api_key:
          type: string
        authorization:
          type: string
        context_id:
          type: string
      required:
        - text
      title: InitialiseContext
    SendTextMulti:
      type: object
      properties:
        text:
          type: string
        context_id:
          type: string
        flush:
          type: boolean
          default: false
      required:
        - text
      title: SendTextMulti
    FlushContext:
      type: object
      properties:
        context_id:
          type: string
        text:
          type: string
        flush:
          type: boolean
          default: false
      required:
        - context_id
        - flush
      title: FlushContext
    CloseContext:
      type: object
      properties:
        context_id:
          type: string
        close_context:
          type: boolean
          default: false
      required:
        - context_id
        - close_context
      title: CloseContext
    CloseSocket:
      type: object
      properties:
        close_socket:
          type: boolean
          default: false
      title: CloseSocket
    KeepContextAlive:
      type: object
      properties:
        text:
          type: string
          enum:
            - ''
          description: >-
            An empty string. Ignored by the server but resets the inactivity
            timeout for the context.
        context_id:
          type: string
      required:
        - text
        - context_id
      title: KeepContextAlive
    V1TextToSpeechVoiceIdMultiStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/InitializeConnectionMulti'
        - $ref: '#/components/schemas/InitialiseContext'
        - $ref: '#/components/schemas/SendTextMulti'
        - $ref: '#/components/schemas/FlushContext'
        - $ref: '#/components/schemas/CloseContext'
        - $ref: '#/components/schemas/CloseSocket'
        - $ref: '#/components/schemas/KeepContextAlive'
      title: V1TextToSpeechVoiceIdMultiStreamInputPublish

```
