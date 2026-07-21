---
title: "WebSocket"
source: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input.md
path: docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WebSocket

GET /v1/text-to-speech/{voice_id}/stream-input

The Text-to-Speech WebSockets API is designed to generate audio from partial text input
while ensuring consistency throughout the generated audio. Although highly flexible,
the WebSockets API isn't a one-size-fits-all solution. It's well-suited for scenarios where:
  * The input text is being streamed or generated in chunks.
  * Word-to-audio alignment information is required.

However, it may not be the best choice when:
  * The entire input text is available upfront. Given that the generations are partial,
    some buffering is involved, which could potentially result in slightly higher latency compared
    to a standard HTTP request.
  * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
    complex than using a standard HTTP API, which might slow down rapid development and testing.


Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Speech Voice Id Stream Input
  version: subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput
  description: >
    The Text-to-Speech WebSockets API is designed to generate audio from partial
    text input

    while ensuring consistency throughout the generated audio. Although highly
    flexible,

    the WebSockets API isn't a one-size-fits-all solution. It's well-suited for
    scenarios where:
      * The input text is being streamed or generated in chunks.
      * Word-to-audio alignment information is required.

    However, it may not be the best choice when:
      * The entire input text is available upfront. Given that the generations are partial,
        some buffering is involved, which could potentially result in slightly higher latency compared
        to a standard HTTP request.
      * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
        complex than using a standard HTTP API, which might slow down rapid development and testing.
channels:
  /v1/text-to-speech/{voice_id}/stream-input:
    description: >
      The Text-to-Speech WebSockets API is designed to generate audio from
      partial text input

      while ensuring consistency throughout the generated audio. Although highly
      flexible,

      the WebSockets API isn't a one-size-fits-all solution. It's well-suited
      for scenarios where:
        * The input text is being streamed or generated in chunks.
        * Word-to-audio alignment information is required.

      However, it may not be the best choice when:
        * The entire input text is available upfront. Given that the generations are partial,
          some buffering is involved, which could potentially result in slightly higher latency compared
          to a standard HTTP request.
        * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
          complex than using a standard HTTP API, which might slow down rapid development and testing.
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
        subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput-publish
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
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputSubscribe'
    subscribe:
      operationId: >-
        subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputPublish'
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
    AudioOutputNormalizedAlignment:
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
      title: AudioOutputNormalizedAlignment
    AudioOutputAlignment:
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
      title: AudioOutputAlignment
    AudioOutput:
      type: object
      properties:
        audio:
          type: string
        is_final:
          type: boolean
        normalized_alignment:
          $ref: '#/components/schemas/AudioOutputNormalizedAlignment'
        alignment:
          $ref: '#/components/schemas/AudioOutputAlignment'
      required:
        - audio
      title: AudioOutput
    FinalOutput:
      type: object
      properties:
        is_final:
          type: boolean
          enum:
            - true
          description: Indicates the generation is complete. When true, audio is null.
      title: FinalOutput
    V1TextToSpeechVoiceIdStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/AudioOutput'
        - $ref: '#/components/schemas/FinalOutput'
      title: V1TextToSpeechVoiceIdStreamInputSubscribe
    InitializeConnectionVoiceSettings:
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
      title: InitializeConnectionVoiceSettings
    InitializeConnectionGenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: integer
      title: InitializeConnectionGenerationConfig
    InitializeConnectionPronunciationDictionaryLocatorsItems:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type: string
      required:
        - pronunciation_dictionary_id
        - version_id
      title: InitializeConnectionPronunciationDictionaryLocatorsItems
    InitializeConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - ' '
          description: The initial text that must be sent is a blank space.
        voice_settings:
          $ref: '#/components/schemas/InitializeConnectionVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/InitializeConnectionGenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: >-
              #/components/schemas/InitializeConnectionPronunciationDictionaryLocatorsItems
        xi_api_key:
          type: string
        authorization:
          type: string
      required:
        - text
      title: InitializeConnection
    SendTextVoiceSettings:
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
      title: SendTextVoiceSettings
    SendTextGenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: integer
      title: SendTextGenerationConfig
    SendText:
      type: object
      properties:
        text:
          type: string
        try_trigger_generation:
          type: boolean
          default: false
        voice_settings:
          $ref: '#/components/schemas/SendTextVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/SendTextGenerationConfig'
        flush:
          type: boolean
          default: false
      required:
        - text
      title: SendText
    CloseConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - ''
          description: End the stream with an empty string.
      required:
        - text
      title: CloseConnection
    V1TextToSpeechVoiceIdStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/InitializeConnection'
        - $ref: '#/components/schemas/SendText'
        - $ref: '#/components/schemas/CloseConnection'
      title: V1TextToSpeechVoiceIdStreamInputPublish

```
