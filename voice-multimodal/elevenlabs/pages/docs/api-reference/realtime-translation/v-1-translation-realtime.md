---
title: "WebSocket"
source: https://elevenlabs.io/docs/api-reference/realtime-translation/v-1-translation-realtime.md
path: docs/api-reference/realtime-translation/v-1-translation-realtime
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WebSocket

GET /v1/translation/realtime

The Realtime Translation WebSocket API streams translation audio continuously to a target language given source audio.

Reference: https://elevenlabs.io/docs/api-reference/realtime-translation/v-1-translation-realtime

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Translation Realtime
  version: subpackage_v1TranslationRealtime.v1TranslationRealtime
  description: >-
    The Realtime Translation WebSocket API streams translation audio
    continuously to a target language given source audio.
channels:
  /v1/translation/realtime:
    description: >-
      The Realtime Translation WebSocket API streams translation audio
      continuously to a target language given source audio.
    bindings:
      ws:
        query:
          type: object
          properties:
            authorization:
              type: string
            target_language:
              type: string
            source_language:
              type: string
            voice_id:
              type: string
            input_format:
              description: Any type
            output_format:
              description: Any type
            tts_model_id:
              $ref: '#/components/schemas/_v1_translation_realtime_tts_model_id'
              default: eleven_v4_turbo
            apply_text_normalization:
              $ref: >-
                #/components/schemas/_v1_translation_realtime_apply_text_normalization
              default: 'off'
            eagerness:
              $ref: '#/components/schemas/_v1_translation_realtime_eagerness'
              default: medium
            client_session_id:
              type: string
            enable_zrm:
              type: boolean
              default: false
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: subpackage_v1TranslationRealtime.v1TranslationRealtime-publish
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
          $ref: '#/components/schemas/V1TranslationRealtimeSubscribe'
    subscribe:
      operationId: subpackage_v1TranslationRealtime.v1TranslationRealtime-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1TranslationRealtimePublish'
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
    _v1_translation_realtime_tts_model_id:
      type: string
      enum:
        - eleven_flash_v2_5
        - eleven_v3
        - eleven_v4_turbo
      default: eleven_v4_turbo
      description: TTS model used to synthesize the translated speech.
      title: /v1/translation/realtime_tts_model_id
    _v1_translation_realtime_apply_text_normalization:
      type: string
      enum:
        - auto
        - 'on'
        - 'off'
      default: 'off'
      description: >-
        This parameter controls text normalization with three modes: 'auto',
        'on', and 'off'. When set to 'auto', the system will automatically
        decide whether to apply text normalization (e.g., spelling out numbers).
        With 'on', text normalization will always be applied, while with 'off',
        it will be skipped.
      title: /v1/translation/realtime_apply_text_normalization
    _v1_translation_realtime_eagerness:
      type: string
      enum:
        - low
        - medium
        - high
      default: medium
      description: >-
        How eagerly translation starts while the speaker is still talking.
        'high' starts translating soonest for the lowest latency. 'low' waits
        for more of the sentence, giving higher quality translations with more
        delay.
      title: /v1/translation/realtime_eagerness
    sessionStarted:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - session_started
          description: The message type identifier.
        session_id:
          type: string
          description: Unique identifier for this session.
        client_session_id:
          type:
            - string
            - 'null'
          description: Client-defined session identifier, if provided during connection.
      required:
        - message_type
        - session_id
      description: Confirms the session has been initialized.
      title: sessionStarted
    status:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - status
          description: The message type identifier.
        status:
          type: string
          description: Current session status (`started` or `stopped`).
      required:
        - message_type
        - status
      description: Session lifecycle update.
      title: status
    partialTranscript:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - partial_transcript
          description: The message type identifier.
        text:
          type: string
          description: Partial transcription text.
      required:
        - message_type
        - text
      description: Interim transcription of the source audio.
      title: partialTranscript
    finalTranscript:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - final_transcript
          description: The message type identifier.
        text:
          type: string
          description: Final transcription text.
      required:
        - message_type
        - text
      description: Final transcription of a completed segment.
      title: finalTranscript
    translation:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - translation
          description: The message type identifier.
        text:
          type: string
          description: Translated text.
      required:
        - message_type
        - text
      description: Translated text in the target language.
      title: translation
    audio:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - audio
          description: The message type identifier.
        data:
          type: string
          description: Base64-encoded audio data.
        sample_rate:
          type: integer
          description: Sample rate of the audio in Hz.
      required:
        - message_type
        - data
        - sample_rate
      description: Base64-encoded audio of the translated speech.
      title: audio
    error:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - error
          description: The message type identifier.
        error:
          type: string
          description: Error message.
      required:
        - message_type
        - error
      description: Error encountered during translation.
      title: error
    TranslateAuthError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - auth_error
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateAuthError
    TranslateRateLimitedError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - rate_limited
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateRateLimitedError
    TranslateQueueOverflowError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - queue_overflow
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateQueueOverflowError
    TranslateInputError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - input_error
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateInputError
    TranslateTranscriberError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - transcriber_error
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateTranscriberError
    TranslateTranslationError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - translation_error
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateTranslationError
    TranslateAudioOutputError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - audio_output_error
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateAudioOutputError
    TranslateQuotaExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - quota_exceeded
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateQuotaExceededError
    TranslatePaymentIssueError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - payment_issue
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslatePaymentIssueError
    TranslateUnacceptedTermsError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - unaccepted_terms
        error:
          type: string
      required:
        - message_type
        - error
      title: TranslateUnacceptedTermsError
    V1TranslationRealtimeSubscribe:
      oneOf:
        - $ref: '#/components/schemas/sessionStarted'
        - $ref: '#/components/schemas/status'
        - $ref: '#/components/schemas/partialTranscript'
        - $ref: '#/components/schemas/finalTranscript'
        - $ref: '#/components/schemas/translation'
        - $ref: '#/components/schemas/audio'
        - $ref: '#/components/schemas/error'
        - $ref: '#/components/schemas/TranslateAuthError'
        - $ref: '#/components/schemas/TranslateRateLimitedError'
        - $ref: '#/components/schemas/TranslateQueueOverflowError'
        - $ref: '#/components/schemas/TranslateInputError'
        - $ref: '#/components/schemas/TranslateTranscriberError'
        - $ref: '#/components/schemas/TranslateTranslationError'
        - $ref: '#/components/schemas/TranslateAudioOutputError'
        - $ref: '#/components/schemas/TranslateQuotaExceededError'
        - $ref: '#/components/schemas/TranslatePaymentIssueError'
        - $ref: '#/components/schemas/TranslateUnacceptedTermsError'
      title: V1TranslationRealtimeSubscribe
    inputAudioChunk:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - input_audio_chunk
          description: The message type identifier.
        audio_base_64:
          type: string
          description: >-
            Base64-encoded audio data. Recommended chunk size is around 100 ms
            of audio.
      required:
        - message_type
        - audio_base_64
      description: A chunk of audio to be translated.
      title: inputAudioChunk
    endOfStream:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - end_of_stream
          description: The message type identifier.
      required:
        - message_type
      description: Signal that the client has finished sending audio.
      title: endOfStream
    V1TranslationRealtimePublish:
      oneOf:
        - $ref: '#/components/schemas/inputAudioChunk'
        - $ref: '#/components/schemas/endOfStream'
      title: V1TranslationRealtimePublish

```
