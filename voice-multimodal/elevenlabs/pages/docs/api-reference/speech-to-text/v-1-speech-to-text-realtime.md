---
title: "Realtime"
source: https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime.md
path: docs/api-reference/speech-to-text/v-1-speech-to-text-realtime
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Realtime

GET /v1/speech-to-text/realtime

Realtime speech-to-text transcription service. This WebSocket API enables streaming audio input and receiving transcription results.

## Event Flow
- Audio chunks are sent as `input_audio_chunk` messages
- Transcription results are streamed back in various formats (partial, committed, with timestamps)
- Supports manual commit or VAD-based automatic commit strategies

Authentication is done either by providing a valid API key in the `xi-api-key` header or by providing a valid token in the `token` query parameter. Tokens can be generated from the [single use token endpoint](/docs/api-reference/tokens/create). Use tokens if you want to transcribe audio from the client side.


Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Speech To Text Realtime
  version: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime
  description: >
    Realtime speech-to-text transcription service. This WebSocket API enables
    streaming audio input and receiving transcription results.


    ## Event Flow

    - Audio chunks are sent as `input_audio_chunk` messages

    - Transcription results are streamed back in various formats (partial,
    committed, with timestamps)

    - Supports manual commit or VAD-based automatic commit strategies


    Authentication is done either by providing a valid API key in the
    `xi-api-key` header or by providing a valid token in the `token` query
    parameter. Tokens can be generated from the [single use token
    endpoint](/docs/api-reference/tokens/create). Use tokens if you want to
    transcribe audio from the client side.
channels:
  /v1/speech-to-text/realtime:
    description: >
      Realtime speech-to-text transcription service. This WebSocket API enables
      streaming audio input and receiving transcription results.


      ## Event Flow

      - Audio chunks are sent as `input_audio_chunk` messages

      - Transcription results are streamed back in various formats (partial,
      committed, with timestamps)

      - Supports manual commit or VAD-based automatic commit strategies


      Authentication is done either by providing a valid API key in the
      `xi-api-key` header or by providing a valid token in the `token` query
      parameter. Tokens can be generated from the [single use token
      endpoint](/docs/api-reference/tokens/create). Use tokens if you want to
      transcribe audio from the client side.
    bindings:
      ws:
        query:
          type: object
          properties:
            model_id:
              description: Any type
            token:
              description: Any type
            audio_format:
              description: Any type
            language_code:
              description: Any type
            secondary_languages:
              description: Any type
            commit_strategy:
              description: Any type
            vad_threshold:
              description: Any type
            vad_silence_threshold_secs:
              description: Any type
            min_speech_duration_ms:
              description: Any type
            min_silence_duration_ms:
              description: Any type
            include_timestamps:
              description: Any type
            include_language_detection:
              description: Any type
            keyterms:
              description: Any type
            no_verbatim:
              description: Any type
            filter_background_audio:
              description: Any type
            enable_logging:
              description: Any type
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime-publish
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
          $ref: '#/components/schemas/V1SpeechToTextRealtimeSubscribe'
    subscribe:
      operationId: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime-subscribe
      summary: publish
      description: Defines the message types that can be sent from client to server
      message:
        name: publish
        title: publish
        description: Defines the message types that can be sent from client to server
        payload:
          $ref: '#/components/schemas/V1SpeechToTextRealtimePublish'
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
    SessionStartedConfigAudioFormat:
      type: string
      enum:
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
      title: SessionStartedConfigAudioFormat
    SessionStartedConfigTimestampsGranularity:
      type: string
      enum:
        - none
        - word
        - character
      default: word
      title: SessionStartedConfigTimestampsGranularity
    SessionStartedConfigModelId:
      type: string
      enum:
        - scribe_v2_realtime
        - scribe_v2_realtime_turbo
      default: scribe_v2_realtime
      title: SessionStartedConfigModelId
    SessionStartedConfig:
      type: object
      properties:
        sample_rate:
          type: integer
        audio_format:
          $ref: '#/components/schemas/SessionStartedConfigAudioFormat'
        language_code:
          type: string
        secondary_languages:
          type: array
          items:
            type: string
        timestamps_granularity:
          $ref: '#/components/schemas/SessionStartedConfigTimestampsGranularity'
          default: word
        vad_commit_strategy:
          type: boolean
          default: false
        vad_silence_threshold_secs:
          type: number
          format: double
          default: 1.5
        vad_threshold:
          type: number
          format: double
          default: 0.4
        min_speech_duration_ms:
          type: integer
          default: 100
        min_silence_duration_ms:
          type: integer
          default: 100
        max_tokens_to_recompute:
          type: integer
          default: 5
        model_id:
          $ref: '#/components/schemas/SessionStartedConfigModelId'
          default: scribe_v2_realtime
        disable_logging:
          type: boolean
          default: false
        include_timestamps:
          type: boolean
          default: false
        include_language_detection:
          type: boolean
          default: false
        filter_background_audio:
          type: boolean
          default: false
        keyterms:
          type: array
          items:
            type: string
        no_verbatim:
          type: boolean
          default: false
        entity_detection:
          type: array
          items:
            type: string
      required:
        - sample_rate
        - audio_format
        - language_code
      title: SessionStartedConfig
    SessionStarted:
      type: object
      properties:
        message_type:
          type: string
          default: session_started
        session_id:
          type: string
        config:
          $ref: '#/components/schemas/SessionStartedConfig'
      required:
        - session_id
        - config
      title: SessionStarted
    PartialTranscript:
      type: object
      properties:
        message_type:
          type: string
          default: partial_transcript
        text:
          type: string
      required:
        - text
      title: PartialTranscript
    FinalTranscript:
      type: object
      properties:
        message_type:
          type: string
          default: final_transcript
        text:
          type: string
      required:
        - text
      title: FinalTranscript
    FinalTranscriptWithTimestampsWordsItemsType:
      type: string
      enum:
        - word
        - spacing
        - audio_event
      description: >-
        The type of the word or sound. 'audio_event' is used for non-word sounds
        like laughter or footsteps.
      title: FinalTranscriptWithTimestampsWordsItemsType
    FinalTranscriptWithTimestampsWordsItemsCharactersItems:
      type: object
      properties:
        text:
          type: string
          description: The character that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the character in seconds.
        end:
          type: number
          format: double
          description: The end time of the character in seconds.
      required:
        - text
      title: FinalTranscriptWithTimestampsWordsItemsCharactersItems
    FinalTranscriptWithTimestampsWordsItems:
      type: object
      properties:
        text:
          type: string
          description: The word or sound that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the word or sound in seconds.
        end:
          type: number
          format: double
          description: The end time of the word or sound in seconds.
        type:
          $ref: '#/components/schemas/FinalTranscriptWithTimestampsWordsItemsType'
          description: >-
            The type of the word or sound. 'audio_event' is used for non-word
            sounds like laughter or footsteps.
        speaker_id:
          type: string
          description: Unique identifier for the speaker of this word.
        logprob:
          type: number
          format: double
          description: >-
            The log of the probability with which this word was predicted.
            Logprobs are in range [-infinity, 0], higher logprobs indicate a
            higher confidence the model has in its predictions.
        characters:
          type: array
          items:
            $ref: >-
              #/components/schemas/FinalTranscriptWithTimestampsWordsItemsCharactersItems
          description: The characters that make up the word and their timing information.
        channel_index:
          type: integer
          description: >-
            The channel this word was spoken on (for multichannel audio). Null
            for single-channel transcriptions.
      required:
        - text
        - type
        - logprob
      description: Word-level detail of the transcription with timing information.
      title: FinalTranscriptWithTimestampsWordsItems
    FinalTranscriptWithTimestamps:
      type: object
      properties:
        message_type:
          type: string
          default: final_transcript_with_timestamps
        text:
          type: string
        language_code:
          type: string
        words:
          type: array
          items:
            $ref: '#/components/schemas/FinalTranscriptWithTimestampsWordsItems'
      required:
        - text
      title: FinalTranscriptWithTimestamps
    CommittedTranscript:
      type: object
      properties:
        message_type:
          type: string
          default: committed_transcript
        text:
          type: string
      required:
        - text
      title: CommittedTranscript
    CommittedTranscriptWithTimestampsWordsItemsType:
      type: string
      enum:
        - word
        - spacing
        - audio_event
      description: >-
        The type of the word or sound. 'audio_event' is used for non-word sounds
        like laughter or footsteps.
      title: CommittedTranscriptWithTimestampsWordsItemsType
    CommittedTranscriptWithTimestampsWordsItemsCharactersItems:
      type: object
      properties:
        text:
          type: string
          description: The character that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the character in seconds.
        end:
          type: number
          format: double
          description: The end time of the character in seconds.
      required:
        - text
      title: CommittedTranscriptWithTimestampsWordsItemsCharactersItems
    CommittedTranscriptWithTimestampsWordsItems:
      type: object
      properties:
        text:
          type: string
          description: The word or sound that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the word or sound in seconds.
        end:
          type: number
          format: double
          description: The end time of the word or sound in seconds.
        type:
          $ref: '#/components/schemas/CommittedTranscriptWithTimestampsWordsItemsType'
          description: >-
            The type of the word or sound. 'audio_event' is used for non-word
            sounds like laughter or footsteps.
        speaker_id:
          type: string
          description: Unique identifier for the speaker of this word.
        logprob:
          type: number
          format: double
          description: >-
            The log of the probability with which this word was predicted.
            Logprobs are in range [-infinity, 0], higher logprobs indicate a
            higher confidence the model has in its predictions.
        characters:
          type: array
          items:
            $ref: >-
              #/components/schemas/CommittedTranscriptWithTimestampsWordsItemsCharactersItems
          description: The characters that make up the word and their timing information.
        channel_index:
          type: integer
          description: >-
            The channel this word was spoken on (for multichannel audio). Null
            for single-channel transcriptions.
      required:
        - text
        - type
        - logprob
      description: Word-level detail of the transcription with timing information.
      title: CommittedTranscriptWithTimestampsWordsItems
    CommittedTranscriptWithTimestamps:
      type: object
      properties:
        message_type:
          type: string
          default: committed_transcript_with_timestamps
        text:
          type: string
        language_code:
          type: string
        words:
          type: array
          items:
            $ref: '#/components/schemas/CommittedTranscriptWithTimestampsWordsItems'
      required:
        - text
      title: CommittedTranscriptWithTimestamps
    CommittedTranscriptEntitiesEntitiesItems:
      type: object
      properties:
        text:
          type: string
          description: The text that was identified as an entity.
        entity_type:
          type: string
          description: >-
            The type of entity detected (e.g., 'credit_card', 'email_address',
            'person_name').
        start_char:
          type: integer
          description: Start character position in the transcript text.
        end_char:
          type: integer
          description: End character position in the transcript text.
      required:
        - text
        - entity_type
        - start_char
        - end_char
      title: CommittedTranscriptEntitiesEntitiesItems
    CommittedTranscriptEntities:
      type: object
      properties:
        message_type:
          type: string
          default: committed_transcript_entities
        text:
          type: string
        entities:
          type: array
          items:
            $ref: '#/components/schemas/CommittedTranscriptEntitiesEntitiesItems'
      required:
        - text
      title: CommittedTranscriptEntities
    ScribeError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - error
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeError
    ScribeAuthError:
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
      title: ScribeAuthError
    ScribeQuotaExceededError:
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
      title: ScribeQuotaExceededError
    ScribeThrottledError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - commit_throttled
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeThrottledError
    ScribeUnacceptedTermsError:
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
      title: ScribeUnacceptedTermsError
    ScribeRateLimitedError:
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
      title: ScribeRateLimitedError
    ScribeQueueOverflowError:
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
      title: ScribeQueueOverflowError
    ScribeResourceExhaustedError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - resource_exhausted
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeResourceExhaustedError
    ScribeSessionTimeLimitExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - session_time_limit_exceeded
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeSessionTimeLimitExceededError
    ScribeInputError:
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
      title: ScribeInputError
    ScribeChunkSizeExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - chunk_size_exceeded
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeChunkSizeExceededError
    ScribeInsufficientAudioActivityError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - insufficient_audio_activity
        error:
          type: string
      required:
        - message_type
        - error
      title: ScribeInsufficientAudioActivityError
    ScribeTranscriberError:
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
      title: ScribeTranscriberError
    V1SpeechToTextRealtimeSubscribe:
      oneOf:
        - $ref: '#/components/schemas/SessionStarted'
        - $ref: '#/components/schemas/PartialTranscript'
        - $ref: '#/components/schemas/FinalTranscript'
        - $ref: '#/components/schemas/FinalTranscriptWithTimestamps'
        - $ref: '#/components/schemas/CommittedTranscript'
        - $ref: '#/components/schemas/CommittedTranscriptWithTimestamps'
        - $ref: '#/components/schemas/CommittedTranscriptEntities'
        - $ref: '#/components/schemas/ScribeError'
        - $ref: '#/components/schemas/ScribeAuthError'
        - $ref: '#/components/schemas/ScribeQuotaExceededError'
        - $ref: '#/components/schemas/ScribeThrottledError'
        - $ref: '#/components/schemas/ScribeUnacceptedTermsError'
        - $ref: '#/components/schemas/ScribeRateLimitedError'
        - $ref: '#/components/schemas/ScribeQueueOverflowError'
        - $ref: '#/components/schemas/ScribeResourceExhaustedError'
        - $ref: '#/components/schemas/ScribeSessionTimeLimitExceededError'
        - $ref: '#/components/schemas/ScribeInputError'
        - $ref: '#/components/schemas/ScribeChunkSizeExceededError'
        - $ref: '#/components/schemas/ScribeInsufficientAudioActivityError'
        - $ref: '#/components/schemas/ScribeTranscriberError'
      title: V1SpeechToTextRealtimeSubscribe
    InputAudioChunk:
      type: object
      properties:
        message_type:
          type: string
          default: input_audio_chunk
        audio_base_64:
          type: string
        commit:
          type: boolean
          default: false
        previous_text:
          type: string
      required:
        - audio_base_64
      title: InputAudioChunk
    V1SpeechToTextRealtimePublish:
      oneOf:
        - $ref: '#/components/schemas/InputAudioChunk'
      title: V1SpeechToTextRealtimePublish

```
