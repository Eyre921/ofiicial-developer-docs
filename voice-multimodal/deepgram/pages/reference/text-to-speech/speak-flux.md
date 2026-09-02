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
            speed:
              $ref: '#/components/schemas/SpeakV2Speed'
              default: 1
            expressivity:
              $ref: '#/components/schemas/SpeakV2Expressivity'
              default: 0
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
              #/components/messages/subpackage_speak/v2.speak.v2-server-4-SpeakV2SpeechInterrupted
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-5-SpeakV2Flushed
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-6-SpeakV2SessionMetadata
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-7-SpeakV2ConfigureSuccess
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-8-SpeakV2ConfigureFailure
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-9-SpeakV2Warning
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-server-10-SpeakV2Error
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
              #/components/messages/subpackage_speak/v2.speak.v2-client-2-SpeakV2Interrupt
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-client-3-SpeakV2Configure
          - $ref: >-
              #/components/messages/subpackage_speak/v2.speak.v2-client-4-SpeakV2Close
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
    subpackage_speak/v2.speak.v2-server-4-SpeakV2SpeechInterrupted:
      name: SpeakV2SpeechInterrupted
      title: SpeakV2SpeechInterrupted
      description: >-
        Receive what the user heard, and the interrupted turn's billing, after
        an Interrupt
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2SpeechInterrupted'
    subpackage_speak/v2.speak.v2-server-5-SpeakV2Flushed:
      name: SpeakV2Flushed
      title: SpeakV2Flushed
      description: Receive an echo confirming receipt of a manual Flush
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Flushed'
    subpackage_speak/v2.speak.v2-server-6-SpeakV2SessionMetadata:
      name: SpeakV2SessionMetadata
      title: SpeakV2SessionMetadata
      description: Receive cumulative session totals before the socket closes
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2SessionMetadata'
    subpackage_speak/v2.speak.v2-server-7-SpeakV2ConfigureSuccess:
      name: SpeakV2ConfigureSuccess
      title: SpeakV2ConfigureSuccess
      description: >-
        Receive confirmation that a Configure was accepted and applied, echoing
        the applied configuration
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2ConfigureSuccess'
    subpackage_speak/v2.speak.v2-server-8-SpeakV2ConfigureFailure:
      name: SpeakV2ConfigureFailure
      title: SpeakV2ConfigureFailure
      description: >-
        Receive notice that a Configure was rejected or failed to apply; the
        prior configuration is retained
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2ConfigureFailure'
    subpackage_speak/v2.speak.v2-server-9-SpeakV2Warning:
      name: SpeakV2Warning
      title: SpeakV2Warning
      description: Receive a warning; synthesis continues and the connection is unaffected
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Warning'
    subpackage_speak/v2.speak.v2-server-10-SpeakV2Error:
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
    subpackage_speak/v2.speak.v2-client-2-SpeakV2Interrupt:
      name: SpeakV2Interrupt
      title: SpeakV2Interrupt
      description: Cancel the active turn because the user barged in
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Interrupt'
    subpackage_speak/v2.speak.v2-client-3-SpeakV2Configure:
      name: SpeakV2Configure
      title: SpeakV2Configure
      description: Update synthesis configuration mid-session
      payload:
        $ref: '#/components/schemas/SpeakV2_SpeakV2Configure'
    subpackage_speak/v2.speak.v2-client-4-SpeakV2Close:
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
    SpeakV2Speed:
      type: number
      format: double
      minimum: 0.5
      maximum: 1.5
      multipleOf: 0.05
      default: 1
      description: >-
        Speech-rate multiplier. `1.0` is the model's nominal rate; lower is
        slower. Accepted values run `0.5` to `1.5` in `0.05` increments. A value
        outside that range is rejected with `SPEED_OUT_OF_RANGE`; a value inside
        it but off the `0.05` increment with `SPEED_INCREMENT_INVALID`. Models
        and languages without runtime speed control reject any value with
        `SPEED_NOT_SUPPORTED`.
      title: SpeakV2Speed
    SpeakV2Expressivity:
      type: string
      enum:
        - '-2'
        - '-1'
        - '0'
        - '1'
        - '2'
      description: >-
        Expressive range of the generated speech, on a calm-to-animated axis.
        Accepted values: `-2`, `-1`, `0`, `1`, `2`. `0` (the default) is the
        voice's tuned delivery and the production-validated setting, with `-2`
        the calm end of the range and `2` the animated end. Supported on all
        Flux voices. Fixed for the connection — not settable via `Configure`.
        Beta: behavior may change in future model versions, and non-default
        values increase the risk of hallucinations and pronunciation errors;
        audition before shipping. An invalid value fails the connection with a
        `400` — `EXPRESSIVITY_OUT_OF_RANGE` for a value outside the range,
        `EXPRESSIVITY_INCREMENT_INVALID` for a fractional value. See
        [Expressivity](/docs/tts-expressivity).
      title: SpeakV2Expressivity
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
            `dg-pronunciations-applied` REST header. Currently always `0`.
        breaks_applied:
          type: integer
          description: >-
            Pause (break) controls successfully applied. Mirrors the Aura-2
            `dg-breaks-applied` REST header. Currently always `0`.
        pronunciation_warnings:
          type: integer
          description: >-
            Pronunciation entries that triggered a warning (invalid IPA, word
            too long). Mirrors the Aura-2 `dg-pronunciation-warnings` REST
            header. Currently always `0`.
      required:
        - pronunciations_applied
        - breaks_applied
        - pronunciation_warnings
      description: >-
        Counts of the inline controls the server acted on during the turn.
        Inline pause and pronunciation controls are not applied at launch —
        support is coming soon — so every count is currently `0`.
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
            Counts of the inline controls the server acted on during the turn.
            Inline pause and pronunciation controls are not applied at launch —
            support is coming soon — so every count is currently `0`.
      required:
        - type
        - speech_id
        - audio_duration_ms
        - input_character_count
        - billable_character_count
        - controls_applied
      title: SpeakV2_SpeakV2SpeechMetadata
    ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadataControlsApplied:
      type: object
      properties:
        pronunciations_applied:
          type: integer
          description: >-
            Pronunciation overrides successfully applied. Mirrors the Aura-2
            `dg-pronunciations-applied` REST header. Currently always `0`.
        breaks_applied:
          type: integer
          description: >-
            Pause (break) controls successfully applied. Mirrors the Aura-2
            `dg-breaks-applied` REST header. Currently always `0`.
        pronunciation_warnings:
          type: integer
          description: >-
            Pronunciation entries that triggered a warning (invalid IPA, word
            too long). Mirrors the Aura-2 `dg-pronunciation-warnings` REST
            header. Currently always `0`.
      required:
        - pronunciations_applied
        - breaks_applied
        - pronunciation_warnings
      description: >-
        Counts of the inline controls the server acted on during the turn.
        Inline pause and pronunciation controls are not applied at launch —
        support is coming soon — so every count is currently `0`.
      title: ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadataControlsApplied
    ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadata:
      type: object
      properties:
        speech_id:
          type: string
          description: Server-assigned turn identifier
        audio_duration_ms:
          type: integer
          description: Audio duration produced for this turn, in milliseconds
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
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadataControlsApplied
          description: >-
            Counts of the inline controls the server acted on during the turn.
            Inline pause and pronunciation controls are not applied at launch —
            support is coming soon — so every count is currently `0`.
      required:
        - speech_id
        - audio_duration_ms
        - input_character_count
        - billable_character_count
        - controls_applied
      description: Billing and timing for a single turn.
      title: ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadata
    SpeakV2_SpeakV2SpeechInterrupted:
      type: object
      properties:
        type:
          type: string
          enum:
            - SpeechInterrupted
          description: Message type identifier
        audio_played_ms:
          type: integer
          description: >-
            How much audio the client had played when the interrupt landed, in
            milliseconds from the start of the session. Echoes the `Interrupt`'s
            `playback_offset` when one was supplied. Otherwise it is the
            server's own total, representing the audio that has been generated
            so far. A client that sends its first `Interrupt` without an offset
            can use this value as the baseline the next one must advance past.
        text_spoken:
          type: string
          description: >-
            The portion of the turn's text the user heard. Omitted when the
            `Interrupt` carried no `playback_offset`.
        text_remaining:
          type: string
          description: >-
            The portion of the turn's text the user did not hear. Omitted when
            the `Interrupt` carried no `playback_offset`.
        metadata:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2SpeechInterruptedMetadata
          description: Billing and timing for a single turn.
      required:
        - type
        - audio_played_ms
        - metadata
      title: SpeakV2_SpeakV2SpeechInterrupted
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
            milliseconds. An `Interrupt` rebases this onto the audio the client
            actually played.
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
    SpeakV2SpeedValue:
      type: number
      format: double
      minimum: 0.5
      maximum: 1.5
      multipleOf: 0.05
      default: 1
      description: >-
        Speech-rate multiplier. `1.0` is the model's nominal rate; lower is
        slower. Accepted values run `0.5` to `1.5` in `0.05` increments. A value
        outside that range is rejected with `SPEED_OUT_OF_RANGE`; a value inside
        it but off the `0.05` increment with `SPEED_INCREMENT_INVALID`. Models
        and languages without runtime speed control reject any value with
        `SPEED_NOT_SUPPORTED`.
      title: SpeakV2SpeedValue
    ChannelsSpeakV2MessagesSpeakV2ConfigureSuccessApplied:
      type: object
      properties:
        speed:
          $ref: '#/components/schemas/SpeakV2SpeedValue'
          default: 1
      description: >-
        Synthesis configuration. A field is present only when it has been set on
        this session.
      title: ChannelsSpeakV2MessagesSpeakV2ConfigureSuccessApplied
    SpeakV2_SpeakV2ConfigureSuccess:
      type: object
      properties:
        type:
          type: string
          enum:
            - ConfigureSuccess
          description: Message type identifier
        applied:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2ConfigureSuccessApplied
          description: >-
            Synthesis configuration. A field is present only when it has been
            set on this session.
      required:
        - type
        - applied
      title: SpeakV2_SpeakV2ConfigureSuccess
    ChannelsSpeakV2MessagesSpeakV2ConfigureFailureCode:
      type: string
      enum:
        - SPEED_OUT_OF_RANGE
        - SPEED_INCREMENT_INVALID
        - SPEED_NOT_SUPPORTED
        - INTERNAL_ERROR
      description: >-
        Failure code, in `SCREAMING_SNAKE_CASE`. `SPEED_OUT_OF_RANGE`: outside
        the range the model publishes. `SPEED_INCREMENT_INVALID`: inside the
        published range but off the `0.05` increment. `SPEED_NOT_SUPPORTED`:
        this model or language has no runtime speed control at all.
        `INTERNAL_ERROR`: the configuration was acceptable but the server could
        not apply it — unlike the others, a server-side failure rather than a
        statement about the request.
      title: ChannelsSpeakV2MessagesSpeakV2ConfigureFailureCode
    ChannelsSpeakV2MessagesSpeakV2ConfigureFailureField:
      type: string
      enum:
        - speed
      description: >-
        The configuration field the failure is about. Absent when the failure is
        not tied to one field.
      title: ChannelsSpeakV2MessagesSpeakV2ConfigureFailureField
    SpeakV2_SpeakV2ConfigureFailure:
      type: object
      properties:
        type:
          type: string
          enum:
            - ConfigureFailure
          description: Message type identifier
        code:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2ConfigureFailureCode
          description: >-
            Failure code, in `SCREAMING_SNAKE_CASE`. `SPEED_OUT_OF_RANGE`:
            outside the range the model publishes. `SPEED_INCREMENT_INVALID`:
            inside the published range but off the `0.05` increment.
            `SPEED_NOT_SUPPORTED`: this model or language has no runtime speed
            control at all. `INTERNAL_ERROR`: the configuration was acceptable
            but the server could not apply it — unlike the others, a server-side
            failure rather than a statement about the request.
        field:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2ConfigureFailureField
          description: >-
            The configuration field the failure is about. Absent when the
            failure is not tied to one field.
        value:
          type: number
          format: double
          description: >-
            The rejected value for `field`. Absent when there is no offending
            value to echo — `SPEED_NOT_SUPPORTED` names the field but carries no
            value, because the rejection is a property of the model.
        description:
          type: string
          description: A human-readable description of the failure
      required:
        - type
        - code
        - description
      title: SpeakV2_SpeakV2ConfigureFailure
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


            Turn-scoped codes: `NO_ACTIVE_SPEECH` (a speech-scoped message
            arrived with no active turn), `NO_SYNTHESIZABLE_TEXT` (the turn's
            text was entirely whitespace or punctuation, so it produced no audio
            and is completed with a zero-duration `SpeechMetadata`), and
            `SYNTHESIS_RETRYING` (a synthesis request failed and is being
            retried).


            Inline-control codes are reserved and not currently emitted, because
            inline pause and pronunciation controls are not yet applied:
            `BREAKS_LIMIT_EXCEEDED` (too many pause controls, or two pauses with
            no intervening text), `BREAK_TOKENS_OUT_OF_RANGE` (pause durations
            outside the range the model supports),
            `BREAK_TOKENS_WITH_INVALID_INCREMENTS` (pause durations off the
            model's supported increment), `PRONUNCIATION_WARNINGS` (a
            pronunciation override contained invalid IPA),
            `PRONUNCIATION_TOO_LONG` (an IPA string exceeded the length limit),
            `PRONUNCIATIONS_LIMIT_EXCEEDED` (too many pronunciation controls in
            one turn).


            Interrupt-scoped codes, each meaning the `Interrupt` was ignored:
            `NO_AUDIO_GENERATED` (the session has produced no audio yet, so
            there is nothing to interrupt), `INTERRUPT_IN_PROGRESS` (an earlier
            `Interrupt` is still being processed — at most one is handled at a
            time), `INVALID_INTERRUPT_OFFSET` (the `playback_offset` did not
            advance past the position a prior interrupt established).
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
        - DATA-0002
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
          description: >-
            The input text to synthesize. Inline pause and pronunciation
            controls are not yet applied; they are stripped from the text before
            synthesis.
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
    ChannelsSpeakV2MessagesSpeakV2InterruptPlaybackOffset:
      type: object
      properties:
        type:
          type: string
          enum:
            - time_ms
          description: Offset unit. `time_ms` is the only supported form.
        value:
          type: integer
          description: Milliseconds of session audio the client played before barging in.
      required:
        - type
        - value
      description: >-
        How much audio the client had played when the user barged in. Optional:
        without it the server cannot split the turn's text, so
        `SpeechInterrupted` omits `text_spoken` and `text_remaining`.


        The offset is cumulative from the start of the *session*, not from the
        start of the current turn. Each `Interrupt` must advance past the
        position the previous one established.
      title: ChannelsSpeakV2MessagesSpeakV2InterruptPlaybackOffset
    SpeakV2_SpeakV2Interrupt:
      type: object
      properties:
        type:
          type: string
          enum:
            - Interrupt
          description: Message type identifier
        playback_offset:
          $ref: >-
            #/components/schemas/ChannelsSpeakV2MessagesSpeakV2InterruptPlaybackOffset
          description: >-
            How much audio the client had played when the user barged in.
            Optional: without it the server cannot split the turn's text, so
            `SpeechInterrupted` omits `text_spoken` and `text_remaining`.


            The offset is cumulative from the start of the *session*, not from
            the start of the current turn. Each `Interrupt` must advance past
            the position the previous one established.
      required:
        - type
      title: SpeakV2_SpeakV2Interrupt
    SpeakV2_SpeakV2Configure:
      type: object
      properties:
        type:
          type: string
          enum:
            - Configure
          description: Message type identifier
        speed:
          $ref: '#/components/schemas/SpeakV2SpeedValue'
          default: 1
      required:
        - type
      title: SpeakV2_SpeakV2Configure
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
