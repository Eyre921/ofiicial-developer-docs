---
title: "Turn-based Audio (Flux)"
source: https://developers.deepgram.com/reference/speech-to-text/listen-flux.md
path: reference/speech-to-text/listen-flux
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Turn-based Audio (Flux)

GET /v2/listen

Real-time conversational speech recognition with contextual turn detection
for natural voice conversations


Reference: https://developers.deepgram.com/reference/speech-to-text/listen-flux

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: listen.v2
  version: subpackage_listen/v2.listen.v2
  description: |
    Real-time conversational speech recognition with contextual turn detection
    for natural voice conversations
channels:
  /v2/listen:
    description: |
      Real-time conversational speech recognition with contextual turn detection
      for natural voice conversations
    bindings:
      ws:
        query:
          type: object
          properties:
            model:
              $ref: '#/components/schemas/ListenV2Model'
            encoding:
              $ref: '#/components/schemas/ListenV2Encoding'
            sample_rate:
              $ref: '#/components/schemas/ListenV2SampleRate'
            eager_eot_threshold:
              $ref: '#/components/schemas/ListenV2EagerEotThreshold'
            eot_threshold:
              $ref: '#/components/schemas/ListenV2EotThreshold'
              default: '0.7'
            eot_timeout_ms:
              $ref: '#/components/schemas/ListenV2EotTimeoutMs'
              default: '5000'
            keyterm:
              $ref: '#/components/schemas/ListenV2Keyterm'
            language_hint:
              $ref: '#/components/schemas/ListenV2LanguageHint'
            profanity_filter:
              $ref: '#/components/schemas/ListenV2ProfanityFilter'
              default: 'false'
            numerals:
              $ref: '#/components/schemas/ListenV2Numerals'
              default: 'false'
            redact:
              $ref: '#/components/schemas/ListenV2Redact'
            mip_opt_out:
              $ref: '#/components/schemas/ListenV2MipOptOut'
            tag:
              $ref: '#/components/schemas/ListenV2Tag'
        headers:
          type: object
          properties:
            Authorization:
              type: string
    publish:
      operationId: listen-v-2-publish
      summary: Server messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-server-0-ListenV2Connected
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-server-1-ListenV2TurnInfo
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-server-2-ListenV2ConfigureSuccess
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-server-3-ListenV2ConfigureFailure
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-server-4-ListenV2FatalError
    subscribe:
      operationId: listen-v-2-subscribe
      summary: Client messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-client-0-ListenV2Media
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-client-1-ListenV2CloseStream
          - $ref: >-
              #/components/messages/subpackage_listen/v2.listen.v2-client-2-ListenV2Configure
servers:
  Production:
    url: wss://api.deepgram.com/
    protocol: wss
    x-default: true
components:
  messages:
    subpackage_listen/v2.listen.v2-server-0-ListenV2Connected:
      name: ListenV2Connected
      title: ListenV2Connected
      description: Receive a connected message
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2Connected'
    subpackage_listen/v2.listen.v2-server-1-ListenV2TurnInfo:
      name: ListenV2TurnInfo
      title: ListenV2TurnInfo
      description: Receive a turn info message
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2TurnInfo'
    subpackage_listen/v2.listen.v2-server-2-ListenV2ConfigureSuccess:
      name: ListenV2ConfigureSuccess
      title: ListenV2ConfigureSuccess
      description: >-
        Sent when a `Configure` message was successfully applied. Returns the
        current, up-to-date values that were applied.
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2ConfigureSuccess'
    subpackage_listen/v2.listen.v2-server-3-ListenV2ConfigureFailure:
      name: ListenV2ConfigureFailure
      title: ListenV2ConfigureFailure
      description: Indicates that a Configure message was rejected
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2ConfigureFailure'
    subpackage_listen/v2.listen.v2-server-4-ListenV2FatalError:
      name: ListenV2FatalError
      title: ListenV2FatalError
      description: Receive a fatal error message
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2FatalError'
    subpackage_listen/v2.listen.v2-client-0-ListenV2Media:
      name: ListenV2Media
      title: ListenV2Media
      description: Send audio or video data to be transcribed
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2Media'
    subpackage_listen/v2.listen.v2-client-1-ListenV2CloseStream:
      name: ListenV2CloseStream
      title: ListenV2CloseStream
      description: Send a CloseStream message to close the WebSocket stream
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2CloseStream'
    subpackage_listen/v2.listen.v2-client-2-ListenV2Configure:
      name: ListenV2Configure
      title: ListenV2Configure
      description: Send a Configure message to update Flux settings
      payload:
        $ref: '#/components/schemas/ListenV2_ListenV2Configure'
  schemas:
    ListenV2Model:
      type: string
      enum:
        - flux-general-en
        - flux-general-multi
      description: Defines the AI model used to process submitted audio.
      title: ListenV2Model
    ListenV2Encoding:
      type: string
      enum:
        - linear16
        - linear32
        - mulaw
        - alaw
        - opus
        - ogg-opus
      description: >-
        Encoding of the audio stream. Required if sending non-containerized/raw
        audio. If sending containerized audio, this parameter should be omitted.
      title: ListenV2Encoding
    ListenV2SampleRate:
      description: Any type
      title: ListenV2SampleRate
    ListenV2EagerEotThreshold:
      description: Any type
      title: ListenV2EagerEotThreshold
    ListenV2EotThreshold:
      description: Any type
      title: ListenV2EotThreshold
    ListenV2EotTimeoutMs:
      description: Any type
      title: ListenV2EotTimeoutMs
    ListenV2Keyterm:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: >
        Keyterm prompting improves recognition of specialized terminology.


        `keyterm` accepts plain terms only. Unlike the legacy `keywords`
        feature,

        it does not support weights or intensifiers. Appending one

        (for example, `keyterm=term:0.15`) is not rejected—the weight is

        silently ignored and the entire value is treated as a literal keyterm.


        To boost multiple separate keyterms, repeat the `keyterm` parameter

        (for example, `keyterm=term1&keyterm=term2`). To boost one multi-word

        phrase as a single keyterm, join the words with `%20` or `+`

        (for example, `keyterm=customer%20service`). Do not separate keyterms

        with commas, semicolons, or line breaks.
      title: ListenV2Keyterm
    ListenV2LanguageHint:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: |
        Language hints constrain and prioritize language detection for the
        flux-general-multi model. Pass multiple language_hint query parameters
        to specify multiple language codes. Empty values are rejected.
        Only valid when model is flux-general-multi.
      title: ListenV2LanguageHint
    ListenV2ProfanityFilter:
      type: string
      enum:
        - 'true'
        - 'false'
      default: 'false'
      description: >-
        Profanity Filter looks for recognized profanity and converts it to the
        nearest recognized non-profane word or removes it from the transcript
        completely.
      title: ListenV2ProfanityFilter
    ListenV2Numerals:
      type: string
      enum:
        - 'true'
        - 'false'
      default: 'false'
      description: Numerals converts numbers from written format to numerical format
      title: ListenV2Numerals
    ListenV2Redact:
      type: string
      enum:
        - numbers
        - aggressive_numbers
      description: >-
        Redaction removes sensitive information from your transcripts. On Flux,
        only `numbers` and `aggressive_numbers` are supported.
      title: ListenV2Redact
    ListenV2MipOptOut:
      description: Any type
      title: ListenV2MipOptOut
    ListenV2Tag:
      description: Any type
      title: ListenV2Tag
    ChannelsListenV2MessagesListenV2ConnectedType:
      type: string
      enum:
        - Connected
      description: Message type identifier
      title: ChannelsListenV2MessagesListenV2ConnectedType
    ListenV2_ListenV2Connected:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsListenV2MessagesListenV2ConnectedType'
          description: Message type identifier
        request_id:
          type: string
          format: uuid
          description: The unique identifier of the request
        sequence_id:
          type: integer
          description: |
            Starts at `0` and increments for each message the server sends
            to the client.  This includes messages of other types, like
            `TurnInfo` messages.
      required:
        - type
        - request_id
        - sequence_id
      title: ListenV2_ListenV2Connected
    ChannelsListenV2MessagesListenV2TurnInfoEvent:
      type: string
      enum:
        - Update
        - StartOfTurn
        - EagerEndOfTurn
        - TurnResumed
        - EndOfTurn
      description: >
        The type of event being reported.


        - **Update** - Additional audio has been transcribed, but the turn state
        hasn't changed

        - **StartOfTurn** - The user has begun speaking for the first time in
        the turn

        - **EagerEndOfTurn** - The system has moderate confidence that the user
        has finished speaking for the turn. This is an opportunity to begin
        preparing an agent reply

        - **TurnResumed** - The system detected that speech had ended and
        therefore sent an **EagerEndOfTurn** event, but speech is actually
        continuing for this turn

        - **EndOfTurn** - The user has finished speaking for the turn
      title: ChannelsListenV2MessagesListenV2TurnInfoEvent
    ChannelsListenV2MessagesListenV2TurnInfoWordsItems:
      type: object
      properties:
        word:
          type: string
          description: The individual punctuated, properly-cased word from the transcript
        confidence:
          type: number
          format: double
          description: Confidence that this word was transcribed correctly
        start:
          type: number
          format: double
          description: The start time of the word
        end:
          type: number
          format: double
          description: The end time of the word
      required:
        - word
        - confidence
      title: ChannelsListenV2MessagesListenV2TurnInfoWordsItems
    ListenV2_ListenV2TurnInfo:
      type: object
      properties:
        type:
          type: string
          enum:
            - TurnInfo
        request_id:
          type: string
          format: uuid
          description: The unique identifier of the request
        sequence_id:
          type: integer
          description: >
            Starts at `0` and increments for each message the server sends to
            the client.  This includes messages of other types, like `Connected`
            messages.
        event:
          $ref: '#/components/schemas/ChannelsListenV2MessagesListenV2TurnInfoEvent'
          description: >
            The type of event being reported.


            - **Update** - Additional audio has been transcribed, but the turn
            state hasn't changed

            - **StartOfTurn** - The user has begun speaking for the first time
            in the turn

            - **EagerEndOfTurn** - The system has moderate confidence that the
            user has finished speaking for the turn. This is an opportunity to
            begin preparing an agent reply

            - **TurnResumed** - The system detected that speech had ended and
            therefore sent an **EagerEndOfTurn** event, but speech is actually
            continuing for this turn

            - **EndOfTurn** - The user has finished speaking for the turn
        turn_index:
          type: integer
          description: The index of the current turn
        audio_window_start:
          type: number
          format: double
          description: Start time in seconds of the audio range that was transcribed
        audio_window_end:
          type: number
          format: double
          description: End time in seconds of the audio range that was transcribed
        transcript:
          type: string
          description: Text that was said over the course of the current turn
        words:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsListenV2MessagesListenV2TurnInfoWordsItems
          description: The words in the `transcript`
        end_of_turn_confidence:
          type: number
          format: double
          description: Confidence that no more speech is coming in this turn
        languages:
          type: array
          items:
            type: string
          description: |
            Detected languages sorted by descending frequency in the
            transcript. Only present when the flux-general-multi model
            detects languages in the audio.
        languages_hinted:
          type: array
          items:
            type: string
          description: |
            The language hints that were supplied for this turn. Only
            present when language hints are configured.
      required:
        - type
        - request_id
        - sequence_id
        - event
        - turn_index
        - audio_window_start
        - audio_window_end
        - transcript
        - words
        - end_of_turn_confidence
      description: Describes the current turn and latest state of the turn
      title: ListenV2_ListenV2TurnInfo
    ChannelsListenV2MessagesListenV2ConfigureSuccessThresholds:
      type: object
      properties:
        eager_eot_threshold:
          $ref: '#/components/schemas/ListenV2EagerEotThreshold'
        eot_threshold:
          $ref: '#/components/schemas/ListenV2EotThreshold'
          default: '0.7'
        eot_timeout_ms:
          $ref: '#/components/schemas/ListenV2EotTimeoutMs'
          default: '5000'
      description: >
        Updates each parameter, if it is supplied. If a particular threshold
        parameter

        is not supplied, the configuration continues using the currently
        configured value.
      title: ChannelsListenV2MessagesListenV2ConfigureSuccessThresholds
    ListenV2_ListenV2ConfigureSuccess:
      type: object
      properties:
        type:
          type: string
          enum:
            - ConfigureSuccess
          description: Message type identifier
        request_id:
          type: string
          format: uuid
          description: The unique identifier of the request
        thresholds:
          $ref: >-
            #/components/schemas/ChannelsListenV2MessagesListenV2ConfigureSuccessThresholds
          description: >
            Updates each parameter, if it is supplied. If a particular threshold
            parameter

            is not supplied, the configuration continues using the currently
            configured value.
        keyterms:
          $ref: '#/components/schemas/ListenV2Keyterm'
        language_hints:
          type: array
          items:
            type: string
          description: >
            The currently active language hints. Only applicable to the
            flux-general-multi model.
        sequence_id:
          type: integer
          description: |
            Starts at `0` and increments for each message the server sends
            to the client.  This includes messages of other types, like
            `TurnInfo` messages.
      required:
        - type
        - request_id
        - thresholds
        - keyterms
        - sequence_id
      title: ListenV2_ListenV2ConfigureSuccess
    ListenV2_ListenV2ConfigureFailure:
      type: object
      properties:
        type:
          type: string
          enum:
            - ConfigureFailure
          description: Message type identifier
        request_id:
          type: string
          format: uuid
          description: The unique identifier of the request
        sequence_id:
          type: integer
          description: |
            Starts at `0` and increments for each message the server sends
            to the client.  This includes messages of other types, like
            `TurnInfo` messages.
      required:
        - type
        - request_id
        - sequence_id
      title: ListenV2_ListenV2ConfigureFailure
    ChannelsListenV2MessagesListenV2FatalErrorType:
      type: string
      enum:
        - Error
      description: Message type identifier
      title: ChannelsListenV2MessagesListenV2FatalErrorType
    ListenV2_ListenV2FatalError:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsListenV2MessagesListenV2FatalErrorType'
          description: Message type identifier
        sequence_id:
          type: integer
          description: |
            Starts at `0` and increments for each message the server sends
            to the client.  This includes messages of other types, like
            `Connected` messages.
        code:
          type: string
          description: A string code describing the error, e.g. `INTERNAL_SERVER_ERROR`
        description:
          type: string
          description: Prose description of the error
      required:
        - type
        - sequence_id
        - code
        - description
      title: ListenV2_ListenV2FatalError
    ListenV2_ListenV2Media:
      type: string
      format: binary
      title: ListenV2_ListenV2Media
    ChannelsListenV2MessagesListenV2CloseStreamType:
      type: string
      enum:
        - CloseStream
      description: Message type identifier
      title: ChannelsListenV2MessagesListenV2CloseStreamType
    ListenV2_ListenV2CloseStream:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsListenV2MessagesListenV2CloseStreamType'
          description: Message type identifier
      required:
        - type
      title: ListenV2_ListenV2CloseStream
    ChannelsListenV2MessagesListenV2ConfigureThresholds:
      type: object
      properties:
        eager_eot_threshold:
          $ref: '#/components/schemas/ListenV2EagerEotThreshold'
        eot_threshold:
          $ref: '#/components/schemas/ListenV2EotThreshold'
          default: '0.7'
        eot_timeout_ms:
          $ref: '#/components/schemas/ListenV2EotTimeoutMs'
          default: '5000'
      description: >
        Updates each parameter, if it is supplied. If a particular threshold
        parameter

        is not supplied, the configuration continues using the currently
        configured value.
      title: ChannelsListenV2MessagesListenV2ConfigureThresholds
    ListenV2_ListenV2Configure:
      type: object
      properties:
        type:
          type: string
          enum:
            - Configure
          description: Message type identifier
        thresholds:
          $ref: >-
            #/components/schemas/ChannelsListenV2MessagesListenV2ConfigureThresholds
          description: >
            Updates each parameter, if it is supplied. If a particular threshold
            parameter

            is not supplied, the configuration continues using the currently
            configured value.
        keyterms:
          $ref: '#/components/schemas/ListenV2Keyterm'
        language_hints:
          type: array
          items:
            type: string
          description: >
            Language hints to constrain and prioritize language detection.

            Only valid when the model is flux-general-multi. If this field is
            not supplied,

            the session will continue to use the currently configured value.
      required:
        - type
      title: ListenV2_ListenV2Configure

```
