---
title: "Turn-based Speech (Flux)"
source: https://developers.deepgram.com/reference/text-to-speech/speak-flux.md
path: reference/text-to-speech/speak-flux
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Turn-based Speech (Flux)

GET /v2/speak

Streaming, turn-based text-to-speech (Flux TTS) built for voice-agent
pipelines. Stream LLM tokens in, speak them to the user, and report
per-turn billing and timing.


Reference: https://developers.deepgram.com/reference/text-to-speech/speak-flux

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: speak.v2
  version: subpackage_speak/v2.speak.v2
  description: |
    Streaming, turn-based text-to-speech (Flux TTS) built for voice-agent
    pipelines. Stream LLM tokens in, speak them to the user, and report
    per-turn billing and timing.
channels:
  /v2/speak:
    description: |
      Streaming, turn-based text-to-speech (Flux TTS) built for voice-agent
      pipelines. Stream LLM tokens in, speak them to the user, and report
      per-turn billing and timing.
    bindings:
      ws:
        query:
          type: object
          properties:
            model:
              $ref: '#/components/schemas/SpeakV2Model'
            encoding:
              $ref: '#/components/schemas/SpeakV2Encoding'
              default: linear16
            sample_rate:
              $ref: '#/components/schemas/SpeakV2SampleRate'
            mip_opt_out:
              $ref: '#/components/schemas/SpeakV2MipOptOut'
              default: 'false'
            tag:
              $ref: '#/components/schemas/SpeakV2Tag'
        headers:
          type: object
          properties:
            Authorization:
              type: string
    publish:
      operationId: subpackage_speak/v2.speak.v2-publish
      summary: Server messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-0-SpeakV2Audio
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-1-SpeakV2Connected
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-2-SpeakV2SpeechStarted
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-3-SpeakV2SpeechMetadata
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-4-SpeakV2Flushed
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-5-SpeakV2SessionMetadata
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-6-SpeakV2Warning
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-7-SpeakV2Error
    subscribe:
      operationId: subpackage_speak/v2.speak.v2-subscribe
      summary: Client messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-client-0-SpeakV2Speak
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-client-1-SpeakV2Flush
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-client-2-SpeakV2Close
servers:
  Production:
    url: wss://api.deepgram.com/
    protocol: wss
    x-default: true
components:
  messages:
    subpackage_speak/v2.speak.v2-server-0-SpeakV2Audio:
      name: SpeakV2Audio
      title: SpeakV2Audio
      description: Receive audio chunks as they are generated
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Audio'
    subpackage_speak/v2.speak.v2-server-1-SpeakV2Connected:
      name: SpeakV2Connected
      title: SpeakV2Connected
      description: Receive a connected message on a successful connection
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Connected'
    subpackage_speak/v2.speak.v2-server-2-SpeakV2SpeechStarted:
      name: SpeakV2SpeechStarted
      title: SpeakV2SpeechStarted
      description: >-
        Receive a message marking the start of a new turn, carrying the turn's
        unique identifier
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2SpeechStarted'
    subpackage_speak/v2.speak.v2-server-3-SpeakV2SpeechMetadata:
      name: SpeakV2SpeechMetadata
      title: SpeakV2SpeechMetadata
      description: Receive per-turn billing and timing after a manual Flush
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2SpeechMetadata'
    subpackage_speak/v2.speak.v2-server-4-SpeakV2Flushed:
      name: SpeakV2Flushed
      title: SpeakV2Flushed
      description: Receive an echo confirming receipt of a manual Flush
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Flushed'
    subpackage_speak/v2.speak.v2-server-5-SpeakV2SessionMetadata:
      name: SpeakV2SessionMetadata
      title: SpeakV2SessionMetadata
      description: Receive cumulative session totals before the socket closes
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2SessionMetadata'
    subpackage_speak/v2.speak.v2-server-6-SpeakV2Warning:
      name: SpeakV2Warning
      title: SpeakV2Warning
      description: Receive a warning; synthesis continues and the connection is unaffected
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Warning'
    subpackage_speak/v2.speak.v2-server-7-SpeakV2Error:
      name: SpeakV2Error
      title: SpeakV2Error
      description: Receive a fatal error message followed by a WebSocket close
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Error'
    subpackage_speak/v2.speak.v2-client-0-SpeakV2Speak:
      name: SpeakV2Speak
      title: SpeakV2Speak
      description: Send text to be synthesized into the active turn
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Speak'
    subpackage_speak/v2.speak.v2-client-1-SpeakV2Flush:
      name: SpeakV2Flush
      title: SpeakV2Flush
      description: End the active turn and generate the remaining audio
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Flush'
    subpackage_speak/v2.speak.v2-client-2-SpeakV2Close:
      name: SpeakV2Close
      title: SpeakV2Close
      description: Gracefully close the connection, draining all remaining and queued audio
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Close'
  schemas:
    SpeakV2Model:
      type: string
      description: >-
        The Flux TTS model used to synthesize speech. Required on every
        connection. Model strings follow the format `flux-{voice}-{language}`
        (e.g. `flux-alexis-en`). An Aura model string is rejected on
        `/v2/speak`; use `/v1/speak` for Aura voices.
      title: SpeakV2Model
    SpeakV2Encoding:
      type: string
      enum:
        - linear16
        - mulaw
        - alaw
      default: linear16
      description: >-
        Encoding of the raw output audio. The streaming WebSocket emits raw
        (non-containerized) audio, so only streaming-compatible encodings are
        supported. Compressed and containerized encodings (`mp3`, `opus`,
        `flac`, `aac`) are available on the batch REST transport only.
      title: SpeakV2Encoding
    SpeakV2SampleRate:
      type: string
      enum:
        - '8000'
        - '16000'
        - '24000'
        - '32000'
        - '44100'
        - '48000'
      description: >-
        Output sample rate in Hz. With `linear16`, valid values are `8000`,
        `16000`, `24000`, `32000`, `44100`, and `48000`. With `mulaw` or `alaw`,
        valid values are `8000` and `16000`. Defaults to the model's native
        sample rate.
      title: SpeakV2SampleRate
    SpeakV2MipOptOut:
      description: Any type
      title: SpeakV2MipOptOut
    SpeakV2Tag:
      description: Any type
      title: SpeakV2Tag
    SpeakV2_SpeakV2Audio:
      type: string
      format: binary
      title: SpeakV2_SpeakV2Audio
    SpeakV2_SpeakV2Connected:
      type: object
      properties:
        type:
          type: string
          enum:
            - Connected
          description: Message type identifier
        request_id:
          type: string
          format: uuid
          description: The unique identifier of the `/v2/speak` request
        model_name:
          type: string
          description: Resolved model name
        model_version:
          type: string
          description: Resolved model version
        model_uuids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Resolved model UUIDs. A list, because a resolved model may be backed
            by more than one underlying model.
      required:
        - type
        - request_id
        - model_name
        - model_version
        - model_uuids
      title: SpeakV2_SpeakV2Connected
    SpeakV2_SpeakV2SpeechStarted:
      type: object
      properties:
        type:
          type: string
          enum:
            - SpeechStarted
          description: Message type identifier
        speech_id:
          type: string
          description: >-
            Server-minted identifier for this turn, of the form `dg_sp_<12 hex
            digits>`. Informational.
      required:
        - type
        - speech_id
      title: SpeakV2_SpeakV2SpeechStarted
    ChannelsSpeakV2MessagesSpeakV2SpeechMetadataControlsApplied:
      type: object
      properties:
        pronunciations_applied:
          type: integer
          description: >-
            Pronunciation overrides successfully applied. Mirrors the Aura-2
            `dg-pronunciations-applied` REST header. Always `0` during Early
            Access.
        pronunciation_warnings:
          type: integer
          description: >-
            Pronunciation entries that triggered a warning (invalid IPA, word
            too long). Mirrors the Aura-2 `dg-pronunciation-warnings` REST
            header. Always `0` during Early Access.
      required:
        - pronunciations_applied
        - pronunciation_warnings
      description: >-
        Controls applied during the turn. Inline pronunciation and pause
        controls are not available during Early Access, so every count is
        currently `0`.
      title: ChannelsSpeakV2MessagesSpeakV2SpeechMetadataControlsApplied
    SpeakV2_SpeakV2SpeechMetadata:
      type: object
      properties:
        type:
          type: string
          enum:
            - SpeechMetadata
          description: Message type identifier
        speech_id:
          type: string
          description: Server-assigned turn identifier
        audio_duration_ms:
          type: integer
          description: Total audio duration produced for this turn, in milliseconds
        input_character_count:
          type: integer
          description: Raw input character count for this turn, before text normalization
        billable_character_count:
          type: integer
          description: >-
            Billable character count for this turn — the input character count
            with stripped control characters removed. Always less than or equal
            to `input_character_count`.
        controls_applied:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2SpeechMetadataControlsApplied
          description: >-
            Controls applied during the turn. Inline pronunciation and pause
            controls are not available during Early Access, so every count is
            currently `0`.
      required:
        - type
        - speech_id
        - audio_duration_ms
        - input_character_count
        - billable_character_count
        - controls_applied
      title: SpeakV2_SpeakV2SpeechMetadata
    SpeakV2_SpeakV2Flushed:
      type: object
      properties:
        type:
          type: string
          enum:
            - Flushed
          description: Message type identifier
        speech_id:
          type: string
          description: Server-assigned turn identifier
      required:
        - type
        - speech_id
      title: SpeakV2_SpeakV2Flushed
    SpeakV2_SpeakV2SessionMetadata:
      type: object
      properties:
        type:
          type: string
          enum:
            - SessionMetadata
          description: Message type identifier
        total_audio_duration_ms:
          type: integer
          description: >-
            Cumulative audio duration produced across the session, in
            milliseconds
        total_input_character_count:
          type: integer
          description: Cumulative raw input character count across the session
        total_billable_character_count:
          type: integer
          description: Cumulative billable character count across the session
      required:
        - type
        - total_audio_duration_ms
        - total_input_character_count
        - total_billable_character_count
      title: SpeakV2_SpeakV2SessionMetadata
    SpeakV2_SpeakV2Warning:
      type: object
      properties:
        type:
          type: string
          enum:
            - Warning
          description: Message type identifier
        code:
          type: string
          description: >-
            Warning code identifying the condition, in `SCREAMING_SNAKE_CASE`.
            Early Access codes are `NO_ACTIVE_SPEECH` (a speech-scoped message
            arrived with no active turn) and `SYNTHESIS_RETRYING` (a synthesis
            request failed and is being retried).
        description:
          type: string
          description: A human-readable description of the warning
      required:
        - type
        - code
        - description
      title: SpeakV2_SpeakV2Warning
    ChannelsSpeakV2MessagesSpeakV2ErrorCode:
      type: string
      enum:
        - MESSAGE-0000
        - DATA-0000
        - BIG-0000
        - NET-0000
        - NET-0001
        - NET-0002
        - NET-0003
        - NET-0004
      description: A code identifying the error, e.g. `MESSAGE-0000` or `NET-0000`.
      title: ChannelsSpeakV2MessagesSpeakV2ErrorCode
    SpeakV2_SpeakV2Error:
      type: object
      properties:
        type:
          type: string
          enum:
            - Error
          description: Message type identifier
        code:
          $ref: '#/components/schemas/ChannelsSpeakV2MessagesSpeakV2ErrorCode'
          description: A code identifying the error, e.g. `MESSAGE-0000` or `NET-0000`.
        description:
          type: string
          description: Prose description of the error
      required:
        - type
        - code
        - description
      title: SpeakV2_SpeakV2Error
    SpeakV2_SpeakV2Speak:
      type: object
      properties:
        type:
          type: string
          enum:
            - Speak
          description: Message type identifier
        text:
          type: string
          description: The input text to synthesize
      required:
        - type
        - text
      title: SpeakV2_SpeakV2Speak
    SpeakV2_SpeakV2Flush:
      type: object
      properties:
        type:
          type: string
          enum:
            - Flush
          description: Message type identifier
      required:
        - type
      title: SpeakV2_SpeakV2Flush
    SpeakV2_SpeakV2Close:
      type: object
      properties:
        type:
          type: string
          enum:
            - Close
          description: Message type identifier
      required:
        - type
      title: SpeakV2_SpeakV2Close

```
